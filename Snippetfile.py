list1=[2,6,8,]
list2=[7,5,4,]
mytuple=("visualbasic.NET","java","PHP","MATLAB","ruby")
myDict={"visualbasic.NET":"easy","java":"moderate","PHP":"difficult","MATLAB":"advanced"}
#assigning elements to different list
list1.append(5)
list2.append(0)
print("Elements availabe in list1 are:",list1,)
print("Elements available in list2 are:",list2,)
#accessing a element from a tuple
print(mytuple[3])
#Dict
print("Programming languages available in dictionaries are:",myDict)
del myDict["PHP"]
#after deleting ruby from dict 
print("Programming languages in dictionaries are:",myDict)