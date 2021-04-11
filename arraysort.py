# Python program to merge two sorted arrays
 
# Merge A[0..n1-1] and
# B[0..n2-1] into
# C[0..n1+n2-1]
def mergeArrays(A, B, n1, n2):
    C = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
 
    # Traverse both array
    while i < n1 and j < n2:
     
        # Check if current element of first array is smaller than current element of second array. 
        #If yes, store first array element and increment first array index.
        # Otherwise do same with second array
        if A[i] < B[j]:
            C[k] = A[i]
            k = k + 1
            i = i + 1
        else:
            C[k] = B[j]
            k = k + 1
            j = j + 1
     
 
    # Store remaining elements of first array
    while i < n1:
        C[k] = A[i];
        k = k + 1
        i = i + 1
 
    # Store remaining elements of second array
    while j < n2:
        C[k] = B[j];
        k = k + 1
        j = j + 1
    print("Array after merging")
    for i in range(n1 + n2):
        print(str(C[i]), end = " ")
 
# Driver code
A = [1, 2, 7, 11] 
n1 = len(A)
 
B = [3,7,13,16,29]
n2 = len(B)
mergeArrays(A, B, n1, n2);