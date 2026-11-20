dictionary={"AAPL":180 ,"TSLA": 250}
stock_name=input("enter stock name : ").upper()
if stock_name not in dictionary:
    print("please enter valid stock name ")
else:
    quantity=int(input("enter quantity : "))
    output=dictionary[stock_name]*quantity
    print("your total investment = ", output, " $ ")
    save=input("do you want to save this stock ? yes/no ").lower()
    if save == "yes":
        file = open("portfolio.txt", "w")
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: {output} $\n")
        file.close()
        print("Saved to portfolio.txt ")