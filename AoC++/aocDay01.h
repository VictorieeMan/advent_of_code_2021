//Advent of Code 2021 - Day 01

#pragma once

#include "AoC++.h"

using namespace std;

int aocDay01()
{
	printString("aocDay01",2);

	string filePath = filePathGen("01",0);

	vector<string> vecStr;
	vecStr = readFileToStringVector(filePath);

	vector<int> inputData;
	inputData = vecStrToInt(vecStr);

	printString("Part One");

	//Parameters
	int ups = 0;
	int downs = 0;
	int notApp = 0; //Short for Not Applicable

	//The depth at each measue point
	int depth = inputData[0];

	//Checking the ups / downs in the data
	for (int i = 1; i < inputData.size(); i++) {
		if (depth < inputData[i]){
			ups += 1;
		}
		else if (depth > inputData[i]) {
			downs += 1;
		}
		else {
			notApp += 0;
		}

		depth = inputData[i];
	}

	printInt(ups);
	printInt(downs);
	printInt(notApp);

	return 0;
}