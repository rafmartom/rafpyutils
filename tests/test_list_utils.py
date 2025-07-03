import unittest
from rafpyutils.list_utils import insert_sublist_between_markers

class TestListUnits(unittest.TestCase):
    def test_insert_sublist_between_markers(self):
        input_list = [
            "The first\n",
            "Intro\n",
            "<B=0> Toc\n",
            "- Luis Garcia\n",
            "- Pep Guardiola\n",
            "- Josko Guardiol\n",
            "<\\B>\n",
            "The first\n",
            "Outro\n",
        ]
        input_sublist = [
            "<B=0> Toc\n",
            " - Erick Cantona\n",
            " - Kike Mateo\n",
            " - Mate Bilic\n",
            " - David Barral\n",
            "<\\B>\n",
        ]
        expected = [
            "The first\n",
            "Intro\n",
            "<B=0> Toc\n",
            " - Erick Cantona\n",
            " - Kike Mateo\n",
            " - Mate Bilic\n",
            " - David Barral\n",
            "<\\B>\n",
            "The first\n",
            "Outro\n",
        ]
        result = insert_sublist_between_markers(input_list, input_sublist, r'<B=0>', r'<\\B>')
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
