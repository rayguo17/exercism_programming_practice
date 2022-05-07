from multiprocessing.sharedctypes import Value


def find_fewest_coins(coins, target):
    #first check coins and target is negative value or not
    if target <0:
        raise ValueError("value cannot be negative")
    for i in coins:
        if i <0:
            raise ValueError("value cannot be negative")
    #then check whether target smaller than smallest coins
    if target<coins[0]:
        raise ValueError("value cannot be smaller than smallest coin")
    index = len(coins)-1
    result = []
    tmp = target
    while index != -1 :
        if tmp - coins[index]>=0:
            result.append(coins[index])
            tmp = tmp-coins[index]
            if tmp==0 :
                break
        else:
            index-=1
    if tmp>0 and index==-1:
        raise ValueError("cannot solve the problem!")
    #print(result)
    #print(tmp)
    #print(index)
    return result

if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    target=1
    find_fewest_coins(coins,target)    

