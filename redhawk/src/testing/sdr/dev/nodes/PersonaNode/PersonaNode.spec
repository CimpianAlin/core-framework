#
# This file is protected by Copyright. Please refer to the COPYRIGHT file
# distributed with this source distribution.
#
# This file is part of REDHAWK core.
#
# REDHAWK core is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# REDHAWK core is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#
# RPM package for PersonaNode
# This file is regularly AUTO-GENERATED by the IDE. DO NOT MODIFY.

# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
# You can override this at install time using --prefix /new/sdr/root when invoking rpm (preferred method, if you must)
%{!?_sdrroot: %define _sdrroot /var/redhawk/sdr}
%define _prefix %{_sdrroot}
Prefix: %{_prefix}

Name: PersonaNode
Summary: Node PersonaNode
Version: 1.0.0
Release: 1
License: None
Group: REDHAWK/Nodes
Source: %{name}-%{version}.tar.gz
# Require the device manager whose SPD is referenced
Requires: DeviceManager
# Require each referenced device/service
Requires: PersonaDevice ProgrammableDevice
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description

%prep
%setup

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p "$RPM_BUILD_ROOT%{_prefix}/dev/nodes/%{name}"
%__install -m 644 DeviceManager.dcd.xml $RPM_BUILD_ROOT%{_prefix}/dev/nodes/%{name}/DeviceManager.dcd.xml

%files
%defattr(-,redhawk,redhawk)
%dir %{_prefix}/dev/nodes/%{name}
%{_prefix}/dev/nodes/%{name}/DeviceManager.dcd.xml
