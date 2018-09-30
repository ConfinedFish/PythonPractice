import operator
from distutils.util import strtobool
from os import linesep

class Product(object):
    def __init__(self,catagory,name,quantity,price):
        self.catagory = catagory
        self.name = name
        self.quantity = quantity
        self.price = price
    def subtotal(self):
        return self.quantity * self.price
def API():
    products = read_file()
    sortkey = ask_receipt_format()
    total = calculate_total(products)
    print_bill(products,sortkey,total)
def read_file():
    products = []
    with open('grocery.txt', 'r') as f:
        for line in f.readlines():
            items = line.strip().split(' ')
            products.append(Product(int(items[0]),items[1],int(items[2]),float(items[3])))
    return products
def ask_receipt_format():
    formatin = int(input("How would you like your reciept formated? \n1: Alphabetically \n2: Catagory \n3: Price "))
    print(" ")
    if formatin is 1:
        return operator.attrgetter('name')
    elif formatin is 2:
        return operator.attrgetter('catagory')
    elif formatin is 3:
        return operator.attrgetter('price')
    else:
        raise ValueError("Incorrect format: %f" % formatin)
def calculate_total(products):
    total = 0
    for product in products:
        total += product.subtotal()
    return total
def print_bill(products,sortkey,total):
    products.sort(key=sortkey)
    results = ["Category  Name           Quantinty   Price     Subtotal"]
    for product in products:
        results.append("%-10i%-15s%-12i%-10.2f%-10.2f" % (product.catagory, product.name, product.quantity, product.price, product.subtotal()))
    results += ['','Total: %s' % total]
    results = linesep.join(results)
    with open('output_bill.txt', 'w') as f:
        print(results)
        f.write(results)
def main():
    API()
if __name__ == '__main__':
    main()
