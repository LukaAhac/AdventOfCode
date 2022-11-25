#include <iostream>
#include <vector>

int main() {

	int steps = 12994925;
	char state = 'A';
	std::vector<int> tape(100, 0);
	int cursor = 0;

	while (steps--) {
		if (state == 'A') {
			if (tape[cursor] == 0) {
				tape[cursor] = 1;
				cursor++;
				state = 'B';
			}
			else {
				tape[cursor] = 0;
				cursor--;
				state = 'F';
			}
		}
		else if (state == 'B') {
			if (tape[cursor] == 0) {
				cursor++;
				state = 'C';
			}
			else {
				tape[cursor] = 0;
				cursor++;
				state = 'D';
			}
		}
		else if (state == 'C') {
			if (tape[cursor] == 0) {
				tape[cursor] = 1;
				cursor--;
				state = 'D';
			}
			else {
				cursor++;
				state = 'E';
			}
		}
		else if (state == 'D') {
			if (tape[cursor] == 0) {
				cursor--;
				state = 'E';
			}
			else {
				tape[cursor] = 0;
				cursor--;
				state = 'D';
			}
		}
		else if (state == 'E') {
			if (tape[cursor] == 0) {
				cursor++;
				state = 'A';
			}
			else {
				cursor++;
				state = 'C';
			}
		}
		else if (state == 'F') {
			if (tape[cursor] == 0) {
				tape[cursor] = 1;
				cursor--;
				state = 'A';
			}
			else {
				cursor++;
				state = 'A';
			}
		}
		if (cursor < 0) {
			tape.insert(tape.begin(), 0);
			cursor++;
		}
		else if (cursor >= tape.size()) {
			tape.push_back(0);
		}
	}

	int counter = 0;
	for (int x = 0; x < tape.size(); ++x) {
		if (tape[x] == 1){
		counter++;
		}
	}

	std::cout << counter;
}