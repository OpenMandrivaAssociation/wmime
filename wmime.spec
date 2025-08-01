%define major 2
%define libname %mklibname wmime
%define devname %mklibname wmime -d

Name:		wmime
Version:	1.1.0
Release:	1
Source0:	https://github.com/grommunio/wmime/releases/download/wmime-%{version}/wmime-%{version}.tar.zst
Summary:	C++ class library for working with RFC-822/MIME messages and mail services (IMAP/POP/SMTP)
URL:		https://github.com/wmime/wmime
License:	GPL-3.0
Group:		System/Libraries
BuildRequires:	doxygen
BuildRequires:	graphviz
# Just so cmake can find the path for the sendmail executable
BuildRequires:	postfix
BuildRequires:	pkgconfig(libgsasl)
BuildRequires:	pkgconfig(gnutls)
BuildSystem:	cmake

%description
VMime is a powerful C++ class library for working with RFC-822 and MIME messages
and Internet messaging services like IMAP, POP or SMTP.

With VMime you can parse, generate and modify messages, and also connect to store
and transport services to receive or send messages over the Internet. The library
offers all the features to build a complete mail client.

wmime is a descendant project for the purpose of release targets
and is drop-in compatible with vmime.

Key Features
------------

* it is free software! GNU GPL license (Commercial licenses available!)
* fully RFC-compliant implementation
* object-oriented and modular design
* very easy-to-use (intuitive design)
* well documented code
* very high reliability
* maximum portability

Features Overview
-----------------

* RFC-2822 and multipart messages
* aggregate documents and embedded objects
* 8-bit MIME and encoded word extensions
* full support for attachments
* POP3, IMAP, SMTP, maildir and sendmail
* SSL/TLS security layer and X.509 certificates (using GNU TLS)
* SASL authentication (using GNU SASL)

%install -a
%libpackages
cat >>%{specpartsdir}/%{mklibname -d wmime}.specpart <<EOF
%{_includedir}/vmime
%{_libdir}/cmake/vmime
%{_libdir}/pkgconfig/vmime.pc
EOF
