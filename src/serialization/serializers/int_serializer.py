from src.serialization.serializers.serializer import Serializer


class IntSerializer(Serializer):
    _SUPPORTED_CLASS = int
    SUPPORTED_CLASS_STATIC_TYPE = "integer"

    def _from_json(self, json_val):
        return json_val

    def _to_json(self, int_val):
        return int_val
