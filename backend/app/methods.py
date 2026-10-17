from litestar import Litestar, get, post, put, patch, delete


@get("/land")
async def land() -> dict[str, str]:
    return {"message": "Todo Backend is running!"}
