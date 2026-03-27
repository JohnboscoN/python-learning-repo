import pytest
import pandas as pd

def sum_xy(x, y):
    sum = x + y
    return sum


# Write a function that finds the product of two numbers (*)
# write a test to check that it works

def test_sum_xy():
    test_output = sum_xy(x=1, y=2)
    assert test_output == 3
    

def product_xy(x, y):
    product = x * y
    return product

def test_product_xy():
    test_output = product_xy(x=2, y=6)
    assert test_output == 12




# Write a function that finds the product of two numbers (*)
# write a test to check that it works
def prod_xy(x, y):
    return x * y

def test_prod_xy():
    assert prod_xy(1, 3) == 3

def sum_prod(x, y):
    return sum_xy(x, y), prod_xy(x, y)

def test_sum_prod():
    output = sum_prod(3, 5)
    assert output[0] == 8
    assert output[1] == 15


def sum_prod(x, y):
    return sum_xy(x, y), prod_xy(x, y)

def test_sum_prod():
    sum, prod = sum_prod(3, 5)
    assert sum == 8
    assert prod == 15


test_df = pd.DataFrame(
        [
            {"ChildId": "child1", "Age": 6},
            {"ChildId": "child3", "Age": 10},
            {"ChildId": "child2", "Age": 4},
            {"ChildId": "child4", "Age": 1},
        ]
    )

expected_df = pd.DataFrame(
        [
            {"ChildId": "child1", "Age": 6},
            {"ChildId": "child3", "Age": 10},
         ]   
    )

def df_slicer(df, age):
    age_or_over = df[df['Age'] >= age]
    return age_or_over

def test_df_slicer():
    test_df = pd.DataFrame(
        [
            {"ChildId": "child1", "Age": 6},
            {"ChildId": "child3", "Age": 10},
            {"ChildId": "child2", "Age": 4},
            {"ChildId": "child4", "Age": 1},
        ]
    )

sliced_df = df_slicer(test_df, 5)

expected_df = pd.DataFrame(
    [
        {"ChildId": "child1", "Age": 6},
        {"ChildId": "child3", "Age": 10},
     ]   
    )

pd.testing.assert_frame_equal(sliced_df, expected_df, check_names=None)
 

