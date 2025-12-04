1 - misol
numbers = [-10, -5, -2, 1]
result = list(map(lambda x: abs(x), numbers))
print(result)

2 - misol
words = ["salom", "dunyo", "hayr"]
result = list(map(lambda x: x[::-1], words))
print(result)

3 - misol
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**3, numbers))
print(result)

4 - misol
words = ["salom", "dunyo", "hayr"]
result = list(map(lambda x: x[0], words))
print(result)

5 - misol
numbers = [10, 20, 39, 40, 69]
result = list(map(lambda x: "Juft" if x % 2 == 0 else "Toq", numbers))
print(result)
