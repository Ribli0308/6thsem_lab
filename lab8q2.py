class Factory:
    def info(self, region, productManafactured):
        self.region = region
        self.item = productManafactured

class Wholesale(Factory):
    def pricing(self, item1, price1, item2, price2):
        self.itemsDict = {}
        self.itemsDict[item1] = price1
        self.itemsDict[item2] = price2

class Retailer(Wholesale):
    def printDetails(self):
        print("Region: ", self.region)
        print("Product Manafactured: ", self.item)
        print(self.itemsDict)

obj = Retailer()
obj.info('Jharkhand', 'SteelandIron')
obj.pricing('iron', 10000, 'steel', 30000)
obj.printDetails()