def openOrSenior(data):
    result = []
    for v in data:
        age = v[0]
        level = v[1]
        if age >= 55 and level >7:
            result.append("Senior")
        else:
            result.append("Open")
    return result


if __name__ == "__main__":
    print(openOrSenior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]))
