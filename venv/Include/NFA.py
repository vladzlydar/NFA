import random
stanPoczatkowy = 'q0'
stanyAkceptujace = ['q8', 'q9', 'q10', 'q11', 'q12', 'q18', 'q19', 'q20', 'q21', 'q22']
tablicaPrzejsc = {
    'q0':{'0':['q1','q3'], '1':['q1','q4'], '2':['q1','q5'], '3':['q1','q6'], '4':['q1','q7'], 'a':['q2','q13'], 'b':['q2','q14'], 'c':['q2','q15'], 'd':['q2','q16'], 'e':['q2','q17']},
    'q1':{'0':['q1','q3'], '1':['q1','q4'], '2':['q1','q5'], '3':['q1','q6'], '4':['q1','q7'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q2':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['q2','q13'], 'b':['q2','q14'], 'c':['q2','q15'], 'd':['q2','q16'], 'e':['q2','q17']},
    'q3':{'0':['q8'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q4':{'0':['X'], '1':['q9'], '2':['X'], '3':['X'], '4':['X'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q5':{'0':['X'], '1':['X'], '2':['q10'], '3':['X'], '4':['X'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q6':{'0':['X'], '1':['X'], '2':['X'], '3':['q11'], '4':['X'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q7':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['q12'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q8':{'0':['q8'], '1':['q8'], '2':['q8'], '3':['q8'], '4':['q8'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q9':{'0':['q9'], '1':['q9'], '2':['q9'], '3':['q9'], '4':['q9'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q10':{'0':['q10'], '1':['q10'], '2':['q10'], '3':['q10'], '4':['q10'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q11':{'0':['q11'], '1':['q11'], '2':['q11'], '3':['q11'], '4':['q11'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q12':{'0':['q12'], '1':['q12'], '2':['q12'], '3':['q12'], '4':['q12'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q13':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['q18'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q14':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['X'], 'b':['q19'], 'c':['X'], 'd':['X'], 'e':['X']},
    'q15':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['X'], 'b':['X'], 'c':['q20'], 'd':['X'], 'e':['X']},
    'q16':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['q21'], 'e':['X']},
    'q17':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['X'], 'b':['X'], 'c':['X'], 'd':['X'], 'e':['q22']},
    'q18':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['q18'], 'b':['q18'], 'c':['q18'], 'd':['q18'], 'e':['q18']},
    'q19':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['q19'], 'b':['q19'], 'c':['q19'], 'd':['q19'], 'e':['q19']},
    'q20':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['q20'], 'b':['q20'], 'c':['q20'], 'd':['q20'], 'e':['q20']},
    'q21':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['q21'], 'b':['q21'], 'c':['q21'], 'd':['q21'], 'e':['q21']},
    'q22':{'0':['X'], '1':['X'], '2':['X'], '3':['X'], '4':['X'], 'a':['q22'], 'b':['q22'], 'c':['q22'], 'd':['q22'], 'e':['q22']},
    'X':{'0':"", '1':"", '2':"", '3':"", '4':"", 'a':"", 'b':"", 'c':"", 'd':"", 'e':""}
}


def NFA(aktualnyStan,tabelaPrzejsc,stanyAkceptujace,word,sciezkaNFA):
    if word == "":
        nfaResult = aktualnyStan in stanyAkceptujace
        if nfaResult == True:
            sciezkaNFA.append(aktualnyStan)
            return (nfaResult,sciezkaNFA)
        if nfaResult == False:
            return (nfaResult,sciezkaNFA)
    else:
        letter = word[0:1]
        if (aktualnyStan in tabelaPrzejsc.keys()) and (letter in tabelaPrzejsc[aktualnyStan].keys()):
            remainder = word[1:]
            noweStany = tabelaPrzejsc[aktualnyStan][letter]
            print("Aktualny stan %s, Analiza litery %s" % (aktualnyStan, letter))
            for nowystan in noweStany:
                (nfaResult, sciezka) = NFA(nowystan,tabelaPrzejsc,stanyAkceptujace,remainder,sciezkaNFA)
                if nfaResult == True:
                    sciezkaNFA.append(aktualnyStan)
                    return (True , sciezkaNFA)
        return (False,sciezkaNFA)


file = open("words_to_analyze.txt","r")
for i in file:
    for j in [x.strip() for x in i.split("#")]:
        print("\nAnalizowany ciag : '%s'"%j)
        sciezkaNFA = []
        accept,sciezkaNFA= NFA(stanPoczatkowy,tablicaPrzejsc,stanyAkceptujace,j,sciezkaNFA)
        sciezkaNFA.reverse()
        if accept == True:
            print("Automat akceptuje analizowane slowo!")
            print("Sciezka NFA: %s" %sciezkaNFA)
        else:
            print("Automat nie akceptuje analizowane slowo")



