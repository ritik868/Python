
email = input("Enter an email: ")
split_index = email.find("@")

username=email[:split_index]
domain=email[split_index:]

tuple=(username,domain)

print(tuple)