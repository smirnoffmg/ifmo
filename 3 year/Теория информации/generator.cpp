#include <fstream>
#include <iostream>
#include <random>

using namespace std;

int main() 
{
    const size_t length = 1024;
    const char charset[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz\t\n\r";

    const size_t max_index = (sizeof(charset) - 1);

    std::random_device engine;
    std::ofstream file("random.txt");
    file.seekp(0);

    for(size_t i = 0; i < length; i++)
    {
        file << charset[engine() % max_index];
    }
    
    return 0;
}