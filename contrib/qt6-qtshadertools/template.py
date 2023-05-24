pkgname = "qt6-qtshadertools"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "perl", "qt6-qtbase"]
makedepends = ["qt6-qtbase-devel"]
depends = [f"qt6-qtshadertools-libs={pkgver}-r{pkgrel}"]
pkgdesc = "Qt6 shader tools"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtshadertools-everywhere-src-{pkgver}.tar.xz"
sha256 = "86618d037f3071f1f7ac5eb7ab76ae4e6f51cfddded0a402bb9aa7f3f79f5775"
debug_level = 1  # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# TODO
options = ["!check", "!cross"]


@subpackage("qt6-qtshadertools-libs")
def _libs(self):
    return self.default_libs()


@subpackage("qt6-qtshadertools-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
