def mul(n):
    if (n <= 0):
        print("{} is invalid".format(n))
    else:
        for num in range(1, n + 1):
            print("-" * 50)
            print("Mul table for :{}".format(num))
            print("-" * 50)
            for i in range(1, 11):
                print("\t {} X {} = {}".format(num, i, num * i))
            else:
                print("-" * 50)

    # else:
    #     for i in range(1,11):
    #         print("\t {} X {} = {}".format(n, i, n * i))
    #     else:
    #         print("-" * 50)