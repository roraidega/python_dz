def f (n, target):
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            if n[i]+n[j] == target:
                return [i,j]
            return

        n = [2,7,11,15]
        target = 9
        print(f(n,target))
