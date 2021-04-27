def swapFileData () :
    text1 = input("enter file name1: ")
    text2 = input("enter file name2: ")
    f1 = open(text1)
    f2 = open(text2)

    data_a = f1.read()
    data_b = f2.read()

    data_w1 = open(text1, "w")
    data_w2 = open(text2, "w")

    data_w1.write(data_b)
    data_w2.write(data_a)

swapFileData()