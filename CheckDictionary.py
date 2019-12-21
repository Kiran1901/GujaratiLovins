#coding=utf-8
import re

class FastDictSearch():
    def __init__(self):
        self.index={}
        self.Dict="dictionarylist.txt"

    def sort_dict(self):
        dictFile = open(self.Dict, "r", encoding="UTF-16")
        index = [word for word in dictFile.readlines()]
        dictFile.close()
        index.sort()                                            # sorts file in increasing order
        dictFile = open(self.Dict, "w", encoding="UTF-16")
        for word in index:
            dictFile.write(word)                                # writes sorted data on the same file
        dictFile.close()

    def make_index(self):
        dictFile = open(self.Dict, "r", encoding="UTF-16")
        word = dictFile.readline()[:-1]
        while word:
            st = re.search("^\w?\W?", word)             #Extracts first one or two characters from word like ક,કો,ગા
            key = word[:st.end()]
            if key not in self.index:
                self.index[key] = dictFile.tell()       #Gets location from file
            word = dictFile.readline()[:-1]
        dictFile.close()

class CheckDictionary(FastDictSearch):

    def CheckDictionary(self,word):

        tmp = word[:re.search("^\w?\W?", word).end()]           #Extract first character from word

        if tmp in self.index.keys():
            loc = self.index[tmp]                               #Get starting location for extracted words
            dictFile = open(self.Dict,"r",encoding='UTF-16')
            out = open("out.csv","a",encoding="UTF-16")
            dictFile.seek(loc)                                  #Go to location of starting character

            line = dictFile.readline()[:-1]                 # line= word from dictionary file

            while(line):                                    #read dictionary words line by line

                if(line[:len(tmp)]==tmp):

                    if len(word)>=len(line):              #word is longer than that of dictionary

                        matched = re.search(line,word)          #search line in word
                        if matched is not None:

                            if len(word[matched.end():])>0:         # line + suff = word
                                suff = word[matched.end():]
                                out.write(word + "," + line + "," + matched.string + "," + suff + "\n")
                                dictFile.close()
                                out.close()
                                return True

                            elif matched.string == word:            # line == word
                                out.write(word + "," + line + "," + matched.string + "," + "Root" + "\n")
                                dictFile.close()
                                out.close()
                                return True


                    elif(len(word)<len(line)):             # word is shorter than that of line

                        matched = re.search(word,line)          # find word in line
                        if matched is not None:
                            if len(word[matched.end():]) > 0:       # word + suff = line
                                suff = line[matched.endpos:]
                                out.write(word + "," + line + "," + matched.string + "," + suff + "\n")
                                dictFile.close()
                                out.close()
                                return True

                else:
                    break

                line=dictFile.readline()[:-1]           # increment the line

            dictFile.close()
            out.close()
        return False

