import tkinter
from tkinter import messagebox
from datetime import datetime

class CashierSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Cashier Checkout Simulator")

        
        input_frame = tkinter.Frame(root, pady=10, padx=10)
        input_frame.grid(row=0, column=0, columnspan=3)

        tkinter.Label(input_frame, text="Item Name:").grid(row=0, column=0)
        self.item_name_var = tkinter.StringVar()
        self.item_name_entry = tkinter.Entry(input_frame, textvariable=self.item_name_var)
        self.item_name_entry.grid(row=0, column=1)

        tkinter.Label(input_frame, text="Quantity:").grid(row=1, column=0)
        self.qty_var = tkinter.IntVar()
        tkinter.Entry(input_frame, textvariable=self.qty_var).grid(row=1, column=1)

        tkinter.Label(input_frame, text="Price per item:").grid(row=2, column=0)
        self.price_var = tkinter.DoubleVar()
        tkinter.Entry(input_frame, textvariable=self.price_var).grid(row=2, column=1)

        tkinter.Button(input_frame, text="Add Item", command=self.add_item).grid(row=3, column=0, columnspan=2, pady=5)

        
        self.items_listbox = tkinter.Listbox(root, width=50)
        self.items_listbox.grid(row=4, column=0, columnspan=2)

        scrollbar = tkinter.Scrollbar(root, command=self.items_listbox.yview)
        scrollbar.grid(row=4, column=2, sticky='ns')
        self.items_listbox.config(yscrollcommand=scrollbar.set)

        
        tkinter.Button(root, text="Remove Item", command=self.remove_item).grid(row=5, column=0, pady=5)
        tkinter.Button(root, text="Edit Item", command=self.edit_item).grid(row=5, column=1, pady=5)
        tkinter.Button(root, text="Generate Receipt", command=self.generate_receipt).grid(row=6, column=0, columnspan=2, pady=5)

        
        tkinter.Label(root, text="Total:").grid(row=7, column=0)
        self.total_var = tkinter.StringVar(value="₹0.00")
        self.total_label = tkinter.Label(root, textvariable=self.total_var)
        self.total_label.grid(row=7, column=1)

        tkinter.Button(root, text="Checkout", command=self.checkout).grid(row=8, column=0, columnspan=2, pady=10)

        self.items = []

        self.item_name_entry.focus_set()

    def add_item(self):
        try:
            name = self.item_name_var.get()
            qty = self.qty_var.get()
            price = self.price_var.get()
            if not name or qty <= 0 or price <= 0:
                messagebox.showerror("Error", "Enter valid item name, quantity, and price.")
                return
            total_price = qty * price
            self.items.append((name, qty, price, total_price))
            self.items_listbox.insert(tkinter.END, f"{name} - Quantity: {qty}, Price: {price:.2f}, Total: {total_price:.2f}")
            self.update_total()
            self.clear_entries()
            self.item_name_entry.focus_set()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def remove_item(self):
        selected = self.items_listbox.curselection()
        if selected:
            index = selected[0]
            del self.items[index]
            self.items_listbox.delete(index)
            self.update_total()
        else:
            messagebox.showerror("Error", "Select an item to remove.")

    def edit_item(self):
        selected = self.items_listbox.curselection()
        if selected:
            index = selected[0]
            item = self.items[index]
            self.item_name_var.set(item[0])
            self.qty_var.set(item[1])
            self.price_var.set(item[2])
            del self.items[index]
            self.items_listbox.delete(index)
            self.update_total()
            self.item_name_entry.focus_set()
        else:
            messagebox.showerror("Error", "Select an item to edit.")

    def update_total(self):
        total = sum(item[3] for item in self.items)
        self.total_var.set(f"₹{total:.2f}")

    def clear_entries(self):
        self.item_name_var.set("")
        self.qty_var.set(0)
        self.price_var.set(0.0)

    def checkout(self):
        total = sum(item[3] for item in self.items)
        messagebox.showinfo("Checkout", f"Total amount to pay: ₹{total:.2f}")
        self.items.clear()
        self.items_listbox.delete(0, tkinter.END)
        self.update_total()
        self.clear_entries()
        self.item_name_entry.focus_set()

    def generate_receipt(self):
        receipt_win = tkinter.Toplevel(self.root)
        receipt_win.title("Receipt")
        text = tkinter.Text(receipt_win, width=100, height=20)
        text.pack(padx=10, pady=10)
        text.insert(tkinter.END, f"Receipt\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        total = 0
        for item in self.items:
            line = f"{item[0]} x{item[1]} @ ₹{item[2]:.2f} = ₹{item[3]:.2f}\n"
            text.insert(tkinter.END, line)
            total += item[3]
        text.insert(tkinter.END, f"\nGrand Total: ₹{total:.2f}")
        text.config(state=tkinter.DISABLED)

if __name__ == "__main__":
    root = tkinter.Tk()
    cashier = CashierSimulator(root)
    root.mainloop()
