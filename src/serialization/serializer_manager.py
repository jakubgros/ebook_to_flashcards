class SerializerManager:
    _SERIALIZER_MAP = {}

    @staticmethod
    def serialize(val):
        from src.serialization.serializable import Serializable

        if isinstance(val, Serializable):
            val_type = val._STATIC_TYPE
        else:
            val_type = SerializerManager._get_type_of_basic_type(val)

        serializer = SerializerManager._get_serializer(val_type)
        return serializer.serialize(val)

    @staticmethod
    def deserialize(json_val):
        obj_type = json_val['type']
        serializer = SerializerManager._get_serializer(obj_type)
        obj = serializer.deserialize(json_val)
        return obj

    @staticmethod
    def register_serializer(serializer, unique_type):
        if unique_type in SerializerManager._SERIALIZER_MAP:
            raise Exception(f"The '{unique_type}' serializer type is not unique")
        SerializerManager._SERIALIZER_MAP[unique_type] = serializer

    @staticmethod
    def _get_serializer(object_type):
        if object_type in SerializerManager._SERIALIZER_MAP:
            return SerializerManager._SERIALIZER_MAP[object_type]()
        else:
            raise TypeError(f"Can't get serializer for the '{object_type}' type")

    @staticmethod
    def _get_type_of_basic_type(obj):
        from src.serialization.serializers.string_serializer import StringSerializer
        from src.serialization.serializers.list_serializer import ListSerializer
        from src.serialization.serializers.bool_serializer import BoolSerializer
        from src.serialization.serializers.int_serializer import IntSerializer
        from src.serialization.serializers.dict_serializer import DictSerializer
        from src.serialization.serializers.set_serializer import SetSerializer
        from src.serialization.serializers.float_serializer import FloatSerializer

        if isinstance(obj, str):
            return StringSerializer.SUPPORTED_CLASS_STATIC_TYPE
        elif isinstance(obj, list):
            return ListSerializer.SUPPORTED_CLASS_STATIC_TYPE
        elif isinstance(obj, dict):
            return DictSerializer.SUPPORTED_CLASS_STATIC_TYPE
        elif isinstance(obj, bool): # Important: has to be before int because bool is subclass of int and would be incorrectly handled if the order would be changed
            return BoolSerializer.SUPPORTED_CLASS_STATIC_TYPE
        elif isinstance(obj, int):
            return IntSerializer.SUPPORTED_CLASS_STATIC_TYPE
        elif isinstance(obj, float):
            return FloatSerializer.SUPPORTED_CLASS_STATIC_TYPE
        elif isinstance(obj, set):
            return SetSerializer.SUPPORTED_CLASS_STATIC_TYPE
        else:
            raise TypeError(f'Not supported type {type(obj)}')
