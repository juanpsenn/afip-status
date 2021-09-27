def fedummy_serializer(response):
    return {
        "app": response.AppServer,
        "db": response.DbServer,
        "auth": response.AuthServer,
    }
