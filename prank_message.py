import os
def rename_files():
  #(1) get file names from a folder
  file.list = os.listdir(r"C:\Users\Evan\Desktop\prank")
  print (file_list)
  saved_path = os.getcwd()
  print("Current Working Directory is "+saved_path)
  os.chdir(r"C:\Users\Evan\Desktop\prank")
  #(2) rename files
  for file_name in file_list:
      os.rename(file_name, file_name.translate(None, "0123456789"))
rename_files()
