
'''
Function which takes in parameters: path of directory, [list of extensions acceptable]

Respect subdirectories relative path in zipped files. 

Passing trough to know if it is a directory or not with os.walk(path)

Seek the 

'''

import os
import zipfile

def zipfiles(path,output,extensions):
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as ziph:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.split('.')[1] in extensions:
                    ziph.write(os.path.join(root, file), 
                            os.path.relpath(os.path.join(root, file),
                            os.path.join(path, '..')))    
        
zipfiles("C:/Users/Researcher/Documents/Churhe's doc",
         "storedata.zip",
         ['jpg','docx']
    )    
    

 