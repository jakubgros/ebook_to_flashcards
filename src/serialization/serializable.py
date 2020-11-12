from src.serialization.serializers.serializer import Serializer
from src.serialization.serializer_manager import SerializerManager

class Serializable:
    def __init_subclass__(cls):
        super().__init_subclass__()

        obligatory_fields = ["_STATIC_TYPE", "_PROPERTIES_TO_SERIALIZE"]
        for field in obligatory_fields:
            if not hasattr(cls, field):
                raise AttributeError(f"The {cls} Serializable class has to define {field} property")

        class SerializableSerializer(Serializer):
            _SUPPORTED_CLASS = cls
            _SUPPORTED_CLASS_STATIC_TYPE = cls._STATIC_TYPE

            def _to_json(self, obj):
                return obj.to_json()

            def _from_json(self, json_obj):
                return self._SUPPORTED_CLASS.from_json(json_obj)

    @classmethod
    def from_json(cls, json):
        obj = cls()                                     #TODO change to serialize everything by default and add list of fields that shouldn't be serialized, because now it's easy to forget to add the new field to the list
        for field_name in cls._PROPERTIES_TO_SERIALIZE: #TODO jagros add support for deserialization default values for new fields added after the object was serialized
            json_val = json[field_name]
            val = SerializerManager.deserialize(json_val)
            setattr(obj, field_name, val)
        return obj

    def to_json(self):
        as_dict = {}
        for field_name in self._PROPERTIES_TO_SERIALIZE:
            val = getattr(self, field_name)
            json_val = SerializerManager.serialize(val)

            as_dict[field_name] = json_val

        return as_dict



