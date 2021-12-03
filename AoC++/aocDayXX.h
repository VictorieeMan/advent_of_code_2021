//Advent of Code 2021 - Day 

#pragma once

#include "AoC++.h"

using namespace std;

int aocDayXX()
{
	printString("aocDay", 2);

	string filePath = filePathGen("X", 0);

	vector<string> vecStr;
	vecStr = readFileToStringVector(filePath);

	vector<int> inputData;
	inputData = vecStrToInt(vecStr);

	printString("Part One");

	

	printString("Part Two");

	

	return 0;
}