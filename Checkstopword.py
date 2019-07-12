#coding=utf-8
class Checkstopword:
    def Checkstopword(self,word):
        Check = 1;
        try:
            list = open('gujarati_stop_words_daiict.txt',encoding='utf-16').read().split()
            for stword in list:
                if (stword == word):
                    Check = 0;
                    break

        except (Exception ):
            print("error in Checkstopword")

        if (Check == 0):
            return True;
        else:
            return False;


