from analysis_fb.collect.api import api

#url=api.fb_gen_url(node='jtbcnews',a=10,b=20,s='nhk321');

##페북에 보낼 url 만듬

#print(url)

"""
id=api.fb_name_to_id("jtbcnews")
print(id)
"""

#api.fb_gen_url()




'''

posts=api.fb_fetch_posts('jtbcnews','2017-01-01','2017-12-31')
print(len(posts))

'''



# yield 로 한거 생성

for posts in api.fb_fetch_posts('jtbcnews','2017-01-01','2017-12-31'):
    print(posts)
#print(posts)


