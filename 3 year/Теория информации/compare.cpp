#include <fstream>
#include <iostream>

using namespace std;

size_t filesize(std::string filename)
{
    std::ifstream in(filename, std::ifstream::ate | std::ifstream::binary);
    return in.tellg(); 
}

int main() 
{

    std::string files[] = {"random.txt", "random.zip", "random.tar.gz", "random.tar.bz2"};

    for(std::string filename : files)
        printf("%-20s %lu bytes \r\n", filename.c_str(), filesize(filename));

    return 0;
}