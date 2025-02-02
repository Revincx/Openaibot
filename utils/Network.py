# -*- coding: utf-8 -*-
# @Time    : 12/20/22 10:51 AM
# @FileName: network.py
# @Software: PyCharm
# @Github    ：sudoskys
from typing import Any

import httpx


class NetworkClient(object):
    def __init__(self, timeout: int = 30, proxy: str = "") -> None:
        proxies = None
        if proxy:
            proxies = {"all://": proxy}
        self.__client = httpx.AsyncClient(timeout=timeout, proxies=proxies)

    async def request(self,
                      method: str,
                      url: str,
                      params: dict = None,
                      data: Any = None,
                      headers: dict = None,
                      **kwargs
                      ):
        param = {
            "method": method.upper(),
            "url": url,
            "params": params,
            "data": data,
            "headers": headers,
        }
        param.update(kwargs)
        resp = await self.__client.request(**param)
        content_length = resp.headers.get("content-length")
        if content_length and int(content_length) == 0:
            raise Exception("CONTENT LENGTH 0")
        return resp
