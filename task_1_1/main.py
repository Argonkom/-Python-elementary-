mydict = {
    "NO": ["###",
           "###",
           "###"],

    "LR": ["###",
           "   ",
           "###"],

    "LT": ["# #",
           "  #",
           "###"],

    "BR": ["###",
           "#  ",
           "# #"],

    "LB": ["###",
           "  #",
           "# #"],

    "TR": ["# #",
           "#  ",
           "###"],
}

NO = mydict["NO"]
LR = mydict["LR"]
LT = mydict["LT"]
BR = mydict["BR"]
LB = mydict["LB"]
TR = mydict["TR"]

def render(list):
    for row in list:
        for i in range(3):
            result = ""
            for el in row:
                result += el[i]
            print(result)
render([
    [NO, BR, LR, LB, NO], [LR, LT, NO, TR, LR]
])
