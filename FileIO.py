import numpy as np

class FileIO:
    def __init__(self, filePathIn):
        self.filePath = filePathIn
        self.dataTable = np.loadtxt(self.filePath, delimiter=',', skiprows=1,usecols=(0,1,2,3,4), dtype=np).astype(float)

