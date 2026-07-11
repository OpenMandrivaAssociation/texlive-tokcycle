%global tl_name tokcycle
%global tl_revision 74841

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Build tools to process tokens from an input stream
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/tokcycle
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tokcycle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tokcycle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The tokcycle package helps one to build tools to process tokens from an
input stream. If a macro to process an arbitrary single token can be
built, then tokcycle can provide a wrapper for cycling through an input
stream (including macros, spaces, and groups) on a token-by-token basis,
using the provided macro on each successive character. tokcycle
characterizes each successive token in the input stream as a Character,
a Group, a Macro, or a Space. Each of these token categories are
processed with a unique directive, to bring about the desired effect of
the token cycle. If condition flags are provided to identify active,
implicit, and catcode-6 tokens as they are digested. The package
provides a number of options for handling groups.

