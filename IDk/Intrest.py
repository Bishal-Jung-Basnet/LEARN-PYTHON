def add(balance, rate):
    NewBalance = balance*(1+rate)
    return NewBalance

def test():
    amount = 1000
    rate = 0.05
    amount=add(amount, rate)
    print(amount)
test()