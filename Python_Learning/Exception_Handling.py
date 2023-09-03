
try:  # Exception code we write here
    firstNo = int(input("Enter first no: "))
    secondNo = int(input("Enter second no: "))
    print("Devidation: ", firstNo / secondNo)
except Exception as e:  # solution for exception (exception handling code) here
    print("Except Block: Exception type is....",e)
else:  # It executed, when did not get exception
    print("Else block: No Excepiton foound")
finally: # It executed in anyhow when weatherwe got exception or not
    print("Finally block: Exception handling process complete")


