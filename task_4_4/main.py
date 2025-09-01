#main.py
def findNum(str):
    result = []
    for i in range(len(str)):
        count = 0
        for j in range(len(str)):
            if str[i] == str[j]:
                count += 1
        result.append(f"{str[i]} occurred {count} time's")
    return result
