import tkinter
from tkinter import messagebox
import datetime
import random
from tkcalendar import DateEntry  

name, phno, add, checkin, checkout, room, price, rc, p, roomno, custid, day = ([] for _ in range(12))

i = 0


def validate_date_obj(d):
    return 2025 <= d.year <= 2027  


def refresh_main():
    for widget in root.winfo_children():
        widget.destroy()
    draw_home()


def draw_home():
    top = tkinter.Frame(root, bg="#004466")
    top.pack(fill="x")

    tkinter.Label(
        top,
        text="WELCOME TO Hotel Havana",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#004466"
    ).pack(pady=15)

    # Center frame
    center = tkinter.Frame(root, bg="#f0f0f0")
    center.pack(fill="both", expand=True, padx=20, pady=20)

    btn_font = ("Arial", 12)

    tkinter.Button(
        center, text="1. Booking", font=btn_font,
        command=draw_booking, bg="#006699", fg="white"
    ).pack(fill="x", pady=5)

    tkinter.Button(
        center, text="2. Records", font=btn_font,
        command=draw_record, bg="#006699", fg="white"
    ).pack(fill="x", pady=5)

    tkinter.Button(
        center, text="3. Payment", font=btn_font,
        command=draw_payment, bg="#006699", fg="white"
    ).pack(fill="x", pady=5)


def draw_booking():
    for widget in root.winfo_children():
        widget.destroy()

    # Frame
    form_frame = tkinter.Frame(root, bg="#f8f8ff", padx=20, pady=20)
    form_frame.pack(fill="both", expand=True)

    tkinter.Label(
        form_frame, text="BOOKING ROOMS",
        font=("Arial", 16, "bold"), bg="#f8f8ff", fg="#003366"
    ).grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # Labels 
    tkinter.Label(form_frame, text="Name:", bg="#f8f8ff").grid(row=1, column=0, sticky="e", pady=3, padx=5)
    entry_name = tkinter.Entry(form_frame, width=30)
    entry_name.grid(row=1, column=1, sticky="w", pady=3)

    tkinter.Label(form_frame, text="Phone No.:", bg="#f8f8ff").grid(row=2, column=0, sticky="e", pady=3, padx=5)
    entry_phone = tkinter.Entry(form_frame, width=30)
    entry_phone.grid(row=2, column=1, sticky="w", pady=3)

    tkinter.Label(form_frame, text="Address:", bg="#f8f8ff").grid(row=3, column=0, sticky="e", pady=3, padx=5)
    entry_address = tkinter.Entry(form_frame, width=30)
    entry_address.grid(row=3, column=1, sticky="w", pady=3)

    # Calender
    tkinter.Label(form_frame, text="Check-In Date:", bg="#f8f8ff").grid(row=4, column=0, sticky="e", pady=3, padx=5)
    entry_checkin = DateEntry(
        form_frame,
        width=27,
        background="darkblue",
        foreground="white",
        borderwidth=2,
        date_pattern="dd/mm/yyyy"
    )
    entry_checkin.grid(row=4, column=1, sticky="w", pady=3)

    tkinter.Label(form_frame, text="Check-Out Date:", bg="#f8f8ff").grid(row=5, column=0, sticky="e", pady=3, padx=5)
    entry_checkout = DateEntry(
        form_frame,
        width=27,
        background="darkblue",
        foreground="white",
        borderwidth=2,
        date_pattern="dd/mm/yyyy"
    )
    entry_checkout.grid(row=5, column=1, sticky="w", pady=3)

    def submit_booking():
        global i

        n = entry_name.get().strip()
        p1 = entry_phone.get().strip()
        a = entry_address.get().strip()

        checkin_date = entry_checkin.get_date()
        checkout_date = entry_checkout.get_date()

        if not (n and p1 and a):
            messagebox.showerror("Error", "All fields are required")
            return

        if not (validate_date_obj(ci_date) and validate_date_obj(co_date)):
            messagebox.showerror("Error", "Enter valid dates in 2025-2027")
            return

        if checkout_date <= checkin_date:
            messagebox.showerror("Error", "Check-Out date must fall after Check-In")
            return

        if p1 in phno and p[phno.index(p1)] == 0:
            messagebox.showerror("Error", "Phone no. already exists and payment not yet done!")
            return

        checkin2 = checkin_date.strftime("%d/%m/%Y")
        checkout2 = checkout_date.strftime("%d/%m/%Y")

        name.append(n)
        phno.append(p1)
        add.append(a)
        checkin.append(checkin2)
        checkout.append(checkout2)

        day_count = (checkout_date - checkin_date).days
        day.append(day_count)

        rn, cid = random.randrange(40) + 300, random.randrange(40) + 10
        while rn in roomno or cid in custid:
            rn = random.randrange(60) + 300
            cid = random.randrange(60) + 10

        roomno.append(rn)
        custid.append(cid)
        price.append(5000)
        rc.append(0)
        p.append(0)
        i += 1

        messagebox.showinfo("Booking Complete", f"Room No: {rn}\nCustomer Id: {cid}")
        refresh_main()

    btn_frame = tkinter.Frame(form_frame, bg="#f8f8ff")
    btn_frame.grid(row=6, column=0, columnspan=2, pady=15)

    tkinter.Button(btn_frame, text="Submit", command=submit_booking, bg="#008000", fg="white", width=12).pack(side="left", padx=10)
    tkinter.Button(btn_frame, text="Back", command=refresh_main, bg="#cc0000", fg="white", width=12).pack(side="left", padx=10)


