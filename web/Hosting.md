**HOSTING**

https://w3techs.com/technologies/overview/web_hosting

Sorted from top to bottom by market share percentage


	Amazon		- 6
	Newfold Digital Group: - 4.1
		Hostgator, Bluehost, iPage
	OVH			- 3.3
	GoDaddy		- 3.1
	Hetzner		- 2.6
	Wix			- 2.5
	SiteGround	- 2.1
	DigitalOcean- 2.1
	United Internet: - 2.1
		1&1, IONOS	
	WPEngine	- 2.1
	Squarespace	- 2.1
	team.blue:	- 1.8
		PTisp, Dominios.pt
	Hostinger	- 1.7
	Namecheap	- 0.7
	Liquid Web	- 0.6
	DreamHost	- 0.5
	Vultr		- 0.4
	A2 Hosting	- 0.4
	InMotion, Vercel (Paas), Netlify (PaaS), Kinsta, Leaseweb(IaaS), Linode (VPS, acquired by Akamai), GreenGeeks, Gandi.net

Note: Most of the shared hosting providers only offer Python, Perl, Ruby using CGI/FCGI alongside the default PHP.
 *usually* mod_wsgi, mod_uwsgi or mod_passenger are not available in most shared hosting setups, but **there are exceptions**.

****************************************************************************************************************************

**Providers supporting Phusion Passenger on Shared Hosting**

**Method 1 - CloudLinux use their LVE (cgroups) solution + mod_passenger, together with cPanel, DirectAdmin or custom panel**
1. https://docs.cloudlinux.com/shared/cloudlinux_os_components/#python-selector
2. https://cloudlinux.zendesk.com/hc/en-us/sections/360004068640-Python-Ruby-NodeJS-Selectors
3. https://www.liquidweb.com/kb/python-web-applications-in-cpanel-on-cloudlinux/
4. https://blog.phusion.nl/2016/02/03/lve-an-alternative-container-technology-to-docker-and-virtuozzolxc/
5. https://www.cloudlinux.com/getting-started-with-cloudlinux-os/40-stability-features/927-lve-manager-for-cpanel/?nab=0

