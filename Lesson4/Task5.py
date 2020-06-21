from functools import reduce

# reduce получает функцию "что делать" в виде лямбда функции
# и list по которому ведутся итерации
result = reduce(lambda a, b: a + b, [step for step in range(100, 1001) if step % 2 == 0])
print(result)
