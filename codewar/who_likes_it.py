def likes(names):
    like = " like"
    likes = " likes"
    postfix = " this"
    
    if not names:
        return "no one" + likes + postfix
    if len(names) == 1:
        return names[0] + likes + postfix
    first_2_names = names[:2]
    left_names_number = len(names) - 2
    
    if left_names_number == 0:
        return first_2_names[0] + " and " + first_2_names[1] + like + postfix
    elif left_names_number == 1:
        return first_2_names[0] + ", " + first_2_names[1] + " and " + names[2:][0] + like + postfix
    else:
        return first_2_names[0] + ", " + first_2_names[1] + " and " + str(left_names_number) + " others" + like + postfix


if __name__ == "__main__":
    print(likes(["Alex", "Jacob", "Mark", "Max"]))
