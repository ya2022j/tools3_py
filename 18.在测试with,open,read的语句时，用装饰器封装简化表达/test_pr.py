

import pr

import unittest
from unittest.mock import patch
from unittest import mock

# 把一连串的返回结果放到一个装饰器里面，等到需要mock的时候，直接套用即可返回想要的结果。
# 等于把with，open，read，三个操作以及连续的引用整理到一个装饰器里面的。方便复用。
from unittest.mock import patch

def mock_with_open_read(return_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with patch('builtins.open') as mock_open:
                # 使用side_effect参数模拟f.read()的行为，返回所需的结果
                mock_open.return_value.__enter__.return_value.read.side_effect = lambda: return_value
                return func(*args, **kwargs)

        return wrapper

    return decorator

# class MyContextManager:
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#
#     with patch('__main__.MyContextManager') as mock_cm:
#         # 使用side_effect参数模拟f.read()的行为，返回所需的结果
#         mock_cm.return_value.__enter__.return_value = mock_cm.return_value
#         mock_cm.return_value.__enter__.return_value.read.side_effect = lambda: 'Mocked content'
#
#         with MyContextManager() as f:
#             ret = f.read()
#
#         assert ret == 'Mocked content'
class TestClass(unittest.TestCase):

    # def test_pr(self):
    #     with patch('MyContextManager') as mock_cm:
    #         # 使用side_effect参数模拟f.read()的行为，返回所需的结果
    #         mock_cm.return_value.__enter__.return_value = mock_cm.return_value
    #         mock_cm.return_value.__enter__.return_value.read.side_effect = lambda: 'Mocked content'
    #
    #         pr.pp("asdf")
    @mock_with_open_read("asss")
    def test_pr(self):

        pr.pp("asdf")




if __name__ == "__main__":
    unittest.main()
