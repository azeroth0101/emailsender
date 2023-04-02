import csv

def add_email(email_address):
    with open('email_list.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([email_address])
    print(f"Email {email_address} added to the list.")

def remove_email(email_address):
    with open('email_list.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[0] != email_address]
    with open('email_list.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Email {email_address} removed from the list.")

while True:
    print("Choose an option:")
    print("1. Add email to list")
    print("2. Remove email from list")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        email = input("Enter email address to add: ")
        add_email(email)
    elif choice == '2':
        email = input("Enter email address to remove: ")
        remove_email(email)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
