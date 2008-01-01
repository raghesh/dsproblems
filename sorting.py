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

  def ChoosePivot(self, List):
    """Returs the index of the pivot element."""
    return 0

  def Partition(self, List, PivotIndex):
    """All elments to the left of pivot element are less than pivot and to the
       right are greater than pivot. Returns the index of pivot element"""
    Pivot = List[PivotIndex]
    
    GreatestElementIndex = PivotIndex
    for Element in List:
      if Element == Pivot:
        GreatestElementIndex += 1
      elif Element > Pivot:
        GreatestElementIndex = List.index(Element)
      elif Element < Pivot:
        # Swap greatest element and current element.
        ElementIndex = List.index(Element)
        List[ElementIndex], List[GreatestElementIndex] = \
        List[GreatestElementIndex], List[ElementIndex]
        # Swap current element and pivot element.
        List[GreatestElementIndex], List[PivotIndex] = \
        List[PivotIndex], List[GreatestElementIndex]
        PivotIndex = GreatestElementIndex
        GreatestElementIndex += 1
      print List, PivotIndex, GreatestElementIndex
    return PivotIndex

  def QSort(self, List):
    if len(List) <= 1:
      return List
    # Pivot is the index of pivot element.
    PivotIndex = self.ChoosePivot(List)
    PivotIndex = self.Partition(List, PivotIndex)
    self.QSort(List[:PivotIndex])
    self.QSort(List[PivotIndex + 1:])
    return List

  def Sort(self, List):
    self.SortedList = self.QSort(List)
    return self.SortedList

  def getComplexity(self, N):
    """Gets the time complexity of specified algorithm.
    """
