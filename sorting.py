class Sorting:
  """This is the base class which implements common functions required for all
     sorting algorithms.
  """

  def __init__(self):
    self.sortedList = []

  def plotComplexityGraph(self):
    """Plot graph to compare complexities of all algorithms for same value of N.
    """

class InsertSort(Sorting):
  """Describe the logic of insertion sort here.
  """

  def __init__(self):
    self.sortedList = []

  def Sort(self, List):
    self.sortedList = List
    return self.sortedList
  
  def getComplexity(self, N):
    """Gets the time complexity of specified algorithm.
    """

class BubbleSort(Sorting):
  """Describe the logic of bubble sort here.
  """

  def __init__(self):
    self.sortedList = []

  def Sort(self, List):
    self.sortedList = List
    return self.sortedList
  
  def getComplexity(self, N):
    """Gets the time complexity of specified algorithm.
    """
