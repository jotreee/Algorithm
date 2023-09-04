import java.io.*;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		int result = N;
		
		for (int i = 0; i < N; i++) {
			boolean[] alpha = new boolean[26];
			char[] str = br.readLine().toCharArray();
			
			int no = 0;
			if (str.length > 1) {
				alpha[(int)str[0] - 97] = true;
				for (int j = 1; j < str.length; j++) {
					if (str[j] != str[j - 1]) {
						if (alpha[(int)str[j] - 97] == true) {
							result -= 1;
							no = 1;
							break;
						}
						else {
							alpha[(int)str[j] - 97] = true;
						}
					}
					if (no == 1) {
						break;
					}
				}
			}
		}
		System.out.println(result);
		bw.close();
	}
}