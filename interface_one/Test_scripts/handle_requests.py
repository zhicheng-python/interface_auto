# encoding:utf-8
# author:wangzhicheng
# time:2019/11/29 15:16
# file:handle_requests.py

import requests, json
from Test_scripts.handle_logger import logger


class ReadRequests:
    def __init__(self):
        self.session = requests.Session()

    def addd_headers(self, headers):
        # 更新请求头
        self.session.headers.update(headers)

    def read_requests(self, url, method="post", data=None, is_json=True, **kwargs):
        """
        传入的data格式有三种： 字典，json格式，字符串字典
        1.如果传入的是字符串（json格式或者字符串字典格式）先用json.loads()转换成字典
        如果转换失败，则不是json格式数据，是字符串字典，直接用eval

        2.如果请求方式为get：
        则用params传参
        如果是在("post","patch","put","delete")中
        则

        """

        # 请求方法全部小写
        method = method.lower()

        # 如果data是一个字符串，先用json.loads()转换成字典
        # 如果转换失败，则不是json格式数据，是字符串字典，直接用eval
        if isinstance(data,str):
            try:
                data = json.loads(data)
                logger.info("传入的data数据是json格式")
            except Exception as e:
                logger.info("传入的data数据不是json格式")
                data = eval(data)

        if method == "get":
            res = self.session.request(url=url, method=method, params=data, **kwargs)

        elif method in ("post", "patch", "put", "delete"):
            if is_json:
                res = self.session.request(url=url, method=method, json=data, **kwargs)
            else:
                res = self.session.request(url=url, method=method, data=data, **kwargs)
        else:
            res = None
            print(f"没有{method}的请求方式")

        return res


    def close(self):
        self.session.close()


if __name__ == '__main__':
    url = "http://api.lemonban.com/futureloan/member/login"
    data = '{"mobile_phone":"13902854691","pwd":"000000000"}'
    headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json",
               "User-Agent": "Mozilla/5.0 KeYou"}

    # do_requests=ReadRequests()
    # do_requests.addd_headers(headers)
    # res=do_requests.read_requests(url=url,data=data)
    # print(res.json())