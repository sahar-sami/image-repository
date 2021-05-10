from storage import *
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def query(category = "", keywords = ""):
  '''
  Returns the top 3 results (or fewer if there are less than 3) of a query that contains a category
  and/or a set of keywords describing the desired images. If a category is provided, results
  are filtered to include only images of that category. If keywords are provided, results 
  are ordered using cosine similarity on the descriptions of the images.

  Return type: DataFrame
  '''
  repo = ImageRepo()
  df = repo.df
  if len(category) > 0:
    df = df[df['category'] == category].reset_index()
    df.drop("index", axis=1, inplace=True)
  if len(df) == 0:
    return df
  if keywords:
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(df['description']).toarray()
    input_tfidf = vectorizer.transform([keywords]).toarray()
    results = []
    for i in range(tfidf.shape[0]):
      # compute cosine similarity based on formula: (A * B) / (||A|| * ||B||)
      tfidf_flat = tfidf[i].flatten()
      input_flat = input_tfidf.flatten()
      cosine_sim = tfidf[i].dot(input_tfidf.T)/(np.linalg.norm(tfidf_flat) * np.linalg.norm(input_flat))
      results.append((i, cosine_sim))
    # sort and return top 3 results
    results = sorted(results, key=lambda x: x[1], reverse=True)[:3]
    final = df.iloc[[idx for idx, score in results]]
  else:
    final = df
  final = final.reset_index()
  final['rank'] = final.index + 1
  final.drop("index", axis=1, inplace=True)
  final = final.set_index('rank')
  return final

  
