//Advent of Code 2021 - Day 01

#pragma once

#include "AoC++.h"

using namespace std;

int aocDay01()
{
	myMessage("aocDay01",2);

	string filePath = filePathGen("01");

	vector<string> vecStr;
	vecStr = readFileToStringVector(filePath);

	vector<int> vecInt;
	vecInt = vecStrToInt(vecStr);

	myMessage("Part One");

	return 0;
}