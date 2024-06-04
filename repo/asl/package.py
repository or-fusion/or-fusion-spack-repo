# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Asl(CMakePackage):
    """A Package for Differentiation of C++ Algorithms."""

    homepage = "https://github.com/whart222/asl"
    url = "https://github.com/whart222/asl/archive/refs/tags/rev_1.1.tar.gz"
    git = "https://github.com/whart222/asl.git"

    version("master", branch="master")

    def cmake_args(self):
        args = []

        args.append("-DCMAKE_INSTALL_PREFIX=%s" % self.prefix)
        args.append("-DBUILD_SHARED_LIBS=ON")
        args.append("-DBUILD_MT_LIBS=ON")
        args.append("-DCMAKE_BUILD_TYPE=Release")

        return args
