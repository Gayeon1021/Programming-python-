import os

data=os.listdir("c:\Users")      #상대 경로 ,현재 디렉터리
#print(data)
for d in data:
    print (d)
    print("is directory?:"+str(os.path.isdir(d)))
    print("is file" + str(os.path.isdir(d)))