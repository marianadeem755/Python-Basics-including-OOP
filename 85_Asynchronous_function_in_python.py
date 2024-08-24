import time
import asyncio
import requests
async def func1():
  URL = "https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram.ico", "wb").write(response.content)
  print("func1")
  return "Maria Nadeem"
async def func2():
  URL = "https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram1.ico", "wb").write(response.content)
  print("func2")
async def func3():
  URL = "https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram2.ico", "wb").write(response.content)
  print("func3")
async def main():
    L=await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    print(L)
#   task=asyncio.create_task(func3())
#   await func1()
#   await func2()
#   await func3()
asyncio.run(main())

