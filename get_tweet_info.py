import ast
import requests

name = ''
checkinsCount = ''
usersCount = ''
tipCount = ''
lat = ''
lng = ''
location_id = ''
pluralName = ''
cate_name = ''
cate_id = ''
cate_shortName = ''
cate_primary = ''


def get_location_info(url):
    
    name = ''
    checkinsCount = ''
    usersCount = ''
    tipCount = ''
    lat = ''
    lng = ''
    location_id = ''
    pluralName = ''
    cate_name = ''
    cate_id = ''
    cate_shortName = ''
    cate_primary = ''
    #print '================================'
    #print url
    #print '================================'
    #url = 'https://www.swarmapp.com/c/dYX3kcIuyaQ'
    response = requests.get(url)
    print response.status_code
    text = (response.text)
    #print text
    #tmp = text.split('\"venue\":{\"name\":')
    tmp = text.split('\"venue\":')
    #tmp2 = tmp[1].split('\"icon\":{\"prefix\"')
    
    #venue = '{\"name\":' + tmp2[0] 
    #venue = tmp2[0] 
    #tmp3 = tmp2[1].split("\"id\":")
    #tmp4 = tmp3[1].split('}],\"verified\":')
    #venue = venue + "\"id\":" + tmp4[0] + '}]}'
    #print len(tmp)
    if response.status_code != 200:
        return [name,checkinsCount,usersCount,tipCount,lat,lng,location_id,pluralName,cate_name,cate_id,cate_shortName,cate_primary]
     
    tmp2 = tmp[1].split(',\"verified\":')
    venue = tmp2[0] + '}'
    venue = venue.replace('true','\"true\"')
    venue = venue.replace('false','\"false\"')
    venue = venue.replace('[','')
    venue = venue.replace(']','')
    #print venue
    try:
        dic = ast.literal_eval(venue)
    except Exception:
        return [name,checkinsCount,usersCount,tipCount,lat,lng,location_id,pluralName,cate_name,cate_id,cate_shortName,cate_primary]
    #print '-------------------------------'
    #print dic
    try:
        name = dic['name']
        name = name.replace(',',' ')
        #print name
    except Exception as e:
        name = ""
        print e
        
    try:
        checkinsCount = dic['stats']['checkinsCount']
    except Exception:
        checkinsCount = ""
        
    try:
        usersCount = dic['stats']['usersCount']
    except Exception:
        userCount = ""
        
    try:
        tipCount = dic['stats']['tipCount']
    except Exception:
        tipCount = ""
        
    try:
        lat = dic['location']['lat']
    except Exception:
        lat = ""
        
    try:
        lng = dic['location']['lng']
    except Exception:
        lng = ""
        
    try:
        location_id = dic['id']
    except Exception:
        location_id = ""
        
    try:
        pluralName = dic['categories']['pluralName']
    except Exception:
        pluralName = ""
        
    try:
        cate_name = dic['categories']['name']
    except Exception:
        cate_name = ""
        
    try:
        cate_id = dic['categories']['id']
    except Exception:
        cate_id = ""
        
    try:
        cate_shortName = dic['categories']['shortName']
    except Exception:
        cate_shortName = ""
        
    try:
        cate_primary = dic['categories']['primary']
    except Exception:
        cate_primary = ""
    
    return [name,checkinsCount,usersCount,tipCount,lat,lng,location_id,pluralName,cate_name,cate_id,cate_shortName,cate_primary]
        
def get_id(dic):
    try:
        tweet_id = dic['id']
    except Exception as e:
         tweet_id = 'Null'
         #print e
    return tweet_id
    
def get_text(dic):
    try:
        text = dic['text']
        text = text.split("https:")
        #print text
        url = text[1].replace('\\/','/')
        url = "https:" + url
        #print url
    except Exception as e:
        url = 'Null'
        print e
    return url
    
def get_created_at(dic):
    try:
        created_at = dic['created_at']
    except Exception as e:
        created_at = 'Null'
        #print e
    return created_at
    
