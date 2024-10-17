Name:		texlive-tabfigures
Version:	25202
Release:	2
Summary:	Maintain vertical alignment of figures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabfigures
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabfigures.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabfigures.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabfigures.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
