class Sorting:
  """This is the base class which implements common functions required for all
     sorting algorithms.
  """

  def __init__(self):
    self.SortedList = []

  def plotComplexityGraph(self):
    """Plot graph to compare complexities of all algorithms for same value of N.
    """

class InsertSort(Sorting):
  """Insertion sort can be compared to arranging playing cards in our left
     hand. Each card is taken from the table and it is placed into its
     position. Eg :- L = [5,| 1, 7, 2, 6]. Here elements left to the symbol
     | are already sorted.
     Step 1: key = 1, L = [1, 5,| 7, 2, 6]
     Step 2: key = 7, L = [1, 5, 7,| 2, 6]
     Step 3: key = 2, L = [1, 2, 5, 7,| 6]
     Step 4: key = 6, L = [1, 2, 5, 6, 7|]
  """

  def __init__(self):
    self.SortedList = []

  def Sort(self, List):
    for I in range(1, len(List)):
      Key = List[I]
      J = I - 1
      while J >= 0 and Key < List[J]:
        List[J + 1] = List[J]
        J = J - 1
      List[J + 1] = Key

    self.SortedList = List
    return self.SortedList
  
  def getComplexity(self, N):
    """Gets the time complexity of specified algorithm.
    """

class BubbleSort(Sorting):
  """Starting from the first element in the list bubble sort compares two
     adjacent elements and swap if the first one is greater than the second.
     After each iteration of the outer loop the greatest element will be placed
     at the end of the sublist under consideration. Eg:- L = [5, 1, 7, 2, 6|].
     Here the sublist right to the symbol are already sorted.
     Step 1: key = 1, L = [1, 5, 2, 6, |7]
     Step 2: key = 1, L = [1, 2, 5, |6, 7]
     Step 3: key = 1, L = [1, 2, |5, 6, 7]
     Step 4: key = 1, L = [1, |2, 5, 6, 7]
  """

  def __init__(self):
    self.SortedList = []
    # This variable keeps the count of inversion lists. That is in a list A 
    # with if i < j and A[i] > A[j] we increment this count.
    self.InversionListCount = 0

  def Sort(self, List):
    N = len(List)
    for I in range(0, N - 1):
      for J in range(0, N - I - 1):
        if List[J] > List[J + 1]:
          # Swap
          List[J], List[J + 1] = List[J + 1], List[J]
          self.InversionListCount += 1

    self.SortedList = List
    return self.SortedList
  
  def GetInversionListCount(self):
    return self.InversionListCount
  
  def getComplexity(self, N):
    """Gets the time complexity of specified algorithm.
    """

class MergeSort(Sorting):

  def __init__(self):
    self.SortedList = []
    # This variable keeps the count of inversion lists. That is in a list A 
    # with if i < j and A[i] > A[j] we increment this count.
    self.InversionListCount = 0

  def Merge(self, L1, L2):
    L = []
    L_len = len(L1) + len(L2)

    i = 0
    j = 0
    for k in range(L_len):
      if i == len(L1) or j == len(L2):
        break
      if L1[i] < L2[j]:
        L.append(L1[i])
        i += 1
      else:
        L.append(L2[j])
        j += 1
        self.InversionListCount += len(L1[i:])
    
    if i == len(L1):
      L.extend(L2[j:])
      self.InversionListCount += len(L1[i:])
    if j == len(L2):
      L.extend(L1[i:])

    return L

  def MSort(self, List):
    if len(List) == 0 or len(List) == 1:
      return List
    L1 = List[0:len(List) / 2]
    L2 = List[len(List) / 2:len(List)]
    L1 = self.MSort(L1)
    L2 = self.MSort(L2)
    L = self.Merge(L1, L2)
    return L

  def Sort(self, List):
    self.SortedList = self.MSort(List)
    return self.SortedList

  def GetInversionListCount(self):
    return self.InversionListCount

  def getComplexity(self, N):
    """Gets the time complexity of specified algorithm.
    """

class QuickSort(Sorting):

  def __init__(self):
    self.SortedList = []
    self.NumberOfComparisons = 0

  def ChoosePivot(self, List, l, r, PivotMethod):
    """Returs the index of the pivot element according to the PivtoMethod."""
    if PivotMethod == "First":
       return l
    if PivotMethod == "Final":
      List[l], List[r - 1] =  List[r - 1], List[l]
    if PivotMethod == "Median":
      First = List[l]
      Final = List[r - 1]
      if (r - l) % 2 == 1:
        MiddleIndex = l + (r - l) / 2
        Middle = List[l + (r - l) / 2]
      else:
        MiddleIndex = l + (((r - l) / 2) - 1)
        Middle = List[l + (((r - l) / 2) - 1)]

      Median = sorted([First, Middle, Final])[1]
      if Median == First:
        return l
      elif Median == Final:
        List[l], List[r - 1] =  List[r - 1], List[l]
      else:
        List[l], List[MiddleIndex] =  List[MiddleIndex], List[l]
      
    return l

  def Partition(self, List, PivotIndex, l, r):
    """All elments to the left of pivot element are less than pivot and to the
       right are greater than pivot. Returns the index of pivot element"""
    p = List[PivotIndex]
    i = l + 1
    for j in range(l + 1, r):
      if List[j] < p: # if List[j] >p, do nothing
        List[i], List[j] = List[j], List[i]
        i += 1

    List[l], List[i - 1] = List[i - 1], List[l]

    PivotIndex = i - 1
    return PivotIndex

  def QSort(self, List, l, r, PivotMethod):
    if l >= r:
      return
    PivotIndex = self.ChoosePivot(List, l, r, PivotMethod)
    self.NumberOfComparisons += (r - l - 1)
    PivotIndex = self.Partition(List, PivotIndex, l, r)
    self.QSort(List, l, PivotIndex, PivotMethod)
    self.QSort(List, PivotIndex + 1, r, PivotMethod)
    # QuickSort is performing in place sorting. So no need to return anything.
    return

  def getNumberOfComparisons(self):
    return self.NumberOfComparisons
  def Sort(self, List, PivotMethod = "First"):
    self.NumberOfComparisons = 0
    self.QSort(List, 0, len(List), PivotMethod)
    self.SortedList = List
    return self.SortedList

  def getComplexity(self, N):
    """Gets the time complexity of specified algorithm.
    """
