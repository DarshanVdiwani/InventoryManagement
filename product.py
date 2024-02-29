import csv
import pandas as pd

class Product():
    allStock = []
    allBills = []
    allPurcheses = []
    discount = 0.2
    threshold = 25

    def __init__(self, name: str, stock: int, mrp: float, dealerPrice):
        assert stock >= 0, f'Stock of {name} should be at least 0, you entered: {stock}.'
        assert mrp > 0, 'mrp can be only positive values.'
        assert dealerPrice > 0, 'Dealer price can be only positive values.'

        self.name = name
        self.stock = stock
        self.mrp = mrp
        self.dealerPrice = dealerPrice
        Product.allStock.append(self)

    # @property
    # def name(self):
    #     return self.name

    # @name.setter
    # def name(self):
    #     pass
    def calculateTotalMrp(self):
        self.totalMrp = self.stock * self.mrp

    def applyDiscount(self):
        self.mrp = self.mrp - self.mrp * self.discount

    def __repr__(self):     # repr: representation
        return f'({self.name}, {self.stock}, {self.mrp}, {self.dealerPrice})'

    @staticmethod
    def printAllStock():
        print('Sr.No\t' + 'Name\t'.expandtabs(20) + 'Stock\tmrp'.expandtabs(8))
        sr_no = 1
        for instance in Product.allStock:
            print(f'{sr_no}\t' + f'{instance.name}\t'.expandtabs(20) +
                  f'{instance.stock}\t{instance.mrp}'.expandtabs(8))
            sr_no += 1

    @staticmethod
    def generateBill():
        items = []
        print("Enter quantity of the following products:")
        totalMrp = 0
        totalDP = 0
        totalProfit = 0
        for product in Product.allStock:
            quantity = int(input(f"{product.name}: "))
            mrp = product.mrp * quantity
            dp = product.dealerPrice * quantity
            profit = mrp - dp
            totalMrp = totalMrp + mrp
            totalDP += dp
            totalProfit += profit
            items.append((product.name, product.mrp, quantity, mrp))
            product.stock -= quantity
        # print(items)
        items.insert(0, (totalMrp, totalDP, totalProfit))
        Product.allBills.append(items)
        print("Sr.No\t_Name of Item\tRate\tQty\tPrice")
        sr_no = 1
        i = 0
        for item in items:
            if i == 0:
                i += 1
                continue
            if item[2] != 0:
                print(
                    f"{sr_no}\t" + f"{item[0]}\t".expandtabs(16) + f"{item[1]}\t{item[2]}\t{item[3]}")
                sr_no += 1

        print("-"*45)
        print("Total:" + f"{totalMrp}".rjust(37))

    @classmethod
    def createObjectsFromCsv(cls):
        df = pd.read_csv(".\product.csv")
        # print(df.head())
        for i in range(len(df.head())):
            cls(str(df.loc[i]["name"]), int(df.loc[i]["stock"]), float(df.loc[i]["mrp"]), float(df.loc[i]["dealerPrice"]))
        
    # with open('product.csv') as f:
    #     reader = csv.DictReader(f)

    #     for line in reader:
    #         cls(str(line['name']), int(line['stock']), float(line['mrp']), float(line['dealerPrice']))

    @staticmethod
    def calculateTotalProfit():
        totalProfit = 0
        for bill in Product.allBills:
            totalProfit += bill[0][2]
        return totalProfit

    @staticmethod
    def makePurchase():
        order = []
        totalDP = 0
        print("Enter quantity of the following products:")
        print("Product _Name\tMinimum Recommended\tYour Choice")
        for product in Product.allStock:
            recomended = product.threshold - product.stock
            if recomended < 0:
                recomended = 0
            quantity = int(input(f"{product.name}:\t{recomended}\t".expandtabs(20)))
            dp = product.dealerPrice * quantity
            totalDP += dp
            order.append(
                (product.name, product.dealerPrice, quantity, totalDP))
            product.stock += quantity

        Product.allPurcheses.append(order)

    @staticmethod
    def saveExit():
        df = pd.read_csv("E:\inventory_management\product.csv")
        count=0
        for i in Product.allStock:
            df.loc[count, 'stock'] = i.stock
            count+=1
            print(i.stock)
            df.to_csv("E:\inventory_management\product.csv", index=False)

# append data frame to CSV file
    @staticmethod
    def addProduct():
        df = pd.read_csv("E:\inventory_management\product.csv")
        df.loc[len(df.index)+1] = [str(input("Enter Product name :")), int(input("Enter how many unit purchase :")), float(input("Enter product mrp :")),float(input("Enter product Dealer Price :"))] 
        df.to_csv("E:\inventory_management\product.csv", index=False)

    @staticmethod
    def removeProduct():
        # Product.printAllStock()
        df = pd.read_csv("E:\inventory_management\product.csv")
        print(df)
        r_product=int(input("Remove product Index :"))
        df.drop(r_product,axis=0,inplace = True)
        print(df)
        df.to_csv("product.csv",index=False)


# if __name__ == "__main__":
#     Product.removeProduct()

