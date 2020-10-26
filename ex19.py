def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# gives the function numbers for the first and second argument
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# gives a variable for the first and second argument
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def testfunc(one, two):
    print(f"The first variable is {one}, the second is {two}.")

testfunc('two', 'one')
testfunc(1+3, 5+2)
ab = 3
ba = 5
testfunc(ab, ba)
testfunc(ab, 14)
testfunc(ba + 14, ab)
testfunc(1, 5 + ba)