import asyncio
import modules
from setup import run, dp


dp.include_router(modules.router)


if __name__ == "__main__":
    asyncio.run(run())
