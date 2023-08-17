def reverseWords(s):
    ListWords = s.split()
    ListWords.reverse()
    str = ""
    for index ,word in enumerate(ListWords):
        if (index !=0):
            str +=  " " + word
        else:
            str += word

    return str
        
        
        
s = "the sky is blue"

out = reverseWords(s)
print(out)