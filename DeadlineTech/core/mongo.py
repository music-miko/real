# ==========================================================
# 🎧 Public Open-Source VC Player Music Bot (Cookies Based)
# 🛠️ Maintained by Team DeadlineTech | Lead Developer: @Its_damiann
# 🔓 Licensed for Public Use — All Rights Reserved © Team DeadlineTech
# ❤️ Openly built for the community, but proudly protected by the passion of its creators.
# ==========================================================


from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Connecting to database :)")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Yukki
    LOGGER(__name__).info("MongoDB Started Successfully :)")
except:
    LOGGER(__name__).error("MongoDB connection failed!")
    exit()
