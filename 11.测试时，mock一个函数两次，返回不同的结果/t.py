

# 相当于mock函数时，使用patch只带入一次，但是同时把两次不同的结果放在装饰器上面。
# https://stackoverflow.com/questions/24897145/python-mock-multiple-return-values
from unittest.mock import patch
from sample import hello_world

@patch('sample.hello_world', side_effect=[{'a': 1, 'b': 2}, {'a': 4, 'b': 5}])
def test_first_test(self, hello_world_patched):
    assert hello_world() == {'a': 1, 'b': 2}
    assert hello_world() == {'a': 4, 'b': 5}
    assert hello_world_patched.call_count == 2
