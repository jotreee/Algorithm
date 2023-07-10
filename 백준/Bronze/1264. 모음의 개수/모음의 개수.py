while True:
    sentence = input()
    if sentence == '#':
        break
    result = 0
    for s in sentence:
        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U':
            result += 1
    print(result)