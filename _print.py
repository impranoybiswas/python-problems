from calculate_factorial import calculate_factorial
from calculation import calculation
from check_even_or_odd import check_even_or_odd
from check_palindrome import is_palindrome
from check_prime import is_prime
from check_vowels import separate_vowels, vowels_count
from genarate_fibonacci import genarate_fibonacci
from duplicates import only_duplicates, remove_duplicates
from reverse import reverse_full_text, reverse_number, reverse_per_word

number = 5
nums = [1, 2, 3, 4, 5, 4]
word = "Programming"
sentence = "I am learning Python"

# calculation(nums)
# print("The number is :", check_even_or_odd(5))
# print("Is Prime Number :", is_prime(6))
# print(reverse_full_text(sentence))
# print(reverse_per_word(sentence))
# print(reverse_number(123444001))

# print("Factorial of", number, ":", calculate_factorial(number))

# print("Is Palindrome :", is_palindrome("malayalam"))

# print("Fibonacci Series :", genarate_fibonacci(10))

# print("Vowels Count :", vowels_count(word))
# print("Vowels Count :", separate_vowels(word))

print("Remove Duplicates :", only_duplicates(nums))