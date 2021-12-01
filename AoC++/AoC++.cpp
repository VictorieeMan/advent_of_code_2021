// AoC++.cpp : Defines the entry point for the application.
// 
//Advent of Code 2021

//Headers
#include "AoC++.h"

//Daily headers
#include "aocDay01.h"

using namespace std;

int main()
{
	cout << "Merry Christmas!" << endl;

    string path = "puzzleData\\";
    string filename = "AoC_day01_input.txt";
    string filePath = path + filename;

    vector<string> vecStr;
    vecStr = readFileToStringVector(filePath);

    vector<int> vecInt;
    vecInt = vecStrToInt(vecStr);

    aocDay01(vecInt);

	return 0;
}
