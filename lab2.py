vowls = ['a','e','i','o','u']
def removeVowels(txt):
    res=""
    for ch in txt:
        if ch not in vowls:
            res+=ch
    return res
      

txt =input()
print(removeVowels(txt)) 


###############################################


def characterLocator (txt,ch):
    res=[]
    for i in range(len(txt)):
        if txt[i]==ch:
            res.append(i)
    return res

txt =input()
char=input()
print (characterLocator(txt,char))


##################################################


def multiplicationTable(number):
    res=[]
    for i in range(1,number+1):
        list=[]
        for j in range (1,i+1):
            list.append(i*j)
        res.append(list)
    return res        


number =input()
print(multiplicationTable(number)) 


##############################################################

def calculateArea(shape, n1, n2=None):

    pi = 3.14   
    if shape == "t":          
        return 0.5 * n1 * n2
    elif shape == "r":        
        return n1 * n2
    elif shape == "s":        
        return n1 * n1
    elif shape == "c":   
        return pi * (n1*n1)
    else:
        return -1

print(calculateArea('c',2)) 

############################################################
def groupNames(names):
    result = {}

    for name in names:
        key = name[0]   
        if key not in result:
            result[key] = []

        result[key].append(name)

    return result

print(groupNames(["ahmed","mohamed","emad"])) 
#######################################################

def marioPyramid(n):
    for i in range(0,n):
        for j in range(0,n):
            if i+j>=n-1:
                print('*', end="")
            else:
                print(' ',end="")
        print()        

marioPyramid(3)