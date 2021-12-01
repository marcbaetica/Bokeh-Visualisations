from bokeh.plotting import figure, show
from random import choice
from time import sleep


increment_amount = [i for i in range(1, 4)]
print(increment_amount)

x = [1, 2, 3]
y = [0, 0, 0]

while all([item < 30 for item in y]):
    index = choice([0, 1, 2])
    y[index] = y[index] + choice(increment_amount)
    print(y)
    # sleep(0.25)
    print([item < 30 for item in y])

p = figure()
p.vbar(x=x, top=y, width=0.8)
show(p)
