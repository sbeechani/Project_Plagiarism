'''
Functions used for Bag_of_words
'''
def dotproduct (file1,file2,wordlist):
    '''
    This function accepts list of words for two files along with main wordlist and returns dot product for the common words in both the files
    '''
    prod=0
    for i in wordlist:
        if i in file1:
            if i in file2:
                prod+=(int(file1[i])*int(file2[i]))
    return prod
def calcfreq (dct):
    '''
    This function returns the denominator value for caculating cosine function by accepting and dictionary of words vs their frequencies
    and returning the euclidean norm of vector
    '''
    val=dct.values()
    summ=0
    for i in val:
        summ+=i**2
    summ=summ**0.5
    return summ
'''
Functions used for LCS
'''
def common_string(list1,list2,word1,word2):
    '''
    This function accepts the word lists of two files along with the indexes in the lists where the words matched and returns the count of continuos characters matched
    '''
    count=0
    while(word2<len(list2) and word1<len(list1) and list1[word1].lower()==list2[word2].lower()):
                        count+=(len(list2[word2]))
                        word1+=1
                        word2+=1
    return(count,word2)

def compare_words(list1,list2):
    '''
    This function accepts word lists of two files and returns maximum count of characters in largest common string
    '''
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

'''
Functions used for fingerprinting
'''


def hash_value(string):
    '''
    This function accepts a word and returns its hash value
    '''
    hashvalue=0
    i=0
    while(i<5):
        hashvalue+=(ord(string[i]))*(5**(5-i))
        i+=1
    return(hashvalue)

def isprime(num):
    '''
    This function accepts a number and returns if the number is prime
    '''
    if num%2==0:
        return(False)
    else:
        for i in range(3,int(num**0.5)+1):
            if num%i==0:
                return(False)
        return(True)

'''
class plagiarism and its methods
'''

class plagiarism (object):

    def __init__(self,file):
        self.file=file
        
    def splitting_words(self,wordlist,dictionary):
        '''
        This function accepts a file along with common wordlist and a dictionary corresponding to this file in list of dictionaries and updates the dictionary
        words in file as keys and its frequency as corresponding value
        '''

        def remove_unwanted(word,wordlist):
            '''
            This function accepts a word and appends word to the wordlist by retaining only letters,digits and underscore in a word and
            removing all other special characters
            '''
            y=""
            word.lower()
            for i in range (len(word)):
                if word[i] in 'abcdefghijklmnopqrstuvwxyz0123456789_':
                    y+=word[i]
                if y not in wordlist:
                    if len(y)!=0:
                        wordlist.append(y)
            return (y,wordlist)
            
        temp_file=open(self.file)
        for line in temp_file:
            wordsinline=line.split(' ')
            for word in wordsinline:
                    word=word.strip("\n")
                    word=word.lower()
                    (word,wordlist)=remove_unwanted(word,wordlist)
                    if word not in dictionary:
                        if len(word)!=0:
                           dictionary[word]=1
                    else:
                        dictionary[word]+=1
    def file_to_words(self):
        '''
        This function accepts a file and returns list of words in that file
        '''
        def add_words(line):
##        '''
##        This function accepts a line and returns list of valid words stripping of '\n' and eliminating nulls
##        '''
            list_words=line.split(' ')
            if len(list_words)>0:
                lastword=list_words[-1]
                lastword=lastword.strip('\n')
                list_words=list_words[:-1]+[lastword]
            if list_words==['']:
                list_words.remove('') 
            return(list_words)

        f=open(self.file)
        words=[]
        for line in f:
            words+=add_words(line)
        return(words)

    def refine_words(self):
        '''
        This function accepts a file and returns a long string, eliminating stop words, spaces and other special characters in the file
        '''
        mainstring=""
        stop_words=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
        for line in open(self.file):
            wordsinline=line.split(' ')
            for word in wordsinline:
                word=word.lower()
                newword=""
                for letter in word:
                    if letter in "abcdefghijklmnopqrstuvwxyz0123456789":
                        newword+=letter
                if newword not in stop_words:
                    mainstring+=newword
        return mainstring
'''
Main Function
'''
import time
import glob,os
path= "C:\\Users\\snehi\\Desktop\\classes implementation"
os.chdir(path)
files=[x for x in os.listdir(path) if x.endswith('.txt') and x!="display.txt"]##considers all text files in the mentioned path except logfile
ltime=time.ctime()
display1=open("display.txt",'a+')
display1.write(time.ctime())##displays current time
display1.write('\n')

