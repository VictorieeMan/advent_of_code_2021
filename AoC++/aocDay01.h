//Advent of Code 2021 - Day 01

#pragma once

#include "AoC++.h"

using namespace std;

int aocDay01()
{
	printString("aocDay01",2);

	string filePath = filePathGen("01",2);

	vector<string> vecStr;
	vecStr = readFileToStringVector(filePath);

	vector<int> inputData;
	inputData = vecStrToInt(vecStr);

	printString("Part One");

	//Parameters
	int ups = 0;
	int downs = 0;
	int notApp = 0;

	//Checking the ups / downs in the data
	for (int i = 0; i < inputData.size(); i++) {
		printInt(inputData[i]);
	}

	return 0;
}