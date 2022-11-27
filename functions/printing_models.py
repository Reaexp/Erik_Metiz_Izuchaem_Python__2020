# Список моделей которые нужно напечатать
# unprintrd_disigns = ['phone case', 'robot pedant', 'dodecahedron']
# completed_model = []
#
# while unprintrd_disigns:
#     current_design = unprintrd_disigns.pop()
#     print(f"Printing model: {current_design}")
#     completed_model.append(current_design)
#
# print("\nThe following models have been printed:")
# for completed_mod in completed_model:
#     print(completed_mod)


unprintrd_disigns = ['phone case', 'robot pedant', 'dodecahedron']
completed_model = []

def print_models(unprintrd_disigns, completed_model ):
    while unprintrd_disigns:
        current_design = unprintrd_disigns.pop()
        print(f"Printing model: {current_design}")
        completed_model.append(current_design)


def show_complited_models(completed_model):
    print("\nThe following models have been printed:")
    for completed_mod in completed_model:
        print(completed_mod)

print_models(unprintrd_disigns, completed_model)
show_complited_models(completed_model)
