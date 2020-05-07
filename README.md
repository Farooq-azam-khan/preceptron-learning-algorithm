# Preceptron Learning Algorithm
- To learn about PLA look at the following files: `preceptron.py`, `linear_function.py`, `boolean_function.py`, and `planar_equation.py`.
  - In the `preceptron.py` file, the `Perceptron()` class contains the perceptron learning algorithm. This is an extremely useful algorithm to understand because neural networks and deep neural networks build on this simple algorithm.
    - The algorithm itself has two main parts to it, predicting results based on input and training based on desired outcome and actual outcome.
    - The reason PLA is simple and not useful in modern day research is because it can only predict linearly separable data (i.e. it can only separate things with a line and can be proven with linear algebra).
  - The `linear_function.py` file contains a graphical understanding of how PLA does linear separation of 2d inputs.
    - The `Point()` class generates random points with a label. The `label=1` if it is above the actual line and `label=-1` if it is below. PLA will try to approximate this line as best as possible by putting a point to either side of a line. Think of it as organizing a bowl of dimes and nickels. The dimes will go in one basket and the nickels in another.
    - There are four outcomes when predicting a set of inputs. It could be false positive, false negative, true positive, and true negative. These can be seen in the legend of the graph.
  - The `boolean_function.py` file contains examples of PLA successes as well as its failure, i.e. the XOR problem. Look at `neural_network.py` for improvement to PLA and a solution to the `xor` problem.
