#include <iostream>

// CODE
// 함수나 클래스를 정의하게 되면 -> 컴파일러를 거쳐서 -> 인스트럭션이 되고
// 프로세스가 실행되면서 인스트럭션은 -> CODE segment로 간다.
int add(int a, int b){
    return a + b;
}

int subtract(int a, int b){
    return a - b;
}

// DATA
// 전역변수나 cpp의 static 지역변수는 DATA segment로 올리온다.
int global_x = 10;

int main(void) {
    // STACK
    // 지역변수는 STACK segment로 올라온다.
    // 특징으로는 순차적으로 쌓이지만 그 한계가 존재한다.
    // 최대치를 할당시키지 않으면 1MB가 부여된다.(최대치가 존재)
    // 할당을 해제하지않아도 자동적으로 해제된다.
    // 최대치를 넘어가면 stack over flow가 발생된다.
    int local_x = 20;

    // HEAP
    // 직접 메모리 공간에 할당을 해줘야한다.(최대치가 없다.)
    // 직접 메모리를 해제시켜줘야한다.

    // 힙의 장점 : 할당과 해제 시점은 프로그래머가 정할 수 있다. 해제시키지 않으면 언제 어디서든 접근이 가능하다.
    // 힙의 단점 :
    // 들어갈 메모리 공간을 탐색해야되서, 스택보다 월등히 느리다.(힙을 사용하는 이유가 명확하지않으면 스택권장)
    // 할당과 해제가 잦아서 메모리의 빈공간이 잘게 나누어짐. 관련 데이터가 한데모이지 못하고 분산됨(단편화) -> 지역성이 적용안됨 -> 캐시미스 확률 상승
    // page fault(페이지 폴트)도 마찬가지
    // 메모리 누수의 위험 존재
    int * heap_x = (int*)malloc(sizeof(int));
    *heap_x = 30;
    frea(heap_x);

    return 0;
}