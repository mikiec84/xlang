import find_projection

import _pyrt
import unittest

class TestNumerics(unittest.TestCase):
    def test_struct_ctor_pos(self):
        r = _pyrt.Rational(2, 4)

        self.assertEqual(r.Numerator, 2)
        self.assertEqual(r.Denominator, 4)

    def test_struct_ctor_kwd(self):
        r = _pyrt.Rational(Denominator=2, Numerator=4)

        self.assertEqual(r.Numerator, 4)
        self.assertEqual(r.Denominator, 2)

    def test_struct_ctor_mix(self):
        r = _pyrt.Rational(3, Denominator=6)

        self.assertEqual(r.Numerator, 3)
        self.assertEqual(r.Denominator, 6)

    def test_struct_ctor_dict(self):
        r = _pyrt.Rational({"Denominator":2, "Numerator":4})

        self.assertEqual(r.Numerator, 4)
        self.assertEqual(r.Denominator, 2)

    def test_vec3(self):
        v = _pyrt.Vector3(1.0, 2.0, 3.0)

        self.assertEqual(v.X, 1.0)
        self.assertEqual(v.Y, 2.0)
        self.assertEqual(v.Z, 3.0)

    def test_plane(self):
        v = _pyrt.Vector3(1.0, 2.0, 3.0)
        p = _pyrt.Plane(v, 4.0)
        n = p.Normal

        self.assertEqual(n.X, 1.0)
        self.assertEqual(n.Y, 2.0)
        self.assertEqual(n.Z, 3.0)
        self.assertEqual(p.D, 4.0)
    
    def test_plane_dict(self):
        p = _pyrt.Plane({"X":1.0, "Y":2.0, "Z":3.0}, 4.0)
        n = p.Normal

        self.assertEqual(n.X, 1.0)
        self.assertEqual(n.Y, 2.0)
        self.assertEqual(n.Z, 3.0)
        self.assertEqual(p.D, 4.0)

if __name__ == '__main__':
    _pyrt.init_apartment()
    unittest.main()
    _pyrt.uninit_apartment()