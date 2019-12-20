import sys
import datatest.points
import math5.approx
import sqlalchemy;

def main(x):
    return x/0.2;

print(main(1920));
result = math5.approx.sqrt_approx(2.0,  20);
print(str(result.returned)+ " | " + str(result.function));
print("orm ver: " + str(sqlalchemy.__version__));
print(datatest.points.get_last_points(25));

datatest.points.add_point(10, 20, -3);