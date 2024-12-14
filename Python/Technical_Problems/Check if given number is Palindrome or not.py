#Write a  python program check if the given number is palindrome or not
number = int(input("Enter the value: "))
num_string = str(number)
if num_string == num_string[::-1]:
    print(number,"is Palindrome")
else:
    print(number,"is not a Palindrome")
