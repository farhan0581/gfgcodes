import asyncio
import time

async def slow():
    await time.sleep(5)

async def test():
    print('start')
    # time.sleep(5)
    await slow()
    print('end')

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        test(),
        test(),
    )
)
loop.close()


# async def main():
#     t1 = asyncio.create_task(test())
#     t2 = asyncio.create_task(test())

#     await t1
#     await t2

# asyncio.run(main())