'''
Bag_of_words
'''
print("Comparision by Bag of words method")
display1.write("Comparision by Bag of words method"+ '\n')
length=len(files)
for i in range(length):
    for j in range(i,length):
                f1=plagiarism(files[i])
                f2=plagiarism(files[j])
                wordlist=[]
                dict_list=[{},{}]
                f1.splitting_words(wordlist,dict_list[0])
                f2.splitting_words(wordlist,dict_list[1])
                if (len(dict_list[0])==0 or len(dict_list[1])==0):##handling the zerodivision error by eliminating the case of comparing empty files
                    print(files[i],",",files[j],": Cant compare, One or both the files is empty or contains only special characters")
                    display1.write(str(files[i])+" , "+str(files[j])+" : Cant compare, One or both the files is empty or contains only special characters"+ '\n')
                else:
                    result=(((dotproduct(dict_list[0],dict_list[1],wordlist))/(calcfreq(dict_list[0])*calcfreq(dict_list[1])))*100)##calculating distance between two documents by cosine similarity
                    print(files[i],",",files[j],": Plagiarism percent for the files is",result)
                    display1.write(str(files[i])+" , "+str(files[j])+" : Plagiarism percent for the files is "+str(result)+'\n')
'''
Largest Common String
'''
print("---------------------------------------")
display1.write("---------------------------------------"+'\n')
print("Comparision by lcs method")
display1.write("Comparision by lcs method"+'\n')
for file1 in range(len(files)):
    for file2 in range(file1,len(files)):
            f1=plagiarism(files[file1])
            f2=plagiarism(files[file2])
            list1=f1.file_to_words()
            list2=f2.file_to_words()
            common=compare_words(list1,list2)
            all_letters=0
            for x in list1:
                all_letters+=len(x)##gets the length of combined strings in file1
            for x in list2:
                all_letters+=len(x)##gets the length of combined strings in file2
            try:
                result=((2*common)/all_letters)*100 ## calculating LCS
                print(files[file1],",",files[file2],": Plagiarism percent between the files is",result)
                display1.write(str(files[file1])+" , "+str(files[file2])+" : Plagiarism percent between the files is "+str(result)+'\n')
            except ZeroDivisionError:
                print(files[file1],",",files[file2],": Cant Compare, both the files are empty")
                display1.write(str(files[file1])+" , "+str(files[file2])+" : Cant Compare, both the files are empty")

'''
Fingerprinting
'''
print("---------------------------------------")
display1.write("---------------------------------------"+'\n')
print("Comparision by fingerprinting method")
display1.write("Comparision by fingerprinting method"+'\n')
for file1 in range(len(files)):
    for file2 in range(file1,len(files)):
        f1=plagiarism(files[file1])
        f2=plagiarism(files[file2])
        mainstring1=f1.refine_words()
        mainstring2=f2.refine_words()
        (hashes1,hashes2)=([],[])
        if len(mainstring1)<5 or len(mainstring2)<5:
            print(files[file1],files[file2],": One or both the files are too small to create fingerprint")
            display1.write("One or both the files among "+str(files[file1])+", "+str(files[file2])+" are too small to create fingerprint"+'\n')
        else:
            i=0
            while(i<=(len(mainstring1)-5)):##creating hashes of length 5
                hashi=mainstring1[i:i+5]
                hashvalue=hash_value(hashi)
                hashes1.append(hashvalue)
                i+=1
            i=0
            while(i<=(len(mainstring2)-5)):
                hashi=mainstring2[i:i+5]
                hashvalue=hash_value(hashi)
                hashes2.append(hashvalue)
                i+=1
            large=max(len(hashes1),len(hashes2))
            large=large*100
            while(True): ##calculating a prime number larger than (number of hashes*100)
                large+=1
                if isprime(large):
                    break
            (finger1,finger2)=([],[])
            for value in hashes1:
                v=value%large
                finger1.append(v)##diving each hashvalue with selected prime number
            for value in hashes2:
                v=value%large
                finger2.append(v)
            match=[]        
            for value in finger1:
                if value in finger2:
                    c=min(finger1.count(value),finger2.count(value))
                    if value not in match:
                        for n in range(c):
                            match.append(value)
            plag_percent=((2*len(match))/(len(finger1)+len(finger2))*100)##calculating plagiarism percent by fingerprinting
            print(files[file1],files[file2],": plagiarism percent between the files is",plag_percent)
            display1.write(str(files[file1])+str(files[file2])+" : plagiarism percent between the files is "+str(plag_percent)+'\n')
display1.close()

    
