from fastapi import FastAPI
from routers import index
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="UNICEF Test API",
    description="A UNICEF Test API",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Joel KUMWENDA",
        "url": "https://github.com/jkumwenda",
        "email": "jkumwenda@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="0.0.0.0",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index.router, tags=["Welcome"], prefix="/api/welcome")
