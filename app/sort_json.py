def sort_json(lis, priority, order):
    reshape_list(lis, priority)
    for i in range(len(lis)):
        # 比較作業を最後まで繰り返し、最大値をソート済みとします。（手順３,4,5）
        for j in reversed(range(i + 1, len(lis))):
            # 数値aとbを比較します。(手順１)
            if order == "up":
                if int(lis[j - 1][priority]) > int(lis[j][priority]):
                    # 数値a>bの場合、aとbの値を入れ替えます。(手順２)
                    lis[j - 1], lis[j] = lis[j], lis[j - 1]
            else:
                if int(lis[j - 1][priority]) < int(lis[j][priority]):
                    # 数値a>bの場合、aとbの値を入れ替えます。(手順２)
                    lis[j - 1], lis[j] = lis[j], lis[j - 1]
    return_lis = []
    none_lis = []
    for i in range(len(lis)):
        if lis[i][priority] == 0:
            lis[i][priority] = None
            none_lis.append(lis[i])
        else:
            return_lis.append(lis[i])

    for i in range(len(none_lis)):
        return_lis.append(none_lis[i])

    # print("return_lis: ",return_lis)
    return return_lis


def reshape_list(lis, priority):
    for i in range(len(lis)):
        if lis[i][priority] == "":
            lis[i][priority] = 0
    return lis
