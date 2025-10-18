from typing import List


class Product:
    
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name  = name
        self.price = price
        self.stock = stock


class Customer:
    
    def __init__(self, name: str, balance: float) -> None:
        self.name    = name
        self.balance = balance

    def deduct_balance(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Balance da mablag yetarli emas: {self.balance}")


class Item:

    def __init__(self, product: Product, quantity: int) -> None:
        self.product  = product
        self.quantity = quantity


class Order:
    
    def __init__(self, customer: Customer) -> None:
        self.customer = customer
        self.items: List[Item] = []

    def add_item(self, product: Product, quantity: int) -> None:
        item = Item(product, quantity)
        self.items.append(item)

    def calculate_total(self) -> float:
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
        return total
    
    def complete_order(self) -> None:
        self.customer.deduct_balance(self.calculate_total())


class Shop:
    
    def __init__(self, name: str):
        self.name                      = name
        self.products: List[Product]   = []
        self.customers: List[Customer] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def add_customer(self, customer: Customer) -> None:
        self.customers.append(customer)

