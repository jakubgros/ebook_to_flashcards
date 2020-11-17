import unittest

from src.word import Word


class TestWord(unittest.TestCase):
    def test_construction(self):

        word = Word("word")

        self.assertEqual(word.stored_word, "word")
        self.assertEqual(word.occurrences, 0)
        self.assertEqual(word.is_known, False) # TODO jagros probably it should be None
        self.assertEqual(word.is_checked, False)

    def test_construction_with_incorrect_word_passed(self):
        with self.assertRaises(ValueError):
            Word("not a single word")

    def test_marking_as_known_or_not(self):
        word = Word("word")

        self.assertFalse(word.is_known) #TODO jagros it should be probably None
        self.assertFalse(word.is_checked)

        for known in [True, False]:
            word.mark_if_known(known)
            self.assertTrue(word.is_checked)
            self.assertEqual(word.is_known, known)


    def test_adding_occurrences(self):
        word = Word("word")

        self.assertEqual(word.occurrences, 0)
        word.add_occurrence()
        self.assertEqual(word.occurrences, 1)
        word.add_occurrence()
        self.assertEqual(word.occurrences, 2)


if __name__ == '__main__':
    unittest.main()
