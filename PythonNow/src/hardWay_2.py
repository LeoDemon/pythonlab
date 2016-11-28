#!/usr/bin/env python

# filename: hardWay_2.py
# description: learning python for <<Learn Python the hard way>>:exercise 41
# author: Demon.Lee
# date: 2016.10.29

import random
import sys
pyVer = sys.version_info
if 2==pyVer[0]:
    from urllib import urlopen
else:
    from urllib.request import urlopen
import sys

WORD_URL="http://learncodethehardway.org/words.txt"
WORDS=[]

PHRASES={
    "class %%%(%%%):":"Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":"class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self,@@@)":"class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":"Set *** to an instance of class %%%.",
    "***.***(@@@)":"From *** get the *** function, and call it with parameters self,@@@.",
    "***.***='***'":"From *** get *** attribute and set it to '***'."
}

def convert(snippet, phrase):
    print('snppet==[%s], pharse==[%s]'%(snippet, phrase))
    class_names=[w.capitalize() for w in random.sample(WORDS, snippet.count('%%%'))]
    print('class_names==%s'%class_names)
    other_names=random.sample(WORDS, snippet.count('***'))
    print('other_names==%s'%other_names)
    results=[]
    param_names=[]
    for i in range(0, snippet.count('@@@')):
        param_count=random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
        print('sentence | result==[%s]'%result)
        for word in class_names:
            print('word==[%s]'%word)
            result = result.replace('%%%', word, 1)
            print('class_names | result==[%s]'%result)

        for word in other_names:
            print('word==[%s]'%word)
            result = result.replace('***', word, 1)
            print('other | result==[%s]'%result)

        for word in param_names:
            print('word==[%s]'%word)
            result = result.replace('@@@', word, 1)
            print('param | result==[%s]'%result)

        results.append(result)

    return results

def testEx41():
    PHRASE_FIRST = False
    if 2==len(sys.argv) and "english" == sys.argv[1]:
        PHRASE_FIRST = True

    for word in urlopen(WORD_URL).readlines():
        WORDS.append(word.strip())

    print('WORDS==%s'%WORDS[1])

    try:
        while True:
            snippets = []
            for kk in PHRASES.keys():
                snippets.append(kk)
            print('snippets==[%s]'%snippets)
            random.shuffle(snippets)
            for snippet in snippets:
                phrase = PHRASES[snippet]
                question,answer=convert(snippet, phrase)
                print('question | asnwer==[%s | %s]'%(question, answer))
                if PHRASE_FIRST:
                    question,answer=answer,question
                    print('question | asnwer==(%s | %s)'%(question, answer))

                print('qustion: [%s]'%question)
                input("> ")
                print("answer: [%s]\n\n"%answer)
    except EOFError:
        print("\nbye!")

if '__main__' == __name__:
    testEx41()
else:
    print('being imported by another module!')

