lst = "Where now? Who now? When now?".split("?")
lst = lst[:3]
for i in range(len(lst)):
    lst[i] = lst[i] + "?"
print(lst)
