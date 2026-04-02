good_girl = True
same_age = 0
criminal = 1

if good_girl and same_age and not criminal:
    print("My frind")
elif (good_girl or same_age )and not criminal:
    print("can be my friend")
elif good_girl or same_age or criminal:
    print("go to jail")
else:
    print("not good")
