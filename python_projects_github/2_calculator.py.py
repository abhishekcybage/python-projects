choice = input("Enter your choice (додати, відняти, помножити, поділити): ")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if choice == "додати":
    result = number1 + number2
    print("Сума:", result)

elif choice == "відняти":
    result = number1 - number2
    print("Різниця:", result)

elif choice == "помножити":
    result = number1 * number2
    print("Множення:", result)

elif choice == "поділити":
    if number2 == 0:
        print("На 0 не ділиться!")
    else:
        result = number1 / number2
        print("Ділення:", result)

else:
    print("Невірний вибір!")

if 'result' in locals():
    print("Результат:", result)
