# try:
#     file = open("abc.txt")
# except Exception as e:
#     print("Exception raised")
#     print(e)
# finally:
#     print("Execution completed")

a=50
b=70

try:
    if a<b:

        raise Exception("OOPS value of A is less than B")
except Exception as e:

    print(e)




