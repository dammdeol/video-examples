from decimal import Decimal
from datetime import datetime, timedelta

# Python String Format Specifiers: https://pyformat.info/

a = Decimal("0.1")
b = Decimal("0.2")
c = a + b
print(f"{a} + {b} = {c}")
print(f"{a!r} + {b!r} = {c!r}")
print()

x = 0.1
y = 0.2
z = x + y
print(f"{x} + {y} = {z}")

print(f"{c} == {z} is {c == z}")
print(f"{c} == {z} is {c == 0.30}")
print(f"{c!r} == 3 * {a!r} is {c == 3*a}")
print()

d1 = datetime.now()
d2 = d1 + timedelta(days=12)
print(d1)
print(d2)

# https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-behavior
print(d2.strftime("%a %Y-%m-%d %H:%M:%S"))
