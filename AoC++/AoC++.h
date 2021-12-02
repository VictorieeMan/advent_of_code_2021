// AoC++.h : Include file for standard system include files,
// or project specific include files.

#pragma once

#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

// TODO: Reference additional headers your program requires here.

//using namespace std;

//Input functions

//File path creator
std::string filePathGen(std::string day, int type = 0) {
	std::string path = "puzzleData\\";
	std::string filename = "AoC_day" + day + "_input";

	if (type == 0) {
		filename += ".txt";
	}
	else {
		filename += std::to_string(type) + ".txt";
	}

	std::string filePath = path + filename;

	return filePath;
}

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

//Other functions

//Conversion functions

//Given vecStr containing numbers, converts to vecInt
std::vector<int> vecStrToInt(std::vector<std::string> vecStr) {
	std::vector<int> vecInt;
	for (int i = 0; i < vecStr.size(); i++) {
		vecInt.push_back(std::stoi(vecStr[i]));
	}
	return vecInt;
}

//Output / Messaging functions

//Outputs given string to terminal, followed by n numbers of linebreakes.
void printString(std::string message, int n = 1) {
	std::cout << message;
	for (int i = 0; i < n; i++) {
		std::cout << std::endl;
	}
}

//Outputs given int to terminal, followed by n numbers of linebreakes.
void printInt(int message, int n = 1) {
	std::cout << message;
	for (int i = 0; i < n; i++) {
		std::cout << std::endl;
	}
}