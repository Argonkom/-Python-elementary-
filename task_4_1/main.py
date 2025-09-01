#main.py
def findNum(str):
    for i in range(len(str)):
        count = 0
        for j in range(len(str)):
            if str[i] == str[j]:
                count += 1
        print(f"{str[i]}, occured {count} time's")
