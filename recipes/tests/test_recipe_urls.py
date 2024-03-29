from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_the_url_recipe_home_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_the_url_category_is_correct(self):
        url = reverse('recipes:category', kwargs={ 'category_id' : 1})
        self.assertEqual(url, '/recipes/category/1/')
    
    def test_the_url_recipes_detail_is_correct(self):
        url = reverse('recipes:recipe', kwargs= { 'id' : 1})
        self.assertEqual(url, '/recipes/1/')