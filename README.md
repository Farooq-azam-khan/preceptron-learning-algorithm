# Preceptron Learning Algorithm (PLA)

- The **PLA** is designed to find linear relationships within a set of data. It is done by tuning the weights of each set of data to be able to find the equation for the line: `y= mx + b`, or more generally: `y = m_1 x_1 + m_2 x_2 + m_3 x_3 + b`
- To learn about PLA look at the following files: `preceptron.py`, `linear_function.py`, `boolean_function.py`, and `planar_equation.py`.
  - In the `preceptron.py` file, the `Perceptron()` class contains the perceptron learning algorithm. This is an extremely useful algorithm to understand because neural networks and deep neural networks build on this simple algorithm to generalize more sophisticated functions.
- For more detail as to how the algorithm works and how it was implemented read the corresponding lesson guide (not yet posted)


    <!-- - The algorithm itself has two main parts to it, predicting results based on input and training based on desired outcome and actual outcome. - The reason PLA is simple and not useful in modern day research is because it can only predict linearly separable data (i.e. it can only separate things with a line and can be proven with linear algebra). - The `linear_function.py` file contains a graphical understanding of how PLA does linear separation of 2d inputs. - The `Point()` class generates random points with a label. The `label=1` if it is above the actual line and `label=-1` if it is below. PLA will try to approximate this line as best as possible by putting a point to either side of a line. Think of it as organizing a bowl of dimes and nickels. The dimes will go in one basket and the nickels in another. - There are four outcomes when predicting a set of inputs. It could be false positive, false negative, true positive, and true negative. These can be seen in the legend of the graph. - The `boolean_function.py` file contains examples of PLA successes as well as its failure, i.e. the XOR problem. Look at `neural_network.py` for improvement to PLA and a solution to the `xor` problem. -->

## Testing the Code

- Python's builtin unittest module was used to make tests
- to run the specfic test file run: `python -m unittest [filename]`
- all test files start wil `test_`.
- [here](https://docs.python-guide.org/writing/tests/) are some testing resources
- importing code from [sibling modlues](https://wiki.python.org/moin/Asking%20for%20Help/How%20can%20I%20import%20a%20module%20from%20a%20sibling%20directory%3F)

## Todo

- [ ] figure out train method
- [ ] write test for train method

### Vector

- [ ] write more tests
- [ ] write documentation for each method [numpy documentation](https://numpydoc.readthedocs.io/en/latest/format.html), another documentation guide is [here](https://realpython.com/documenting-python-code/).
