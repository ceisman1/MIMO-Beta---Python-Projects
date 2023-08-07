class Product:
  def __init__(self, name, price, units):
    self.name = name
    self.price = price
    self.units = units
    self.is_on_sale = False

  def describe(self):
    print(f"Product name: {self.name}")
    print(f"Product price: {self.price}")
    print(f"Available units: {self.units}")
    print(f"On sale? {self.is_on_sale}")
    print(f"In stock? {self.is_in_stock()}")
    print("-------------------------")
    
  def add_units(self, units):
    self.units += units
  
  def reduce_units(self, units):
    if self.units - units >= 0:
      self.units -= units
    else:
      print("Error: Not enough units in inventory.")

  def reduce_price(self, discount):
    self.price = self.price * (1 - discount)
    self.is_on_sale = True

  def is_in_stock(self):
    return self.units > 0

laptop = Product("Dell Laptop", 850, 12)
laptop.describe()
laptop.add_units(15)
laptop.reduce_units(10)
laptop.reduce_units(20)
laptop.reduce_price(0.1)
laptop.describe()
