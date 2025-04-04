from bank import *
print("_________________________________\n")
print("🙏 Wlecome to OOPS Bank of India 🙏")
print("_________________________________\n")


while True:
    print("1:- Create Account\n2:- Check Balance\n3:- Withdraw\n4:- Deposite\n5:- Transfer\n6:- Exit")
    print("_________________________________\n")
    
    service=int(input("Please Enter the number for the desired service:- "))
    print("_________________________________\n")

    match service:
        case 1:
            name,amount,pswd=input("Please Enter Name Amount and Password: ").split(",")
            Account(name,amount,pswd)
        case 2:
            name,pswd=input("Please Enter Name and Password: ").split(",")
            print("_________________________________\n")
            Account.GetBalance(name,pswd.strip())




