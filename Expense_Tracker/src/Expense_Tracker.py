import time
import json

class Expense:
    def __init__(self, ID, Description, Amount, Date):
        self.ID = ID
        self.Description = Description
        self.Amount = Amount
        self.Date = Date

    def show_data(self):
        return {
            'ID': self.ID,
            'Description': self.Description,
            'Amount': self.Amount,
            'Date': self.Date
        }


class ListExpense:
    def __init__(self):
        self.list_expenses = {}
        self.available_ids = set()
        self.next_id = 1

    def add_expense(self, Description, Amount, Date):
        # Reuse an available ID or generate a new one
        if self.available_ids:
            new_id = min(self.available_ids)
            self.available_ids.remove(new_id)
        else:
            new_id = self.next_id
            self.next_id += 1

        new_expense = Expense(str(new_id), Description, Amount, Date)
        self.list_expenses[new_id] = new_expense
        print(f"Expense with ID {new_id} has been added")

    def view_all_expenses(self):
        if not self.list_expenses:
            print("No expenses recorded.")
        else:
            for id, expense in sorted(self.list_expenses.items()):
                data = expense.show_data()
                print(f"\nExpense ID: {id}")
                for key, value in data.items():
                    print(f"{key}: {value}")

    def update_expense(self, id, Description, Amount, Date):
        if id in self.list_expenses:
            updated_expense = Expense(str(id), Description, Amount, Date)
            self.list_expenses[id] = updated_expense
            print(f"Expense with ID {id} has been successfully updated")
        else:
            print(f"No expense found with ID {id}")

    def delete_expense(self, id):
        if id not in self.list_expenses:
            print(f"No expense exists with ID {id}")
        else:
            del self.list_expenses[id]
            self.available_ids.add(id)
            print(f"Expense with ID {id} has been deleted")

    def summary_all_expenses(self):
        total = sum(int(expense.Amount) for expense in self.list_expenses.values())
        print(f"Total of all expenses: {total}")

    def expenses_by_month(self, month):
        total = sum(int(expense.Amount) for expense in self.list_expenses.values() if expense.Date[5:7] == month)
        if total == 0:
            print(f"No expenses found for month {month}.")
        else:
            print(f"Total expenses for month {month}: {total}")

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json_data = {id: expense.show_data() for id, expense in self.list_expenses.items()}
            json.dump(json_data, file, indent=4)
            print(f"Expenses saved to {filename}")

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                json_data = json.load(file)
                for id, data in json_data.items():
                    loaded_expense = Expense(data['ID'], data['Description'], data['Amount'], data['Date'])
                    self.list_expenses[int(id)] = loaded_expense
                print(f"Expenses loaded from {filename}")
        except FileNotFoundError:
            print(f"No file found named {filename} Starting with an empty expense list.")


# Example usage
current_time = time.localtime()
formatted_date = time.strftime("%Y-%m-%d", current_time)

expense_list = ListExpense()

# Add expenses
expense_list.add_expense("Paint", "20", formatted_date)
expense_list.add_expense("Car", "10", formatted_date)
expense_list.add_expense("Pencil", "1", formatted_date)

# View all expenses
expense_list.view_all_expenses()

# Update an expense
expense_list.update_expense(1, "Helmet", "60", formatted_date)

# View after update
print("\nAfter update:")
expense_list.view_all_expenses()

# Delete an expense
expense_list.delete_expense(1)

# View after deletion
print("\nAfter deletion:")
expense_list.view_all_expenses()

# Add a new expense which should reuse ID 1
expense_list.add_expense("Backpack", "40", formatted_date)

# View after adding new expense
print("\nAfter adding new expense (should reuse ID 1):")
expense_list.view_all_expenses()

# Summary of all expenses
expense_list.summary_all_expenses()

# Expenses by month
expense_list.expenses_by_month(formatted_date[5:7])
