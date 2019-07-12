from CheckDictionary import CheckDictionary
from Checkstopword import Checkstopword


def A(base):
    # A   No restrictions on stem
    return len(base) > 1


def B(base):
    return len(base) > 2


def C(base):
    return len(base) > 3


def D(base):
    return len(base) > 4


m = [None] * 9

m[8] = dict((('વાળાઓનું', C), ('ાવડાવવું',B )))

m[6] = dict((
    ('વાળાઓએ', C ), ('ાવનારો', A), ('ેવડાવી', A), ('ેવડાવો', A), ('ાવવાને', A), ('ોમાંથી', A), ('ામાંથી', A),
    ('ઓમાંથી', A), ('ોમાંની', A), ('ોમાંના', A), ( 'નારનું', A), ('નારાનો', A), ('વેરાને', A), ('વેરાના', A)))

m[7] = dict((
    ('વાળાઓની', A), ('વાળાઓને', A), ('વાળાઓનો', A), ('નારાઓની', A), ('ોવાળાના', A), ('વાલીનું', A), ('ાવવામાં', A),
    ('ીઓમાંથી', C)))

m[5] = dict((
    ('ીવાળી', C), ('વાળાઓ', A), ('વાળાએ', A), ('વાલાએ', A), ('વાલીએ', A), ('માંથી', A), ('ાઓનું', A), ('ાઓનાં', A),
    ('ીઓનું', C), ('માનનો', A), ('માનને', A), ('ાવેલી', A), ('વાળું', A), ('વામાં', A), ('વાનું', A), ('માંના', A),
    ('નારાઓ', A), ('નારાએ', A), ('નારના', A), ('નારને', A), ('નારનો', A), ('નારની', A), ('પૂ઼ણઁ', A)))

m[4] = dict((
    ('વાલી', A), ('ાવવા', A), ('ાઓનો', A), ( 'ીઓની', C), ('ીઓનો', C), ('ીઓને', C), ( 'ાઓને', A), ('ાઓથી', A),
    ('ાઓની', A), ('ોઓથી', A), ('ઓમાં', A), ( 'વાળા', A), ('વાળી', A), ( 'વાળો', A), ('વાના', A), ('વાની', A),
    ('વાનો', A),
    ('વાને', A), ('વાથી', A), ('વાલા', A), ('ઓનું', A), ('ઓનાં', A), ( 'શાળી', A), ('નારા', A), ('ોમાં', A),
    ('ામાં', A), ( 'ીમાં', A),
    ('ેનું', A), ( 'ોનું', A), ('ોનાં', A), ('વેરા', A), ('ીનાં', C), ( 'ીનું', C)))

m[3] = dict((
    ('ાઓએ', A), ('ઓથી', A), ('વવા', A), ('ઓની', A), ('ઓના', A), ('ઓને', A), ('ઓનો', A), ('ઓથી', A), ('એથી', A),
    ('નાર', A), ( 'કાળ', A), ('કાર', A), ( 'નાર', A), ('ોના', A), ('ોને', A), ('ાને', A), ('ેના', A), ('ીના', C),
    ('ેની', A), ('ોની', A), ( 'ીની', C), ('ોનો', A), ( 'ેથી', A), ('ોથી', A), ('ાથી', A), ('ીથી', C), ('ાનો', A),
    ('ોને', A), ('ીને', C), ( 'માન', A), ('ાની', A), ('ીતા', C), ('ોની', A), ('ાના', A), ('ેનો', A), ('ાશે', A),
    ('નાં', A), ( 'નું', A), ( 'માં', A), ('તાં', A), ( 'વું', A)))

m[2] = dict((
    ('ઓએ', A), ('ોએ', A), ('ીએ', C), ('ીઓ', A), ( 'ાઓ', A), ('ોએ', A), ('ેએ', A), ('ાએ', A), ('ના', A), ( 'ની', A),
    ('ને', A), ('નો', A), ('વા', A), ('તા', C), ( 'તો', A), ( 'થી', A), ('શો', A), ('શે', A), ( 'ું', A), ('ાં', A), ('સર', A)))

m[1] = dict((('ી', C), ('ે', B), ('ો', A), ('એ', A), ('ઓ', A), ( 'ા', A)))


def remove_ending(word):
    length = len(word)
    el = 8
    while el > 0:
        if length - el > 1:
            ending = word[length - el:]
            cond = m[el].get(ending)
            if cond:
                base = word[:length - el]
                if cond(base):
                    print(word + "\t\t" + ending, end="     ")
                    return base
        el -= 1
    return word


list = open("input.txt","r",encoding="utf-8-sig").read().split()
dictionary = CheckDictionary()
stopword = Checkstopword()
#dictionary.sort_dict()
dictionary.make_index()

for word in list:

    if word.endswith(","):
        word = word.replace(",", "")
    if word.startswith("‘"):
        word = word.replace("‘", "")
    if word.endswith("’"):
        word = word.replace("’", "")
    if word.startswith("'"):
        word = word.replace("'", "")
    if word.startswith('"'):
        word = word.replace('"', '')
    if word.endswith("."):
        word = word.replace(".", "")

    if (stopword.Checkstopword(word) == False):
        if (dictionary.CheckDictionary(word) == True):
            print(word + "    root")
        # else:
            # print("Not Found")
            # print(remove_ending(word))
