from src.v1.databases.models import Status
from src.v1.helpers.clients import get_client
from src.v1.helpers.serializers import fedummy_serializer


async def fetch_status() -> Status:
    """Fetches current status from AFIP's servers

    Initializes a Zeep client to fetch status from AFIP's servers,
    then logs the response to the database for availability reports.
    """
    client = get_client("wsfe", False)
    response = client.service.FEDummy()
    json_response = fedummy_serializer(response)
    status = await Status.create(**json_response)
    return status
