pkgname = "podman"
pkgver = "4.8.1"
pkgrel = 0
build_style = "go"
make_build_args = ["-mod", "vendor", "./cmd/podman", "./cmd/rootlessport"]
hostmakedepends = [
    "bash",
    "ggrep",
    "gmake",
    "go",
    "go-md2man",
    "mandoc",
    "python",
    "pkgconf",
]
makedepends = [
    "device-mapper-devel",
    "gpgme-devel",
    "libassuan-devel",
    "libbtrfs-devel",
    "libseccomp-devel",
    "sqlite-devel",
]
depends = [
    "aardvark-dns",
    "cni-plugins",
    "conmon",
    "containers-common",
    "fuse-overlayfs",
    "iptables",
    "netavark",
    "oci-runtime",
    "slirp4netns",
]
go_build_tags = [
    "apparmor",
    "containers_image_openpgp",
    "containers_image_ostree_stub",
    "seccomp",
]
pkgdesc = "Container and image management tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://podman.io"
source = f"https://github.com/containers/podman/archive/v{pkgver}.tar.gz"
sha256 = "d09697ed01cdc5c36069344b0ec2fdd26065554ff071e61a4701d31f008f0398"
# objcopy fails to split on ppc
options = ["!debug", "!check"]


def post_build(self):
    self.do("gmake", "docs", "GREP=ggrep", "GOMD2MAN=/usr/bin/go-md2man")


def post_install(self):
    self.install_service(self.files_path / "podman")
    self.install_service(self.files_path / "podman-docker")
    self.install_file(
        self.files_path / "podman-docker.libexec",
        "usr/libexec",
        name="podman-docker",
        mode=0o755,
    )
    self.install_dir("usr/libexec/podman")
    self.mv(
        self.destdir / "usr/bin/rootlessport",
        self.destdir / "usr/libexec/podman",
    )
    self.do(
        "gmake", "install.man", "PREFIX=/usr", f"DESTDIR={self.chroot_destdir}"
    )
    self.do(
        "gmake",
        "install.completions",
        "PREFIX=/usr",
        f"DESTDIR={self.chroot_destdir}",
    )
