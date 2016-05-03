from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import time
#liguanyao
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = ["jsy6HgL7ryEQZSu9aIZjaKOmq","lHhCjsLuD0OZYNnCOXrz7D0Yt","eTrOlOO7xbjVMUjle2btGdCH9","ZYUXCgw8fyvuLUUWMEeHNCCGB","4HakbZjsWykndMoKQsOFdxQ4o","Q8hJtUvPUCDK8FY07qu6Ybijx","tFDpGPBbrV3OdqUe4rNpml0o5","v6Y9komkZyVuVvpjW5NWurfAT","oY0RfahlF1K4X8bZdvOYCa4oC","92pVypCfa2xlETbMvXBNkDE1P","VL1v0Xm82BqFWldOeNEnblBJQ","fjJoM12h1xeWNmVyZuDebzINd","mUsQjilBM3EarLdEBJooxr3Gi","n3RNVdoGblDJiVeo7urpxIDKQ","KgpAXNjl6bIrMgi1QVRdGG8F0","dh1aRKX1ZT2oAmIg6L6SUKA6h","5RRG9XHhHlII2lO9ne9LkUOb9","j9sOtN4W52Jf7Gz43A9zHYG8l","fzKeP5mMsWzfAfZLk92P2yWGq","tCkPtE1WrpnPZmCtTffS8kCRI","lsn27iZECuRNOgXCm62Vxfdfe","Oi1czs1GflvU26asdsJAkilA7","KCXWphuyUeZt0vZy7KRbW2qDO","qCul87jV2kCrUmadzprOP8b7J","wk1twmf7AFoqqCrOFfcIfbAzv","Rh7TOc67JUzTxre5js8j0Kkqa","LFvZCk7fsna6wsRKLKd3zE6p6","h79uAlDrU2BaMeL266G9MeluN","3CNjz2ooigMDkeR9E0hQ5fxeM","JV9NdDnxbC6pYZk8C2B6X9N4s","skMIdSMpgpZAcSmCDbEAP9sCB","fTsCrzfpHPcxhicFFInOLqR03","K62Kml4OaSNi3H3u55yY6yVcg","XVlZsb5pUXHkCvdiwEaIC3mrg"]
CONSUMER_SECRET = ["uLnfx6bxqhDCi8ts2ku8KUfmIc9EVUGP2NAOHCVflS0GkdZ2NW","7WSdmBPiXjRavJ7lJnPm3XDyGmVbsFURJmAaONKjbDvVR2NkZ2","FLjDzLdrtOVffyvku958vZyYgdQ7CYjuK5sD79eSUdS3HrNnzG","IJOrApswsvKpoCbO3BG1zM8w5GKgZfeJWFKziOpZBRHg9B7Tg1","i2hliODZHreLuQR0AIl8xSahRrQaBvBJD4ea1STsizonzcOYqj","GFP6MsUtIc8Xo9xzMNAmIEjMAyPocbdeWhsL6gqvfg2ZImQVmb","fAeR4ASu4b3OBvQ5qIZCdrfYaBSbqPNHmIP7VMgTzPWDHgwuZ1","AnJVUVt9kIFBAHM3tKMdWv3HjL3uxKhLsfz5dlrrAUP3bvoF9p","ZVbC1A0qMrAIp7gMIKqe8fRJVrABaxNnSgqdjNQv91ZtTWj1le","8azsDKLnKnivWXyRyxZEc9HskUQBTMZ1FvAXtDNDec3pB1w4La","9X1T0xI4v7ZaySVbUeQc9yyWUSdva7XjWynHaE7yVzudrSbgMm","dkzxMFiqxm2ypLbBoo8Q4sJLyexqz3BW6UCw6s7ULEOOmhnbME","FlARciNM0Z6Wq6zT4p8xjvO0OrYRqOxwXp0UB1hc9GMvP1WbQR","dHc9l5oFGbE873r0p67wbbOsYpVJ6BG0aab8KSfym4m6WL2lqV","DumBsdgvNylA2m08dgVbfzcR2gTJaKUroZX52XWWKrxsLirCPV","DKoZGGsPHAXQntAdLkwWnt4QD1zEIiGb39l1GhBHBvwmRBwmC7","R2uvODb3aY5RuF2zQTLwdPGq5FtGwUWZLn5J118Xwuu0A4wdr4","NxYI9bz8PFynS4rVXaMfzBL3AE9GOX6bFhOk2cAHDEcXsZafsf","YqGKF99KK8vheeuWaezoruVr4D71IS6nVCU20DkGeK5k0KhOov","4awmx4E7KEiAHgsntv7XtHINllICgcFzcVSaIXswfWD02EPfcy","qDp2H4Te7BM9pBzpIO7Y0EAFuQmD8tfD2UBtStFUxBoyONMr0k","y89MmVJY1DWs4Qmceh98jHsSynNw5xxEilxyCtvdqXYcgwaZTE","q8GBp89LLMawnXErwqwOaj1ciVoLbm6tifx9tsIsdZzY6WG2h4","Feo6LZvaOOSDsldWvpOV6eb3QMPB0Cptts3efJvd58OqBTMMnx","zVZAHamLSOau85aipMlCi2INNQqckKbD7eBv1o0pm6DWjtBMQS","liIwwLfKqbYGL1e4BfCZXjWWYHVzRCM9I9jkNNyNSpR36bP92N","ZXHdQ8K3eg7oaXIXZkuTDRLyuAnB2JPjKPJ7Y9GeQ5AlsmrNA0","bXDgB2XewMuWRHI11ErSBizum6WJvbc1F6TFT70HW1rN3LCcJK","HBKGGU8Lvd7VoOetBugaR9UTorNHypfCvVxTlqhSaXTuYoDLfI","CwGSMqPNWtxGQ0wseG4sMowfJMg3kuAkaKnTyDN0GELXsHxBNF","vZYNjwYFc1JNDUzJszINNu1ZG9HuDCeIBy4RzigslYYnl3XXY5","osnAeLAMdB9CIDbHzEz51EEUZx6L7pEiAOkOcDlfm78R9iY9:1M","lmeEXojaIZ2IDYRYtWREJ5VY9XVoydMMd1dCK5LobknsHLnZxG","KbUmzpikBz90DduZ0ST8WVTEZAFPuMUDw7rgSyGSugNxNeAfCo"]


