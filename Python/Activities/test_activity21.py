import pytest

def test_addition():
	num1 = 15
	num2 = 15
	sum = num1 + num2
	assert sum == 30
 
def test_subtraction():
	num1 = 50
	num2 = 30
	diff = num1 - num2
	assert diff == 20

def test_multiplication():
	num1 = 5
	num2 = 10
	res1 = num1 * num2
	assert res1 == 50

def test_division():
	num1 = 100
	num2 = 10
	res2 = num1 / num2
	assert res2 == 10
