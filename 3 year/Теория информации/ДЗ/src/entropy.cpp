#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

double entropy(string &st)
{
    vector<char> stvec(st.begin(), st.end());
    set<char> alphabet(stvec.begin(), stvec.end());
    vector<double> freqs;
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
        freqs.push_back((double)ctr / (double)stvec.size());
    }
    for (vector<double>::iterator f = freqs.begin(); f != freqs.end(); ++f)
    {
        ent += *f * log(*f) / ln2;
    }
    ent = -ent;
    return ent;
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

        cout << entropy(content) << endl;
    }

    return 0;
}