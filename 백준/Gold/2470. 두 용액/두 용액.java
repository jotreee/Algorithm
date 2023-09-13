import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		int i = 0;
		int j = N - 1;
		int[] result = { Math.abs(arr[0] + arr[N - 1]), arr[0], arr[N - 1] };
		while (i < j) {
			if (arr[i] + arr[j] == 0) {
				result[0] = 0;
				result[1] = arr[i];
				result[2] = arr[j];
				break;
			} else if (Math.abs(arr[i] + arr[j]) < result[0]) {
				result[0] = Math.abs(arr[i] + arr[j]);
				result[1] = arr[i];
				result[2] = arr[j];
			}
			if (arr[i] + arr[j] < 0) {
				i += 1;
			} else {
				j -= 1;
			}
		}
	System.out.println(result[1] + " " + result[2]);
	}

}
