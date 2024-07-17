#include <iostream>
#include <string>

using namespace std;
int main() {
	// 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
	string a, b, c;
	int i;
	cin >> a >> b >> c;
	if (a != "Fizz" && a != "Buzz" && a != "FizzBuzz") {
		i = stoi(a) + 3;
	}
	else if (b != "Fizz" && b != "Buzz" && b != "FizzBuzz") {
		i = stoi(b) + 2;
	}
	else {
		i = stoi(c) + 1;
	}

	if (i % 15 == 0) {
		cout << "FizzBuzz" << endl;
	}
	else if (i % 5 == 0) {
		cout << "Buzz" << endl;
	}
	else if (i % 3 == 0) {
		cout << "Fizz" << endl;
	}
	else {
		cout << i << endl;
	}

	return 0;
}