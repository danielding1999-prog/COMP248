# NON-MODULAR VERSION - All code in one block
# Sales Tax Calculator - Teaching Example for Design Students
# This version shows all code in sequential order for beginners

import os
from datetime import datetime

TAX_RATE = 0.13
DOCUMENT_PATH = os.path.join(os.path.expanduser("~"), "Documents")
FILE_PATH = os.path.join(DOCUMENT_PATH, "sales_transactions.txt")

# Calculate sales tax (13%)
def CalculateSaleTax(price):
    sales_tax = price * TAX_RATE
    return sales_tax

# Create transaction record
def CreateTranRecord(item_name, price, sales_tax, total_price):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = f"{timestamp} - Item: {item_name}, Price: ${price:.2f}, Tax: ${sales_tax:.2f}, Total: ${total_price:.2f}\n"
    return transaction

# Write to file in Documents folder
def WriteFile(transaction):
    
    with open(FILE_PATH, "a") as file:
        file.write(transaction)
        return FILE_PATH

# Display result to user
def DisplayResult(item_name, price, sales_tax, total_price):    
    print(f"\n--- TRANSACTION SUMMARY ---")
    print(f"Item: {item_name}")
    print(f"Price: ${price:.2f}")
    print(f"Sales Tax (13%): ${sales_tax:.2f}")
    print(f"Total: ${total_price:.2f}")
    print(f"Transaction saved to: {FILE_PATH}")

def main():
    item_name = input("Enter the item name: ")
    price = float(input("Enter the price of the item: $"))
    sales_tax = CalculateSaleTax(price)
    total_price = price + sales_tax
    tran_record = CreateTranRecord(item_name, price, sales_tax, total_price)
    WriteFile(tran_record)
    DisplayResult(item_name, price, sales_tax, total_price)
    
if __name__ == "__main__":
    main()
