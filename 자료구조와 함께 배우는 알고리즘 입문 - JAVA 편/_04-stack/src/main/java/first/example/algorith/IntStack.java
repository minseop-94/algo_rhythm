package first.example.algorith;

public class IntStack {

    private int[] stk; // 스택용 배열
    private int capacity; // 스택 용량
    private int ptr; // 스택 포인터

    // 실행 시 예외 : 스택이 비어 있음
    public class EmptyIntStackExcetption extends RuntimeException {
        public EmptyIntStackExcetption() {}
    }

    // 실행 시 예외 : 스택이 가득 참
    public class OverflowIntStackException extends RuntimeException {
        public OverflowIntStackException() {}
    }

    // 생성자
    public IntStack(int maxlen){
        ptr = 0;
        capacity = maxlen;
        try {
            stk = new int[capacity];
        } catch (OutOfMemoryError e) {
            capacity = 0;
        }
    }

    // stack에 x를 push
    public int push(int x) throws OverflowIntStackException {
        if (ptr >= capacity) // stack이 가득 참
            throw new OverflowIntStackException();
        return stk[ptr++] = x;
    }

    // stack에서 데이터를 pop(꼭대기에 있는 데이터를 꺼냄)
    public int pop() throws EmptyIntStackExcetption {
        if (ptr <= 0)
            throw new EmptyIntStackExcetption();
        return stk[--ptr];
    }

    // stack에서 data를 peek(꼭대기에 있는 데이터를 들여다 봄)
    public int peek() throws EmptyIntStackExcetption {
        if (ptr <= 0)
            throw new EmptyIntStackExcetption();
        return stk[ptr - 1];
    }

    // stack을 비움
    public void clear() {
        ptr = 0;
    }

    // 스택에서 x를 찾아 index(없으먄 -1) 을 반환
    public int indexOf(int x) {
        for (int i = ptr - 1; i >=0 ; i--) // 꼭대기 쪽부터 선형 검색
            if (stk[i] == x)
                return i ; // 검색 서공
            return -1;
    }

    // stack의 용량을 반환
    public int getCapacity() {
        return capacity;
    }

    // 스택에 쌓여 있는 데이터 개수를 반환
    public int size(){
        return ptr;
    }

    // 스택이 비어 있는가?
    public boolean isEmpty(){
        return ptr <= 0;
    }

    // 스택이 가득 찼는가?
    public boolean isFull() {
        return ptr >= capacity;
    }

    // 스택 안의 모든 데이터를 바닥 -> 꼭대기 순서로 출력
    public void dump() {
        if (ptr <= 0)
            System.out.println("스택이 비어 있습니다");
        else {
            for (int i = 0; i < ptr; i++)
                System.out.println(stk[i] + " ");
            System.out.println();
        }
    }
}
