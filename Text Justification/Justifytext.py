def mergeAlternately(word1, word2):

    finalword = []
    word1list = list(word1)
    word2list = list(word2)
    length1 = len(word1list)
    length2 = len(word2list)
    if length1 > length2:
        legth = length1
    else:
        legth = length2
    for i in range(legth):
        if(len(word1list) > len(word2list)):
            finalword.append(word1list[i])   
            if(len(word2list) > i):
                finalword.append(word2list[i])
        else:
            if(len(word1list) > i):
                finalword.append(word1list[i])
            finalword.append(word2list[i])   
            
            
    str1 = ""
    # traverse in the string
    for ele in finalword:
        str1 += ele
 
    print(str1)
    return  str1
    
    
    
    

word1 = "abc"
word2 = "pqr"
    
mergeAlternately(word1, word2)

