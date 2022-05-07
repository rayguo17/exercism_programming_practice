from math import sqrt
from math import floor


def factors(value):
    result=[]
    if value<=1:
        return result
    if value<=3:
        result.append(value)
        return result
    index=2
    tmp=value
    while index<value:
        print("index:",index)
        if tmp %index ==0:
            result.append(index)
            tmp = tmp//index
            print(tmp)
            continue
        else:
            index+=1
        if tmp==1:
            break
            
    return result 
    

if __name__ == "__main__":
    value = 60
    
    print(factors(8))