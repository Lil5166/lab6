def truthCheck(formula):
    # S0
    disjunctsList = formulaToDisjunctsList(formula)
    S = [disjunctsList]
    temporaryS = []

    # Формируем S1
    for i in range(len(S[0])):
        for j in range(i, len(S[0])):
            resolutionDisjunct = resolution(S[0][i], S[0][j])
            if resolutionDisjunct:
                if not inList(resolutionDisjunct, temporaryS):
                    temporaryS.append(resolutionDisjunct)
    S.append(temporaryS)
    if checkForEmptyDisjuncts(S[0]): return "правильне"

    # Метод резолюций для последующих Sn
    sCounter = 0
    while True:
        temporaryS = []
        missingResolutions = 0
        for i in range(len(S[sCounter])):
            for j in range(1, len(S[sCounter + 1])):
                resolutionDisjunct = resolution(S[sCounter][i], S[sCounter + 1][j])
                if resolutionDisjunct:
                    if not inList(resolutionDisjunct, temporaryS):
                        temporaryS.append(resolutionDisjunct)
                else: missingResolutions += 1
        S.append(temporaryS)

        if checkForEmptyDisjuncts(S[sCounter + 1]): return "правильне"
        if missingResolutions == len(S[sCounter]) * (len(S[sCounter + 1]) - 1): return "неправильне"
        sCounter += 1


def formulaToDisjunctsList(formula):
    disjunctsList = []
    implicationsList = formula.split(",")
    for i in range(len(implicationsList)):
        if implicationsList[i][1] == "-":
            disjuncts = implicationsList[i].split("->")
            if disjuncts[0][0] == '¬':
                disjuncts[0] = disjuncts[0][1]
            else:
                disjuncts[0] = '¬' + disjuncts[0]
        if implicationsList[i][1] == "V":
            disjuncts = implicationsList[i].split("V")
        disjunctsList.append(disjuncts)
    return disjunctsList


def oppositeDisjunct(disjunct):
    if disjunct[0] == '¬':
        disjunct = disjunct[1]
    else: disjunct = '¬' + disjunct[0]
    return disjunct


# A V B, ¬A V C -> B V C
def resolution(disjuncts1, disjuncts2):
    resolutionDisjunct = []
    # находим А
    for i in range(len(disjuncts1)):
        for j in range(len(disjuncts2)):
            if disjuncts1[i] == oppositeDisjunct(disjuncts2[j]):
                # Если В == "∅", то меняем его местами с С согласно правилу комутативности дизъюнкции,
                # для удобства последующих вычислений
                if disjuncts1[i^1] == "∅": resolutionDisjunct = [disjuncts2[j^1], disjuncts1[i^1]]
                else: resolutionDisjunct = [disjuncts1[i^1], disjuncts2[j^1]]
    return resolutionDisjunct


def inList(disjunct, sList):
    if disjunct in sList: return True
    elif list(reversed(disjunct)) in sList: return True
    else: return False


def checkForEmptyDisjuncts(disjunctsList):
    for disjunct in disjunctsList:
        if disjunct[0] == '∅' and disjunct[1] == '∅': return True
    return False