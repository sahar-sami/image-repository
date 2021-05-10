import pandas as pd
import os
class ImageRepo:

  def __init__(self):
    if os.path.exists("repo.csv"):
      try: 
        df = pd.read_csv("repo.csv")
      except pandas.io.common.EmptyDataError:
        df = pd.DataFrame(columns=["path", "category", "description"])
    else:
      df = pd.DataFrame(columns=["path", "category", "description"])
    self.df = df
    self.df.to_csv("repo.csv", index=False)


  def add_image(self, path, category, description):
    if path in list(self.df['path']):        # this image already exists
      return False
    self.df = self.df.append({"path": path, "category": category, "description": description}, ignore_index=True)
    self.df.to_csv("repo.csv", index=False)
    return True


  def delete_image(self, ids):
    # ids should be a list of integers
    for i in ids:
      if i < 0 or i >= len(self.df): # at least one of the indices is out of range
        return False
    self.df = self.df.iloc[[i for i in range(len(self.df)) if i not in ids]]
    self.df = self.df.reset_index().drop("index", axis=1)
    self.df.to_csv("repo.csv", index=False)
    return True

  def row_exists(self, path, category, desc):
    return ((self.df['path'] == path) & (self.df['category'] == category) & (self.df['description'] == desc)).any()

  def clear_repo(self):
    os.remove("repo.csv")
    self.df = pd.DataFrame(columns=["path", "category", "description"])