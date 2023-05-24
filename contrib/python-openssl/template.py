pkgname = "python-openssl"
pkgver = "23.1.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-cryptography"]
checkdepends = [
    "python-pytest",
    "python-flaky",
    "python-pretend",
    "python-cryptography",
]
pkgdesc = "Python interface to OpenSSL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://pyopenssl.org"
source = f"$(PYPI_SITE)/p/pyOpenSSL/pyOpenSSL-{pkgver}.tar.gz"
sha256 = "841498b9bec61623b1b6c47ebbc02367c07d60e0e195f19790817f10cc8db0b7"
# unpackaged checkdepends
options = ["!check"]
