# pybind11 template

Here is a simple example to wrap the library in here: https://github.com/jpiqueras/modern-cpp-lib-template

Using [pybind11](https://github.com/pybind/pybind11) and [scikit-build-core](https://github.com/scikit-build/scikit-build-core)

To make it work just:

1. Create the package for the C++ library with conan. [Follow instructions 1 to 4 from here] (https://github.com/jpiqueras/test-modern-cpp-lib-template).

2. Clone this repository and open a terminal in the root folder.

3. Install the C++ library with conan so CMake can find it.

```
conan install .
```

4. Now CMake will work fine, so just install the package normally with pip, [scikit-build-core](https://github.com/scikit-build/scikit-build-core) does the rest.

```
pip install .
```

5. Run the script in the test folder to check it works.

