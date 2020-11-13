from src.serialization.serializers.serializer import Serializer


class FloatSerializer(Serializer):
    _SUPPORTED_CLASS = float
    SUPPORTED_CLASS_STATIC_TYPE = "float"

    def _from_json(self, json_val):
        return json_val

    def _to_json(self, float_val):
        return float_val
