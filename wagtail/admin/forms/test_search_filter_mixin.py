import unittest
from wagtail.admin.forms.choosers import SearchFilterMixin
from unittest.mock import MagicMock

class TestSearchFilterMixin(unittest.TestCase):

    def setUp(self):
        self.form = SearchFilterMixin()

    def test_filter_with_search_query_and_autocomplete(self):
        self.form.cleaned_data = {'q': 'termo de pesquisa'}
        objects = MagicMock()
        objects.model.get_autocomplete_search_fields.return_value = True

        result = self.form.filter(objects)

        self.assertTrue(result)

    def test_filter_with_search_query_and_no_autocomplete(self):
        self.form.cleaned_data = {'q': 'termo de pesquisa'}
        objects = MagicMock()
        objects.model.get_autocomplete_search_fields.return_value = False
        result = self.form.filter(objects)

        self.assertTrue(result)

    def test_filter_without_search_query_and_autocomplete(self):
        self.form.cleaned_data = {'q': ''}
        objects = MagicMock()
        objects.model.get_autocomplete_search_fields.return_value = True
        result = self.form.filter(objects)

        self.assertEqual(result, objects)

    def test_filter_without_search_query_and_no_autocomplete(self):
        self.form.cleaned_data = {'q': ''}
        objects = MagicMock()
        objects.model.get_autocomplete_search_fields.return_value = False

        result = self.form.filter(objects)

        self.assertEqual(result, objects)

if __name__ == '__main__':
    unittest.main()
