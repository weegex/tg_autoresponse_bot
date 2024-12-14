import asyncio
import modules
from setup import run, dp
from modules import autoresponse, config
from utils import middlewares


# Routers
dp.include_routers(
    config.router
)


# Middlewares for non-working days
dp.business_message.middleware(middlewares.NoAdminMiddleware())
dp.business_message.middleware(middlewares.BusinessMiddleware())
dp.callback_query.middleware(middlewares.BusinessMiddleware())


# Routers for non-working days
dp.include_routers(
    autoresponse.router
)


# Entry point
if __name__ == "__main__":
    asyncio.run(run())
