
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009    = 91 × 99.
This program intends to find the largest palindrome made from the product of    two n-digit numbers.
'''

digits_str = input("Enter no. of digits in multipliers : ")
digits = int(digits_str)

min_plier = (10 ** (digits-1))   # Minimum n-digit   number for eg. if digits = 3, min_plier = 100
max_plier = int("9" * digits)   # Maximum n-digit number for eg. if digits = 3, max_plier = 999

# Calculate product and get palindrome
pallindromes = []
for z in range (max_plier, min_plier , -1):
    max_plier_copy = z          # To avoide repetitive calcualtions.
    for x in range(max_plier_copy, min_plier, -1):
        global pallindromes
        product = z * x

        # Check if product obtained is palindrome and is greater than previously obtained palindrome.
        if (str(product) == str(product)[::-1]) :
            pallindromes.append(product)

print("Largest palindrome is : " + str(max(pallindromes)))
