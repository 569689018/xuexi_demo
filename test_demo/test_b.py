import pytest



def test_1(login):
    print("测试用例1111")
    assert 1==2


def test_2(login):
    print("测试用例22222")
    assert 1==2


@pytest.mark.repeat(3)
def test_3(login):
    print("测试用例3333")

# pytest test_b.py --count=3 -s 重复执行3次 -s控制台打印出来内容
# pytest test_b.py::test_2 --count=3 -s 重复执行test_b下得节点test_2