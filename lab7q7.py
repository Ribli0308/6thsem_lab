#7. wap class called restaurant with attributes: menu items, book table, customer order and design suitable methods to perform: add items to the menue, make table reservations and also take order ad print all[use dict and lists to store the data].
class Restaurant:
    def __init__(self):
        self.menuItems = {}
        self.bookTable = []
        self.orders = []

    def addToMenu(self, item, price):
        self.menuItems[item] = price

    def booking(self, tableNumber):
        self.bookTable.append(tableNumber)

    def customerOrder(self, tableNumber, order):
        orderDetails = {'tableNumber': tableNumber, 'order': order}
        self.orders.append(orderDetails)

    def printMenu(self):
        for item, price in self.menuItems.items():
            print("{}: {}".format(item, price))

    def printReservations(self):
        for table in self.bookTable:
            print("Table {}".format(table))

    def printOrders(self):
        for order in self.orders:
            print("Table {}: {}".format(order['tableNumber'], order['order']))

restaurant = Restaurant()

restaurant.addToMenu("Cheeseburger", 999)
restaurant.addToMenu("Mexican Salad", 800)
restaurant.addToMenu("Pizza", 199)
restaurant.addToMenu("French Fries", 399)
restaurant.addToMenu("King Fish", 150)
restaurant.booking(1)
restaurant.booking(2)
restaurant.customerOrder(1, "Pizza")
restaurant.customerOrder(2, "King Fish")
print("\nPopular dishes in the restaurant along with their prices:")
restaurant.printMenu()
print("\nTable reserved in the Restaurant:")
restaurant.printReservations()
print("\nPrint customer orders:")
restaurant.printOrders()