*CloudLinux* providing cagefs = grsecurity, lve = cgroups:
1. *cgroups* integration into cron jobs, apache, ssh, mysql --> on per user level (cgroups usually work for whole MySQL, not particular user, same with apache/cron...)
full blown set of statistics, notifications, etc... so you can show users how much they use, when they are limited, etc...
performance optimizations for shared hosting (cgroups in mainland kernel don't work well when processes enter/leave LVE hundreds of times a second)
2. *cagefs* is actually namespaces --> it makes individual shared hosting account closer to VPS from isolation standpoint. Users don't see other users.
3. Ruby/Python selector -> ability for end user to select among multiple versions of python & ruby for hosting
4. mod_lsapi -> faster way to serve PHP (in shared hosting environment). Apache mod_lsapi is a module based on LiteSpeed Technologies API for PHP.



**A2 Hosting, Passenger with cPanel:**
For shared and reseller hosting accounts:

Python Selector on cPanel and Passenger
1. https://www.a2hosting.com/kb/cpanel/cpanel-software/using-the-python-selector/

configure Django on a Linux shared hosting account that uses cPanel
2. https://www.a2hosting.com/kb/developer-corner/python/installing-and-configuring-django-on-linux-shared-hosting/

install Flask on a Linux shared hosting account that uses cPanel
3. https://www.a2hosting.com/kb/developer-corner/python/installing-and-configuring-flask-on-linux-shared-hosting/

NodeJS Selector on cPanel
4. https://www.a2hosting.com/kb/cpanel/cpanel-software/create-application-with-nodejs-selector/

For VPS and Dedicated Server accounts:
5. https://www.a2hosting.com/kb/cpanel/cpanel-software/using-the-application-manager-to-deploy-applications-with-passenger/


**Namecheap, Passenger with cPanel:**
1. https://www.namecheap.com/support/knowledgebase/article.aspx/10048/2182/how-to-work-with-python-app/
2. https://forum.djangoproject.com/t/deploying-django-app-on-namecheap/1185
3. https://www.namecheap.com/support/knowledgebase/article.aspx/129/22/what-version-of-the-software-is-used-on-your-servers/

**Method 2 - custom made solution, uses Phusion Passenger**

**DreamHost Hosting, Passenger with custom control panel (TBC on shared hosting?)**
Passenger is the preferred way to deploy and host Ruby, Python, NodeJS applications and is free on every DreamHost hosting plan.
1. https://help.dreamhost.com/hc/en-us/articles/217141627/
2. https://help.dreamhost.com/hc/en-us/articles/216137717-Python-overview
3. https://help.dreamhost.com/hc/en-us/articles/215319598-Django-overview
4. https://help.dreamhost.com/hc/en-us/articles/217185397-Node-js-overview
5. https://help.dreamhost.com/hc/en-us/sections/203812837-Passenger
6. https://help.dreamhost.com/hc/en-us/articles/216385637-Enable-Passenger-on-a-domain
7. https://help.dreamhost.com/hc/en-us/articles/215769578-Passenger-overview
8. https://help.dreamhost.com/hc/en-us/articles/216635268-Passenger-troubleshooting
9. https://help.dreamhost.com/hc/en-us/articles/360002341572-Creating-a-Django-project
10. https://gist.github.com/paulera/918e4ea000a8128719222f629905c49f


**OVH Hosting, Power Web, Passenger with custom control panel:**
1. https://help.ovhcloud.com/csm/en-ie-documentation-ovhcloud-labs-power-web-hosting-getting-started?id=kb_browse_cat&kb_id=3f28cba1551974502d4c6e78b74219df&kb_category=25341555f49801102d4ca4d466a7fd77
2. https://help.ovhcloud.com/csm/en-ie-power-web-hosting-getting-started?id=kb_article_view&sysparm_article=KB0035197
3. https://help.ovhcloud.com/csm/en-ie-documentation-ovhcloud-labs-power-web-hosting-python?id=kb_browse_cat&kb_id=3f28cba1551974502d4c6e78b74219df&kb_category=e9341555f49801102d4ca4d466a7fd78
4. https://help.ovhcloud.com/csm/en-ie-power-web-hosting-python-install-django?id=kb_article_view&sysparm_article=KB0047842
5. https://labs.ovhcloud.com/en/managed-python/
6. https://webhosting-infos.hosting.ovh.net/


**Method 3 - custom made solution, relies on a managed vps-based config**

**OVH Hosting, Cloud Web, managed VPS-based (no root access):**
1. https://cloudweb-infos.hosting.ovh.net/
2. https://www.ovhcloud.com/en-gb/web-hosting/cloud-web-offer/
3. https://help.ovhcloud.com/csm/en-ie-cloud-web-hosting-manage-runtime-software-applications?id=kb_article_view&sysparm_article=KB0051444
4. https://help.ovhcloud.com/csm/en-ie-cloud-web-hosting-install-ghost?id=kb_article_view&sysparm_article=KB0051432



**Gandi.net - managed VPS-based (no root access):**
Python uWSGI
1. https://docs.gandi.net/en/web_hosting/languages/python.html
2. https://docs.gandi.net/en/web_hosting/advanced_configurations/uwsgi.html
3. https://docs.gandi.net/en/web_hosting/languages/nodejs.html
4. https://docs.gandi.net/en/web_hosting/index.html
5. https://www.gandi.net/en/hosting/p/python

**Alternatives, any VPS providers:**
Any dedicated VPS with cPanel, Plesk, DirectAdmin or custom config...
OVH, Hetzner, DigitalOcean, Vultr, Linode, ...

**Liquidweb** uses the control panel management system called Sync Pro. you can choose cPanel as well as the Plesk.

In **GreenGeeks** you will be able to control all aspects of your VPS through their proprietary VPS management portal.
CPANEL/WHM License Included. In GreenGeeks your VPS will come pre-installed with cPanel/WHM.


****************************************************************************************************************************

**CPANEL:**
1. https://docs.cpanel.net/cpanel/software/application-manager/
This interface allows you to deploy applications with the Phusion Passenger® application server. A Phusion Passenger server functions as a process manager, reverse proxy, and provides operations tools to its users.
2. https://www.youtube.com/watch?v=zSLxOjtp89Y
3. https://docs.cpanel.net/knowledge-base/web-services/how-to-install-a-python-wsgi-application/

Before you install cPanel & WHM or cPanel DNSOnly®, make certain that your system meets all of our minimum requirements. 
cPanel & WHM supports the following operating systems:
	System Requirements for AlmaLinux OS
	System Requirements for Rocky Linux
	System Requirements for Ubuntu
https://docs.cpanel.net/installation-guide/system-requirements-ubuntu/

****************************************************************************************************************************

**DirectAdmin:**

1. https://directadmin.com/features_list.php
2. https://docs.directadmin.com/
3. https://docs.directadmin.com/getting-started/installation/installguide.html
4. https://docs.directadmin.com/getting-started/first-steps/what-makes-da-unique.html
5. https://operavps.com/docs/install-directadmin-on-debian/
6. https://operavps.com/docs/install-directadmin-on-almalinux/
7. https://docs.directadmin.com/webservices/nginx_unit/



1. Nginx Unit
We've been working hard to bring you Nginx Unit! A dream come true for polyglots, the Nginx Unit application server supports the following languages:

Perl, PHP, Python, Ruby, Java, 
Upcoming: Go, Node.js

Nginx Unit allows you to run different versions of the same language, can deploy configuration changes without interruptions to services, and can run alongside any webserver. Several popular frameworks and web applications run seamlessly with Nginx Unit, including frameworks such as Django, Express, Flask, and Laravel, and webapps including WordPress, Joomla, Drupal, Jira, phpBB, and MediaWiki amongst several others.

We use *Nginx Unit* to support multiple languages, while the competition usually utilizes *Phusion Passenger* for this purpose. Nginx Unit offers features that just aren't available with Passenger. Some of the benefits of Nginx Unit when compared to Phusion Passenger include:

*Multithreading (applications can use multiple cores)*
Native support for many languages not supported by Passenger (Java, Go, Assembly, Perl, and PHP).
Support of Linux namespaces and chroot natively to isolate the users/applications from each other. Namespace and file system isolation is available for operating systems that support it. You also have a choice between static or dynamic process management. More information here.
*Feature-rich.* Nginx Unit as a standalone server supports routing, proxying and some other 'common webserver' features, such as HTTP/2 support. HTTP rewrites are planned. Proxying requests and load balancing by defining upstream servers is also possible. You can even serve Nginx in front of Unit to secure the Unit Control Socket (if you require the Control Socket to be accessible remotely, that is).
ASGI support for Python. With ASGI, processing becomes asynchronous in Python. It lets you achieve high throughput in IO-bound contexts. Additionally, it fully supports *WebSockets*,which are bidirectional, low-latency, persistent connections between the server and the client that allows either participant to send messages at any time without the overhead of HTTP. Websockets are supported currently for Node.js, Java, and Python. Websocket support is planned for Ruby, Go, Perl, and PHP.
*Nginx Templates for shared webhosting*
Nginx has no support for .htaccess, thus friendly-URLs do not work automatically. DirectAdmin officially supports Nginx Templates to support most common CMS (content management system) applications with a single click. Select "WordPress", "Drupal" or some other CMS from drop-down, save the selection and that's it! It also has an API available, so, plugins like Installatron or Softaculous could have it integrated easily and make it work automatically after the installation of a new application.

2. *OpenLiteSpeed* webserver support
OpenLiteSpeed is the Open Source edition of LiteSpeed Web Server Enterprise. OpenLiteSpeed contains all of the essential features found in LiteSpeed Enterprise, including LiteSpeed cache support for common content management systems like WordPress, Joomla or OpenCart. See some benchmarks here conveying how well LScache performs. It offers .htaccess support for URL rewrites, and DirectAdmin offers a way to re-load OpenLiteSpeed automatically if any .htaccess changes are detected.
2.1. https://docs.litespeedtech.com/lsws/cp/directadmin/

3. Bubblewrap/JailShell
Better security is provided by using a *bubblewrap* for PHP, SSH, and crons, which actually does 'lock' a user in their own file system. This serves as an alternative solution to CageFS for those not using CloudLinux.
3.1. https://docs.litespeedtech.com/lsws/bubblewrap/

4. cgroups
4.1. https://docs.litespeedtech.com/lsws/cgroups/
4.2. https://openlitespeed.org/kb/using-cgroups-v2-with-openlitespeed/
4.3. https://docs.directadmin.com/operation-system-level/os-general/user_cgroups.html
4.4. https://docs.directadmin.com/other-hosting-services/pro-resource-throttling/
4.5. https://www.cloudlinux.com/getting-started-with-cloudlinux-os/40-stability-features/927-lve-manager-for-cpanel/?nab=0

5. UPDATE: As of 2023 August, DirectAdmin has switched to a unified codebase where all licenses for sale automatically contain all features. The "Pro Pack" concept is now retired.


****************************************************************************************************************************

**PLESK:**

Node.js:
1. https://www.plesk.com/blog/product-technology/node-js-plesk-onyx/
2. https://www.plesk.com/extensions/node-js/

Python:
1. https://support.plesk.com/hc/en-us/articles/12377801128087  (mode_python deprecated)
2. https://support.plesk.com/hc/en-us/articles/12377591003415  (Apache mod_WSGI)
3. https://www.plesk.com/blog/product-technology/plesk-and-django/  (2014, Plesk 12, Passenger, python 2)
4. https://www.plesk.com/blog/guides/django-hosting-latest-plesk-onyx/  (2019, Pleask 17, Apache directives, Passenger, Python 3.x)
5. https://support.plesk.com/hc/en-us/articles/12377516625559  (Apache mod_passenger, Phusion Passenger, Python 3.x, Django)
Follow the tutorial to activate WSGI support with Phusion Passenger. 
Follow Passenger tutorial to deploy/restart applications.
Use Git and Ansible to deploy the application via SSH, install the requirements and restart the app.
Configure a dedicated domain in plesk for the app, like any other site in the Websites & Domains overview.

https://www.plesk.com/blog/product-technology/how-to-use-cgroups-manager-increase-website-performance-through-resource-isolation-linux/
Cgroups Manager is currently available for Linux: Debian 10, 11, Ubuntu 20.04 and AlmaLinux 8 – supported by Plesk.
Cgroups Manager does not account and limit resources for Ruby, Python, and Node.js web-applications using the Phusion Passenger.

https://docs.plesk.com/release-notes/obsidian/software-requirements/
Commonly supported Linux 64-bit operating systems for Plesk include:
	AlmaLinux 8, 9 
	Rocky Linux 8
	Ubuntu 22
	Debian 11

1. https://support.plesk.com/hc/en-us
2. https://support.plesk.com/hc/en-us/articles/12377600194583-How-to-secure-a-Plesk-server
3. https://www.plesk.com/blog/product-technology/recommended-operating-systems-for-plesk/
4. https://support.plesk.com/hc/en-us/articles/12377657599383-How-to-install-Plesk-for-Linux-
5. https://docs.plesk.com/en-US/obsidian/deployment-guide/quick-start.76607/
6. https://www.plesk.com/content-contributor-program/

Plesk and cgroups:
7. https://www.plesk.com/blog/product-technology/how-to-use-cgroups-manager-increase-website-performance-through-resource-isolation-linux/
8. https://docs.plesk.com/en-US/obsidian/administrator-guide/plesk-administration/plesk-for-linux-cgroups-manager.78308/
9. https://www.plesk.com/blog/product-technology/plesk-docker-extension/


****************************************************************************************************************************

**PaaS options:
https://kinsta.com/application-hosting/pricing/
OVH, ...



****************************************************************************************************************************

**AlmaLinux OS**

https://docs.hetzner.com/robot/dedicated-server/operating-systems/standard-images/


https://www.redswitches.com/blog/almalinux-vs-rocky-linux/
Package Managers:
dnf is the default built-in package manager for AlmaLinux. 
On the other hand, the Rocky Linux team decided to opt for the standard RPM.
AlmaLinux decided to include dnf, the “successor” to the more familiar yum to enhance the “cutting edge” of the distro. 
In contrast, Rocky Linux decided to keep things traditional and use RPM to better align it to other RHEL distros.

Security:
Users of AlmaLinux can customize their system security thanks to the inclusion of the Center for Internet Security (CIS) Benchmark. The benchmark includes a CIS-CAT tool that generates comprehensive reports on potential security problems.
The OpenSCAP program, which automatically scans the system for vulnerabilities, is also included with AlmaLinux. The OpenSCAP Workbench app or the console can access the tool.
With its 2.6 kernel, Rocky Linux now uses the new security mechanism SELinux (Security Enhanced Linux). The National Security Agency (NSA) developed SELinux to implement a strong MAC (Mandatory Access Control) architecture.

https://fossforce.com/2023/08/the-almalinux-dilemma-when-upstream-suddenly-disappears/

The future of AlmaLinux OS:
Red Hat announced (June 2023) they will no longer be providing the means for downstream clones to continue to be 1:1 binary copies of Red Hat Enterprise Linux (RHEL). The AlmaLinux OS Foundation board today (July 2023) has decided to drop the aim to be 1:1 binary compatible with RHEL. AlmaLinux OS will instead aim to be Application Binary Interface (ABI) compatible.


SUSE said that it was spending $10 million to develop a line-by-line clone of RHEL and to create a foundation that will make the code freely available to whomever wants to use it. Then SUSE, Rocky Linux, and Oracle announced a partnership to make this vision a reality.

https://www.suse.com/news/OpenELA-for-a-Collaborative-and-Open-Future/
CIQ, Oracle and SUSE today announced their intent to form the Open Enterprise Linux Association (OpenELA), a collaborative trade association to encourage the development of distributions compatible with Red Hat Enterprise Linux (RHEL) by providing open and free Enterprise Linux (EL) source code.
https://openela.org/about/


****************************************************************************************************************************

**Phusion Passenger:**
*random notes from the internet, some might be outdated*

https://stackoverflow.com/questions/tagged/passenger

Passenger wsgi-loader.py:
the Python app checks whether it is running under the correct Python interpreter, and if not, re-executes itself under the correct Python interpreter.
However, before Phusion Passenger ever loads your app, it first runs a "loader" application (wsgi-loader.py) (ex., "/nginx/passenger/helper-scripts/wsgi-loader.py") which sets up the environment for your app. 
And it is that loader application that requires Python >= 2.6. 

So the re-execution trick only works properly if the Python that was used to run the loader, is >= 2.6. (At your service provider, that's apparently not the case.)
The correct way to run your app under a different Python is not by re-executing itself, but by using the PassengerPython configuration
option inside the web server:
**If your provider gives you access to the Apache vhost.conf config file, you can set it there directly.**
If they don't, then you *might* still be able to customize it through .htaccess, assuming that you are allowed to do this through 'AllowOverride' on the default config.
Otherwise, you might want to consider switching provider.

***

1. https://web.archive.org/web/20160109124040/http://wiki.dreamhost.com/Passenger
2. https://web.archive.org/web/20160128110355/http://wiki.dreamhost.com/Django
3. https://web.archive.org/web/20151025025433/http://wiki.dreamhost.com/Python_FastCGI
4. https://web.archive.org/web/20160403001106/http://wiki.dreamhost.com/Passenger_Troubleshooting
5. https://gist.github.com/paulera/918e4ea000a8128719222f629905c49f


***
The "public" subdirectory:
Passenger maps the directory named "public" to be the document root for your domain/subdomain.
If a static HTML file named "public/index.html" exists, it's then used as the response for requests for the root document (i.e., "/").
If you want your application to handle requests for the root document, then you must first remove "public/index.html" (if it exists).
By default, Ruby on Rails creates a static "public/index.html" file.
Likewise, a file inside the "public" subdirectory that is named with one of the suffixes recognized by Apache (e.g., "public/foo.cgi" or "public/foo.pl", "public/foo.php") will be treated as an executable CGI script in the usual Apache fashion.

***
Basic operation
The following are the basic actions that take place once a file is requested from a domain running Passenger and Ruby on Rails:
When a request is made to a domain/subdomain (vhost), the Apache HTTP Server passes the request to Passenger.
Passenger first looks for an appropriately-named HTML or CGI file (Index files)  in the domain/subdomain's /public subdirectory.
If no matching file is found, the request is passed to Passenger's Rack interface.
In order to generate a response, Rack looks for a file named "config.ru" in the domain/subdomain's root directory (i.e., the parent of the domain's /public subdirectory, one level up from the /public dir).
Rack requires that you place the appropriate Ruby code into "config.ru" to invoke your desired web framework or application to handle the request.
When running a RoR application, the only Rack-related files you are likely to modify are possibly adding GEM_PATH information to "config.ru" and "touching" the "tmp/restart.txt" file.

***
Use of Passenger vs. FastCGI
Passenger should only be enabled if you intend to run a Ruby on Rails (RoR) or other Ruby/Python-based program as the sole application for the entire (vhost) domain or subdomain. Passenger directs all requests for the designated domain/subdomain to the associated Rack-compliant application. So it's best to leave Passenger disabled if you do not actually need it. It's not possible to have Passenger enabled to run Ruby/Python apps and to keep PHP enabled for the same vhost as well, it's one language (Python, Ruby, PHP) per vhost.
If you want to access your application via www.example.com/path-to-myapp then use FastCGI instead of Passenger (update - now supports PassengerBaseURI).

***
A couple of technical notes
Output to STDERR for processes run through the Rack interface is directed to the master Apache error log file rather than the domain/subdomain specific log file. You do not have direct access to the master log file. This limitation can make debugging initialization errors (in particular syntax errors and gem resolution issues) tricky. 
Passenger will often produce an error output webpage including a stack traceback. However, in some cases it does not. If you have a persistent problem and Passenger is not producing sufficiently useful error output, you can try contacting the DreamHost support staff and ask them to examine the master log file for you. Once a framework (such as RoR) is up and running, its error output is typically handled by the framework's own error logging mechanism. For example, RoR records its error output in a file named "log/production.log".

Activating Passenger on a domain will break the phpMyAdmin (PHP) on any subdomain under the domain. To use phpMyAdmin and Passenger, you must have a non-Passenger-enabled domain with an active phpMyAdmin. (update - TBC ? - Passenger can be set to PassengerEnable off in subdirectories)

In the interest of ease of use and 'Upload and Go' functionality, Passenger disables some mod_rewrite functionality. That means it will automatically override an existing 'dispatch.fcgi' setup you have in place. This is not a problem for your Rails application but it may have other side effects (such as breaking other mod_rewrite rules you have set up). If this causes a problem for your website, try using the FastCGI method.

Passenger automatically launches applications and leaves them running as long as they are not idle. It also caches the code for Ruby on Rails itself to speed up application launching.

***


