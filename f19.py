#Write a Python program to create Fibonacci series upto n using Lambda.
n=int(input("Enter a number:- "))
def fibonacci(count):
	fib_list = [0, 1]

	any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
										range(2, count)))

	return fib_list[:count]

print(fibonacci(n)) 
