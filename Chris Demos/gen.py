def frange(start=1.0, stop=1.0, step=0.25):
    num = start
    if step != 0:
        while num < stop:
            yield num
            num += step

print(list(frange(1.1, 3)))
print(list(frange(1, 3, 0.33)))
print(list(frange(1, 3, 1))) # Should print [1.0, 2.0]
print(list(frange(3, 1))) # Should print an empty list
print(list(frange(1, 3, 0))) # Should print an empty list
print(list(frange(-1, -0.5, 0.1)))

for num in frange(3.142, 12):
    print(f"{num:05.2f}")