# We have dict {"Name": "", "Age": , "Hobby": ""}. Create method that will fill it with data.

def create_dict(name: str, age: int, hobby: str):
    my_dict = {"Name": name, "Age": age, "Hobby": hobby}
    return my_dict

name = input("What is your name?")
while True:
  try:
    age = int(input("What is your age?"))
    break
  except ValueError:
    print("You need to enter a number")

hobby = input("What is your hobby?")

print(create_dict(name, age, hobby))