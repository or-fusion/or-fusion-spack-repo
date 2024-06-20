# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Scip(CMakePackage):
    """SCIP optimization solver."""

    homepage = "https://github.com/scipopt/scip"
    url = "https://github.com/scipopt/scip/archive/v901.tar.gz"
    git = "https://github.com/scipopt/scip.git"
    maintainers("whart222")

    license("Apache-2.0")

    version("9.0.1", sha256="08ad3e7ad6f84f457d95bb70ab21fa7fc648dd43103099359ef8a8f30fcce32e")

    depends_on("soplex@7.0.1:", type="build")
    depends_on("metis@5.1.0:", type="build")
    depends_on("ipopt+mumps@3.14.9:", type="build")
    depends_on("gurobi", type="build")

    def url_for_version(self, version):
        url = "https://github.com/scipopt/scip/archive/v{0}.tar.gz"
        return url.format(version.joined, version)

    def cmake_args(self):
        args = []

        args.append("-DAUTOBUILD=ON")

        return args
