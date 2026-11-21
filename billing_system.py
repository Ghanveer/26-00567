

from datetime import datetime

PRODUCTS = {"rice": 50, "sugar": 40, "oil": 120}   # product catalogue (dictionary)
GST_RATE = 0.05                                    # 5% of subtotal
BILL_FILE = "bill.txt"

bill_items = []                                    # bill items (list of dictionaries)


def show_products():
    print("\nAvailable products:")
    for name, price in PRODUCTS.items():
        print(f"  {name.title():<8} Rs.{price}")


def add_item(name, quantity):
    """Validate and add an item to the bill. Returns True if added."""
    key = name.strip().lower()
    if key not in PRODUCTS:
        available = ", ".join(p.title() for p in PRODUCTS)
        print(f"Invalid product. Available: {available}")
        return False
    if not isinstance(quantity, int) or quantity < 1:
        print("Quantity must be at least 1.")
        return False

    amount = PRODUCTS[key] * quantity
    # If the product is already on the bill, merge the quantity
    for item in bill_items:
        if item["name"] == key:
            item["qty"] += quantity
            item["amount"] += amount
            break
    else:
        bill_items.append({"name": key, "price": PRODUCTS[key],
                           "qty": quantity, "amount": amount})
    print(f"{key.title()} x{quantity} added | Amount: {amount}")
    return True


def calculate_totals():
    subtotal = sum(item["amount"] for item in bill_items)
    gst = subtotal * GST_RATE
    return subtotal, gst, subtotal + gst


def build_bill_text(customer):
    subtotal, gst, grand = calculate_totals()
    line = "=" * 44
    out = [line, "            SIMPLE BILLING SYSTEM", line,
           f"Customer : {customer}",
           f"Date     : {datetime.now():%d-%m-%Y %H:%M}",
           "-" * 44,
           f"{'Item':<10}{'Price':>8}{'Qty':>6}{'Amount':>12}",
           "-" * 44]
    for it in bill_items:
        out.append(f"{it['name'].title():<10}{it['price']:>8}{it['qty']:>6}{it['amount']:>12.2f}")
    out += ["-" * 44,
            f"{'Subtotal':<24}{subtotal:>20.2f}",
            f"{'GST (5%)':<24}{gst:>20.2f}",
            f"{'Grand Total':<24}{grand:>20.2f}",
            line, "      Thank you! Visit again.", line]
    return "\n".join(out)


def view_bill(customer="Customer"):
    if not bill_items:
        print("No items added yet.")
        return
    print("\n" + build_bill_text(customer))


def generate_bill(customer):
    """Print the final bill and save it to bill.txt."""
    if not bill_items:
        print("Cannot generate bill: no items added.")
        return
    subtotal, gst, grand = calculate_totals()
    print()
    for it in bill_items:
        print(f"{it['name'].title()} x{it['qty']} = {it['amount']}", end=" | ")
    print()
    print(f"Subtotal: {subtotal:g} | GST (5%): {gst:.2f}")
    print(f"Grand Total: {grand:.2f}")
    print("\n" + build_bill_text(customer))
    try:
        with open(BILL_FILE, "w", encoding="utf-8") as f:
            f.write(build_bill_text(customer) + "\n")
        print(f"\nBill saved to {BILL_FILE}")
    except OSError as err:
        print(f"Could not save bill: {err}")


def read_quantity():
    raw = input("Quantity: ").strip()
    try:
        return int(raw)
    except ValueError:
        return 0   # non-numeric treated as invalid


def main():
    print("=== Simple Billing System ===")
    customer = input("Customer name: ").strip() or "Customer"

    while True:
        print("\n1. Show products\n2. Add item\n3. View bill\n4. Generate bill\n5. New customer\n6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_products()
        elif choice == "2":
            name = input("Add item: ")
            qty = read_quantity()
            add_item(name, qty)
        elif choice == "3":
            view_bill(customer)
        elif choice == "4":
            generate_bill(customer)
        elif choice == "5":
            bill_items.clear()
            customer = input("Customer name: ").strip() or "Customer"
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
