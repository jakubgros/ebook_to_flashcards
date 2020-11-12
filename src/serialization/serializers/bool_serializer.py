from src.serialization.serializers.serializer import Serializer


class BoolSerializer(Serializer):
    _SUPPORTED_CLASS = bool
    _SUPPORTED_CLASS_STATIC_TYPE = "bool"

    def _from_json(self, json_val):
        return json_val

    def _to_json(self, int_val):
        return int_val
