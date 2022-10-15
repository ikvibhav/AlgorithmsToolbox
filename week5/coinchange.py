import sys

def CoinChange_Recursion(CC_CoinsList, CC_MoneyVal):
    if CC_MoneyVal == 0:
        return 0
    
    AbsMinCoins = sys.maxsize

    for CoinVal in CC_CoinsList:
        if CoinVal <= CC_MoneyVal:
            MinCoins = 1 + CoinChange_Recursion(CC_CoinsList, CC_MoneyVal - CoinVal)
            if MinCoins < AbsMinCoins:
                AbsMinCoins = MinCoins
    
    if AbsMinCoins == sys.maxsize:
        return -1
    else:
        return AbsMinCoins

def CoinChange_DP(CC_CoinsList, CC_MoneyVal):
    MinCoinsList = [sys.maxsize]*(CC_MoneyVal+1)

    #Base Case
    MinCoinsList[0] = 0

    for i in range(1, CC_MoneyVal+1):
        for CoinVal in CC_CoinsList:

            if CoinVal <= i:
                
                # When i = CoinVal, that means that a Coin Denomination equals the CoinVal to be found
                # In this Case, MinCoinsList[0] is considered
                SubRes = MinCoinsList[i - CoinVal]
                if SubRes!=sys.maxsize and SubRes+1 < MinCoinsList[i]:
                    MinCoinsList[i] = SubRes + 1
    
    if MinCoinsList[CC_MoneyVal] == sys.maxsize:
        return -1
    
    return MinCoinsList[CC_MoneyVal]

if __name__ == "__main__":
    CoinsList = [1,3,4]
    MoneyVal = int(input())
    print(CoinChange_DP(CoinsList, MoneyVal))