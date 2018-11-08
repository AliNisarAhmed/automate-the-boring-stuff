def commaCode(list):
  result = ''
  for elem in list:
    if list[-1] == elem:
      result += 'and ' + str(elem)
    else:
      result += str(elem) + ', '
  return result

print(commaCode([1, 2, 3, 4]))
print(commaCode(['a', 'b', 'c', 'd']))