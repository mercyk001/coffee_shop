from customer import Customer
from coffee import Coffee
from order import Order

# customers
alice = Customer("Alice")
bob = Customer("Bob")
mercy = Customer("Mercy")
bena = Customer("Bena")



# coffee types
latte = Coffee("Latte")
espresso = Coffee("Espresso")
cappucino = Coffee("Cappuccino")
latte = Coffee("Latte")

# Create orders using create_order method
order1 = alice.create_order(latte, 5.0)
order2 = alice.create_order(espresso, 4.5)
order3 = bob.create_order(latte, 6.0)
order4 = bob.create_order(latte, 4.0)
order5 = mercy.create_order(cappucino, 7.0)
order6 = mercy.create_order(latte, 5.5)
order7 = bena.create_order(latte, 3.5)

# Test Customer methods
print(f"{alice.name}'s orders: {[order.price for order in alice.orders()]}")
print(f"{alice.name}'s coffees: {[coffee.name for coffee in alice.coffees()]}")
print(f"{bob.name}'s orders: {[order.price for order in bob.orders()]}")
print(f"{mercy.name}'s coffees: {[coffee.name for coffee in mercy.coffees()]}")
print(f"{bena.name}'s orders: {[order.price for order in bena.orders()]}")




# Test Coffee methods
print(f"{latte.name} has {latte.num_orders()} orders.")
print(f"Customers who ordered {latte.name}: {[customer.name for customer in latte.customers()]}")
print(f"Average price of {latte.name}: {latte.average_price():.2f}")

print(f"{espresso.name} has {espresso.num_orders()} orders.")
print(f"Customers who ordered {espresso.name}: {[customer.name for customer in espresso.customers()]}")
print(f"Average price of {espresso.name}: {espresso.average_price():.2f}")

print(f"{cappucino.name} has {cappucino.num_orders()} orders.")
print(f"Customers who ordered {cappucino.name}: {[customer.name for customer in cappucino.customers()]}")
print(f"Average price of {cappucino.name}: {cappucino.average_price():.2f}")




# Test most_aficionado class method
most_loyal = Customer.most_aficionado(latte)
print(f"Most loyal {latte.name} customer: {most_loyal.name if most_loyal else 'None'}")

most_loyal = Customer.most_aficionado(espresso)
print(f"Most loyal {espresso.name} customer: {most_loyal.name if most_loyal else 'None'}")
