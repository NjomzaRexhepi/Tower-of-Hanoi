#include<iostream>
using namespace std;
int binarySearch(int arr[], int toBeSearched, int first, int last) {
	if (first > last) {
		return -1;
	}
	int mid = (first + last) / 2;
	if (arr[mid] == toBeSearched) {
		return mid;
	}
	else if (arr[mid] > toBeSearched) {
		return binarySearch(arr, toBeSearched, first, mid - 1);
	}
	else {
		return binarySearch(arr, toBeSearched, mid + 1, last);
	}
}

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