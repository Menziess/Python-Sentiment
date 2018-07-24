import csv

class Writer:
  """Writes array to csv"""

  def toCsv(filename, array):
    """

    Parameters
    ----------
    filename : str
        Location to write file to.
    array : List
        Array that needs to be written.

    """
    with open(filename, 'w', newline='') as c:
        writer = csv.writer(c, delimiter=',')
        writer.writerow(array)
