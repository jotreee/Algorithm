import java.io.*;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < N; i++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());

            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            
            double d = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
            
            if (x1 == x2 && y1 == y2 && r1 == r2){
            	bw.write(-1 + "\n");
            } else if (d == Math.abs(r1 - r2) || d == (r1 + r2)) {
            	bw.write(1 + "\n");
            } else if (Math.abs(r1 - r2) < d && d < (r1 + r2)) {
            	bw.write(2 + "\n");
            } else {
            	bw.write(0 + "\n");
            }
		}
		
		bw.close();

	}

}
