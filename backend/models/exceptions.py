from fastapi import HTTPException
from fastapi.responses import JSONResponse

async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

def register_exceptions(app):
    app.add_exception_handler(HTTPException, http_exception_handler)
