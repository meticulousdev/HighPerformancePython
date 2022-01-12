#include <stdbool.h>

struct Point
{
    double x;
    double y;
    bool isActive;
    const char *id;
    int num_times_visited;
};