import Expense_Tracker
import time
import os


def main():
    expense_list = Expense_Tracker.ListExpense()
    expense_list.load_from_json('Expense_Tracker/src/expenses.json')
    current_time = time.localtime()
    formatted_date = time.strftime("%Y-%m-%d", current_time)

    while True:
        print("Hello, welcome to your own personal expense tracker")
        choice = int(input(
            "1- Add expense\n"
            "2- List all expenses\n"
            "3- Update expense\n"
            "4- Delete expense\n"
            "5- Summary of all expenses\n"
            "6- Summary of expenses in a month\n"
            "7- Exit\n"
        ))

        try:
            if choice == 1:
                x = input("Add your expense (Description Amount): ")
                partes = x.split()
                if len(partes) != 2:
                    print("Introduce correct format: name price")
                else:
                    expense_list.add_expense(partes[0], partes[1], formatted_date)

            elif choice == 2:
                expense_list.view_all_expenses()

            elif choice == 3:
                x = input("Update an expense (ID Description Amount): ")
                partes = x.split()
                if len(partes) != 3:
                    print("Introduce correct format: id name price")
                else:
                    expense_list.update_expense(int(partes[0]), partes[1], partes[2], formatted_date)

            elif choice == 4:
                x = input("Introduce expense ID you want to delete: ")
                expense_list.delete_expense(int(x))

            elif choice == 5:
                expense_list.summary_all_expenses()

            elif choice == 6:
                x = input("Introduce month of expenses (format: 01 for January, 12 for December): ")
                expense_list.expenses_by_month(x)

            elif choice == 7:
                expense_list.save_to_json('Expense_Tracker/src/expenses.json')
                print("Expenses saved. Goodbye!")
                break

            else:
                print("Select a valid option.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Current Working Directory:", os.getcwd())
    main()
