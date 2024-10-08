pkgname = "perl-mailtools"
pkgver = "2.21"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl", "perl-timedate"]
depends = ["perl", "perl-timedate"]
pkgdesc = "Various e-mail related modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/MailTools"
source = f"$(CPAN_SITE)/Mail/MailTools-{pkgver}.tar.gz"
sha256 = "4ad9bd6826b6f03a2727332466b1b7d29890c8d99a32b4b3b0a8d926ee1a44cb"
