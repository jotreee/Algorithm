while True:
    code = input()
    if code == "END":
        break
    code = reversed(list(code))
    print("".join(code))