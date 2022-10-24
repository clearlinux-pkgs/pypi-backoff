#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-backoff
Version  : 2.2.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/47/d7/5bbeb12c44d7c4f2fb5b56abce497eb5ed9f34d85701de869acedd602619/backoff-2.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/47/d7/5bbeb12c44d7c4f2fb5b56abce497eb5ed9f34d85701de869acedd602619/backoff-2.2.1.tar.gz
Summary  : Function decoration for backoff and retry
Group    : Development/Tools
License  : MIT
Requires: pypi-backoff-license = %{version}-%{release}
Requires: pypi-backoff-python = %{version}-%{release}
Requires: pypi-backoff-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
backoff
=======
.. image:: https://travis-ci.org/litl/backoff.svg
:target: https://travis-ci.org/litl/backoff
.. image:: https://coveralls.io/repos/litl/backoff/badge.svg
:target: https://coveralls.io/r/litl/backoff?branch=python-3
.. image:: https://github.com/litl/backoff/workflows/CodeQL/badge.svg
:target: https://github.com/litl/backoff/actions/workflows/codeql-analysis.yml
.. image:: https://img.shields.io/pypi/v/backoff.svg
:target: https://pypi.python.org/pypi/backoff
.. image:: https://img.shields.io/github/license/litl/backoff
:target: https://github.com/litl/backoff/blob/master/LICENSE

%package license
Summary: license components for the pypi-backoff package.
Group: Default

%description license
license components for the pypi-backoff package.


%package python
Summary: python components for the pypi-backoff package.
Group: Default
Requires: pypi-backoff-python3 = %{version}-%{release}

%description python
python components for the pypi-backoff package.


%package python3
Summary: python3 components for the pypi-backoff package.
Group: Default
Requires: python3-core
Provides: pypi(backoff)

%description python3
python3 components for the pypi-backoff package.


%prep
%setup -q -n backoff-2.2.1
cd %{_builddir}/backoff-2.2.1
pushd ..
cp -a backoff-2.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665066023
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-backoff
cp %{_builddir}/backoff-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-backoff/59469f232f5d88e7ef381cd91912e799324951d7 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-backoff/59469f232f5d88e7ef381cd91912e799324951d7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
