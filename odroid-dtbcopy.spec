Name:           odroid-dtbcopy
Version:        0.1.0
Release:        1%{?dist}
Summary:        Script to copy device tree blobs to the u-boot root

Group:          System Environment/Base
License:        BSD
URL:            http://csc.mcs.sdsmt.edu
Source0:        dtbcopy

BuildArch:      noarch

%description
This script installs a post-install hook for kernel packages which copies any
device tree blobs (*.dtb files) which come with the kernel to the uboot
directory so that they may be loaded by uboot with the kernel.

%prep

%build

%install
install -D -m0755 -p %{SOURCE0} %{buildroot}%{_sysconfdir}/kernel/postinst.d/dtbcopy

%files
%dir %{_sysconfdir}/kernel/
%dir %{_sysconfdir}/kernel/postinst.d/
%{_sysconfdir}/kernel/postinst.d/dtbcopy

%changelog
* Fri May 01 2015 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Initial package
