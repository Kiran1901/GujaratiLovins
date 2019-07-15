#coding=utf-8
import re

class fastDictSearch():
    def __init__(self):
        self.index={}
        self.Dict="dictionarylist.txt"

    def sort_dict(self):
        f = open(self.Dict, "r", encoding="UTF-16")
        index = [word for word in f.readlines()]
        f.close()
        index.sort()
        f = open(self.Dict, "w", encoding="UTF-16")
        for word in index:
            f.write(word)
        f.close()

    def make_index(self):
        f = open(self.Dict, "r", encoding="UTF-16")
        word = f.readline()[:-1]
        while word:
            st = re.search("^\w?\W?", word)
            key = word[:st.end()]
            if key not in self.index:
                self.index[key] = f.tell()
            word = f.readline()[:-1]
        f.close()

class CheckDictionary(fastDictSearch):
    def CheckDictionary(self,word):

        # Check = 1;
        #
        # try:
        #     list = open('dictionarylist.txt',encoding='utf-16').read().split()
        #
        #     for dword in list:
        #         if (dword == word):
        #             Check = 0
        # except Exception:
        #     print("error in checkDictionary")
        # if (Check == 0):
        #     return True
        # else :
        #     return False;
        Check = 0
        if word[:2] in self.index.keys():
            loc = self.index[word[:2]]


            f = open(self.Dict,"r",encoding='UTF-16')
            f.seek(loc)
            suff=[]
            line = f.readline()[:-1]
            while(line):
                if(word[:2]!=line[:2]):
                    break
                else:
                    r = re.search(line,word)
                    if r is not None:
                        Check = 1
                        if(r.end()<=len(word)-1):
                            suff = word[r.end():]
                            if(len(suff)==0):
                                print("word: ",word," RoOt")
                                break
                            matched = word[:r.end()]
                            print("word: " + word + " line: " + line + " Matched " + matched + " suff: " + suff)
                line=f.readline()
            f.close()

        if Check:
            return True
        else :
            return False

