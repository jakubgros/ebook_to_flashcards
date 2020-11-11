import unittest

from src.iterator import Iterator


class IteratorTest(unittest.TestCase):

    def test_iteration_over_empty_container(self):
        empty_container = []
        it = Iterator(empty_container)

        with self.assertRaises(Exception):
            it.get()

        self.assertFalse(it.next())
        self.assertFalse(it.previous())

    def test_iterator_is_set_to_first_element_on_initialization(self):
        container = [5, 6, 7]
        it = Iterator(container)

        expected_idx = 0
        expected_elem = container[expected_idx]
        self.assertEqual((expected_idx, expected_elem), it.get())

    def test_normal_iteration(self):
        container = [10, 5, 15]
        it = Iterator(container)

        expected_values = [
            (0, 10),
            (1, 5),
            (2, 15),
        ]

        for expected in expected_values:
            self.assertEqual(expected, it.get())
            it.next()

        # now it points to the last element. Test going backward
        for expected in expected_values[::-1]:
            self.assertEqual(expected, it.get())
            it.previous()

    def test_boundaries_check_mechanism(self):
        container = [10, 5, 15]

        it = Iterator(container)  # it -> container[0]
        self.assertEqual(it.previous(), False)  # it -> container[0]
        self.assertEqual(it.next(), True)  # it -> container[1]
        self.assertEqual(it.previous(), True)  # it -> container[0]
        self.assertEqual(it.next(), True)  # it -> container[1]
        self.assertEqual(it.next(), True)  # it -> container[2]
        self.assertEqual(it.next(), False)  # it -> container[2]
        self.assertEqual(it.previous(), True)  # it -> container[1]

    def test_iteration_with_matching_predicate(self):
        container = [
            (10, False),
            (55, False),
            (11, True),
            (43, False),
            (41, True),
            (41, False),
        ]

        def predicate(elem):
            return elem[1] is True

        it = Iterator(container)

        expected_values = [
            (2, (11, True)),
            (4, (41, True)),
        ]

        for exp_idx, exp_elem in expected_values:
            self.assertTrue(it.next(predicate))
            idx, elem = it.get()
            self.assertEqual(exp_idx, idx)
            self.assertEqual(exp_elem, elem)

        # move iterator to the end
        while it.next():
            pass

        for exp_idx, exp_elem in expected_values[::-1]:
            self.assertTrue(it.previous(predicate))
            idx, elem = it.get()
            self.assertEqual(exp_idx, idx)
            self.assertEqual(exp_elem, elem)

    def test_iteration_with_not_matching_predicate(self):
        container = [
            (10, False),
            (55, False),
            (11, False),
            (43, False),
            (41, False),
            (41, False),
        ]

        def predicate(elem):
            return elem[1] is True

        it = Iterator(container)

        pre = it.get()
        self.assertFalse(it.next(predicate))
        post = it.get()
        self.assertEqual(pre, post)

if __name__ == '__main__':
    unittest.main()
