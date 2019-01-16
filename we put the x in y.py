import re

def f(s, pat):
    pat = r'(\w*%s\w*)' % pat       # Not thrilled about this line
    return re.findall(pat, s)

# print (f("This is just a simple text to test some basic things", "si"))

with open('words_alpha.txt','r') as a:
    for wordtofind in a:
        if (len(str.rstrip(wordtofind)) > 1):
            with open('words_alpha.txt','r') as b:
                for wordtosearch in b:
                    if (f(wordtosearch,wordtofind) != []) and (wordtosearch != wordtofind) and (len(wordtofind) > 1):
                        text = 'We put the \"'+str.rstrip(wordtofind)+'\" in \"'+str.rstrip(wordtosearch)+'\"\n'
                        with open('we_put_the_x_in_y.txt','a') as out:
                            out.write(text)