# revision 24025
# category Package
# catalog-ctan /macros/latex/contrib/tabfigures
# catalog-date 2011-09-19 11:41:25 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-tabfigures
Version:	1.0
Release:	1
Summary:	Maintain vertical alignment of figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabfigures
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabfigures.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabfigures.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabfigures.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Knuth designed his original fonts with tabular figures (figures
whose width is uniform); this makes some layout problems rather
simple. In more recent times, fonts (such as Minion Pro), which
offer proportionally spaced figures, are increasingly being
used. The package provides mechanisms whereby such proportional
figures may still be aligned in tabular style (for example, in
the table of contents).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabfigures/tabfigures.sty
%doc %{_texmfdistdir}/doc/latex/tabfigures/README
%doc %{_texmfdistdir}/doc/latex/tabfigures/tabfigures.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tabfigures/tabfigures.dtx
%doc %{_texmfdistdir}/source/latex/tabfigures/tabfigures.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
