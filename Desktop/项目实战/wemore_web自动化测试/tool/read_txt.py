def read_txt(filename):
    filepath = "../data/"+filename
    with open(filepath,"r", encoding="utf-8") as f:
        return f.readlines()


# if __name__ == '__main__':
#     arrange = []
#     for data in read_txt("login.txt"):
#         arrange.append(tuple(data.strip().split(",")))
#     print(arrange[1:])
#     增加一行注释
