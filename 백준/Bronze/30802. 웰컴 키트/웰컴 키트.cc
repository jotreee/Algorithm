#include <iostream>

using namespace std;
int main() {
	int N, T, P;
	int size[6] = { 0 };
	cin >> N;
	for (int i = 0; i < 6; i++) {
		cin >> size[i];
	}
	cin >> T >> P;

	int T_answer = 0;
	for (int i = 0; i < 6; i++) {
		T_answer += int(size[i] / T);
		if (size[i] % T > 0) {
			T_answer += 1;
		}
	}

	cout << T_answer << endl;
	cout << int(N / P) << " " << N % P << endl;

	return 0;
}