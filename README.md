# Preceptron Learning Algorithm (PLA)

- The **PLA** is designed to find linear relationships within a set of data. It is done by tuning the weights of each set of data to be able to find the equation for the line: `y= mx + b`, or more generally: `y = m_1 x_1 + m_2 x_2 + m_3 x_3 + b`
- To learn about PLA look at the following files: `preceptron.py`, `linear_function.py`, `boolean_function.py`, and `planar_equation.py`.
  - In the `preceptron.py` file, the `Perceptron()` class contains the perceptron learning algorithm. This is an extremely useful algorithm to understand because neural networks and deep neural networks build on this simple algorithm to generalize more sophisticated functions.
- For more detail as to how the algorithm works and how it was implemented read the corresponding lesson guide (not yet posted)
- To check out real world applications of the **PLA** reference the `src/examples` directory

## Testing the Code

- Python's builtin unittest module was used to make tests
- to run the specfic test file run: `python -m unittest [filename]`
- all test files start wil `test_`.
- [here](https://docs.python-guide.org/writing/tests/) are some testing resources
- importing code from [sibling modlues](https://wiki.python.org/moin/Asking%20for%20Help/How%20can%20I%20import%20a%20module%20from%20a%20sibling%20directory%3F)

## Todo

- [x] figure out train method
- [ ] proofread document

### Vector

- [ ] write documentation for each method [numpy documentation](https://numpydoc.readthedocs.io/en/latest/format.html), another documentation guide is [here](https://realpython.com/documenting-python-code/).

## Resources / References

- [d3js in ipynb file](https://www.stefaanlippens.net/jupyter-custom-d3-visualization.html)
- [pla article](https://towardsdatascience.com/perceptron-learning-algorithm-d5db0deab975)
