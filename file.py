with open("demo.txxt") as f1:
    # print(f.tell())
    # print(f.read(10))
    # print(f.tell())
    # f.seek(5)
    # print(f.read(5))
    # f.seek(10)
    # print(f.readlines())
    with open("1.txt","a") as f2:
        f2.write("")
        for a in f1:
          f2.write(a)