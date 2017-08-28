from os import listdir
import glob,os
path= "C:\\Users\\snehi\\Desktop\\project"
os.chdir(path)
files=[x for x in listdir(path) if x.endswith('.txt')]
def removeunwanted(x,wordlist):
    y=""
    x.lower()
    for i in range (len(x)):
        if x[i] in 'abcdefghijklmnopqrstuvwxyz0123456789_':
            y+=x[i]
        if y not in wordlist:
            if len(y)!=0:
                wordlist.append(y)
    return (y,wordlist)
def dotproduct (file1,file2,wordlist):
    prod=0
    for i in wordlist:
        if i in file1:
            if i in file2:
                prod+=(int(file1[i])*int(file2[i]))
    return prod
def calcfreq (dct):
    val=dct.values()
    summ=0
    for i in val:
        summ+=i**2
    summ=summ**0.5
    return summ
length=len(files)
dict_list=[]
wordlist=[]
i=0
for file in files:
    dict_list.append({})
    temp_file=open(file)
    for line in temp_file:
        wordsinline=line.split(' ')
        for word in wordsinline:
            word=word.strip("\n")
            (word,wordlist)=removeunwanted(word,wordlist)
            if word not in dict_list[i]:
                if len(word)!=0:
                    dup=dict_list[i]
                    dup[word]=1
            else:
                dup=dict_list[i]
                dup[word]+=1
    i+=1
##print(dict_list)
for i in range(length):
    for j in range(i,length):
        if (len(dict_list[i])==0 or len(dict_list[j])==0):
            print(files[i],",",files[j],": Cant compare, One or both the files is empty or contains only special characters")
        else:
            result=(((dotproduct(dict_list[i],dict_list[j],wordlist))/(calcfreq(dict_list[i])*calcfreq(dict_list[j])))*100)
            print(files[i],",",files[j],": Plagiarism percent for the files is",result)


    
