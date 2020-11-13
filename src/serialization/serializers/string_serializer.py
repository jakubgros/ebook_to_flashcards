from src.serialization.serializers.serializer import Serializer


class StringSerializer(Serializer):
    _SUPPORTED_CLASS = str
    SUPPORTED_CLASS_STATIC_TYPE = "string"

    def _from_json(self, json_str):
        return json_str

    def _to_json(self, str_obj):
        return str_obj