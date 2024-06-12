# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Scip(CMakePackage):
    """SCIP optimization solver."""

    homepage = "https://github.com/scipopt/scip"
    url = "https://github.com/scipopt/scip/archive/refs/tags/v901.tar.gz"
    git = "https://github.com/scipopt/scip.git"
    maintainers("whart222")

    depends_on("soplex@7.0.1:", type="build")
    depends_on("metis@5.1.0:", type="build")
    depends_on("ipopt+mumps@3.14.9:", type="build")
    depends_on("gurobi", type="build")
    license("Apache-2.0")

    version("9.0.1", sha256="X10175ad66e7f113ac5dc00c9d6650a620663a6884fbf2942d6eb7a3d854604f")

    def cmake_args(self):
        args = []

        args.append("-DAUTOBUILD=ON")

        return args
