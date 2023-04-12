def geom_progr_gen(start, step):
    item = start
    while True:
        yield item
        item *= step


g = geom_progr_gen(1, 2)
for i in range(10):
    print(next(g))
