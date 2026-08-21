from fastapi import FastAPI

from src.core.config import settings
from src.auth import router as auth
from src.organizers import router as organizers
from src.venues import router as venues
from src.categories import router as categories
from src.events import router as events

# Barcha SQLAlchemy modellari mapper konfiguratsiyasidan oldin import qilinishi kerak,
# aks holda `relationship()` ichidagi satr(string) sifatidagi class nomlari topilmaydi.
from src.users import models as user_models  # noqa: F401
from src.organizers import models as organizer_models  # noqa: F401
from src.venues import models as venue_models  # noqa: F401
from src.categories import models as category_models  # noqa: F401
from src.events import models as event_models  # noqa: F401

app = FastAPI(title=settings.PROJECT_NAME)

# Keyingi fazalarda domain router'lari shu yerga ulanadi ([[09-project-structure.md]] §4):
# api = settings.API_V1_PREFIX
app.include_router(auth.router, prefix=f"{settings.API_V1_PREFIX}/auth", tags=["auth"])
app.include_router(events.router, prefix=f"{settings.API_V1_PREFIX}/events", tags=["events"])
# app.include_router(orders.router, prefix=f"{api}/orders", tags=["orders"])
# app.include_router(payments.router, prefix=f"{api}/payments", tags=["payments"])
# app.include_router(checkin.router, prefix=f"{api}/checkin", tags=["checkin"])
app.include_router(
    organizers.router, prefix=f"{settings.API_V1_PREFIX}/organizers", tags=["organizers"]
)
app.include_router(venues.router, prefix=f"{settings.API_V1_PREFIX}/venues", tags=["venues"])
app.include_router(
    categories.router, prefix=f"{settings.API_V1_PREFIX}/categories", tags=["categories"]
)
# app.include_router(admin.router, prefix=f"{api}/admin", tags=["admin"])


@app.get("/", tags=["root"])
async def root() -> dict[str, str]:
    return {"message": f"{settings.PROJECT_NAME} ishga tushdi"}
