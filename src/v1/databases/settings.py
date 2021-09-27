import os
import pytz

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "mysql://{}:{}@{}:{}/{}".format(
    os.environ["MYSQL_USER"],
    os.environ["MYSQL_PASSWORD"],
    os.environ.get("MYSQL_HOST", "127.0.0.1"),
    os.environ.get("MYSQL_PORT", "3306"),
    os.environ.get("MYSQL_DB", "my_db"),
)

TZ_AR = pytz.timezone(pytz.country_timezones["ar"][0])
