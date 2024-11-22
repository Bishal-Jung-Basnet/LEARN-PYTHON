def addIntrest(balance, rate):
    for i in range(len(balance)):
        balance[i]=balance[i]*(rate+1)

def test():
    amount = [1000, 2000, 3000]
    rate = 0.5
    addIntrest(amount, rate)
    print(amount)
test()