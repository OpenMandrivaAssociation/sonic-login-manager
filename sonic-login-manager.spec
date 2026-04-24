Name:      sonic-login-manager
Version:   6.6.3
Release:   1
License:   GPL-2.0
URL:       https://github.com/Sonic-DE/sonic-login-manager
Summary:   Display Manager for SonicDE
Source0:   %url/archive/%version/%name-%version.tar.gz
Source1:   sonic-login-manager.pam
Source2:   sonic-login-manager-autologin.pam

BuildSystem:  cmake
BuildOption:  -DUID_MIN=1000
BuildOption:  -DUID_MAX=60000
BuildOption:  -DINSTALL_PAM_CONFIGURATION:BOOL=OFF

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6ShaderTools)

BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)

BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(xau)

BuildRequires: %{_lib}SonicFrameworksWindowSystem-devel
BuildRequires: %{_lib}SonicFrameworksAuth-devel
BuildRequires: %{_lib}SonicFrameworksIO-devel
BuildRequires: %{_lib}SonicDE-devel
BuildRequires: %{_lib}SonicDEScreen-devel
BuildRequires: %{_lib}sonic-workspace-devel

BuildRequires: pam pkgconfig gettext

# For /etc/X11/Xsession
Requires: xinitrc
%systemd_requires
Provides: dm

%description
%summary

%install -a 
install -Dpcm 644 %{S:1} %{buildroot}%{_sysconfdir}/pam.d/sonic-login-manager
install -Dpcm 644 %{S:2} %{buildroot}%{_sysconfdir}/pam.d/sonic-login-manager-autologin

%files -f %name.lang
%doc README.md
%{_bindir}/plasma-login-wallpaper
%{_bindir}/plasmalogin
%{_bindir}/startplasma-login-x11
%{_unitdir}/plasmalogin.service
%{_userunitdir}/plasma-login-kwin_x11.service
%{_userunitdir}/plasma-login-x11.target
%{_userunitdir}/plasma-login.service
%{_userunitdir}/plasma-wallpaper.service
%{_sysusersdir}/plasmalogin.conf
%{_tmpfilesdir}/plasmalogin.conf
%{_sysconfdir}/pam.d/%name
%{_sysconfdir}/pam.d/%name-autologin
%{_libdir}/libexec/kf6/kauth/kcmplasmalogin_authhelper
%{_libdir}/libexec/plasma-login-greeter
%{_libdir}/libexec/plasmalogin-helper
%{_libdir}/libexec/plasmalogin-helper-start-x11user
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_plasmalogin.so
%{_datadir}/applications/kcm_plasmalogin.desktop
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmplasmalogin.service
%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmplasmalogin.conf
%{_datadir}/plasmalogin/scripts/Xsession
%{_datadir}/plasmalogin/scripts/Xsetup
%{_datadir}/plasmalogin/scripts/Xstop
%{_datadir}/plasmalogin/scripts/wayland-session
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmplasmalogin.policy

