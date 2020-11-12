from src.serialization.serializer_manager import SerializerManager
from src.serialization.serializers.serializer import Serializer


class SetSerializer(Serializer):
    _SUPPORTED_CLASS = set
    _SUPPORTED_CLASS_STATIC_TYPE = "set"

    def _from_json(self, json_set):
        return set(SerializerManager.deserialize(elem) for elem in json_set)

    def _to_json(self, set_obj):
        return list(SerializerManager.serialize(elem) for elem in set_obj)