OAUTH_TOKEN = ["4090852874-9K0DoVrW4kJpV1llgWZLSRuDetbUegL1maLYin0","4090852874-5q4yg5AbqAu2etkkbWLyLNEwfXJVO4wIr7OLJua","4090852874-KXAOwNwGhaugWttC9zNTDB7spgq0v33ubTu8SCT","4090852874-IOcuEUQmGaGndi1cGJOLDZtiNVYTB7suMvAAvfK","4090852874-68SyuuZto3m06VdmRftWlQZHh2qR0irmNFDuU4w","4090852874-fT8r7TDVCUj58qHoSfTvORlAib3FKieTusZy5fM","4090852874-QK3DEWmFQ53sh2Zu6tLaXrMOdmso5aIrzrygv2p","4090852874-UOToOVg9YKFMZhyCsyWUrjMHg3FYQesDBELXVoX","4090852874-2Ty9ElTY3fetQ1UsOQ7oniYByRKNHJG5nuZjOc5","4090852874-2j8SDwX79sAqOVOyIJ9R5Z6ZQqi5mHwKQn8nmey","4090852874-joS0AVlRgMBywCKinUxNeJZnfEiYOq1euVxmBba","4090852874-wrRkDthsifToYWLr2L7eDF57Gvbe2O8axyevdDm","4090852874-y0zwEoy55Kxs9rsLfvq51pfHqscXXUyzmbBWJIs","4090852874-Gqp3n8eJNNpT87hmak96mv0P43tCrKQPyb3kROy","4090852874-v0p3lkgkXHOimbk1SZ5jlXz8EqjRM91X6JgwNnq","dh1aRKX1ZT2oAmIg6L6SUKA6h","4090852874-cjXhvpubYzqzdjrAprJhm483u7E0ffiCBF80p1t","4090852874-WWFbKVQTdq0MSARlCRRu7TPZF0meiHqZF4loWrv","4090852874-gd9znPImkLTHzkFne5amFsLtjKTUppclmR0nbpS","4090852874-u5ca3iwb5Mt75slGxMuHqrYQhif5oz8viANEFbm","4090852874-8n80CKDfV2K2gJcPOEV7qzt5XlcZ10VkyGhZ8aP","4090852874-0qwsAXlo71bqhap4DS9z75HxtQZnDwbksYnPUOX","4090852874-JZpxtmuPwQQ2vGT7QmvsbJZBHYvpH7fKaX6W4Um","4090852874-IIMBuIdrjaUmv76AMBM2f5jwi4WRLjLyIOUhjt0","4090852874-QMQTSuGBW1c50oejLMjnqGbsbpwtHKl1ToYe8zQ","4090852874-doFOZNM3dPkegROrlQBTUnopI3XY1q2L5HVNMK2","4090852874-ouNhkGBxqS7fkqGDyHDBC44YQYaS82xToa6UOqJ","4090852874-1FvOtlmBOdFMO8pfJuqXuUHkC7pqi0kvQeQl9lB","4090852874-MrLc951HhE2TRIXDOBKoKtKT7YjSJMTwoopbLjy","4090852874-pPio5M5D6FDjZCCWS1za0JAzrSE2RdqLfXpI1DZ","4090852874-CqSoOrAzjm2Nj9iCZpPqUR1hvLGVbY1vYt9gpch","4090852874-sN08iTN51eKZeISfIq9J2jibtVHzeQh5tGBz6Vh","4090852874-fdJUCJXRPHM4Opb2XZ05yvdxVdEdhdSuzq6hGh8","4090852874-GrMvrmyo4xZerxLEjp10IoyTvzgrserdZZCyYGW"]
OAUTH_TOKEN_SECRET = ["RQGVgbLSEpJy2sxPvONPzEsV88XBsucu3cjzuYoIdidft","I35X2IngW0w4cfUQ4HWMg6epY33vETIgLuSyrN6RhT3zQ","C1dfSCs2aKpJ0p1d33yoECSl7ZEU2qZ2Jhv7wh6FyNDbi","UymeNzzOjYQxsnNmFXnOGoe5ZYdhIjlmLb2xRQfznPe6v","RbOfSoPViV643fXCZc2ym5h6uydI1In0m8QJEPUpGgfDa","rpL591YeOS54Vzh6sj8FeGt895EikthX61dTRzuDowZge","XGyRyyrhHAdqpvxO1CpTEUiwINwChS05Regdv1xqDlqkd","KJpYMp19D9lRejMG7KlLwjohDVUG7PFvpXobwGZ0GKtNI","YcSUvvQ81AAEJ90PXMnrpJ3EWCGjlbU2Q2uCbFNSq4IiT","wuFoP17uM3T3QDFgryCZe2K2nMjqm6MhfmTajaDuAfbz6","LuliKGVGE0MiwioC4uPSKsSdbLpzPJNQLld3PYNOKYwV8","7YrpwOg0fbDyquIHwz6v7sY2njCpLVTHeKLeBQwdAnSYD","kFBWZNhfyAAlQOEYPmCLVLnhz1J149L7zifLajgcNzVjT","KrmbAxqmkeDYrOgVncW5ALfCeR3B0C3KvYHdfSBzlInbb","h6K9vvcIaEghz7p32UjVGUKMaEWT6aYgB81bga6ESWySC","DKoZGGsPHAXQntAdLkwWnt4QD1zEIiGb39l1GhBHBvwmRBwmC7","cdonZGND9gd9Fs06IFQOltlfJYT0q7vRixl7zSN8DDhdM","8Z98vyRmNluwdTz5Y1D7EmiwUbiVDrIg14HUQlTxxM14T","or5xmHRCzIWkq6RmjK0FPaU9zJx37nonMxyytTSZd7baM","Y8RRWfxnGxRsmIOMXDcKmxrANxLgoBDNXrbrvEOLZYOCR","EqYniDHli1vH5o8nnWBeng7Yop3WUNPOKaEl4b1UVmxyR","bzjt8iLDU1Rx9j98dlTB14XuBED9peI6pfrQvfeGyYDbP","Ct2MLx5c4ctpcA6HB4zBU0YCWJB8UBVP9rmwxFdMYjj3K","ACr4XxiosDs9JR0GnuhTHqU9F5ki4wfonOFuFcA9G4JhO","EoHqtM2qeR6s2SBvkYNmWb5aqGUOJEqY35eAoiBakz5Pt","Pzs2nF9fBR59HkAqyPd2WRdKL0qYIQ8CC4RmPp5WRNLaR","6cIZrlviQ3AwHczNj3uy4jkkGWrZvkIPR0DTA6NdbChTu","YoEd1TlV0UXaIa4FLK1mYRwCVAhpuVjqohJvIJB3Tjrys","FrWSUDJDhLWEJ5Hzu8eE8isAhKtsG3zNn3U6HIHPDC6fn","9baFwTbd7GOT0LGN6qORjKDhn6W4Jv08d68HGX8eKtTFy","6bt1JrSN1nbfdYyy5TF6XgaMy8TndgmMps1M3RSOGoAGJ","wfUtTAp7fGCRnKugzDvIWNXf5gfKpToFEcjbaxuzlmTVL","mS2Q1wpmLp0SimZILtWlu0kcQ1YP19f0cPK4sI6VnhlYY","eN79Ya7i8jUUfinioAQnYKlhNBZ8zPxfVxoqXYhBBIhGs"]

