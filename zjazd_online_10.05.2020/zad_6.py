class Vector:

    def _init_(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<Vector>: x={self.x}, y={self.y}"

    def __add__(self,other):
        q = self.x + other.x
        r = self.y + other.y

        return  Vector(q,r)

    def __sub__(self, other):

        q = self.x - other.x
        r = self.y - other.y

        return Vector(q, r)

    def __mul__(self, other):
        if isinstance(other,(int,float)):
            q = self.x * other
            r = self.y * other
            return Vector(q,r)
        elif isinstance(other,Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise NotImplementedError()
    @property
    def length(self):
        return pow(self.x ** 2 + self.y ** 2, 0.5)

    def __eq(self,other):
        return self.length == other.length

    def __gt__(self, other):
        return self.length > other.length


    def __lt__(self, other):
        return self.length < other.length






class TestVector:
    def test_init(self):
        vector_1 = Vector(1,2)
        assert vector_1.x == 1
        assert vector_1.y == 2

    def test_add(self,other):
        vector_1 = Vector(1, 2)
        vector_2 = Vector(3, 4)
        vector_3 = vector_1 + vector_2
        assert vector_3 == (4,6)
        assert vector_3.x == 4
        assert vector_3.y == 6

    def test_sub(self,other):
        vector_1 = Vector(1, 2)
        vector_2 = Vector(3, 4)
        vector_3 = vector_1 + vector_2
        assert vector_3 == (-2,-2)
    def test_mul_two_vectors(self):
        vector_1 = Vector(1,2)
        vector_2 = Vector(3,4)
        assert vector_1 * vector_2 == 1*3 + 2*4

    def test_mul_vector_int(self):
        vector_1 = Vector(1,2)
        vector_2 = vector_1 * 3
        assert vector_2.x == 3
        assert vector_2.y == 6

    def test_vector_comparison(self):
        vector_1 = Vector(1, 2)
        vector_2 = Vector(3, 4)
        vector_3 = Vector(1, 2)
        assert vector_2 > vector_1
        assert vector_1 < vector_2
        assert vector_1 == vector_3
        assert vector_1 != vector_2


    def test_str(self):
        vector_1 = Vector(3,4)




