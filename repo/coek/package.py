# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Coek(CMakePackage, PythonExtension):
    """coek optimization monorepo, which installs libcoek, pycoek, and various
    python packages (especially poek).
    """

    homepage = "https://github.com/sandialabs/coek"
    url = "https://github.com/sandialabs/coek/archive/refs/tags/1.4.0.tar.gz"
    git = "https://github.com/sandialabs/coek.git"
    maintainers("whart222")

    license("BSD")

    version("1.4.0", sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    version("main", branch="main")
    version("dev", branch="dev")
    version("dev-weh", branch="dev-weh")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20", conditional("23", when="^cmake@3.20.3:")),
        multi=False,
        description="Use the specified C++ standard when building",
    )
    variant("debug", default=False, description="Enable debugging")
    variant("verbose", default=False, description="Enable verbose build")
    variant("threads", default=True, description="Build with threads enabled")
    variant("shared", default=True, description="Build shared library")

    variant("tests", default=False, description="Build coek test executables")
    variant("python", default=False, description="Build pycoek and install coek python libraries")
    variant("compact", default=False, description="Build compact expressions in coek")

    variant("openmp", default=True, description="Build with openmp")
    variant("gurobi", default=False, description="Build with Gurobi optimization library")
    variant("highs", default=True, description="Build with Highs optimization library")
    variant("cppad", default=False, description="Build with the CppAD library")
    variant("asl", default=False, description="Build with the ASL library")

    depends_on("cmake@3.13.0:", type="build")
    depends_on("catch2@3.6.0:", when="+tests")
    with when("+python"):
        depends_on("py-pip", type="build")
        depends_on("py-pybind11@2.10.4")
        extends("python")
    depends_on("fmt@8.0.1")
    depends_on("rapidjson@1.1.0")

    depends_on("highs", when="+highs")

    with when("+cppad"):
        depends_on("cppad@20240000.4:")
    with when("+asl"):
        depends_on("asl")

    def setup_run_environment(self, env):
        if self.spec.satisfies("+python"):
            # Extend PYTHONPATH to find the pycoek shared object libraries
            env.append_path("PYTHONPATH", self.spec.prefix.lib)
            env.append_path("PYTHONPATH", self.spec.prefix.lib64)

    def cmake_args(self):
        spec = self.spec
        args = []

        args.append("-Dwith_spack=ON")

        args.append("-Dwith_fmtlib=ON")
        args.append("-Dwith_rapidjson=ON")

        if self.spec.satisfies("+shared"):
            args.append("-DBUILD_SHARED_LIBS=ON")
        elif self.spec.satisfies("-shared"):
            args.append("-DBUILD_SHARED_LIBS=OFF")

        if self.spec.satisfies("+debug"):
            args.append("-Dwith_debug=ON")

        if self.spec.satisfies("+verbose"):
            args.append("-Dwith_verbose=ON")

        if self.spec.satisfies("+threads"):
            args.append("-Dwith_threads=ON")

        if self.spec.satisfies("+openmp"):
            args.append("-Dwith_openmp=ON")

        if self.spec.satisfies("+tests"):
            args.append("-Dwith_tests=ON")
            args.append("-Dwith_catch2=ON")

        if self.spec.satisfies("+python"):
            args.append("-Dwith_python=ON")
            args.append("-Dwith_pybind11=ON")

        if self.spec.satisfies("+compact"):
            args.append("-Dwith_compact=ON")

        if self.spec.satisfies("+asl"):
            args.append("-Dwith_asl=ON")

        if self.spec.satisfies("+cppad"):
            args.append("-Dwith_cppad=ON")
        if self.spec.satisfies("+highs"):
            args.append("-Dwith_highs=ON")
        #
        # External gurobi dependency found by CMAKE, not spack
        #
        if self.spec.satisfies("+gurobi"):
            args.append("-Dwith_gurobi=ON")
        #
        # Require standard at configure time to guarantee the
        # compiler supports the selected standard.
        #
        args.append("-DCMAKE_CXX_STANDARD_REQUIRED=ON")
        args.append("-DCMAKE_CXX_STANDARD={0}".format(spec.variants["cxxstd"].value))

        return args
