user1 = ''
user2 = ''
result1 = ''
result2 = ''

import tweepy
from tweepy import OAuthHandler

consumer_key = 'O5ZLoPi5H0PbmBDEdy8xcrACd'
consumer_secret = 'cLeQFWD6TQefTSFHTNgnvg0XOWZpI3nGj5KQuRoJxqR08RGFR4'
access_token = '835550501102051329-cfM2Mm1P1KFNbp6syzEIARECSIOA4kJ'
access_secret = '45Spr0z5O7tUo4i872eVlqEOAbizaQKYA1cG28ixyQ50D'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


print("DOSTE TO ONOMA TOY 1ou XRISTI:")
print("1os XRISTIS:")
user1=input()
print()

print("DOSTE TO ONOMA TOY 2ou XRISTI:")
print("2os XRISTIS:")
user2=input()
print()

i = 1
qtweet =[]
stuff =[]
stuff = api.user_timeline(onoma = user1, count = 10, )
for qtweet in stuff:
    result1 += str(i) + ") " + str(qtweet.created_at) + " *** " + qtweet.text + '\n'
    i+=1
    

i = 1
qtweet =[]
stuff = []
stuff = api.user_timeline(onoma = user2, count = 10, )
for qtweet in stuff:
    result2 += str(i) + ") " + str(qtweet.created_at) + " *** " + qtweet.text + '\n'    
    i+=1
    

print()
print()
print(user1 + ": PERIEXEI " + str(len(result1.split())) + " LEKSEIS.")
print(result1)    
print()
print()
print(user2 + ": PERIEXEI " + str(len(result2.split())) + " LEKSEIS.")
print(result2) 


print()
print()
if (len(result1.split()) > len(result2.split())):
    print("O XRISTIS " + user1 + " EXEI PERISSOTERES LEKSEIS STA 10 TELEYTAIA  TWEETS")
elif (len(result2.split()) > len(result1.split())):
     print("O XRISTIS " + user2 + " EXEI PERISSOTERES LEKSEIS STA 10 TELEYTAIA TWEETS")
else:
    print("OI XRISTES " + user1 + ", " + user2 + " EXOUN TON IDIO ARITHMO LEKSEWN")