def draw_record():
    for widget in root.winfo_children():
        widget.destroy()

    container = tkinter.Frame(root, bg="#f0f0f0", padx=10, pady=10)
    container.pack(fill="both", expand=True)

    tkinter.Label(
        container, text="*** HOTEL RECORD ***",
        font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#003366"
    ).pack(pady=(0, 10))

    # Search
    search_frame = tkinter.Frame(container, bg="#f0f0f0")
    search_frame.pack(fill="x", pady=(0, 10))

    tkinter.Label(
        search_frame,
        text="Search (Name or Phone):",
        bg="#f0f0f0"
    ).pack(side="left", padx=(0, 5))

    search_var = tkinter.StringVar()
    search_entry = tkinter.Entry(search_frame, textvariable=search_var, width=30)
    search_entry.pack(side="left", padx=(0, 5))

    # Records
    records_frame = tkinter.Frame(container, bg="white", bd=1, relief="sunken")
    records_frame.pack(fill="both", expand=True)

    header = tkinter.Label(
        records_frame,
        text="| Name | Phone No. | Address | Check-In | Check-Out | Price |",
        font=("Arial", 10, "bold"),
        bg="#d9edf7"
    )
    header.pack(fill="x")

    list_frame = tkinter.Frame(records_frame, bg="white")
    list_frame.pack(fill="both", expand=True)

    text_widget = tkinter.Text(list_frame, wrap="none", height=15)
    text_widget.pack(side="left", fill="both", expand=True)

    scrollbar = tkinter.Scrollbar(list_frame, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)

    def render_records(filter_text=""):
        text_widget.config(state="normal")
        text_widget.delete("1.0", "end")

        if not phno:
            text_widget.insert("end", "No Records Found\n")
            text_widget.config(state="disabled")
            return

        key = filter_text.strip().lower()
        for idx in range(i):
            if key:
                if key not in name[idx].lower() and key not in phno[idx].lower():
                    continue
            row = f"| {name[idx]} | {phno[idx]} | {add[idx]} | {checkin[idx]} | {checkout[idx]} | {price[idx]} |\n"
            text_widget.insert("end", row)
        text_widget.config(state="disabled")

    def do_search(*args):
        render_records(search_var.get())

    tkinter.Button(search_frame, text="Search", command=do_search, bg="#006699", fg="white").pack(side="left", padx=5)
    tkinter.Button(search_frame, text="Clear", command=lambda: [search_var.set(""), render_records("")],
              bg="#999999", fg="white").pack(side="left")

    search_entry.bind("<Return>", lambda event: do_search())

    render_records()  

    tkinter.Button(container, text="Back", command=refresh_main, bg="#cc0000", fg="white", width=12).pack(pady=10)

def draw_payment():
    for widget in root.winfo_children():
        widget.destroy()

    frame = tkinter.Frame(root, bg="#fffaf0", padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    tkinter.Label(
        frame, text="PAYMENT",
        font=("Arial", 16, "bold"), bg="#fffaf0", fg="#663300"
    ).grid(row=0, column=0, columnspan=2, pady=(0, 15))

    tkinter.Label(frame, text="Phone Number:", bg="#fffaf0").grid(row=1, column=0, sticky="e", pady=5, padx=5)
    entry_phone = tkinter.Entry(frame, width=25)
    entry_phone.grid(row=1, column=1, sticky="w", pady=5)

    def submit_payment():
        ph = entry_phone.get().strip()
        if ph not in phno:
            messagebox.showerror("Invalid", "Invalid Customer Id")
            return

        idx = phno.index(ph)
        if p[idx] == 1:
            messagebox.showinfo("Info", "Payment already made.")
            return

        amount = price[idx] * day[idx] + rc[idx]
        result = messagebox.askquestion("Pay For Havana", f"Amount: {amount}\nPay Now?")
        if result == "yes":
            p[idx] = 1
            roomno[idx] = 0
            custid[idx] = 0
            messagebox.showinfo("Paid", f"Payment Complete!\nTotal Amount: {price[idx] * day[idx]}\nThank You")
            refresh_main()
        else:
            messagebox.showwarning("Cancelled", "Payment not made.")

    tkinter.Button(frame, text="Submit", command=submit_payment, bg="#008000", fg="white", width=12).grid(
        row=2, column=0, columnspan=2, pady=10
    )
    tkinter.Button(frame, text="Back", command=refresh_main, bg="#cc0000", fg="white", width=12).grid(
        row=3, column=0, columnspan=2
    )

# Window
root = tkinter.Tk()
root.title("Hotel Havana")
root.geometry("800x700")
root.configure(bg="#e6f2ff")

draw_home()
root.mainloop()
