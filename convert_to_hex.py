def convert_to_list():
    print("Hu")
    data = "05 1E 7D 01 00 0B 03 00 03 01 01 00 09 00 00 00 00 00 00 00 EE 59"
    lst =data.split()
    print (lst)
    #lst2 = [hex(int(x, 16)) for x in lst]
    lst2 = ['0x' + x for x in lst]
    return lst2
 
if __name__ == "__main__":
    print (("[{0}]".format(', '.join(map(str, convert_to_list())))))