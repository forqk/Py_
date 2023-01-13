import os.path

class FileReader:
    def __init__(self, filePath = None):
        self._filePath = filePath
        
    def read(self):
        try:
            if not os.path.exists(self._filePath):
                raise FileNotFoundError()  
            
            with open(self._filePath, 'r') as file:
                return(file.read())

        except FileNotFoundError:
            return('')
            
        
