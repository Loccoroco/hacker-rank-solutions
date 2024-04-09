def twoArrays(k, A, B):
    yes = 0
    A.sort()
    B.sort()
    n = 'yes'

    for num_a in A:

        for num_b in B:

            if num_a + num_b >= k:
                yes += 1
                B.remove(num_b)
                break

    if n == yes:

        return 'YES'

    else:

        return 'NO'


print (twoArrays(2, [1,2,3], [1,2,3]))
