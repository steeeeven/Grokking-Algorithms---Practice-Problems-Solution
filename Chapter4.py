# Problem 4.1
def sum(arr):
  
  # print(val)
  if arr == []:
    return 0
  else:
    val = arr.pop(0)
    # print(val)
    # print(f"{arr} \n")
    return val + sum(arr)
array = [5,3,7,3,8,20]
print(sum(array))


# Problem 4.2
def count(list):
  if list == []:
    return 0
  return 1+count(list[1:])

list = [2,6,3,9,0,2,1]
print(count(list))
