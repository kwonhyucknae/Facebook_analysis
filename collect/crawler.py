import os
import json
from datetime import datetime,timedelta
from .api import api


RESULT_DIRECTORY='__result__/crawling'


#전처리 과정

def preprocess_post(post):
    #공유수
    #print("들어온 post type==",type(post))
    if 'shares' not in post:
        #빠져 있다면 0
        post['count_shares']=0
    else:
        post['count_shares']=post['shares']['count']
    #전체 리액션 수
    if 'reactions' not in post:
        post['count_reactions']=0
    else:
        post['count_reactions'] = post['reactions']['summary']['total_count']
    #전체 코멘트 수
    if 'comments' not in post:
        post['count_comments']=0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']
    #시간대 변경
    # KST=UTC+9
    kst=datetime.strptime(post['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    kst += timedelta(hours=9)
    post['created_time']=kst.strftime('%Y-%m-%d %H:%M:%S')


#fb_fetch_posts 로 얻어온 포스트를
#전처리를 통해 원하는 결과를 얻고
#그 결과를 파일에 넣는 함수
def crawling(pagename,since,until,fetch=True):

    results=[]
    filename='%s/%s_%s_%s.json' %(RESULT_DIRECTORY,pagename,since,until)
    if fetch:
         for posts in api.fb_fetch_posts(pagename, since, until):
            for post in posts:
                preprocess_post(post)
            results += posts
         #save results to file (저장, 적재)

         with open(filename,'w',encoding='utf-8') as outfile:
            json_string=json.dumps(results,indent=4,sort_keys=True,ensure_ascii=False)
            outfile.write(json_string)
        #with as 구문은 close가 자동으로 된다

    return filename

if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)
