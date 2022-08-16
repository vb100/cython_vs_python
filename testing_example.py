import timeit


if __name__ == '__main__':
    py_file = timeit.timeit(
        'example_py.sum_number(5000)', setup='import example_py', number=10_000
    )

    cy_file = timeit.timeit(
        'example_cy.sum_number(5000)', setup='import example_cy', number=10_000
    )

print(py_file, cy_file)
print(f'CPython is more faster than Python {py_file/cy_file} times')
