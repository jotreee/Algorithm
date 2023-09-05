import java.io.*;
import java.util.Arrays;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		char[] arr = br.readLine().toCharArray();
		int result = arr.length;
		
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == '=' || arr[i] == '-') {
				result -= 1;
				if(i > 1 && arr[i] == '=' && arr[i - 1] == 'z' && arr[i - 2] == 'd') {
					result -= 1;
				}
			} else if (i > 0 && arr[i] == 'j') {
				if (arr[i - 1] == 'l' || arr[i - 1] == 'n') {
					result -= 1;
				}
			}
		}
		System.out.println(result);
		bw.close();
	}
}