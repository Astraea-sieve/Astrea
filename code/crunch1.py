import re
import string

data=open("C:/Users/Edmund/Desktop/Astraea/Data/AllPosts.txt","r",errors='ignore')
wordListFile=open("C:/Users/Edmund/Desktop/Astraea/Data/keyWords.csv","r",errors='ignore')

data2=[]
wordList=[]

for line in data:
    line.encode('ascii',errors='ignore')
    l1=line.strip("\n")
    l2=re.sub("\?","." ,l1)
    l3=re.sub("\!",".",l2)
    l4=re.sub("\)",".",l3)
    l5=l4.strip()
    l6=l5.lower()
    l7=re.sub("[^a-z0-9 ]","",l6)
    #l7=l6
    l8=[l7,0]
    if len(l7)>0:
        data2.append(l8)

for phrase in wordListFile:
    phrase.encode('ascii',errors='ignore')
    phrase=phrase.strip("\n")
    wordList.append(phrase)

        
#for post in data2:
    #for word in dict:
        #if re.search(word,post[0]):
        #if re.search('bitch',post[0]):
#   post[1]=1

for i in range(len(data2)):
    for j in range(len(wordList)):
        if re.search(wordList[j],data2[i][0]):
            data2[i][1]=1
            
data.close()
wordListFile.close()

otFile=open("C:/Users/Edmund/Desktop/Astraea/Data/scoredPosts.csv","w")

for post in data2:
    otFile.write(post[0]+','+str(post[1])+','+'\n')


otFile.close()

