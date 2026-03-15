#Write a program to calculate the total and average of a list of sales numbers.

user = input("Enter numbers separated by space: ")
my_list = list(map(int, user.split()))
print(my_list)

print("Total is: ", sum(my_list))
print("Average is: ", sum(my_list)/len(my_list))