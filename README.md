# Simple Billing System

A console billing system for a small shop, written in Python 3. The cashier adds products with quantities for a customer and generates a bill with subtotal, GST and grand total. The bill is saved to `bill.txt`.

## Features

- Product catalogue stored in a dictionary: Rice Rs.50, Sugar Rs.40, Oil Rs.120
- Bill items stored in a list
- Functions to add an item, view the bill and generate the final bill
- GST calculated at 5% of the subtotal
- Input validation for product name and quantity
- Neatly formatted bill, saved to `bill.txt`
- Bonus: a web version (`billing.html`) with the same logic

## Concepts Used

Lists, Dictionaries, Functions, File Handling

## Files

| File | Description |
|------|-------------|
| `billing_system.py` | Main Python program (console) |
| `billing.html` | Web version (open in any browser) |
| `bill.txt` | Generated bill (created when you run the program) |
| `README.md` | Project documentation |

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal (`Ctrl + ~`).
3. Run:

```bash
python billing_system.py
```

## Menu Options

```
1. Show products
2. Add item
3. View bill
4. Generate bill
5. New customer
6. Exit
```

## Sample Run

```
Customer name: Riya
Choose an option (1-6): 2
Add item: Rice
Quantity: 2
Rice x2 added | Amount: 100
...
Subtotal: 340 | GST (5%): 17.00
Grand Total: 357.00
Bill saved to bill.txt
```

## Test Cases

| # | Scenario | Input | Expected Output |
|---|----------|-------|-----------------|
| 1 | Normal input | Rice, Qty 2 | `Rice x2 added \| Amount: 100` |
| 2 | Minimum input | Sugar, Qty 1, generate bill | Subtotal 40, GST 2.00, Grand Total 42.00 |
| 3a | Invalid product | Soap | `Invalid product. Available: Rice, Sugar, Oil` |
| 3b | Invalid quantity | Rice, Qty 0 | `Quantity must be at least 1.` |
| 4 | Different valid scenario | Riya: Rice x2, Oil x1, Sugar x3 | Subtotal 340, GST 17.00, Grand Total 357.00, bill saved |

## How It Works

1. `add_item(name, quantity)` checks the product exists in the dictionary and the quantity is at least 1, then appends the item to the bill list. Adding the same product again merges the quantity.
2. `calculate_totals()` adds up all item amounts to get the subtotal, then GST (5%) and grand total.
3. `view_bill()` prints the current bill.
4. `generate_bill()` prints the final bill and writes it to `bill.txt`.

## Future Improvements

- Add more products and an option to edit prices
- Discount support
- Store bills in a database
- Print the bill with a unique invoice number
