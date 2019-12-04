# encoding:utf-8
# author:wangzhicheng
# time:2019/11/22 16:53
# file:handle_requests.py


import requests, json
from Test_scripts.handle_phone import do_phone


class HttpRequests:
    def __init__(self):
        self.session = requests.Session()

    def add_headers(self, headers):  # 添加公共请求头
        self.session.headers.update(headers)  # session.headers.update()

    # def http_requests(self, method, url, **kwargs):  # **kwargs 关键字传参 data="" ,json=""
    #
    #     if method.lower() in ("get", "post", "put", "patch", "delete"):  # 请求方法lower()一下
    #
    #         res = self.session.request(method, url, **kwargs)
    #     else:
    #         res = None
    #         print(f"{method}_不支持此请求方式！")
    #
    #     return res

    def http_requests(self, url, method="post", data=None, is_json=True, **kwargs):
        """
        发起请求
        :param url: url地址
        :param method: 请求方法, 通常为get、post、put、delete、patch
        :param data: 传递的参数, 可以传字典、json格式的字符串、字典类型的字符串, 默认为None
        :param is_json: 是否以json的形式来传递参数, 如果为True, 则以json形式来传, 如果为False则以www-form形式来传, 默认为True
        :param kwargs: 可变参数, 可以接收关键字参数, 如headers、params、files等
        :return: None 或者 Response对象
        """
        # data可以为如下三种类型：
        # data = {"name": '可优', 'gender': True}       # 字典类型
        # data = '{"name": "可优", "gender": true}'     # json格式的字符串
        # data = "{'name': '优优', 'gender': True}"     # 字典类型的字符串

        if isinstance(data, str):  # 判断data是否为str字符串类型, 如果为str类型, 会返回True, 否则返回False
            try:
                # 假设为json字符串, 先使用json.loads转化为字典
                data = json.loads(data)

            except Exception as e:  # 如果不为json字符串会抛出异常, 然后使用eval函数来转化
                print("使用日志器来记录日志")
                data = eval(data)

        # 将传递的method请求方法统一转化为小写
        method = method.lower()
        if method == "get":  # 如果为get请求, 那么传递的data, 默认传查询字符串参数
            # res = self.one_session.get(url, params=data, **kwargs)
            res = self.session.request(method, url, params=data, **kwargs)

        elif method in ("post", "put", "delete", "patch"):  # 如果为post、put、delete、patch请求
            if is_json:  # 如果is_json为True, 那么以json格式的形式来传参
                # res = self.one_session.post(url, json=data, **kwargs)
                res = self.session.request(method, url, json=data, **kwargs)
            else:  # 如果is_json为False, 那么以www-form的形式来传参
                # res = self.one_session.post(url, data=data, **kwargs)
                res = self.session.request(method, url, data=data, **kwargs)
        else:
            res = None
            print(f"不支持{method}请求方法")
        return res

    def close(self):  # 关闭会话
        self.session.close()


if __name__ == '__main__':
    do_request = HttpRequests()

    phone = do_phone.get_no_register_phone()

    data = {"mobile_phone": phone, "pwd": "12345678"}

    headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json",
               "User-Agent": "Mozilla/5.0 KeYou"}

    do_request.add_headers(headers)
    res = do_request.http_requests(method="post", url=r"http://api.lemonban.com/futureloan/member/register", data=data)
    print(res.json())

    do_request.close()
