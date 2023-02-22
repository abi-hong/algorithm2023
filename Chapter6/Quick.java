package Chapter6;

public class Quick {

    public static void quicksort(int[] arr, int start, int end) {
        // 재귀함수 종료조건 : 배열의 원소개수가 1개일 때
        if (start >= end) return;

        int pivot = start;
        int left = start + 1;
        int right = end;
        while (left <= right) {
            while (left <= end && arr[left] <= arr[pivot]) left++;
            while (right > start && arr[right] >= arr[pivot]) right--;

            if (left > right) {
                int temp = arr[pivot];
                arr[pivot] = arr[right];
                arr[right] = temp;
            } else {
                int temp = arr[right];
                arr[right] = arr[left];
                arr[left] = temp;
            }
        }
        quicksort(arr, start, right - 1);
        quicksort(arr, right + 1, end);
    }

    public static void main(String[] args) {
        int arr[] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        quicksort(arr, 0, arr.length - 1);

        for (int i = 0; i < arr.length ; i++) {
            System.out.println(arr[i] + " ");
        }
    }
}
