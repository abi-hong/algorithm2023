package Chapter6;

public class Insertion {
    public static void main(String[] args) {
        int arr[] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        int swapValue = 0;
        for (int i = 1; i < arr.length; i++) {
            for (int j = i; j > 0; j--) {
                // 한칸씩 왼쪽으로 이동
                if (arr[j] < arr[j - 1]) {
                    swapValue = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = swapValue;
                } else {
                    break;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i] + " ");
        }
    }
}
