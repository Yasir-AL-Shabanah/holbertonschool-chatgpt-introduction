#!/usr/bin/python3
# محاكاة Checkbook بسيطة مع معالجة ValueError للسحب/الإيداع

def prompt_amount(label):
    while True:
        raw = input(label).strip()
        try:
            amt = float(raw)
            return amt
        except ValueError:
            print("Invalid amount. Please enter a number.")

def main():
    balance = 0.0
    while True:
        cmd = input("[d]eposit, [w]ithdraw, [b]alance, [q]uit: ").strip().lower()
        if cmd == "d":
            amt = prompt_amount("Deposit amount: ")
            if amt < 0:
                print("Amount must be non-negative.")
                continue
            balance += amt
            print(f"Balance: {balance:.2f}")
        elif cmd == "w":
            amt = prompt_amount("Withdraw amount: ")
            if amt < 0:
                print("Amount must be non-negative.")
                continue
            if amt > balance:
                print("Insufficient funds.")
                continue
            balance -= amt
            print(f"Balance: {balance:.2f}")
        elif cmd == "b":
            print(f"Balance: {balance:.2f}")
        elif cmd == "q":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
