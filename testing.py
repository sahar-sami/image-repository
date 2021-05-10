import unittest
from storage import *
from search import *
repo = ImageRepo()
repo.clear_repo()
class TestStorage(unittest.TestCase):

    def test_add_new(self):
      self.assertEqual(repo.add_image("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill"), True, "Should have been added")
      self.assertTrue(repo.row_exists("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill"))
      repo.clear_repo()
    
    def test_add_existing(self):
      repo.add_image("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill")
      self.assertFalse(repo.add_image("test_imgs/sunset1.jfif", "sunsets", "another description"), "image should already exist")
      repo.clear_repo()

    def test_delete_existing(self):
      repo.add_image("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill")
      repo.add_image("test_imgs/sunset2.jfif", "sunsets", "pink cloudy sunset")
      self.assertTrue(repo.delete_image([1]), "should have deleted")
      self.assertFalse(repo.row_exists("test_imgs/sunset2.jfif", "sunsets", "pink cloudy sunset"), "row should not exist anymore")
      repo.clear_repo()

    def test_delete_multiple(self):
      repo.add_image("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill")
      repo.add_image("test_imgs/sunset2.jfif", "sunsets", "pink cloudy sunset")
      self.assertTrue(repo.delete_image([0, 1]), "should have deleted")
      self.assertFalse(repo.row_exists("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill"), "row should not exist anymore")
      self.assertFalse(repo.row_exists("test_imgs/sunset2.jfif", "sunsets", "pink cloudy sunset"), "row should not exist anymore")

    def test_delete_nonexisting(self):
      self.assertFalse(repo.delete_image([0]), "should not be able to delete")
      self.assertFalse(repo.delete_image([-1]), "should not be able to delete")

    def test_search_no_category(self):
      repo.add_image("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill")
      repo.add_image("test_imgs/sunset2.jfif", "sunsets", "pink cloudy sunset")
      repo.add_image("test_imgs/sunset3.jfif", "sunsets", "sunset on the beach")
      repo.add_image("test_imgs/butterfly1.jfif", "butterflies", "butterfly on a pink flower")
      repo.add_image("test_imgs/butterfly2.jfif", "butterflies", "blue butterfly")
      repo.add_image("test_imgs/party1.jfif", "party pictures", "bonfire beach party")
      repo.add_image("test_imgs/party2.jfif", "party pictures", "dance party")
      repo.add_image("test_imgs/party3.jfif", "party pictures", "small dinner get together")
      results = query(keywords="pink sunset")
      print(results)
      self.assertEqual(results.loc[1]["path"], "test_imgs/sunset2.jfif", "the pink cloudy sunset should be the closest match")
      repo.clear_repo()

    def test_search_no_keywords(self):
      repo.add_image("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill")
      repo.add_image("test_imgs/sunset2.jfif", "sunsets", "pink cloudy sunset")
      repo.add_image("test_imgs/sunset3.jfif", "sunsets", "sunset on the beach")
      repo.add_image("test_imgs/butterfly1.jfif", "butterflies", "butterfly on a pink flower")
      repo.add_image("test_imgs/butterfly2.jfif", "butterflies", "blue butterfly")
      repo.add_image("test_imgs/party1.jfif", "party pictures", "bonfire beach party")
      repo.add_image("test_imgs/party2.jfif", "party pictures", "dance party")
      repo.add_image("test_imgs/party3.jfif", "party pictures", "small dinner get together")
      results = query(category="butterflies")
      print(results)
      self.assertEqual(len(results), 2, "only 2 butterfly images")
      repo.clear_repo()

    def test_search_full(self):
      repo.add_image("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill")
      repo.add_image("test_imgs/sunset2.jfif", "sunsets", "pink cloudy sunset")
      repo.add_image("test_imgs/sunset3.jfif", "sunsets", "sunset on the beach")
      repo.add_image("test_imgs/butterfly1.jfif", "butterflies", "butterfly on a pink flower")
      repo.add_image("test_imgs/butterfly2.jfif", "butterflies", "blue butterfly")
      repo.add_image("test_imgs/party1.jfif", "party pictures", "bonfire beach party")
      repo.add_image("test_imgs/party2.jfif", "party pictures", "dance party")
      repo.add_image("test_imgs/party3.jfif", "party pictures", "small dinner get together")
      results = query(keywords = "pink", category="butterflies")
      print(results)
      self.assertEqual(results.loc[1]["path"], "test_imgs/butterfly1.jfif", "the pink butterfly should be the closest match")
      repo.clear_repo()

    def test_search_empty(self):
      repo.add_image("test_imgs/sunset1.jfif", "sunsets", "sunset on a hill")
      repo.add_image("test_imgs/sunset2.jfif", "sunsets", "pink cloudy sunset")
      repo.add_image("test_imgs/sunset3.jfif", "sunsets", "sunset on the beach")
      repo.add_image("test_imgs/butterfly1.jfif", "butterflies", "butterfly on a pink flower")
      repo.add_image("test_imgs/butterfly2.jfif", "butterflies", "blue butterfly")
      repo.add_image("test_imgs/party1.jfif", "party pictures", "bonfire beach party")
      repo.add_image("test_imgs/party2.jfif", "party pictures", "dance party")
      repo.add_image("test_imgs/party3.jfif", "party pictures", "small dinner get together")
      results = query(keywords = "pink", category="colors")
      self.assertEqual(len(results), 0, "results should be empty")
      repo.clear_repo()







if __name__ == '__main__':
    unittest.main()