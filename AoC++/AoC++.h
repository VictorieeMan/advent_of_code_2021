// AoC++.h : Include file for standard system include files,
// or project specific include files.

#pragma once

#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

//using namespace std;

//Input functions

//Given a file path, read file line by line to StringVector and return it
std::vector<std::string> readFileToStringVector(std::string inputFilePath) {
	std::ifstream inputFile;
	std::vector<std::string> fileLines;
	std::string line;

	inputFile.open(inputFilePath, std::ios::in);
	if (inputFile.is_open()) {
		while (!inputFile.eof()) {
			std::getline(inputFile, line);
			fileLines.push_back(line);
		}
	}
	else {
		std::cout << "File not open...";
		int dummy;
		std::cin >> dummy;
	}

	return fileLines;
}

//Convert functions

//Given vecStr containing numbers, converts to vecInt
std::vector<int> vecStrToInt(std::vector<std::string> vecStr) {
	std::vector<int> vecInt;
	for (int i = 0; i < vecStr.size(); i++) {
		vecInt.push_back(std::stoi(vecStr[i]));
	}
	return vecInt;
}

// TODO: Reference additional headers your program requires here.
