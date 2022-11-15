Name:		texlive-ctan_chk
Version:	36304
Release:	1
Summary:	CTAN guidelines verifier and corrector for uploading projects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ctan_chk
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctan_chk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctan_chk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Basic gawk program that uses CTAN's published guidelines for
authors to help eliminate sloppiness in uploaded
files/projects. It is completely open for users to program
additional guidelines as well as CTAN's future adjustments.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/support/ctan_chk

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
