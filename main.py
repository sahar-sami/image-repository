from storage import ImageRepo
from search import query
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.withdraw()

repo = ImageRepo()

def main():
  selection = ""
  while selection.lower() not in ['a', 'b', 'c', 'd']:
    selection = input("Please select an action: \
      \n [A] List all images \n [B] Search for an image \
      \n [C] Add an image \n [D] Delete an image \n")
  if selection.lower() == "a":
    if len(repo.df) == 0:
      print("No images here yet.")
    else:
      print(repo.df)
  elif selection.lower() == "b":
    category = input("Enter a category to search, or press Enter if you don't want a certain category: ")
    keywords = input("Enter some keywords, like 'beach picture', or press Enter: ")
    result = query(category, keywords)
    if len(result) == 0:
      print("No images were found.")
    else:
      print("Top Results:")
      print(result)
      see_images = input("Would you like to see the images? Input Y if yes. ")
      if see_images.lower() == "y":
        images = list(result['path'])
        for img in images:
          Image.open(img).show()

  elif selection.lower() == "c":
    print("Select an image: ")
    pathname = filedialog.askopenfilename()
    possible_categories = repo.df['category'].unique()
    categories_string = "\n".join([f"\t[{i}] {name}" for i, name in enumerate(possible_categories)])
    print("Select a category from the following, or input a new category name: ")
    category = input(categories_string + "\n")
    if category.isdigit() and int(category) < len(possible_categories):
      category = possible_categories[int(category)]
    description = input("Enter a short phrase describing your image: ")
    if repo.add_image(pathname, category, description):
      print("Image successfully added!")
    else:
      print("Image already exists. ")
  else:
    print(repo.df)
    ids = input("Enter the ID number of each image you want to delete separated by spaces: ").split()
    ids = [int(id) for id in ids]
    if repo.delete_image(ids):
      print("Image successfully deleted.")
    else:
      print("This image does not exist in the repository.")
  return

if __name__ == '__main__':
  cont = "Y"
  while cont.lower() == "y":
    main()
    cont = input("Continue? (Y/N): ")