total = 0
shouqian = 0


f = open('c.txt', 'r', encoding='utf-8')
readline = f.readline()
while readline:
    total += 1
    str_array = readline.replace("\n", "").split(' ')

    # my_send_msg(str_array[0], str_array[1])
    print(str_array[0].split("：")[1],end='')
    if '售前' in str_array[1]:
        print(f'(售前未成交，{str_array[2].split("，")[0].split("：")[1]})，',end='')
        shouqian += 1
    elif '售后' in str_array[1]:
        print(f'({str_array[1]}，{str_array[2].split("，")[0].split("：")[1]})，',end='')

    # print(str_array[0],str_array[1])
    readline = f.readline()
print()
print(f'总数：{total}，售前：{shouqian}')