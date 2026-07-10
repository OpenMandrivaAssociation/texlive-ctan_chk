%global tl_name ctan_chk
%global tl_revision 36304

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	CTAN guidelines verifier and corrector for uploading projects
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/ctan_chk
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctan_chk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctan_chk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Basic gawk program that uses CTAN's published guidelines for authors to
help eliminate sloppiness in uploaded files/projects. It is completely
open for users to program additional guidelines as well as CTAN's future
adjustments.

