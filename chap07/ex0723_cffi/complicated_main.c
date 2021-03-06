#include <stdio.h>
#include "complicated.h"

int main(void)
{
    struct Point pnt;
    pnt.x = 0.0;
    pnt.y = 0.0;
    pnt.isActive = true;
    pnt.id = "center";
    pnt.num_times_visited = 0;

    printf("point info.\n");
    printf("position: (%f, %f)\n", pnt.x, pnt.y);
    printf("id: %s\n", pnt.id);
    printf("visited: %d\n", pnt.num_times_visited);

    return 0;
}