#include "simplicial_hom.h"

class Simplex {
    public:
        int dim;
        std::vector<char> vertices;
        Simplex(std::vector<char> vertices);

        Simplex& operator=(const Simplex &rhs);
        Simplex& operator+=(const Simplex &rhs);
        Simplex operator+(Simplex const &other);
        Simplex operator-(Simplex const &other);
};

Simplex::Simplex(std::vector<char> vertices) {
    this->vertices = vertices;
    this->dim = vertices.size() - 1
}

Simplex& Simplex::operator=(const Simplex &rhs){
    if (this == &rhs) {
        return *this;
    }

    dim = rhs.dim;
    vertices = rhs.vertices;
}

Simplex& Simplex::operator+=(const Simplex &rhs){
    assert(dim == rhs.dim);

    // 
}

Simplex Simplex::operator+(Simplex const &other) {

}

Simplex Simplex::operator-(Simplex const &other) {

}

