from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range(size-1):
    for j in range(i+1,size):
        minimum = i
        if array[j] < array[minimum]:
            minimum = j
      temp = array[minimum]
      array[i] = array[mimimum]
      array[i] = temp
    
      

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
