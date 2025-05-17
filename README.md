# Coffee Shop

A python project modelling a cofee shop with customers, coffees and orders.

## Overview
This project is a basic simulation of a Coffee shop ordering system. It does the following:
- Create customers and coffees
- Place orders by linking customers and coffees with a price
- Trcak who ordered what and for how much
- Analyze coffee popularity

## Files and Basic Description.

### coffee.py
Defines the `Coffee` class. Coffees have names, can show all orders for themselves, list all customers who ordered them, count how many orders were placed, and calculate their average selling price.


### customer.py
Defines the `Customer` class. Customers have names, can place new orders, view their past orders, see all different coffees they’ve tried, and find out who is the biggest fan of a certain coffee.


### order.py
Defines the `Order` class. An Order represents a transaction: a customer buying a certain coffee at a certain price. It keeps track of all orders created, and ensures data is valid (correct types and price range).


## Requirements.

- Python 3
No external libraries required

## Notes
- Price of a coffee must be a float between 1.0 and 10.0.
- Customer names: 1–15 characters.
- Coffee names: at least 3 characters.

## License

MIT

