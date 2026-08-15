from fastapi import FastAPI

from src.core.config import settings
from src.auth import router as auth

app = FastAPI(title=settings.PROJECT_NAME)

# Keyingi fazalarda domain router'lari shu yerga ulanadi ([[09-project-structure.md]] §4):
# api = settings.API_V1_PREFIX
app.include_router(auth.router, prefix=f"{settings.API_V1_PREFIX}/auth", tags=["auth"])
# app.include_router(events.router, prefix=f"{api}/events", tags=["events"])
# app.include_router(orders.router, prefix=f"{api}/orders", tags=["orders"])
# app.include_router(payments.router, prefix=f"{api}/payments", tags=["payments"])
# app.include_router(checkin.router, prefix=f"{api}/checkin", tags=["checkin"])
# app.include_router(organizers.router, prefix=f"{api}/organizers", tags=["organizers"])
# app.include_router(admin.router, prefix=f"{api}/admin", tags=["admin"])


@app.get("/", tags=["root"])
async def root() -> dict[str, str]:
    return {"message": f"{settings.PROJECT_NAME} ishga tushdi"}
