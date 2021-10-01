# creating  a function to take the input array 
#sorting according to the complexity of selection sort algorithm and returning the output.
def sort(A):  
    k=len(A)
    for i in range(k-1):
        minu=99999999
        for j in range(i,k-1):
            if(A[j]<minu):
                minu=A[j]
                m=j
        temp=A[i]
        A[i]=minu
        A[m]=temp
    print(A)
    return A    
