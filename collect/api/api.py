#FaceBook API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN="EAACEdEose0cBACV4Qs3BlwzjxghPyGjUqZBbjl6hy0gtLL4eXFv9t4cq6XsUDdoa5xGhyiduAQ5qpQesmpUIZAwbFrzzdLzKQLD8Yw4t5JWAhSKQ5UZCMvnqA7GYLkpOA4mO2XlFoQybdKtXLvZBbYbDrBMm8cSH3TcruZC4tZAzYeE8OQiBSUngBTv9KU4QgZD"
BASE_URL_FB_API= "https://graph.facebook.com/v3.0"


# params dictionary 형태로 들어온다
#params{"since":20173221, "until":2018dwqdwq}


def fb_gen_url(base=BASE_URL_FB_API,
               node='',
               **params):
    url='%s/%s/?%s' % (base,node,urlencode(params))
    return url


def fb_name_to_id(pagename):
    url=fb_gen_url(node=pagename,access_token=ACCESS_TOKEN)

    json_result=json_request(url=url)
    return json_result.get("id")



#yield로 만들기
#크롤러를 만든기 위한 기반함수
#모듈화 -> 함수를 나눠준다 기능이 많으면 코드를 잘라서 사용

def fb_fetch_posts(pagename,since,until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + "/posts",
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN
    )

    print("url======"+url)

    #빈 리스트 생성

    isnext=True
    while isnext is True:
        json_result = json_request(url=url)

        #삼항연산자로 적으면 이렇게
        paging = None if json_result is None else json_result.get('paging')
        posts=None if json_result is None else json_result.get('data')
    #리스트를 더해준다

        #results+=posts

        #탈출 조건 생성
        url =None if paging is None else paging.get("next")

        isnext = url is not None

        yield posts
    #for문 안에서 yield




'''

def fb_fetch_posts(pagename,since,until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + "/posts",
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN
    )

    print("url======"+url)

    #빈 리스트 생성
    results = []

    isnext=True
    while isnext is True:
        json_result = json_request(url=url)

        #삼항연산자로 적으면 이렇게
        paging = None if json_result is None else json_result.get('paging')
        posts=None if json_result is None else json_result.get('data')
    #리스트를 더해준다

        results+=posts

        #탈출 조건 생성
        url =None if paging is None else paging.get("next")

        isnext = url is not None

    return results
'''


 #삼항을 if문으로 할때는 이렇게

'''
        if json_result is None:
            paging = None
        else:
            paging= json_result.get('paging')
'''

#return json_result


