def fibbonacci_generator(num):
    x = 1
    y = 1
    sum = 0
    fibbo_nums = []
    fibbo_nums.append(x)
    fibbo_nums.append(y)
    for i in range(num):
        checkFib = x + y
        if checkFib <= num:
            fibbo_nums.append(checkFib)
            x, y = y, checkFib
    print(fibbo_nums)

    for j in range(len(fibbo_nums)):
        if fibbo_nums[j]%2 != 0 and fibbo_nums[j] <= num:
            sum += fibbo_nums[j]
    print(f'Sum of all fibbonaci odd numbers in range {num} is {sum}')
        
        

fibbonacci_generator(100)
