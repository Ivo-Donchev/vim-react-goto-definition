from unittest import TestCase
from src.utils import get_imports_from_file_content


class GetImportsFromFileContentTests(TestCase):
    def setUp(self):
        self.util = get_imports_from_file_content

    def test_simple_import(self):
        file_content = """
        import a1 from 'b1';

        import a2 from 'b2';
        import
            a3
            from
            'b3';
        """
        result = self.util(file_content)
        expected_result = [
            {
                'imports': [{'imported_as': 'a1', 'used_as': 'a1', 'default': True}],
                'source': 'b1'
            },
            {
                'imports': [{'imported_as': 'a2', 'used_as': 'a2', 'default': True}],
                'source': 'b2'
            },
            {
                'imports': [
                    {'imported_as': 'a3', 'used_as': 'a3', 'default': True},
                ],
                'source': 'b3'
            },
        ]
        self.assertEqual(expected_result, result)

    def test_import_with_brackets(self):
        file_content = """
        import a1 from 'b1';

        import { a2 } from 'b2';
        import {a31, a32 as a33, default as a34} from 'b3';
        """
        result = self.util(file_content)
        expected_result = [
            {
                'imports': [{'imported_as': 'a1', 'used_as': 'a1', 'default': True}],
                'source': 'b1'
            },
            {
                'imports': [{'imported_as': 'a2', 'used_as': 'a2', 'default': False}],
                'source': 'b2'
            },
            {
                'imports': [
                    {'imported_as': 'a31', 'used_as': 'a31', 'default': False},
                    {'imported_as': 'a32', 'used_as': 'a33', 'default': False},
                    {'imported_as': 'default', 'used_as': 'a34', 'default': True}
                ],
                'source': 'b3'
            },
        ]
        self.assertEqual(expected_result, result)