user_id_list = []

    
def get_oauth(index):
    oauth = OAuth1(CONSUMER_KEY[index],
                client_secret=CONSUMER_SECRET[index],
                resource_owner_key=OAUTH_TOKEN[index],
                resource_owner_secret=OAUTH_TOKEN_SECRET[index])
    return oauth
                
def init():                                   
    f = open("/home/lgy/twitter_api/twitter_USA/data/original_user_id_0415.csv")
    for line in f:
        line = line.replace('\n','')
        user_id_list.append(line)
    f.close()
    

   
def main():
    init()
    
    f = open("./user_show.json",'a')
    
    key_index = 0
    id_index = 0
    
    while True:
        user_id = user_id_list[id_index] 
        oauth = get_oauth(key_index)
        url = "https://api.twitter.com/1.1/users/show.json?user_id=" +user_id
        try:
            r = requests.get(url=url, auth=oauth)
            data = r.json()
        except Exception as e:
                print e
        print r.status_code 
        if(r.status_code == 429):            
            key_index = key_index + 1
            if key_index > 33:
                key_index = 0
            oauth = get_oauth(key_index)
        elif  r.status_code == 401:
            key_index = key_index + 1
            if key_index > 33:
                key_index = 0
            oauth = get_oauth(key_index)
            id_index +=1
        if(r.status_code == 200):
            id_index +=1
            f.write(str(data))
            f.write('\n')
        if id_index == len(user_id_list):
            break
    f.close()
            
            
                        
main()     
        
        

