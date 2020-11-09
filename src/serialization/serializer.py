
from src.serialization.serializer_manager import SerializerManager

class Serializer:

    # FIELDS TO OVERLOAD START
    _SUPPORTED_CLASS = None
    _SUPPORTED_CLASS_STATIC_TYPE = None

    def _from_json(self, json_obj):
        raise NotImplemented

    def _to_json(self, obj):
        raise NotImplemented

    #FIELDS TO OVERLOAD END

    @staticmethod
    def _validate_obligatory_fields(cls):

        obligatory_fields = ["_SUPPORTED_CLASS", "_SUPPORTED_CLASS_STATIC_TYPE"]
        for field in obligatory_fields:
            if not hasattr(cls, field):
                raise AttributeError(f"Serializable class has to define {field} property")

    def __init_subclass__(cls):
        super().__init_subclass__()

        Serializer._validate_obligatory_fields(cls)
        SerializerManager.register_serializer(cls, cls._SUPPORTED_CLASS_STATIC_TYPE)


    def serialize(self, obj):
        if not isinstance(obj, self._SUPPORTED_CLASS):
            raise TypeError(f"Can't process the provided '{type(obj)}' type")

        return {
            "type": self._SUPPORTED_CLASS_STATIC_TYPE,
            'properties': self._to_json(obj)
        }


    def deserialize(self, json_obj):
        if json_obj['type'] != self._SUPPORTED_CLASS_STATIC_TYPE:
            raise TypeError(f"Can't process the provided '{json_obj['type']}' type")

        return self._from_json(json_obj['properties'])


class StringSerializer(Serializer):
    _SUPPORTED_CLASS = str
    _SUPPORTED_CLASS_STATIC_TYPE = "string"

    def _from_json(self, json_str):
        return json_str

    def _to_json(self, str_obj):
        return str_obj


class ListSerializer(Serializer):
    _SUPPORTED_CLASS = list
    _SUPPORTED_CLASS_STATIC_TYPE = "list"

    def _from_json(self, json_list):
        return [SerializerManager.deserialize(elem) for elem in json_list]

    def _to_json(self, list_obj):
        return [SerializerManager.serialize(elem) for elem in list_obj]


class DictSerializer(Serializer):
    _SUPPORTED_CLASS = dict
    _SUPPORTED_CLASS_STATIC_TYPE = "dictionary"

    def _from_json(self, json_dict):
        return {key: SerializerManager.deserialize(json_val) for (key, json_val) in json_dict.items()}

    def _to_json(self, dict_obj):
        return {key: SerializerManager.serialize(obj_val) for (key, obj_val) in dict_obj.items()}

class IntSerializer(Serializer):
    _SUPPORTED_CLASS = int
    _SUPPORTED_CLASS_STATIC_TYPE = "integer"

    def _from_json(self, json_val):
        return json_val

    def _to_json(self, int_val):
        return int_val

class BoolSerializer(Serializer):
    _SUPPORTED_CLASS = bool
    _SUPPORTED_CLASS_STATIC_TYPE = "bool"

    def _from_json(self, json_val):
        return json_val

    def _to_json(self, int_val):
        return int_val

