#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

void density(string &st)
{
    vector<char> stvec(st.begin(), st.end());
    set<char> alphabet(stvec.begin(), stvec.end());
    vector<double> freqs;
    int size = stvec.size();
    double prob;
    double ent = 0;
    double ln2 = log(2);

    for (set<char>::iterator c = alphabet.begin(); c != alphabet.end(); ++c)
    {
        int ctr = 0;
        for (vector<char>::iterator s = stvec.begin(); s != stvec.end(); ++s)
        {
            if (*s == *c)
            {
                ++ctr;
            }
        }
        cout << (double)ctr / size << endl;
        // printf("'%c' %10d %10f\n", *c, ctr, (double)ctr / size);
    }
}

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        cout << "Please, provide a filename" << endl;
    }
    else
    {

        std::ifstream ifs((std::string)string(argv[1]));
        std::string content((std::istreambuf_iterator<char>(ifs)),
                            (std::istreambuf_iterator<char>()));

        density(content);
    }

    return 0;
}