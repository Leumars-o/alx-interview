#!/usr/bin/python3
"""This module defines a function: Pascal's Triangle
"""

def pascal_triangle(n):
    """This function returns a list of lists of integers representing the Pascal's triangle of n
        args:
            n: an integer
        return:
            a list of lists of integers
    """
    # Handle the case when n is 0 or less
    if n <= 0:
        return []

    # Create an empty array to store the triangle
    triangle = []

    # create base case
    rowOne = [1]
    triangle.append(rowOne)

    # create the rest of the rows 
    for row in range(1, n):
        # create an empty row
        currentRow = []

        # add the first element of the row
        currentRow.append(1)

        # add the rest of the elements
        for i in range(1, row):
            # Calculate the value of the row using the previous row
            value = triangle[row - 1][i - 1] + triangle[row -1][i]
            currentRow.append(value)
        
        # add the last element of the row
        currentRow.append(1)

        # add the row to the triangle
        triangle.append(currentRow)
    
    # return the triangle
    return triangle