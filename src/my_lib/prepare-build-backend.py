# For a "regular" build with scikit-build-core, you would just use in the pyproject.toml:
# build-backend = "scikit_build_core.build"
# But here, we want to conan install the C++ dependencies before calling cmake, so there are three options:
# 1. To continue using scikit-build-core directly, but befor calling `pip install .` you would need to call `conan install .`
# 2. To integrate conan in CMake. This is still experimental for Conan 2.0. I might try it in the future.
# 3. To use a custom build backend that just do the conan install before leaving the rest to scikit-build-core, which is what we do here.

# Guard against direct execution of this file
if __name__ == "__main__":
    raise TypeError(
        "This module cannot be executed directly. It should be called by pip install."
    )


# Import the hooks from scikit-build-core that will be called by pip
from scikit_build_core.build import *
import subprocess


result = subprocess.run(
    ["conan", "create", "src/my_lib/modern-cpp-lib-template", "--build=missing"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
if result.returncode == 0:
    print("Success!")
else:
    print("Error:", result.stderr.decode())
    raise RuntimeError("Conan install failed. See error above.")

# "Inject" the conan install before the build hooks are called.
result = subprocess.run(
    ["conan", "install", "src/my_lib", "--build=missing"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
if result.returncode == 0:
    print("Success!")
else:
    print("Error:", result.stderr.decode())
    raise RuntimeError("Conan install failed. See error above.")
