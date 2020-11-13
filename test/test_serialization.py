import unittest

from src.serialization.serializable import Serializable
from src.serialization.serializer_manager import SerializerManager


class SerializationTest(unittest.TestCase):
    def test_validation_of_obligatory_fields(self):

        with self.assertRaises(AttributeError) as cm:
            class MySerializableClass(Serializable):
                pass

        self.assertEqual(str(cm.exception),
                         "The MySerializableClass class has to define the following properties: _STATIC_TYPE, _PROPERTIES_TO_SERIALIZE")

        with self.assertRaises(AttributeError) as cm:
            class MySerializableClass(Serializable):
                _PROPERTIES_TO_SERIALIZE = ""

        self.assertEqual(str(cm.exception),
                         "The MySerializableClass class has to define the following properties: _STATIC_TYPE")

    def test_class_is_auto_registered_to_serializer_manager_by_inheritance(self):
        static_type = "SerializableClass"

        class SerializableClass(Serializable):
            _STATIC_TYPE = static_type
            _PROPERTIES_TO_SERIALIZE = []

        serializableObj = SerializableClass()
        SerializerManager.serialize(serializableObj)

        class NotSerializableClass:
            pass

        notSerializableObj = NotSerializableClass()

        with self.assertRaises(TypeError) as cm:
            SerializerManager.serialize(notSerializableObj)

        self.assertEqual(f"Not supported type {type(notSerializableObj)}", str(cm.exception))

    def test_serialization(self):

        class OtherSerializableClass(Serializable):
            _STATIC_TYPE = "OtherSerializableClass"
            _PROPERTIES_TO_SERIALIZE = ["a"]

            def initialize(self, a):
                self.a = a
                return self

            def __eq__(self, other):
                return self.a == other.a

        class MySerializableClass(Serializable):
            _STATIC_TYPE = "MySerializableClass"
            _PROPERTIES_TO_SERIALIZE = ["int_val", "int_val_for_composed_class", "float_val", "a_dict", "a_list", "a_set"]

            def initialize(self, int_val, int_val_for_composed_class, float_val, a_dict, a_list, a_set):
                self.int_val = int_val
                self.int_val_for_composed_class = OtherSerializableClass().initialize(int_val_for_composed_class)
                self.float_val = float_val
                self.a_dict = a_dict
                self.a_list = a_list
                self.a_set = a_set
                return self

            def __eq__(self, other):
                return self.int_val == other.int_val \
                       and self.int_val_for_composed_class == other.int_val_for_composed_class \
                       and self.float_val == other.float_val \
                       and self.a_dict == other.a_dict \
                       and self.a_list == other.a_list \
                       and self.a_set == other.a_set

        obj = MySerializableClass().initialize(1, 2, 3.5, {"key1": 1, "key2": 2}, [1, 2, 3, 4], {1, 2, 3})

        serialized = SerializerManager.serialize(obj)
        deserialized = SerializerManager.deserialize(serialized)
        self.assertEqual(obj, deserialized)

if __name__ == '__main__':
    unittest.main()
