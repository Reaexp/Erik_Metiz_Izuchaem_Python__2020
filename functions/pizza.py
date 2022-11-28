# def make_pizza(*topings):
#     print(topings)
# make_pizza('peperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(*topings):
#     print("Making pizzas with the following topings: ")
#     for toping in topings:
#         print(f' - {toping}')
# make_pizza('peperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(size, *topings):
    print(f"Making {size} with the following topings: ")
    for toping in topings:
        print(f' - {toping}')
make_pizza(16, 'peperoni')
make_pizza(23, 'mushrooms', 'green peppers', 'extra cheese')