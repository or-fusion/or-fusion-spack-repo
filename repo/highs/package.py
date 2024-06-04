# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Highs(CMakePackage):
    """Highs optimization solver."""

    homepage = "https://github.com/ERGO-Code/HiGHS"
    url = "https://github.com/ERGO-Code/HiGHS/archive/refs/tags/v1.7.0.tar.gz"
    git = "https://github.com/ERGO-Code/HiGHS.git"
    maintainers("whart222")

    license("MIT")

    version("1.7.0", sha256="d10175ad66e7f113ac5dc00c9d6650a620663a6884fbf2942d6eb7a3d854604f")

    def cmake_args(self):
        args = [
            self.define("FAST_BUILD", "ON"),
        ]

        return args
