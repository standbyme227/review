# 프로젝트를 하려느데 기본 개념조차 아직 완전 이해는 되지 않은거 같아서
# 조금이라도 반복학습의 힘을 빌리고자 복습한다.

# 전역변수를 선언한다.
# 전역변수란 말그대로 전체의 범위내에서 사용가능한 변수.
# global한 변수라고 생각하면된다.
g_var = 10


#
# # 그래서 이렇게 함수를 선언하고
# # 그 안에서 호출하면 바로 사용할 수 있다.
# def func():
#     print("g_var = {}".format(g_var))


# def func():
#     # 이건 지역변수를 선언한거다.
#     # 전역 변수를 덮어씌운게 아니냐라고 할 수 있겠지만
#     # 이건 현재 전역변수와 이름만 같을 뿐 전혀 다른 존재이다
#     # 동명이인 정도 되려나??/
#     # 거기다가 살수있는 범위는 함수 내부적로 한정되어있어서
#     # 로직이 다 돈다음에는 사라진다.
#     g_var = 20
#     # 함수 안의 변수가 어떻게 적용되는지 나온다.
#     print("g_var = {} in function".format(g_var))
#
#
#
def func():
    # 전역변수에 접근하기위해서 global을 사용했다.
    global g_var
    g_var = 20


if __name__ == "__main__":
    # 이건 전역변수가 선언되었을때 print와
    print("g_var : {} before".format(g_var))
    func()
    # # 이건 과연 g_var의 값이 바뀌었는지를 확인하기 위한 작업같다.
    # print("g_var : {} in main".format(g_var))

    # global로 접근해서 수정했을때 어떻게 다르게 나오는지를 확인하기 위한 작업이다.
    print("g_var: {} after".format(g_var))

# a는 지역변수이다.
# b도 지역변수이다.
# 하지만 a와 b의 지역은 다르다.
# 일단 생각으로는 inner에서 a에 접근은 쉽지만
# outer에서 b는 당연히 접근을 못할 것이다.
c = 10

def outer():
    a = 10
    print(a)

    def inner():
        b = 20
        print(a)
        print(b)

    inner()

if __name__ == "__main__":
    outer()
