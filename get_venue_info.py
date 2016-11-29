# -*- coding: utf-8 -*-
import requests
import ast
f = open('E://venue.dat','a')
category = []

latitude = ''
longtitude = ''

price = {}

check_in_count = ''
userscount = ''
tipcount = ''
visitcount = ''

rating = ''
num_of_rate = ''

num_of_like = ''

num_of_photo = ''

venue_id = '4cfa2257d8468cfa5ebceb6b'
f.write(venue_id + ',')
r = requests.get("https://api.foursquare.com/v2/venues/"+venue_id+"?oauth_token=WCBQHBOR2BAY5AJBMCAZMGXYHCL2JIZH5XPPHLLXIKGHTVNV&v=20161129")
result =  r.text
tmp = result.replace('false','False')
tmp = tmp.replace('true','True')
tmp = tmp.replace('null','\'null\'')
dic = ast.literal_eval(tmp)




#category
cat_list = dic['response']['venue']['categories']
for tmp_dic in cat_list:
    name = str(tmp_dic['name'])
    category.append(name)

f.write(str(category) + ',')    

#latitude & longtitude
latitude = str(dic['response']['venue']['location']['lat'])
longtitude = str(dic['response']['venue']['location']['lng'])
f.write(latitude + ',')
f.write(longtitude + ',')

#price
price['tier'] = str(dic['response']['venue']['price']['tier'])
price['message'] = str(dic['response']['venue']['price']['message'])
f.write(price['tier']+',')
f.write(price['message']+',')

#checkinCount & userscount & tipcount & visitcount 
check_in_count = str(dic['response']['venue']['stats']['checkinsCount'])
userscount = str(dic['response']['venue']['stats']['usersCount'])
tipcount = str(dic['response']['venue']['stats']['tipCount'])
visitcount = str(dic['response']['venue']['stats']['visitsCount'])
f.write(check_in_count + ',')
f.write(userscount + ',')
f.write(tipcount + ',')
f.write(visitcount + ',')

#rating & number of rating 
rating = str(dic['response']['venue']['rating'])
num_of_rate = str(dic['response']['venue']['ratingSignals'])
f.write(rating + ',')
f.write(num_of_rate + ',')

#number of like 
num_of_like = str(dic['response']['venue']['likes']['count'])
f.write(num_of_like+',')

#number of photo
num_of_photo = str(dic['response']['venue']['photos']['count'])
f.write(num_of_photo + '\n')
f.close()