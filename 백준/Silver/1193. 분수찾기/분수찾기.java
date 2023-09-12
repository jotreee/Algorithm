import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		if (N == 1) {
			System.out.println("1/1");
		} else if (N == 2) {
			System.out.println("1/2");
		} else {
			int n = N;
			for(int i = 0; i < N; i++) {
				if (n > i) {
					n -= i;
				} else {
					if (i % 2 == 0) {
						System.out.println(n+"/"+(i + 1 - n));
						break;
					} else {
						System.out.println((i + 1 - n) +"/"+n);
						break;
					}
				}
			}
		}
		
	}

}
