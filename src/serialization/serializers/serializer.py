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













