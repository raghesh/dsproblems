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
     adjascent elements and swap if the first one is greater than the second.
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

  def Sort(self, List):
    N = len(List)
    for I in range(0, N - 1):
      for J in range(0, N - I - 1):
        if List[J] > List[J + 1]:
          # Swap
          List[J], List[J + 1] = List[J + 1], List[J]

    self.SortedList = List
    return self.SortedList
  
  def getComplexity(self, N):
    """Gets the time complexity of specified algorithm.
    """
