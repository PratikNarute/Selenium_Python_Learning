# break: it break loop and start to next line
# continue: it stop execution with next line and continue with loop until and unless the condition become true


list = [1,2,3,4,5,6,7,8,9,10]
index=0
while index < len(list):

    print(list[index])
    index=index + 1

    if index == 5:
        break
print("===========stop=============")

tup = (1,2,3,4,5)

index=0

while index<len(tup):
    print(tup[index])
    if index == 4:
       print("Stop iteration")
       break
    else:
        print("Start iteration")
        index += 1
        continue


