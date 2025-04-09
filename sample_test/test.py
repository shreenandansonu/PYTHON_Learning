from bank import *
shree = savingsAcct("shree", 1000)
shree.deposit(1000)
shree.GetBalance()

suru= savingsAcct("suru", 1000)
suru.withdrawal(500)

shree.Transfer(suru,1000)