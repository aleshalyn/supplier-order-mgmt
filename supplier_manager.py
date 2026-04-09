import re
from datetime import datetime
 
class Supplier:
    def __init__(self, supplier_id, supplier_name, contact_person,
                 contact_number, email_address, address, status):
        self.__supplier_id    = supplier_id
        self.__supplier_name  = supplier_name
        self.__contact_person = contact_person
        self.__contact_number = contact_number
        self.__email_address  = email_address
        self.__address        = address
        self.__status         = status
        self.__date_added     = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_supplier_id(self):
        return self.__supplier_id
    def get_supplier_name(self):
        return self.__supplier_name
    def get_contact_person(self):
        return self.__contact_person
    def get_contact_number(self):
        return self.__contact_number
    def get_email_address(self):
        return self.__email_address
    def get_address(self):
        return self.__address
    def get_status(self):
        return self.__status
    def get_date_added(self):
        return self.__date_added

    def set_supplier_name(self, value):
        self.__supplier_name = value
    def set_contact_person(self, value):
        self.__contact_person = value
    def set_contact_number(self, value):
        self.__contact_number = value
    def set_email_address(self, value):
        self.__email_address = value
    def set_address(self, value):
        self.__address = value
    def set_status(self, value):
        self.__status = value

    # display method
    def display_supplier(self):
        print(f"Supplier ID    : {self.__supplier_id}")
        print(f"Supplier Name  : {self.__supplier_name}")
        print(f"Contact Person : {self.__contact_person}")
        print(f"Contact Number : {self.__contact_number}")
        print(f"Email Address  : {self.__email_address}")
        print(f"Address        : {self.__address}")
        print(f"Status         : {self.__status.upper()}")
        print(f"Date Added     : {self.__date_added}")


#Storage
suppliers = []
id_counter = 1

def generate_id():
    global id_counter
    new_id = f"SUP-{id_counter:03d}"
    id_counter += 1
    return new_id

def input_non_empty(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("⚠️  This field cannot be empty. Try again.")

def input_email():
    email = input("Email Address   : ").strip()
        

def input_contact():
   number = input("Contact Number  : ").strip()
        

def input_status():
    while True:
        status = input("Status (active/inactive) [active]: ").strip().lower()
        if status == "":
            return "active"
        if status in ("active", "inactive"):
            return status
        print("⚠️  Please enter 'active' or 'inactive'.")

def find_supplier(query):
    query = query.lower()
    for s in suppliers:
        if s.get_supplier_id().lower() == query or s.get_supplier_name().lower() == query:
            return s
    return None


# ── CRUD Functions ──────────────────────────────────────────────────────────

def add_supplier():
    print("\n===== Add New Supplier =====")
    supplier_id = generate_id()
    print(f"Auto-generated Supplier ID: {supplier_id}\n")

    supplier_name  = input_non_empty("Supplier Name   : ")
    contact_person = input_non_empty("Contact Person  : ")
    contact_number = input_contact()
    email_address  = input_email()
    address        = input_non_empty("Address         : ")
    status         = input_status()

    supplier = Supplier(
        supplier_id, supplier_name, contact_person,
        contact_number, email_address, address, status
    )
    suppliers.append(supplier)
    print("✅ Supplier added successfully!\n")


def view_suppliers():
    print("\n===== Supplier List =====")
    if not suppliers:
        print("No suppliers found.\n")
        return
    
    result = suppliers
    label = "All"

    if not result:
        print(f"No {label.lower()} suppliers found.\n")
        return

    print(f"\nShowing {label} Suppliers ({len(result)} found):")
    for s in result:
        print("\n--- Supplier ---")
        s.display_supplier()
    print()


def update_supplier():
    print("\n===== Update Supplier =====")
    if not suppliers:
        print("No suppliers found.\n")
        return

    query = input("Enter Supplier ID or Name to update: ").strip()
    supplier = find_supplier(query)

    if not supplier:
        print(f"⚠️  No supplier found matching '{query}'.\n")
        return

    print("\n--- Supplier Found ---")
    supplier.display_supplier()
    print("\nLeave a field blank to keep the current value.\n")

    def update_field(label, current, setter):
        value = input(f"{label} [{current}]: ").strip()
        if value:
            setter(value)

    update_field("Supplier Name   ", supplier.get_supplier_name(),  supplier.set_supplier_name)
    update_field("Contact Person  ", supplier.get_contact_person(), supplier.set_contact_person)
    update_field("Contact Number  ", supplier.get_contact_number(), supplier.set_contact_number)
    update_field("Email Address  ", supplier.get_email_address(), supplier.set_email_address)
    update_field("Address         ", supplier.get_address(), supplier.set_address)

    # status
    while True:
        raw = input(f"Status (active/inactive) [{supplier.get_status()}]: ").strip().lower()
        if raw == "":
            break
        if raw in ("active", "inactive"):
            supplier.set_status(raw)
            break
        print("⚠️  Please enter 'active' or 'inactive'.")

    print("✅ Supplier updated successfully!\n")


def delete_supplier():
    print("\n===== Delete Supplier =====")
    if not suppliers:
        print("No suppliers found.\n")
        return

    query = input("Enter Supplier ID or Name to delete: ").strip()
    supplier = find_supplier(query)

    if not supplier:
        print(f"⚠️  No supplier found matching '{query}'.\n")
        return

    print("\n--- Supplier Found ---")
    supplier.display_supplier()

    confirm = input(f"\nAre you sure you want to delete '{supplier.get_supplier_name()}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        suppliers.remove(supplier)
        print("✅ Supplier deleted successfully!\n")
    else:
        print("❌ Deletion cancelled.\n")


def search_supplier():
    print("\n===== Search Supplier =====")
    if not suppliers:
        print("No suppliers found.\n")
        return

    query = input("Enter Supplier ID or Name to search: ").strip().lower()
    if not query:
        print("⚠️  Search query cannot be empty.\n")
        return

    results = [
        s for s in suppliers
        if query in s.get_supplier_id().lower()
        or query in s.get_supplier_name().lower()
    ]

    if not results:
        print(f"No supplier found matching '{query}'.\n")
        return

    print(f"\n{len(results)} result(s) found:")
    for s in results:
        print("\n--- Supplier ---")
        s.display_supplier()
    print()


# ── CLI Menu ────────────────────────────────────────────────────────────────

def menu():
    print("\nWelcome to the Supplier Management System!")
    print("Data is stored in memory only — records are cleared on exit.")
    while True:
        print("\n===== Supplier Management System =====")
        print("1. Add Supplier")
        print("2. View Supplier List")
        print("3. Update Supplier Information")
        print("4. Delete Supplier")
        print("5. Search Supplier")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_supplier()
        elif choice == "2":
            view_suppliers()
        elif choice == "3":
            update_supplier()
        elif choice == "4":
            delete_supplier()
        elif choice == "5":
            search_supplier()
        elif choice == "6":
            print("Exiting system. Goodbye!\n")
            break
        else:
            print("Invalid choice. Try again.\n")


# run program
menu()