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

	//inputData
	vector<int> dataSet = inputData;

	//The depth at each measue point
	int depth = dataSet[0];

	//Checking the ups / downs in the data
	for (int i = 1; i < dataSet.size(); i++) {
		if (depth < dataSet[i]){
			ups += 1;
		}
		else if (depth > dataSet[i]) {
			downs += 1;
		}
		else {
			notApp += 0;
		}

		depth = dataSet[i];
	}

	printInt(ups);
	printInt(downs);
	printInt(notApp);

	printString("Part Two");

	vector<int> processedData;

	for (int i = 0; i < inputData.size() - 2; i++) {
		int temp = inputData[i] + inputData[i + 1] + inputData[i + 2];
		processedData.push_back(temp);
	}

	//Parameters
	ups = 0;
	downs = 0;
	notApp = 0; //Short for Not Applicable

	//inputData
	dataSet = processedData;

	//The depth at each measue point
	depth = dataSet[0];

	//Checking the ups / downs in the data
	for (int i = 1; i < dataSet.size(); i++) {
		if (depth < dataSet[i]) {
			ups += 1;
		}
		else if (depth > dataSet[i]) {
			downs += 1;
		}
		else {
			notApp += 0;
		}

		depth = dataSet[i];
	}

	printInt(ups);
	printInt(downs);
	printInt(notApp);

	return 0;
}