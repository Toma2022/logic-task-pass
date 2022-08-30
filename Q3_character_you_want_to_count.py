a=list(str(input("input a word")))
count_char=str(input("input character you want to count"))

result = dict((count_char, a.count(count_char)) for i in a)
print(result)

