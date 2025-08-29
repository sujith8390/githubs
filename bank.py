class Bank:


    def __init__(self):
        self.accounts = {}
        self._next_number = 1000

    def create_account(self, holder, initial=0.0):

        if initial < 0:
            raise ValueError("Initial deposit cannot be negative.")
        acc_no = self._generate_acc_no()
        self.accounts[acc_no] = {"holder": holder, "balance": float(initial)}
        return acc_no

    def deposit(self, acc_no, amount):
        if acc_no not in self.accounts:
            raise KeyError("Account not found.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.accounts[acc_no]["balance"] += float(amount)
        return self.accounts[acc_no]["balance"]

    def withdraw(self, acc_no, amount):
        if acc_no not in self.accounts:
            raise KeyError("Account not found.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.accounts[acc_no]["balance"]:
            raise ValueError("Insufficient funds.")
        self.accounts[acc_no]["balance"] -= float(amount)
        return self.accounts[acc_no]["balance"]

    def check_balance(self, acc_no):
        if acc_no not in self.accounts:
            raise KeyError("Account not found.")
        return self.accounts[acc_no]["balance"]


    def _generate_acc_no(self):
        while self._next_number <= 9999 and f"{self._next_number:04d}" in self.accounts:
            self._next_number += 1
        if self._next_number > 9999:
            raise ValueError("No 4-digit account numbers available.")
        acc_no = f"{self._next_number:04d}"
        self._next_number += 1
        return acc_no



def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    bank = Bank()
    print("=== Mini Bank (Auto 4-digit Account Numbers) ===")

    while True:
        print("\nChoose an option:")
        print("1) Create account")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Check balance")
        print("5) Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            holder = input("Enter account holder name: ").strip()
            initial = read_float("Enter initial deposit (0 if none): ")
            try:
                acc_no = bank.create_account(holder, initial)
                print(f"Account created for {holder}. "
                      f"Your 4-digit account number is {acc_no}. "
                      f"Balance: {bank.check_balance(acc_no)}")
            except (ValueError, KeyError) as e:
                print("Error:", e)

        elif choice == "2":
            acc_no = input("Enter 4-digit account number: ").strip()
            amount = read_float("Enter amount to deposit: ")
            try:
                new_bal = bank.deposit(acc_no, amount)
                print(f"Deposited. New balance for {acc_no}: {new_bal}")
            except (ValueError, KeyError) as e:
                print("Error:", e)

        elif choice == "3":
            acc_no = input("Enter 4-digit account number: ").strip()
            amount = read_float("Enter amount to withdraw: ")
            try:
                new_bal = bank.withdraw(acc_no, amount)
                print(f"Withdrawn. New balance for {acc_no}: {new_bal}")
            except (ValueError, KeyError) as e:
                print("Error:", e)

        elif choice == "4":
            acc_no = input("Enter 4-digit account number: ").strip()
            try:
                bal = bank.check_balance(acc_no)
                holder = bank.accounts[acc_no]["holder"]
                print(f"Account {acc_no} ({holder}) balance: {bal}")
            except KeyError as e:
                print("Error:", e)

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()

