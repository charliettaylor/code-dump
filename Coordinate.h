#ifndef HEADER_H
#define HEADER_H

class Coordinate
{
public:
    Coordinate() : x(0), y(0) {}
    Coordinate(double, double);

    // big 5
    Coordinate(const Coordinate&); // copy constructor
    Coordinate& operator=(Coordinate&); // assignment operator

    Coordinate(Coordinate&&); // move constructor
    Coordinate&& operator=(Coordinate&&); //move assignment operator

    double distance(const Coordinate&) const;
    int quadrant() const;

    void flip_x();
    void flip_y();
    void mirror();

    ~Coordinate() {}
private:
    int x;
    int y;
};

#endif