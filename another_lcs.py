def add_words(line):
    list_words=line.split(' ')
    if len(list_words)>0:
        lastword=list_words[-1]
        lastword=lastword.strip('\n')
        list_words=list_words[:-1]+[lastword]
    if list_words==['']:
        list_words.remove('') 
    return(list_words)

def file_to_words(file):
    f=open(file)
    words=[]
    for line in f:
        words+=add_words(line)
    return(words)
def common_string(list1,list2,word1,word2):
    count=0
    while(word2<len(list2) and word1<len(list1) and list1[word1].lower()==list2[word2].lower()):
                        count+=(len(list2[word2]))
                        word1+=1
                        word2+=1
    return(count,word2)

def compare_words(list1,list2):
    word1=0
    word2=0
    maxu=0
    while (word1<len(list1)):
        while (word2<len(list2)):
            if list1[word1].lower()==list2[word2].lower():
                (count,word2)=common_string(list1,list2,word1,word2)
                if maxu<count:
                       maxu=count
            else:
                count=0
                word2+=1
        word1+=1
        word2=0
    return(maxu)
import os,glob
from os import listdir
path= "C:\\Users\\snehi\\Desktop\\project"
os.chdir(path)
files=[x for x in listdir(path) if x.endswith('.txt')]
for file1 in range(len(files)):
    for file2 in range(file1,len(files)):
        list1=file_to_words(files[file1])
        list2=file_to_words(files[file2])
        common=compare_words(list1,list2)
        all_letters=0
        for x in list1:
            all_letters+=len(x)
        for x in list2:
            all_letters+=len(x)
        try:
            result=((2*common)/all_letters)*100
            print(files[file1],",",files[file2],": Plagiarism percent by LCS method between the files is",result)
        except ZeroDivisionError:
            print(files[file1],",",files[file2],": Cant Compare, both the files are empty")
        
        
        
    
        
        
        
