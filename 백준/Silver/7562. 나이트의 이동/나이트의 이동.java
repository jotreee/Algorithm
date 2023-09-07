import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] dr = {2, 2, 1, 1, -1, -1, -2, -2};
		int[] dc = {1, -1, 2, -2, 2, -2, 1, -1};
		
		int N = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < N; tc++) {
			int n = Integer.parseInt(br.readLine());
			int[][] board = new int[n][n];
			for (int i = 0; i < n; i++) {
				Arrays.fill(board[i], 0);
			}
			
			
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st1.nextToken());
			int y = Integer.parseInt(st1.nextToken());
			int X = Integer.parseInt(st2.nextToken());
			int Y = Integer.parseInt(st2.nextToken());
			
			if (x == X && y == Y) {
				System.out.println(0);
			} else {
				ArrayList<Integer>[] loc = new ArrayList[2];
				loc[0] = new ArrayList<Integer>();
				loc[1] = new ArrayList<Integer>();
				loc[0].add(x);
				loc[1].add(y);
				board[x][y] = 1;
				int cnt = 0;
				int out = 0;
				while(true) {
					cnt += 1;
					
					ArrayList<Integer>[] nxt = new ArrayList[2];
					nxt[0] = new ArrayList<Integer>();
					nxt[1] = new ArrayList<Integer>();
					
					for(int m = 0; m < loc[0].size(); m++) {
						int i = loc[0].get(m);
						int j = loc[1].get(m);
						
						for(int k = 0; k < 8; k++) {
							if (i + dr[k] == X && j + dc[k] == Y) {
								System.out.println(cnt);
								out = 1;
								break;
							} else if (0 <= i + dr[k] && i + dr[k] < n && 0 <= j + dc[k] && j + dc[k] < n && board[i + dr[k]][j + dc[k]] == 0) {
								board[i + dr[k]][j + dc[k]] = 1;
								nxt[0].add(i + dr[k]);
								nxt[1].add(j + dc[k]);
							}
						}
						
						if (out == 1) {
							break;
						}
						
					}
					
					if (out == 1) {
						break;
					} else {
						loc = nxt;
					}
					
				}
			}
			
		}
	}

}
