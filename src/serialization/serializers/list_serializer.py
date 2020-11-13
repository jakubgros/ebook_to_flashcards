from src.serialization.serializer_manager import SerializerManager
from src.serialization.serializers.serializer import Serializer


class ListSerializer(Serializer):
    _SUPPORTED_CLASS = list
    SUPPORTED_CLASS_STATIC_TYPE = "list"

    def _from_json(self, json_list):
        return [SerializerManager.deserialize(elem) for elem in json_list]

    def _to_json(self, list_obj):
        return [SerializerManager.serialize(elem) for elem in list_obj]
