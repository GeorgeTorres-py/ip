import asyncio

async def getaddrinfo(host, port):
    loop = asyncio.get_event_loop()
    return (await loop.getaddrinfo(host, port))

addrs = asyncio.run(getaddrinfo('google.com', 443))
for a in addrs:
    family, typ,proto, name, sockaddr = a
    print(sockaddr)
