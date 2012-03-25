import sorting as Sort

f = open("IntegerArray1.txt")
f_content = f.read()
l = f_content.split()
l_int = [int(i) for i in l]
S = Sort.BubbleSort()
#S = Sort.MergeSort()
S.Sort(l_int)
print S.GetInversionListCount()
