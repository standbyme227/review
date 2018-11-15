# a = 1
#
# # b, c는 글로벌이 아니다
# # inner에서 a를 접근하려면 global을 선언하면 되는 걸로 알고있다.
# # 그렇다면 b와 c는 어떻게 접근할 것인가????
# def outer():
#     b = 2
#     c = 3
#     print(a, b, c)
#
#     def inner():
#         d = 4
#         e = 5
#         print(a, b, c, d, e)
#
#     inner()
#
# if __name__ == "__main__":
#     outer()


# nonlocal 키워드

def outer():
    a = 2
    b = 3

    def inner():
        nonlocal a
        a = 100

    inner()

    print(
        "locals in outer : a = {}, b = {}".format(a, b)
    )


if __name__ == "__main__":
    outer()
