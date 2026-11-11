
a_map = {

}

f = open('a.txt', 'r', encoding='utf-8')
readline = f.readline()
while readline:
    str_array = readline.replace("\n","").split(' ')

    # my_send_msg(str_array[0], str_array[1])
    if str_array[1] in a_map:
        a_map[str_array[1]] = a_map[str_array[1]] + str_array[0]+'\n'
    else:
        a_map[str_array[1]] = str_array[0]+'\n'

    # print(str_array[0],str_array[1])
    readline = f.readline()

# with open("data.txt", "w", encoding="utf-8") as f:
#     f.write(str(a_map))
print(a_map['金香鸭屎'])