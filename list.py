def ConsolodateList(input_list):
    output_list = []
    for el in input_list:
        if not el in output_list:
            output_list.append(el)
    return output_list


print(ConsolodateList([1,2,3,3,3,3,4,5,5,5,5,1,1,1,1]))


