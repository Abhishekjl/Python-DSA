# creating factorial program

# def fact(n):
#     if n == 0: # if we pass n = negative then n will never be zero
#         return 1
#     if n<0:
#         print('factorial of negative number not defined')
#         return None    
#     else:
#         small_answer = n*fact(n-1)
#         return small_answer


# print(fact(10))            


# fibonacci series
def fibo(n):
    if n == 0: # base case
        return 0 
    if n == 1:
        return 1    

    # recursive case
    small_output1 = fibo(n-1)
    small_output2 = fibo(n-2)

    # calculation 

    return small_output1+small_output2


print([fibo(i) for i in range(10)])