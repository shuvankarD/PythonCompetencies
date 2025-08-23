with open("test.txt","r") as reader:
    list = reader.readlines()
    rev_list=reversed(list)

    with open("test.txt","w") as writer:
        for i in rev_list:
          writer.write(i)

