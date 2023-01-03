public class Hanoi {
    // no개의 원반을 x번 기둥에서 y번 기둥으로 옮김
    static void move(int no, int x, int y) {
        if (no > 1)
            move(no-1, x, 6-x-y);
        
        System.out.println("원반[%d]을 %d번 기둥에서 %d번 기둥으로 옮김\n", no, x, y)

        if (no > 1)
            move(no-1, 6-x-y, y);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("하노이의 탑");
        System.out.println("원반의 개수: ");
        
        int n = sc.nextInt();

        move(n, 1, 3);
    } 
}
