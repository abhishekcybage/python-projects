name = input("enter your name:")
print("your nickname is", name.capitalize())
username = input("enter your username:")
print("your username is", username.capitalize())
number = input("enter your number:")

number = number
nickname = name.capitalize()
username = username.capitalize()


def hello(nickname, username):
    print("hello world".capitalize())  # перетворюємо рядок на великі літери
    print(f"Hi, {nickname} {username}")


hello(nickname, username)

print('your number is', number)
