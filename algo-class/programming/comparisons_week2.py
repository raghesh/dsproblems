import sorting as Sort

f = open("QuickSort.txt")
f_content = f.read()
l = f_content.split()
l_int = [int(i) for i in l]
S = Sort.QuickSort()
S.Sort(l_int, PivotMethod = "First")
#S.Sort(l_int, PivotMethod = "Final")
#S.Sort(l_int, PivotMethod = "Median")
print S.getNumberOfComparisons()
