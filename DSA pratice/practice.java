import java.util.*;

class test {
    public static int matrixOperation(int arr[], int n) {
        ArrayList<Integer> evenArr = new ArrayList<>();
        ArrayList<Integer> oddArr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                evenArr.add(arr[i]);
            } else {
                oddArr.add(arr[i]);
            }
        }
        int evenArrSize = evenArr.size();
        int oddArrSize = oddArr.size();
        Collections.sort(evenArr);
        Collections.sort(oddArr);

        int evenArrSlar = evenArr.get(evenArrSize - 2);
        int oddArrSlar = oddArr.get(oddArrSize - 2);

        return evenArrSlar + oddArrSlar;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the size of the array :");
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.println("Enter the element of the array : ");
            arr[i] = sc.nextInt();
        }

        int sum = matrixOperation(arr, n);

        System.out.println(sum);

    }

}