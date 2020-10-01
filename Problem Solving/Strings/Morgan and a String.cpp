#include <bits/stdc++.h>

using namespace std;

// Complete the morganAndString function below.
string morganAndString(string a, string b) {

    int top_a = 0;
    int top_b = 0;

    string result;

    while(true){

        if(top_a >= a.length() && top_b >= b.length()){
            break;
        }

        if(top_a >= a.length() && top_b < b.length()){
            while(top_b < b.length()){
                result.push_back(b[top_b]);
                top_b++;
            }
            break;
        }

        if(top_b >= b.length() && top_a < a.length()){
            while(top_a < a.length()){
                result.push_back(a[top_a]);
                top_a++;
            }
            break;
        }

        printf("Checking %c and %c \n", a[top_a], b[top_b]);

        if(a[top_a] > b[top_b]){
            result.push_back(b[top_b]);
            top_b++;
        }

        if(b[top_b] > a[top_a]){
            result.push_back(a[top_a]);
            top_a++;
        }

        if(a[top_a] == b[top_b]){
            int i = top_a+1;
            int j = top_b+1;

            while(i < a.length() and j < b.length()){
                if(a[i] == b[j]){
                    i++;
                    j++;
                }

                if(a[i] > b[j]){
                    result.push_back(b[top_b]);
                    top_b++;
                    break;
                }

                if(b[j] > a[i]){
                    result.push_back(a[i]);
                    top_a++;
                    break;
                }

            }
        }

    }

    return result;



}

int main()
{

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string a;
        getline(cin, a);

        string b;
        getline(cin, b);

        string result = morganAndString(a, b);

        cout << result << "\n";
    }

    return 0;
}
