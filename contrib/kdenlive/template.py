pkgname = "kdenlive"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTING=OFF"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kbookmarks-devel",
    "kcodecs-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "kguiaddons-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "mlt-devel",
    "purpose-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtnetworkauth-devel",
    "qt6-qtsvg-devel",
    "solid-devel",
    "v4l-utils-devel",
]
depends = [
    "ffmpeg",
    "frei0r",
]
pkgdesc = "KDE video editor"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdenlive"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdenlive-{pkgver}.tar.xz"
sha256 = "e4306a2aa5a7535cea50aeff493ea9de8b7292d499d7204c41780cb044752f96"
# avoid crashes
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# INT: crashes spacertest/trimmingtest
hardening = ["vis", "!int"]
# TODO
# check: takes forever to build + sometimes hangs etc
options = ["!cross", "!check"]
