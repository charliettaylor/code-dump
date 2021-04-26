#include "Coordinate.h"

#include <iostream>
#include <cmath>

using namespace std;

Coordinate::Coordinate(double newX, double newY)
{
    x = newX;
    y = newY;
}

Coordinate::Coordinate(const Coordinate& other)
{
    x = other.x;
    y = other.y;
}

Coordinate& Coordinate::operator=(Coordinate& other)
{
    if(this == &other)
    {
        cerr << "Attempted self assignment";
    }
    else
    {
        x = other.x;
        y = other.y;
    }
}

Coordinate::Coordinate(Coordinate&& other)
{
    if(this == &other)
    {
        cerr << "Attempted self assignment";
    }
    else
    {
        x = other.x;
        y = other.y;

        other.x = 0;
        other.y = 0;
    }
}

Coordinate&& Coordinate::operator=(Coordinate&& other)
{
    if(this == &other)
    {
        cerr << "Attempted self assignment";
    }
    else
    {
        x = other.x;
        y = other.y;

        other.x = 0;
        other.y = 0;
    }
}

double Coordinate::distance(const Coordinate& other) const
{
    return sqrt(pow(other.x - x, 2) +  pow(other.y - y, 2));
}

int Coordinate::quadrant() const
{
    if(x > 0 && y > 0)
    {
        return 1;
    }
    else if (x < 0 && y > 0)
    {
        return 2;
    }
    else if(x < 0 && y < 0)
    {
        return 3;
    }
    else if(x > 0 && y < 0)
    {
        return 4;
    }
    else
    {
        return 0;
    }
}

void Coordinate::flip_x()
{
    y = y * -1;
}

void Coordinate::flip_y()
{
    x = x * -1;
}

void Coordinate::mirror()
{
    x = x * -1;
    y = y * -1;
}