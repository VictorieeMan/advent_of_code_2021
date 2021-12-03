// AoC++.cpp : Defines the entry point for the application.
// 
//Advent of Code 2021

//Headers
#include "AoC++.h"

//Daily headers
#include "aocDay01.h"
#include "aocDay02.h"

using namespace std;

int main()
{
	cout << "Merry Christmas!" << endl;
    aocDay02();

	return 0;
}

//My standard code for opening and reading file to memory
// 
//string filePath = filePathGen("01");
//
//vector<string> vecStr;
//vecStr = readFileToStringVector(filePath);
//
//vector<int> vecInt;
//vecInt = vecStrToInt(vecStr);