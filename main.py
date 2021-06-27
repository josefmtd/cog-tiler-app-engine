from fastapi import FastAPI
from titiler.core.factory import TilerFactory

# Create a FastAPI application
app = FastAPI(
    description="A lightweight Cloud Optimized GeoTIFF tile server",
)

# Create a set of COG endpoints
cog = TilerFactory()

# Register the COG endpoints to the application
app.include_router(cog.router, prefix='/cog', tags=["Cloud Optimized GeoTIFF"])
