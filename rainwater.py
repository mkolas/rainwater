with open("elevation1.txt") as f:
    elevations = f.readline()

elevations = [int(x) for x in elevations]
map_ = []

for y in range(max(elevations)):  # create our dumb map
    map_.append(['#' if x > y else '.' for x in elevations])

for row in map_:
    start_catch = -1
    for i, x in enumerate(row):
        if x is '#':
            if start_catch > -1 and (i - start_catch) > 1:
                row[start_catch+1:i] = ['~' for i in range(i-(start_catch+1))]
            start_catch = i

for row in map_[::-1]:
    print(row)
