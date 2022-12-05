Compiled Python: acceleration
==============================


The aim of this repository is to store examples to compile Python code using Cython_ for performace improvement. The files used are:

1. **fib_py.py:** This file contains a looped version of the Fibonacci problem.

2. **fib_c_annoted.pyx:** Cython annotated file as an accelerated version of the previous code.

3. **setup.py:** This file contains the needed commands to compile the previous file.

4. **test.py:** This file contains a simple test to record the performance.


How to compile ?
===================

The code to compile is **fib_c_annoted.pyx**. For doing this, we need to check if there is an available version of **GCC**.

The compilation is done using the following steps:

1. python setup.py build_ext --inplace

To test the code and compare with the only Python version, one can type

2. python test.py NUMBER

where **NUMBER** is a integer to computhe the Fibonacci number. For example:

.. code_block:: bash

   python test.py 35
 
The expected output should be something like:

.. code_block:: bash

   Pure python: answer = 5702887, time = 0.1646157400100492, speedup = 1.0
   Cython double variables: answer = 5702887.0, time = 0.007783060020301491, speedup = 21.15051658096715

.. _Cython: https://cython.org/
