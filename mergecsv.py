import csv

def mergefiles(list_of_filess, out_put_path):
  #get the general fieldnames
  fieldnames=[]
  
  for file_path in list_of_filess:
    with open(file_path,'r') as readerFile:
      field= csv.DictReader(readerFile).fieldnames
      fieldnames.extend(column for column in field if column not in fieldnames) 
  #writing in the file
  with open(out_put_path,'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  
    for file_path in list_of_filess:
      with open(file_path) as csvfile:
        reader= csv.DictReader(csvfile)
        for row in reader:
          writer.writerow(row)

