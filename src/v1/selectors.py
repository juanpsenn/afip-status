from src.v1.databases.models import Status
from src.v1.helpers.clients import get_client
from src.v1.helpers.serializers import fedummy_serializer


async def get_current_status():
    client = get_client("wsfe", False)
    dummy_response = client.service.FEDummy()
    json_response = fedummy_serializer(dummy_response)
    await Status.create(**json_response)
    return json_response
