# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Soplex(CMakePackage):
    """Soplex optimization solver."""

    homepage = "https://github.com/scipopt/soplex"
    url = "https://github.com/scipopt/soplex/archive/refs/tags/release-701.tar.gz"
    git = "https://github.com/scipopt/soplex.git"
    maintainers("whart222")

    license("Apache-2.0")

    version("7.0.1", sha256="d10175ad66e7f113ac5dc00c9d6650a620663a6884fbf2942d6eb7a3d854604f")

    variant("gmp", default=False, description="Build with GMP to enable exact rational LP solver")
    variant("boost", default=False, description="Build with Boost")

    def cmake_args(self):
        args = []

        if self.spec.satisfies("+gmp"):
            args.append("-DGMP=ON")
        else:
            args.append("-DGMP=OFF")
        if self.spec.satisfies("+boost"):
            args.append("-DBOOST=ON")
        else:
            args.append("-DBOOST=OFF")

        args.append("-DFAST_BUILD=ON")

        return args
