import unittest

from src.utilities import validate_obligatory_fields


class UtilitiesTest(unittest.TestCase):
    def test_validation_of_obligatory_fields(self):

        class ClassWithValues:
            val1 = 1
            val2 = 2

        validate_obligatory_fields(ClassWithValues, ['val1', 'val2'])


        class ClassWithoutValues:
            pass

        with self.assertRaises(AttributeError) as cm:
            validate_obligatory_fields(ClassWithoutValues, ['val1', 'val2'])
        self.assertEqual(
            "The ClassWithoutValues class has to define the following properties: val1, val2",
            str(cm.exception))


        class BaseClass:
            val = 1
        class DerivedClass(BaseClass):
            pass

        validate_obligatory_fields(BaseClass, ['val'])

        with self.assertRaises(AttributeError) as cm:
            validate_obligatory_fields(DerivedClass, ['val'])

        self.assertEqual("The DerivedClass class has to define the following properties: val", str(cm.exception))


if __name__ == '__main__':
    unittest.main()
