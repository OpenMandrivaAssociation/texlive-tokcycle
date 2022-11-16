Name:		texlive-tokcycle
Version:	60320
Release:	1
Summary:	Build tools to process tokens from an input stream
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tokcycle
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tokcycle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tokcycle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tokcycle package helps one to build tools to process tokens
from an input stream. If a macro to process an arbitrary single
token can be built, then tokcycle can provide a wrapper for
cycling through an input stream (including macros, spaces, and
groups) on a token-by-token basis, using the provided macro on
each successive character. tokcycle characterizes each
successive token in the input stream as a Character, a Group, a
Macro, or a Space. Each of these token categories are processed
with a unique directive, to bring about the desired effect of
the token cycle. If condition flags are provided to identify
active, implicit, and catcode-6 tokens as they are digested.
The package provides a number of options for handling groups.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/tokcycle
%doc %{_texmfdistdir}/doc/generic/tokcycle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
