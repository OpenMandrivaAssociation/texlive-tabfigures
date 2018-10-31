# revision 25202
# category Package
# catalog-ctan /macros/latex/contrib/tabfigures
# catalog-date 2012-01-25 23:45:22 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-tabfigures
Version:	1.1
Release:	10
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


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 770283
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756427
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719633
- texlive-tabfigures
- texlive-tabfigures
- texlive-tabfigures

