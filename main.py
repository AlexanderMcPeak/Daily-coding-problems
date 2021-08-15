A = [10, 15, 3, 7]
k = 17

j = 0
P = "17"
i = 0
while i != len(A):
    j = i + 1
    while j != len(A):
        if(A[i] + A[j] == 17):
            print(A[i])
            print(A[j])
            print(i)
            print(j)
        j = j + 1
    i = i + 2



