number = int(input("1-ден 9-ға дейінгі санды таңдаңыз: "))


if 1 <= number <= 9:
    for n in range(1, number + 1):
        print(f"{n} санының көбейту кестесі:")
        for i in range(1, n + 1):
            result = n * i
            print(f"{n} x {i} = {result}")
        for i in range(n + 1, 10):  # 1-ден 9-ға дейін
            result = n * i
            print(f"{n} x {i} = {result}")
        print()  # Әр кестеден кейін жаңа жол
else:
    print("Қате! 1-ден 9-ға дейінгі сан таңдаңыз.")