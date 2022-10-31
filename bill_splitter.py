from random import choice


def friend_bill(friends, split_bill):
    for friend in friends:
        friends[friend] = split_bill
    return friends


def bill_splitter(total_bill, people):
    return round(total_bill / people, 2)


def who_is_lucky(friends):
    is_lucky = choice(list(friends.keys()))
    return is_lucky


people_amount = int(input("Enter the number of friends joining (including you):\n"))
friend_names = {}

if people_amount < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(people_amount):
        friend_names[input()] = 0
    bill = float(input("Enter the total bill value:\n"))
    bill_split = bill_splitter(bill, people_amount)
    friend_names = friend_bill(friend_names, bill_split)
    lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")
    if lucky == "Yes":
        lucky_friend = who_is_lucky(friend_names)
        print(f"{lucky_friend} is the lucky one!")
        friend_names[lucky_friend] = 0
        people_amount -= 1
        bill_split = bill_splitter(bill, people_amount)
        friend_bill(friend_names, bill_split)
        friend_names[lucky_friend] = 0
        print(friend_names)
    else:
        print("No one is going to be lucky\n"
              f"{friend_names}")
