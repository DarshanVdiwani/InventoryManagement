
from product import Product

Product.createObjectsFromCsv()

while True:
    print("Press 1 to make new sell")
    print("Press 2 to make purchase")
    print("Press 3 to display all stock")
    print("Press 4 to show total profit")
    print("Press 5 to add new product to stock")
    print("Press 6 to remove product to stock")
    # print("Press 7 to save & exit")
    print("Press 7 to save & exit")

    print("Press 8 to exit without saving")

    choice = int(input())

    # Product.printAllStock()

    if choice == 1:
        Product.generateBill()

    elif choice == 2:
        Product.makePurchase()

    elif choice == 3:
        Product.printAllStock()

    elif choice == 4:
        print("Total profit till date =", Product.calculateTotalProfit())

    elif choice == 5:
        Product.addProduct()

    elif choice == 6:
        Product.removeProduct()
    
    elif choice == 7:
        Product.saveExit()
        break

    elif choice == 8:
        break

    else:
        print("Invalid input, please try again...")

    # Product.printAllStock()
