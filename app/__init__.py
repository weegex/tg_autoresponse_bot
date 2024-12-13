import asyncio
from setup import run, dp
from . import modules


dp.include_router(modules.router)


if __name__ == "__main__":
    asyncio.run(run())
