def greedy_money_change(G_MoneyValue):
    return G_MoneyValue//10 + (G_MoneyValue%10)//5 + ((G_MoneyValue%10)%5)

if __name__ == "__main__":
    MoneyVal = int(input())
    print(greedy_money_change(MoneyVal))        