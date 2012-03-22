def get_inversions_list(l):
  count = 0
  ilist = []
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[i] > l[j]:
        count = count + 1
        #ilist.append([l[i], l[j]])

  return count

f = open("IntegerArray.txt")
f_content = f.read()
l = f_content.split()
l_int = [int(i) for i in l]
print get_inversions_list(l_int)
