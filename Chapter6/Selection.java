package Chapter6;

public class Selection {
    public static void main(String[] args) {
        int arr[] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        int swapValue = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[i]) {
                    swapValue = arr[i];
                    arr[i] = arr[j];
                    arr[j] = swapValue;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i] + " ");
        }
    }


    /* 
    public static int[] main(int[] nums) {
        int swapValue = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] < nums[i]) {
                    swapValue = nums[i];
                    nums[i] = nums[j];
                    nums[j] = swapValue;
                }
            }
        }
        return nums;
    }
    */
}