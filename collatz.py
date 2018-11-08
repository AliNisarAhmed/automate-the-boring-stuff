# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.
# (Amazingly enough, this sequence actually works for any integer—sooner
# or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
# sure why. Your program is exploring what’s called the Colltaz sequence

def collatz(num):
  if num == 1:
    return 1
  elif num % 2 == 0:
    num = num // 2
    print(num)
    return collatz(num)
  else:
    num = num * 3 + 1
    print(num)
    return collatz(num)

num = int(input('Enter a number: '))
print(num)
collatz(num)