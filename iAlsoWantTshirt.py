getInput = 'nayannamantenet'
palinList = []
x = 2   
def checkPalindrome (word): 
    for x in range(len(word)+1):
        # if len(word[:x:])>=2:
            if word[:x:] == word[:x:][::-1]:
                palinList.append(word[:x:])
                return word[x::]
try:
    while len(getInput)!=0:    
        getInput = checkPalindrome(getInput)
except TypeError:
    print('TypeError ocurred')
    

try:
    if len(getInput)==3:
        print (*palinList,sep='\n')
    else: print ('impossible')
except:
    pass
