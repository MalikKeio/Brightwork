#!/usr/bin/env python3

#### 冗談 ####
from __future__ import braces
import antigravity
##### 完 ####

class Date:
    # static変数の作り方：
    USE_COUNT = 0
    DELIMITER = "/"
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day
        Date.USE_COUNT += 1
    # static関数の作り方：
    def reset_counter():
        Date.USE_COUNT = 0
    reset_counter = staticmethod(reset_counter)
    def set_delimiter(new_delimiter):
        Date.DELIMITER = new_delimiter
    set_delimiter = staticmethod(set_delimiter)
    def parse(date_string, delimiter=None):
        # delimiterが未記入の場合、デフォルトのdelimiterを使用
        if delimiter is None:
            delimiter = Date.DELIMITER
        date_ints = [int(x) for x in date_string.split(delimiter)]
        return Date(date_ints[0], date_ints[1], date_ints[2])
    parse = staticmethod(parse)

    def __str__(self):
        return Date.DELIMITER.join([str(x) for x in [self.year, self.month, self.day] ])

print(Date.USE_COUNT)
d1 = Date(2012, 1, 1)
print(Date.USE_COUNT, d1)
d2 = Date(2013, 2, 4)
Date.DELIMITER = "--"
print(Date.USE_COUNT, d2)
Date.DELIMITER = "."
print(Date.USE_COUNT, d2)
print(Date.parse("2015-03-4", "-"))


# 関数実行の前後にコードを走らせたい場合：
def is_allowed(myfunc):
    def inner_func(user):
        if user == "admin": #ユーザチェック、権限チャック、パスワードチャックみたいな作業を行う。
            return myfunc(user)
        else:
            print("%s is not allowed!" % user)
            return "却下！"
    return inner_func

@is_allowed
def get_secret(user):
    print("%s will get the secret!" % user)
    return "supersecret!"

print("SECRET: %s" % get_secret("malik"))
print("SECRET: %s" % get_secret("admin"))



# 無論、これでも行ける：
def get_secret(user):
    if user == "admin":
        print("%s will get the secret!" % user)
        return "supersecret!"
    else:
        print("%s is not allowed!" % user)
        return "却下！"
# だが、get_secretみたいな関数が滅多に多いとき、decoratorは便利になる。

# ちなみにDecoratorを使うと、上記のDateクラスがもっと短くて、わかりやすくなる！
class Date:
    # static変数の作り方：
    USE_COUNT = 0
    DELIMITER = "/"
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day
        Date.USE_COUNT += 1
    # static関数の作り方：
    @staticmethod
    def reset_counter():
        Date.USE_COUNT = 0
    @staticmethod
    def set_delimiter(new_delimiter):
        Date.DELIMITER = new_delimiter


# splitとjoinを使用する例：URL parse実装
url = "http://example.com/over/there?name=ferret&field1=value1&field2=value2&field3=value3"
page_url, query = url.split("?")
print(page_url, query)
contents = query.split("&")
print(contents)
parsedQuery = {}
for keyValuePair in contents:
    key, value = keyValuePair.split("=")
    parsedQuery[key] = value
print(parsedQuery)