def get_in_reply_to_screen_name(dic):
    try:
        reply_to_screen_name = dic['in_reply_to_screen_name']
    except Exception as e:
         reply_to_screen_name = 'Null'
         #print e
    return reply_to_screen_name

def get_in_reply_to_status_id(dic):
    try:
        reply_to_status_id = dic['in_reply_to_status_id']
    except Exception as e:
         reply_to_status_id = 'Null'
         #print e
    return reply_to_status_id

def get_reply_to_user_id(dic):
    try:
        reply_to_user_id = dic['in_reply_to_user_id']
    except Exception as e:
         reply_to_user_id = 'Null'
         #print e
    return reply_to_user_id            


def get_retweet_count(dic):
    try:
        retweet = int(dic['retweet_count'])
    except Exception as e:
        retweet = 0
        #print e
    return retweet
    
def get_user_id(dic):
    try:
        user_id = dic['user']['id']
    except Exception as e:
        user_id = 'Null'
        #print e
    return user_id

def get_original_tweet_id(dic):
    try:
        tweet_id = dic['retweeted_status']['id']
    except Exception as e:
        tweet_id = 'Null'
        #print e
    return tweet_id

def get_original_user_id(dic):
    try:
        user_id = dic['retweeted_status']['user']['id']
    except Exception as e:
        user_id = 'Null'
        #print e
    return user_id

def get_isOriginal(dic):
    try:
        retweet = dic['retweeted_status']
        isOriginal = 1
    except Exception as e:
        isOriginal = 0
    return isOriginal
    

for file_num in range(1):
    #filename = './user_timeline_'+str(file_num)+'.json'
    #filename = 'C://Users/GYLi/Desktop/4sq_twitter/code/twitter_streaming_with_4sq_5.txt'
    filename = './file_1.json'
    f = open(filename)                  
    #f = open("C:/Users/GYLi/Desktop/twitter_dataset/user_timeline_1.json")
    data = []
    
    for line in f:
        data.append(line)  
    f.close()  
    count = 0
    w_filename = './tweet_info_1.csv'
    dbf = open(w_filename,'w')
    
    for tweet in data:
         
        count = count + 1
        print count
        if len(tweet) < 10:
            #print count
            #print 'true'
            #print tweet
            continue  
        tweet = tweet.replace('u\'','\'')
        tweet = tweet.replace('\n','')
        if not tweet.endswith('}}'):
            continue
        
        dic = ast.literal_eval(tweet)
        tweet_id = get_id(dic)
        user_id = get_user_id(dic)
        retweet_count =  get_retweet_count(dic)
        date = get_created_at(dic)
        url = get_text(dic)
        #print url
        reply_to_user_id = get_reply_to_user_id(dic)
        isOriginal = get_isOriginal(dic)
        original_tweet_id = get_original_tweet_id(dic)
        original_user_id = get_original_user_id(dic)
        #location_info = get_location_info(url)
        name = ''
        checkinsCount = ''
        usersCount = ''
        tipCount = ''
        lat = ''
        lng = ''
        location_id = ''
        pluralName = ''
        cate_name = ''
        cate_id = ''
        cate_shortName = ''
        cate_primary = ''
        try:
            location_info = get_location_info(url)
        except Exception:
            location_info = [name,checkinsCount,usersCount,tipCount,lat,lng,location_id,pluralName,cate_name,cate_id,cate_shortName,cate_primary]
        #[name,checkinsCount,usersCount,tipCount,lat,lng,location_id,pluralName,cate_name,cate_id,cate_shortName,cate_primary]                  
        dbf.write(str(tweet_id)+','+str(user_id)+','+str(date)+','+str(location_info[0])+','+str(location_info[4])+','+str(location_info[5])+',')
        dbf.write(str(retweet_count)+','+str(isOriginal)+','+str(original_tweet_id)+','+str(original_user_id)+','+str(reply_to_user_id)+','+str(location_info[1])+','+str(location_info[2])+','+str(location_info[3])+','+str(location_info[6])+','+str(location_info[7])+','+str(location_info[8])+','+str(location_info[9])+','+str(location_info[10])+','+str(location_info[11])+'\n')
        #print name
        #break
        
dbf.close() 
