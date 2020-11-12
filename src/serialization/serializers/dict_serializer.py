from src.serialization.serializer_manager import SerializerManager
from src.serialization.serializers.serializer import Serializer


class DictSerializer(Serializer):
    _SUPPORTED_CLASS = dict
    _SUPPORTED_CLASS_STATIC_TYPE = "dictionary"

    def _from_json(self, json_dict):
        return {key: SerializerManager.deserialize(json_val) for (key, json_val) in json_dict.items()}

    def _to_json(self, dict_obj):
        return {key: SerializerManager.serialize(obj_val) for (key, obj_val) in dict_obj.items()}
