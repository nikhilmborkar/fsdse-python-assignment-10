def convert(input_lst):
    C_to_F = []
    for items in input_lst:
        C_to_F.append(((items*9)/5)+32)
    return C_to_F
