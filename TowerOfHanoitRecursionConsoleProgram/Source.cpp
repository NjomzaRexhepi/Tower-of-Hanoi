#include<iostream>
using namespace std;


void towersOfHanoi(int start, int end, char source, char aux, char destination) {
	if (start > end) {
		return;
	}
	towersOfHanoi(start, end - 1, source, destination, aux);
	cout << "Move disk " << end << " from " << source << " to " << destination << endl;
	towersOfHanoi(start, end - 1, aux, source, destination);

}

int main() {
	towersOfHanoi(1, 5, 'A', 'B', 'C');
}
