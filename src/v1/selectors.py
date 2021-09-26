from src.v1.helpers.clients import get_client
from src.v1.helpers.serializers import fedummy_serializer


def get_current_status():
    client = get_client("wsfe", False)
    dummy_response = client.service.FEDummy()
    return fedummy_serializer(dummy_response)
