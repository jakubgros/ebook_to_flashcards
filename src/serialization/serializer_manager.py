class SerializerManager:
    SERIALIZER_MAP = {}

    @staticmethod
    def register_serializer(serializer, unique_type):
        if unique_type in SerializerManager.SERIALIZER_MAP:
            raise Exception(f"The '{unique_type}' serializer type is not unique")
        SerializerManager.SERIALIZER_MAP[unique_type] = serializer

    @staticmethod
    def _get_serializer(type):
        if type in SerializerManager.SERIALIZER_MAP:
            return SerializerManager.SERIALIZER_MAP[type]()
        else:
            raise TypeError(f"Can't get serializer for the '{type}' type")

    @staticmethod
    def deserialize(json_val):
        obj_type = json_val['type']

        serializer = SerializerManager._get_serializer(obj_type)
        obj = serializer.deserialize(json_val)

        return obj

    @staticmethod
    def _get_type_of_basic_type(obj):
        if isinstance(obj, str):
            return "string"
        elif isinstance(obj, list):
            return "list"
        elif isinstance(obj, dict):
            return "dictionary" #TODO dehardcode (it's used in many places, put it into single place)
        elif isinstance(obj, bool): # Important: has to be before int because bool is subclass of int and would be incorrectly handled if the order would be changed
            return "bool" #TODO dehardcode (it's used in many places, put it into single place)
        elif isinstance(obj, int):
            return "integer" #TODO dehardcode (it's used in many places, put it into single place)
        elif isinstance(obj, float):
            return "float" #TODO dehardcode (it's used in many places, put it into single place)
        elif isinstance(obj, set):
            return "set"
        else:
            raise TypeError(f'Not supported type {type(obj)}')

    @staticmethod
    def serialize(val):
        from src.serialization.serializable import Serializable

        if isinstance(val, Serializable):
            val_type = val._STATIC_TYPE
        else:
            val_type = SerializerManager._get_type_of_basic_type(val)

        serializer = SerializerManager._get_serializer(val_type)

        return serializer.serialize(val)