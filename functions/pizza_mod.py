def make_pizza(size, *topings):
    print(f"Making {size} with the following topings: ")
    for toping in topings:
        print(f' - {toping}')
