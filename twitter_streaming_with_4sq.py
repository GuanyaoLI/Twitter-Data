from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import ast
#Variables that contains the user credentials to access Twitter API
access_token = "4090852874-1M64pZ2WiHUpm1Eum5GknFgIE72fhLfrnWvUCl7"
access_token_secret = "KxtzPwJQeSqiTRNXTZtSHkW0aXVN46xIp1GaDEIBXnggQ"
consumer_key = "CuCyVTB9gARh5ob1KV2rjTAsk"
consumer_secret = "jFrtWlKysD9kdncNdqNoRUO17wVEQDYMhm3vxZtKI97XMpt04G"

'''global count_4sq
global count_no_4sq
count_4sq = 0
count_no_4sq = 0'''
'''global f_4sq
f_4sq = open('./Twitter_USA_4sq_0.txt','w')
global f_no_4sq
f_no_4sq = open('./Twitter_USA_no_4sq_0.csv','w')'''
#This is a basic listener that just prints received tweets to stdout.

def get_source(dic):
    try:
        source = dic['source']
    except Exception as e:
        source = ''
    return source

def get_user_id(dic):
    try:
        user_id = dic['user']['id']
    except Exception as e:
        user_id = ''
    return user_id

def get_id(dic):
    try:
        tweet_id = dic['id_str']
    except Exception as e:
        tweet_id = 'Null'

    return tweet_id

def get_geo(dic):
    try:
        if dic["geo"]["type"] == 'Point':
            geo = dic["geo"]["coordinates"]
        else:
            return 'Null'
    except Exception as e:
        return 'Null'
    return geo

def get_created_at(dic):
    try:
        date = dic['created_at']
    except Exception as e:
        date = ''
    return date

class StdOutListener(StreamListener):
    #count_4sq = 0
    #count_no_4sq = 0
    #count_4sq = 0

    def get_source(dic):
        try:
            source = dic['source']
        except Exception as e:
            source = ''
        return source

    def get_user_id(dic):
        try:
            user_id = dic['user']['id']
        except Exception as e:
            user_id = ''
        return user_id

    def get_id(dic):
        try:
            tweet_id = dic['id_str']
        except Exception as e:
            tweet_id = 'Null'
        return tweet_id

    def get_geo(dic):
        try:
            if dic["geo"]["type"] == 'Point':
                geo = dic["geo"]["coordinates"]
            else:
                return 'Null'
        except Exception as e:
            return 'Null'
        return geo

    def get_created_at(dic):
        try:
            date = dic['created_at']
        except Exception as e:
            date = ''
        return date


    def on_data(self, data):
        #print data
        #print '====================================='
        #print count_4sq
        #print count_4sq
        #print count_no_4sq
        '''if count_4sq > 200000:

            #f_4sq.close()
            tmp = count_4sq / 200000
            #f_4sq = open('./Twitter_USA_4sq_'+str(tmp)+'.txt','w')
        if count_no_4sq > 200000:
            #f_no_4sq.close()
            tmp = count_no_4sq /200000
            #f_no_4sq = open('./Twitter_USA_no_4sq_'+str(tmp)+'.csv','w')'''
        tmp = data.replace('false','False')
        tmp = tmp.replace('true','True')
        tmp = tmp.replace('null','\'null\'')
        dic = ast.literal_eval(tmp)
        #print dic
        source = get_source(dic)
        #print '========================='
        if 'Foursquare' in source:
            print dic
            '''
        else:
            count_no_4sq +=1
            user_id = get_user_id(dic)
            twitter_id = get_id(dic)
            location = get_geo(dic)
            date = get_created_at(dic)
            f_no_4sq.write(str(twitter_id)+','+str(user_id)+','+str(date)+','+str(location)+'\n')
        return True'''

    def on_error(self, status):
        print status


if __name__ == '__main__':
    count_4sq = 0
    count_no_4sq = 0
    #f_4sq = open('./Twitter_USA_4sq_0.txt','w')
    #f_no_4sq = open('./Twitter_USA_no_4sq_0.csv','w')
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    try:
        stream.filter(locations=[-124.47,24.0,-66.56,49.3843])
    except Exception as e:
        stream.filter(locations=[-124.47,24.0,-66.56,49.3843]) 
