def MyRange(*args):
    args = list(args)
    args = list(map(int, args))
    if len(args) == 1:
        finish = args[0]
        num = 0
        step = 1
        while num < finish and step > 0:
            yield num
            num += step

    if len(args) == 2:
        finish = args[1]
        num = args[0]
        step = 1
        while num < finish and step > 0:
            yield num
            num += step

    if len(args) == 3:
        finish = args[1]
        num = args[0]
        step = args[2]
        while num < finish and step > 0:
            yield num
            num += step

        while num > finish and step < 0:
            yield num
            num += step

for i in MyRange(0, 68):
    print(i)