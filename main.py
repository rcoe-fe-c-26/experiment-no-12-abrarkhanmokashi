# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder:
# Date:

print("--- Extracting Words from Text File ---\n")
with open("story.txt","r") as file:
  text=file.read().split()
  length=int(input("Enter Length of Words: "))
  list1=[]
  for x in text:
    if (len(x)==length):
      list1.append(x.lower())
  new_list=sorted(set(list1))
  print(f"Words with length {length} are: {new_list}")

