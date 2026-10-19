
# Membership Operators: in and not in

numbers = input(
    "Enter numbers separated by spaces: "
).split()

text = input("Enter a text: ")
search_number = input("Enter number to search: ")
search_text = input("Enter text to search: ")

print(search_number, "in numbers:", search_number in numbers)
print(search_text, "in text:", search_text in text)

print(search_number, "not in numbers:",
      search_number not in numbers)
print(search_text, "not in text:",
      search_text not in text)
