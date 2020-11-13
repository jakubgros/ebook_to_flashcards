from src.serialization.serializer_manager import SerializerManager
from src.utilities import validate_obligatory_fields


class Serializer:
    def __init_subclass__(cls):
        super().__init_subclass__()
        obligatory_fields = ["_SUPPORTED_CLASS", "SUPPORTED_CLASS_STATIC_TYPE", "_from_json", "_to_json"]

        validate_obligatory_fields(cls, obligatory_fields)
        SerializerManager.register_serializer(cls, cls.SUPPORTED_CLASS_STATIC_TYPE)

    def serialize(self, obj):
        if not isinstance(obj, self._SUPPORTED_CLASS):
            raise TypeError(f"Can't process the provided '{type(obj)}' type")

        return {
            "type": self.SUPPORTED_CLASS_STATIC_TYPE,
            'properties': self._to_json(obj)
        }

    def deserialize(self, json_obj):
        if json_obj['type'] != self.SUPPORTED_CLASS_STATIC_TYPE:
            raise TypeError(f"Can't process the provided '{json_obj['type']}' type")

        return self._from_json(json_obj['properties'])













