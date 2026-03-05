class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        # FIX: Initialize the missing attribute here!
        self.previous_transactions = [] 

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self.total += amount
        
        for _ in range(quantity):
            self.items.append(title)
        
        # Store this specific transaction so we can undo it later
        self.previous_transactions.append({
            'amount': amount,
            'quantity': quantity
        })

    def void_last_transaction(self):
        if self.previous_transactions:
            # Get the last transaction info
            last = self.previous_transactions.pop()
            
            # Undo the math
            self.total -= last['amount']
            
            # Remove the correct number of items from the end of the list
            for _ in range(last['quantity']):
                if self.items:
                    self.items.pop()
        else:
            print("No transactions to void.")

    def apply_discount(self):
        if self.discount > 0:
            reduction = self.total * (self.discount / 100)
            self.total -= reduction
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")