def good_subarray_sum(N, A):
    total_sum = 0
    length = 1  

    for i in range(1, N):
        if abs(A[i] - A[i - 1]) == 1:
            length += 1  
        else:
            total_sum += (length * (length + 1) // 2) * sum(A[i - length:i])
            length = 1  

    total_sum += (length * (length + 1) // 2) * sum(A[N - length:])

    return total_sum