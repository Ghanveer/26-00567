Simple Billing System: Project Description

The Simple Billing System is a console-based application written in Python 3 for a small shop. It lets a cashier add products with quantities for a customer and generate a bill showing the subtotal, GST and grand total. The final bill is saved to a text file named bill.txt.

The program uses four core Python concepts. The product catalogue is stored in a dictionary, with Rice at Rs.50, Sugar at Rs.40 and Oil at Rs.120. The items added to the bill are kept in a list. Separate functions handle adding an item, viewing the bill, calculating totals and generating the final bill. File handling saves the finished bill to bill.txt.

The cashier starts by entering the customer’s name, then picks options from a menu. When an item is added, the program checks that the product exists in the catalogue and that the quantity is at least 1. Invalid input produces a clear message, such as “Invalid product. Available: Rice, Sugar, Oil” or “Quantity must be at least 1.” Valid items are added with their amount, for example “Rice x2 added | Amount: 100”. If the same product is added again, its quantity is merged into the existing line.

When the bill is generated, the program calculates the subtotal by adding all item amounts. It then calculates GST at 5% of the subtotal and adds the two to get the grand total. For example, Rice x2, Oil x1 and Sugar x3 give a subtotal of 340, GST of 17.00 and a grand total of 357.00. The bill is printed in a neat table with customer name, date, items, prices, quantities and totals, and then written to bill.txt.

A web version of the same system is also provided as a bonus. It follows the same logic and validation messages, so it is easy to demonstrate.
