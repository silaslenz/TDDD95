#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;


int get_root(int a, vector<int> &parent) {
    if (parent.at(a) != a){
        parent.at(a) = get_root(parent.at(a), parent);
    }
    return parent.at(a);
//    auto root = a;
//    while (parent.at(root) != root && parent.at(root) != -1)
//        root = parent.at(root);
////    cout << "root: "<<root << endl;
//    return root;
}

bool is_in_same(int a, int b, vector<int> &parent) {
    return get_root(a, parent) == get_root(b, parent);
}

void merge(int a, int b, vector<int> &parent) {
    if (a == b)
        return;
    auto root_of_a = get_root(a, parent);
    auto root_of_b = get_root(b, parent);
    if (root_of_a == root_of_b)
        return;
    if (root_of_a < root_of_b)
        parent.at(root_of_a) = root_of_b;
    else
        parent.at(root_of_b) = root_of_a;
}

static const char no[]= "no\n";
static const char yes[]= "yes\n";


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N, Q;
    scanf("%i %i", &N, &Q);
    std::vector<int> parent(N);
    iota(begin(parent),end(parent), 0);
//    string result;
    for (int i = 0; i < Q; ++i) {
        char op;
        int a, b;
        scanf(" %c %i %i", &op, &a, &b);
//        cout << op << " "<<a << " " <<b <<endl;
        if ('=' == op) {
            merge(a, b, parent);
        } else {
            if (is_in_same(a, b, parent)) {
                std::cout.write(yes,4);
            } else {
                std::cout.write(no,3);
            }
        }
    }
//    cout << result;
    return 0;
}


