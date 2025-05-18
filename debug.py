from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffee types
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders using create_order method
order1 = alice.create_order(latte, 5.0)
order2 = alice.create_order(espresso, 4.5)
order3 = bob.create_order(latte, 6.0)
order4 = bob.create_order(latte, 4.0)

# Test Customer methods
print(f"{alice.name}'s orders: {[order.price for order in alice.orders()]}")
print(f"{alice.name}'s coffees: {[coffee.name for coffee in alice.coffees()]}")

# Test Coffee methods
print(f"{latte.name} has {latte.num_orders()} orders.")
print(f"Customers who ordered {latte.name}: {[customer.name for customer in latte.customers()]}")
print(f"Average price of {latte.name}: {latte.average_price():.2f}")

# Test most_aficionado class method
most_loyal = Customer.most_aficionado(latte)
print(f"Most loyal {latte.name} customer: {most_loyal.name if most_loyal else 'None'}")
