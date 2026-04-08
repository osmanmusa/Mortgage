# Loan Calculator
# Paying Back a Fixed Amount Periodically

# Lambda function (inline function) for loan payment calculation
payment_factor = lambda r, T: r * (1 + r)**T / ((1 + r)**T - 1)
extra_payment_factor = lambda r, T, Te: r * ((1 + r)**(T - Te) - 1) / ((1 + r)**T - 1)

# Prompt user for rate type
print("Choose loan type:")
print("1. Fixed rate")
print("2. Mixed rate")
choice = input("Enter your choice (1 or 2): ")

# Prompt user for loan parameters
total_years = float(input("Enter the total duration of the loan in years: "))
T = int(total_years * 12)  # Convert years to months
loan_input = input("Enter the loan amount (in thousands, e.g., 100 for 100k): ")
G = float(loan_input if loan_input else "100") * 1000  # Loan amount, default 100k

# Prompt user for multiple extra payments
extra_payments = []  # List of tuples (amount, month)
print("\nEnter extra payments (press Enter without input to finish):")
while True:
    extra_payment_input = input("Enter extra payment amount (in thousands): ")
    if not extra_payment_input:
        break

    E = float(extra_payment_input) * 1000
    extra_payment_month_input = input("Enter the month of extra payment (1-" + str(T) + "): ")
    Te = int(extra_payment_month_input) if extra_payment_month_input else 1

    extra_payments.append((E, Te))

if choice == "1":
    # Fixed rate calculation
    rate_percent = float(input("Enter the annual interest rate (in %, e.g., 4.49 for 4.49%): "))
    r = (rate_percent / 100) / 12  # Monthly interest rate (annual rate divided by 100 and 12)

    # Calculate total payment using the loan payment formula with extra payments
    U = G * T * payment_factor(r, T)
    for E, Te in extra_payments:
        U -= E * T * extra_payment_factor(r, T, Te)

    print(f"\nTotal amount to be paid: ${U:,.2f}")
    print(f"Monthly payment: ${U/T:,.2f}")
    print(f"Value paid for each 1€ borrowed: {U/G:.4f}€")

elif choice == "2":
    # Mixed rate calculation
    # Prompt user for rates
    rf_percent = float(input("Enter the fixed period annual interest rate (in %, e.g., 3.516 for 3.516%): "))
    rf = (rf_percent / 100) / 12  # Fixed period monthly interest rate

    rv_percent = float(input("Enter the variable period annual interest rate (in %, e.g., 3.315 for 3.315%): "))
    rv = (rv_percent / 100) / 12  # Variable period monthly interest rate

    # Prompt user for fixed period duration
    fixed_years = float(input("Enter the duration of the fixed period in years: "))
    Tf = fixed_years * 12  # Convert years to months

    U = G * T * (payment_factor(rv, T) + payment_factor(rf, Tf) - payment_factor(rv, Tf))

    print(f"\nTotal amount to be paid: ${U:,.2f}")
    print(f"Monthly payment: ${U/T:,.2f}")
    print(f"Value paid for each 1€ borrowed: {U/G:.4f}€")
else:
    print("\nInvalid choice. Please run the program again and select 1 or 2.")

# https://www.calculator.net/loan-calculator.html?cloanamount=58%2C690.80&cloanterm=6&cloantermmonth=0&cinterestrate=4.49&ccompound=monthly&cpayback=month&x=Calculate&type=1#monthlyfixedr
