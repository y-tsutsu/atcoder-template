#include <algorithm>
#include <cctype>
#include <cstddef>
#include <iostream>
#include <iterator>
#include <string_view>
#include <type_traits>

// g++ -std=c++17 -DLOCAL -o main main.cpp
#ifdef LOCAL
#include "debug_print.hpp"
#define debug(...) debug_print::multi_print(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (static_cast<void>(0))
#endif

#include <cstdint>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;
using i32 = int32_t;
using i64 = int64_t;
using point = pair<i32, i32>;

int main(int argc, char const *argv[])
{
    i32 a = 42;
    debug(a);
    return 0;
}
