default_device_network = [
    {
        "nodes": [
            {
                "type": "Network",
                "name": "Enterprise Network",
                "id": "#73:0",
                "globalId": "ENT-NETWORK"
            },
            {
                "type": "Device",
                "name": "Hacker",
                "id": "#53:0",
                "platform": "Linux",
                "os": "Kali",
                "external": True,
                "ipAddress": "62.252.60.104",
                "facility": "",
                "unit": "",
                "machineClass": "Laptop",
                "function": "Attack",
                "globalId": "d1"
            },
            {
                "type": "Device",
                "name": "Switch",
                "id": "#53:1",
                "platform": "Cisco",
                "os": "Catalyst-2970",
                "external": False,
                "ipAddress": "172.1.1.1",
                "facility": "",
                "unit": "",
                "machineClass": "Switch",
                "function": "Switch",
                "globalId": "d4"
            },
            {
                "type": "Software",
                "name": "Router Firmware",
                "id": "#58:0",
                "platform": "Cisco",
                "os": "Cisco 12000",
                "vendor": "cisco",
                "product": "12000_router"
            },
            {
                "type": "Software",
                "name": "Rejetto HTTP File Server",
                "id": "#58:1",
                "platform": "Windows",
                "os": "Windows Server 2012",
                "vendor": "rejetto",
                "product": "http_file_server"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#56:2",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.1.61",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d8"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#56:3",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.1.64",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d11"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#56:4",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.1.67",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d14"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#56:5",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.45",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d17"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#56:6",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.48",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d20"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#56:7",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.51",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d23"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#56:8",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.54",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d26"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#57:8",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.55",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d27"
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2001-0865",
                "id": "#64:1",
                "integrityImpact": "PARTIAL",
                "confidentialityImpact": "PARTIAL",
                "availabilityImpact": "PARTIAL",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.ciac.org/ciac/bulletins/m-018.shtml, http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml, http://www.securityfocus.com/bid/3540, http://xforce.iss.net/static/7552.php]",
                "summary": "Cisco 12000 with IOS 12.0 and line cards based on Engine 2 does not support the \"fragment\" keyword in an outgoing ACL, which could allow fragmented packets in violation of the intended access.",
                "cvss": 7.5
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2011-0396",
                "id": "#64:2",
                "integrityImpact": "NONE",
                "confidentialityImpact": "COMPLETE",
                "availabilityImpact": "NONE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.cisco.com/en/US/products/products_security_advisory09186a0080b6e14d.shtml, http://www.securitytracker.com/id?1025108, http://www.vupen.com/english/advisories/2011/0493, http://xforce.iss.net/xforce/xfdb/65591]",
                "summary": "Cisco Adaptive Security Appliances (ASA) 5500 series devices with software 8.0 before 8.0(5.23), 8.1 before 8.1(2.49), 8.2 before 8.2(4.1), and 8.3 before 8.3(2.13), when a Certificate Authority (CA) is configured, allow remote attackers to read arbitrary files via unspecified vectors, aka Bug ID CSCtk12352.",
                "cvss": 7.8
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2010-2815",
                "id": "#64:3",
                "integrityImpact": "NONE",
                "confidentialityImpact": "NONE",
                "availabilityImpact": "COMPLETE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.cisco.com/en/US/products/products_security_advisory09186a0080b3f12f.shtml, http://www.securityfocus.com/bid/42198]",
                "summary": "Unspecified vulnerability in the Transport Layer Security (TLS) implementation on Cisco Adaptive Security Appliances (ASA) 5500 series devices with software 7.2 before 7.2(5), 8.0 before 8.0(5.15), 8.1 before 8.1(2.44), 8.2 before 8.2(2.17), and 8.3 before 8.3(1.6) and Cisco PIX Security Appliances 500 series devices allows remote attackers to cause a denial of service (device reload) via a sequence of crafted TLS packets, aka Bug ID CSCtf55259.",
                "cvss": 7.8
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2005-4258",
                "id": "#64:4",
                "integrityImpact": "NONE",
                "confidentialityImpact": "NONE",
                "availabilityImpact": "COMPLETE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.securityfocus.com/bid/15864, http://xforce.iss.net/xforce/xfdb/44543]",
                "summary": "Unspecified Cisco Catalyst Switches allow remote attackers to cause a denial of service (device crash) via an IP packet with the same source and destination IPs and ports, and with the SYN flag set (aka LanD). NOTE: the provenance of this issue is unknown; the details are obtained solely from the BID.",
                "cvss": 7.8
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2015-0063",
                "id": "#64:5",
                "integrityImpact": "COMPLETE",
                "confidentialityImpact": "COMPLETE",
                "availabilityImpact": "COMPLETE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "MEDIUM",
                "references": "[http://secunia.com/advisories/62808, http://technet.microsoft.com/security/bulletin/MS15-012, http://www.securityfocus.com/bid/72460, http://www.securitytracker.com/id/1031720, http://xforce.iss.net/xforce/xfdb/100439]",
                "summary": "Microsoft Excel 2007 SP3; the proofing tools in Office 2010 SP2; Excel 2010 SP2; Excel 2013 Gold, SP1, and RT; Excel Viewer; and Office Compatibility Pack SP3 allow remote attackers to execute arbitrary code or cause a denial of service (memory corruption) via a crafted Office document, aka \"Excel Remote Code Execution Vulnerability.\"",
                "cvss": 9.3
            },
            {
                "type": "Device",
                "name": "Router",
                "id": "#56:0",
                "platform": "Cisco",
                "os": "Cisco 12000",
                "external": False,
                "ipAddress": "172.0.0.5",
                "facility": "",
                "unit": "",
                "machineClass": "Modem",
                "function": "Modem",
                "globalId": "d2"
            },
            {
                "type": "Device",
                "name": "Switch",
                "id": "#56:1",
                "platform": "Cisco",
                "os": "Catalyst-2970",
                "external": False,
                "ipAddress": "172.1.2.1",
                "facility": "",
                "unit": "",
                "machineClass": "Switch",
                "function": "Switch",
                "globalId": "d5"
            },
            {
                "type": "Software",
                "name": "Firewall Firmware",
                "id": "#59:0",
                "platform": "Cisco",
                "os": "ASA 5505",
                "vendor": "cisco",
                "product": "asa_5505"
            },
            {
                "type": "Software",
                "name": "Microsoft Office Excel 2013 RT",
                "id": "#59:1",
                "platform": "Windows",
                "os": "Windows 7",
                "vendor": "microsoft",
                "product": "excel_2013_rt"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#57:2",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.1.62",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d9"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#57:3",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.1.65",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d12"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#57:4",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.43",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d15"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#57:5",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.46",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d18"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#57:6",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.49",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d21"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#57:7",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.52",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d24"
            },
            {
                "type": "Software",
                "name": "Rootkit",
                "id": "#60:1",
                "platform": "Windows",
                "os": "Windows 7",
                "vendor": "Cr4ashers",
                "product": "Rootkit"
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2001-0867",
                "id": "#65:0",
                "integrityImpact": "PARTIAL",
                "confidentialityImpact": "PARTIAL",
                "availabilityImpact": "PARTIAL",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.ciac.org/ciac/bulletins/m-018.shtml, http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml, http://www.securityfocus.com/bid/3538, http://xforce.iss.net/static/7555.php]",
                "summary": "Cisco 12000 with IOS 12.0 and line cards based on Engine 2 does not properly filter does not properly filter packet fragments even when the \"fragment\" keyword is used in an ACL, which allows remote attackers to bypass the intended access controls.",
                "cvss": 7.5
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2001-0864",
                "id": "#65:1",
                "integrityImpact": "PARTIAL",
                "confidentialityImpact": "PARTIAL",
                "availabilityImpact": "PARTIAL",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.ciac.org/ciac/bulletins/m-018.shtml, http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml, http://www.securityfocus.com/bid/3536, http://xforce.iss.net/static/7553.php]",
                "summary": "Cisco 12000 with IOS 12.0 and line cards based on Engine 2 does not properly handle the implicit \"deny ip any any\" rule in an outgoing ACL when the ACL contains exactly 448 entries, which can allow some outgoing packets to bypass access restrictions.",
                "cvss": 7.5
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2011-0395",
                "id": "#65:2",
                "integrityImpact": "NONE",
                "confidentialityImpact": "NONE",
                "availabilityImpact": "COMPLETE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.cisco.com/en/US/products/products_security_advisory09186a0080b6e14d.shtml, http://www.securitytracker.com/id?1025108, http://www.vupen.com/english/advisories/2011/0493, http://xforce.iss.net/xforce/xfdb/65590]",
                "summary": "Cisco Adaptive Security Appliances (ASA) 5500 series devices with software 8.0 before 8.0(5.20), 8.1 before 8.1(2.48), 8.2 before 8.2(3), and 8.3 before 8.3(2.1), when the RIP protocol and the Cisco Phone Proxy functionality are configured, allow remote attackers to cause a denial of service (device reload) via a RIP update, aka Bug ID CSCtg66583.",
                "cvss": 7.8
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2010-1578",
                "id": "#65:3",
                "integrityImpact": "NONE",
                "confidentialityImpact": "NONE",
                "availabilityImpact": "COMPLETE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.cisco.com/en/US/products/products_security_advisory09186a0080b3f12f.shtml]",
                "summary": "Unspecified vulnerability in the SunRPC inspection feature on Cisco Adaptive Security Appliances (ASA) 5500 series devices with software 7.2 before 7.2(5), 8.0 before 8.0(5.19), 8.1 before 8.1(2.47), and 8.2 before 8.2(2) and Cisco PIX Security Appliances 500 series devices allows remote attackers to cause a denial of service (device reload) via crafted SunRPC UDP packets, aka Bug ID CSCtc77567.",
                "cvss": 7.8
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2014-6287",
                "id": "#65:4",
                "integrityImpact": "PARTIAL",
                "confidentialityImpact": "PARTIAL",
                "availabilityImpact": "PARTIAL",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://packetstormsecurity.com/files/128243/HttpFileServer-2.3.x-Remote-Command-Execution.html, http://packetstormsecurity.com/files/135122/Rejetto-HTTP-File-Server-2.3.x-Remote-Code-Execution.html, http://www.kb.cert.org/vuls/id/251276, https://github.com/rapid7/metasploit-framework/pull/3793, https://www.exploit-db.com/exploits/39161/]",
                "summary": "The findMacroMarker function in parserLib.pas in Rejetto HTTP File Server (aks HFS or HttpFileServer) 2.3x before 2.3c allows remote attackers to execute arbitrary programs via a %00 sequence in a search action.",
                "cvss": 7.5
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2013-1315",
                "id": "#65:5",
                "integrityImpact": "COMPLETE",
                "confidentialityImpact": "COMPLETE",
                "availabilityImpact": "COMPLETE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "MEDIUM",
                "references": "[http://technet.microsoft.com/security/bulletin/MS13-067, http://technet.microsoft.com/security/bulletin/MS13-073, http://www.us-cert.gov/ncas/alerts/TA13-253A]",
                "summary": "Microsoft SharePoint Server 2007 SP3, 2010 SP1 and SP2, and 2013; Office Web Apps 2010; Excel 2003 SP3, 2007 SP3, 2010 SP1 and SP2, 2013, and 2013 RT; Office for Mac 2011; Excel Viewer; and Office Compatibility Pack SP3 allow remote attackers to execute arbitrary code or cause a denial of service (memory corruption) via a crafted Office document, aka \"Microsoft Office Memory Corruption Vulnerability.\"",
                "cvss": 9.3
            },
            {
                "type": "Device",
                "name": "Maintenance Laptop",
                "id": "#57:25",
                "platform": "Linux",
                "os": "Mint 18",
                "external": False,
                "ipAddress": "172.0.0.18",
                "facility": "Power Station",
                "unit": "",
                "machineClass": "Workstation",
                "function": "",
                "globalId": "d888"
            },
            {
                "type": "Device",
                "name": "Firewall",
                "id": "#57:0",
                "platform": "Cisco",
                "os": "ASA 5505",
                "external": False,
                "ipAddress": "172.1.0.3",
                "facility": "",
                "unit": "",
                "machineClass": "Firewall",
                "function": "Firewall",
                "globalId": "d3"
            },
            {
                "type": "Device",
                "name": "File Server",
                "id": "#57:1",
                "platform": "Windows",
                "os": "Windows Server 2012",
                "external": False,
                "ipAddress": "172.1.0.14",
                "facility": "",
                "unit": "",
                "machineClass": "Server",
                "function": "File Server",
                "globalId": "d6"
            },
            {
                "type": "Software",
                "name": "Switch Firmware",
                "id": "#60:0",
                "platform": "Cisco",
                "os": "Catalyst-2970",
                "vendor": "cisco",
                "product": "catalyst_2970"
            },
            {
                "type": "Device",
                "name": "Insider Threat",
                "id": "#53:2",
                "platform": "Windows",
                "os": "Windows 7",
                "external": True,
                "ipAddress": "172.1.1.60",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d7"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#53:3",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.1.63",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d10"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#53:4",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.1.66",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d13"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#53:5",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.44",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d16"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#53:6",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.47",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d19"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#53:7",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.50",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d22"
            },
            {
                "type": "Device",
                "name": "Workstation",
                "id": "#53:8",
                "platform": "Windows",
                "os": "Windows 7",
                "external": False,
                "ipAddress": "172.1.2.53",
                "facility": "",
                "unit": "",
                "machineClass": "Workstation",
                "function": "Workstation",
                "globalId": "d25"
            },
            {
                "type": "SoftwareVulnerability",
                "name": "Arbitrary code execution vulnerability",
                "id": "#64:0",
                "integrityImpact": "COMPLETE",
                "confidentialityImpact": "COMPLETE",
                "availabilityImpact": "COMPLETE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "",
                "summary": "",
                "cvss": 9.5
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2001-0866",
                "id": "#66:0",
                "integrityImpact": "PARTIAL",
                "confidentialityImpact": "PARTIAL",
                "availabilityImpact": "PARTIAL",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.ciac.org/ciac/bulletins/m-018.shtml, http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml, http://www.iss.net/security_center/static/7554.php, http://www.securityfocus.com/bid/3537]",
                "summary": "Cisco 12000 with IOS 12.0 and lines card based on Engine 2 does not properly handle an outbound ACL when an input ACL is not configured on all the interfaces of a multi port line card, which could allow remote attackers to bypass the intended access controls.",
                "cvss": 7.5
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2001-0863",
                "id": "#66:1",
                "integrityImpact": "NONE",
                "confidentialityImpact": "NONE",
                "availabilityImpact": "PARTIAL",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.ciac.org/ciac/bulletins/m-018.shtml, http://www.cisco.com/warp/public/707/GSR-ACL-pub.shtml, http://www.securityfocus.com/bid/3539, http://xforce.iss.net/static/7551.php]",
                "summary": "Cisco 12000 with IOS 12.0 and line cards based on Engine 2 does not handle the \"fragment\" keyword in a compiled ACL (Turbo ACL) for packets that are sent to the router, which allows remote attackers to cause a denial of service via a flood of fragments.",
                "cvss": 5
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2010-1579",
                "id": "#66:2",
                "integrityImpact": "NONE",
                "confidentialityImpact": "NONE",
                "availabilityImpact": "COMPLETE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://www.cisco.com/en/US/products/products_security_advisory09186a0080b3f12f.shtml]",
                "summary": "Unspecified vulnerability in the SunRPC inspection feature on Cisco Adaptive Security Appliances (ASA) 5500 series devices with software 7.2 before 7.2(5), 8.0 before 8.0(5.19), 8.1 before 8.1(2.47), and 8.2 before 8.2(2) and Cisco PIX Security Appliances 500 series devices allows remote attackers to cause a denial of service (device reload) via crafted SunRPC UDP packets, aka Bug ID CSCtc79922.",
                "cvss": 7.8
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2013-1100",
                "id": "#66:3",
                "integrityImpact": "NONE",
                "confidentialityImpact": "NONE",
                "availabilityImpact": "COMPLETE",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "HIGH",
                "references": "[http://tools.cisco.com/security/center/content/CiscoSecurityNotice/CVE-2013-1100]",
                "summary": "The HTTP server in Cisco IOS on Catalyst switches does not properly handle TCP socket events, which allows remote attackers to cause a denial of service (device crash) via crafted packets on TCP port (1) 80 or (2) 443, aka Bug ID CSCuc53853.",
                "cvss": 5.4
            },
            {
                "type": "SoftwareVulnerability",
                "name": "CVE-2014-7226",
                "id": "#66:4",
                "integrityImpact": "PARTIAL",
                "confidentialityImpact": "PARTIAL",
                "availabilityImpact": "PARTIAL",
                "authenticationCapability": "NONE",
                "accessVector": "NETWORK",
                "accessComplexity": "LOW",
                "references": "[http://packetstormsecurity.com/files/128532/HTTP-File-Server-2.3a-2.3b-2.3c-Remote-Command-Execution.html, http://www.exploit-db.com/exploits/34852, http://www.rejetto.com/forum/hfs-~-http-file-server/new-version-2-3d/, http://www.securityfocus.com/bid/70216]",
                "summary": "The file comment feature in Rejetto HTTP File Server (hfs) 2.3c and earlier allows remote attackers to execute arbitrary code by uploading a file with certain invalid UTF-8 byte sequences that are interpreted as executable macro symbols.",
                "cvss": 7.5
            }
        ],
        "edges": [
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:0",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#53:0",
                "target": "#56:0"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:1",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#57:0",
                "target": "#56:1"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:2",
                "connectionType": "Buried Ethernet",
                "priority": 1,
                "source": "#57:0",
                "target": "#57:1"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:3",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#53:1",
                "target": "#57:2"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:4",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#53:1",
                "target": "#57:3"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:5",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#57:4"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:6",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#57:5"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:7",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#57:6"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:8",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#57:7"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#106:9",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#57:8"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:0",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#56:0",
                "target": "#57:0"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:1",
                "connectionType": "Buried Ethernet",
                "priority": 1,
                "source": "#53:1",
                "target": "#57:1"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:2",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#53:1",
                "target": "#53:2"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:3",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#53:1",
                "target": "#53:3"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:4",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#53:1",
                "target": "#53:4"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:5",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#53:5"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:6",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#53:6"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:7",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#53:7"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:8",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#53:8"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#107:25",
                "connectionType": "WiFi",
                "priority": 1,
                "source": "#56:0",
                "target": "#57:25"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#108:0",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#57:0",
                "target": "#53:1"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#108:1",
                "connectionType": "Buried Ethernet",
                "priority": 1,
                "source": "#56:1",
                "target": "#57:1"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#108:2",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#53:1",
                "target": "#56:2"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#108:3",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#53:1",
                "target": "#56:3"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#108:4",
                "connectionType": "Fiber Ethernet",
                "priority": 1,
                "source": "#53:1",
                "target": "#56:4"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#108:5",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#56:5"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#108:6",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#56:6"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#108:7",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#56:7"
            },
            {
                "type": "NetworkConnectionEdge",
                "id": "#108:8",
                "connectionType": "802.11 Wi-Fi",
                "priority": 1,
                "source": "#56:1",
                "target": "#56:8"
            },
            {
                "type": "SoftwareEdge",
                "id": "#109:0",
                "source": "#56:0",
                "target": "#58:0"
            },
            {
                "type": "SoftwareEdge",
                "id": "#109:1",
                "source": "#56:1",
                "target": "#60:0"
            },
            {
                "type": "SoftwareEdge",
                "id": "#109:2",
                "source": "#56:2",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#109:3",
                "source": "#56:3",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#109:4",
                "source": "#56:4",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#109:5",
                "source": "#56:5",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#109:6",
                "source": "#56:6",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#109:7",
                "source": "#56:7",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#109:8",
                "source": "#56:8",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#110:0",
                "source": "#57:0",
                "target": "#59:0"
            },
            {
                "type": "SoftwareEdge",
                "id": "#110:1",
                "source": "#57:1",
                "target": "#58:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#110:2",
                "source": "#57:2",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#110:3",
                "source": "#57:3",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#110:4",
                "source": "#57:4",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#110:5",
                "source": "#57:5",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#110:6",
                "source": "#57:6",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#110:7",
                "source": "#57:7",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#110:8",
                "source": "#57:8",
                "target": "#60:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#111:0",
                "source": "#53:1",
                "target": "#60:0"
            },
            {
                "type": "SoftwareEdge",
                "id": "#111:1",
                "source": "#53:2",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#111:2",
                "source": "#53:3",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#111:3",
                "source": "#53:4",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#111:4",
                "source": "#53:5",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#111:5",
                "source": "#53:6",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#111:6",
                "source": "#53:7",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#111:7",
                "source": "#53:8",
                "target": "#59:1"
            },
            {
                "type": "SoftwareEdge",
                "id": "#111:8",
                "source": "#57:8",
                "target": "#59:1"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#118:0",
                "applicability": "YES",
                "source": "#60:1",
                "target": "#64:0"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#118:1",
                "applicability": "YES",
                "source": "#58:0",
                "target": "#64:1"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#118:2",
                "applicability": "YES",
                "source": "#59:0",
                "target": "#64:2"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#118:3",
                "applicability": "YES",
                "source": "#59:0",
                "target": "#64:3"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#118:4",
                "applicability": "YES",
                "source": "#60:0",
                "target": "#64:4"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#118:5",
                "applicability": "YES",
                "source": "#59:1",
                "target": "#64:5"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#119:0",
                "applicability": "YES",
                "source": "#58:0",
                "target": "#65:0"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#119:1",
                "applicability": "YES",
                "source": "#58:0",
                "target": "#65:1"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#119:2",
                "applicability": "YES",
                "source": "#59:0",
                "target": "#65:2"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#119:3",
                "applicability": "YES",
                "source": "#59:0",
                "target": "#65:3"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#119:4",
                "applicability": "YES",
                "source": "#58:1",
                "target": "#65:4"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#119:5",
                "applicability": "YES",
                "source": "#59:1",
                "target": "#65:5"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#120:0",
                "applicability": "YES",
                "source": "#58:0",
                "target": "#66:0"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#120:1",
                "applicability": "YES",
                "source": "#58:0",
                "target": "#66:1"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#120:2",
                "applicability": "YES",
                "source": "#59:0",
                "target": "#66:2"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#120:3",
                "applicability": "YES",
                "source": "#60:0",
                "target": "#66:3"
            },
            {
                "type": "SoftwareVulnerabilityEdge",
                "id": "#120:4",
                "applicability": "YES",
                "source": "#58:1",
                "target": "#66:4"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:0",
                "source": "#73:0",
                "target": "#53:0"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:1",
                "source": "#73:0",
                "target": "#53:1"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:2",
                "source": "#73:0",
                "target": "#58:0"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:3",
                "source": "#73:0",
                "target": "#58:1"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:4",
                "source": "#73:0",
                "target": "#56:2"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:5",
                "source": "#73:0",
                "target": "#56:3"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:6",
                "source": "#73:0",
                "target": "#56:4"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:7",
                "source": "#73:0",
                "target": "#56:5"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:8",
                "source": "#73:0",
                "target": "#56:6"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:9",
                "source": "#73:0",
                "target": "#56:7"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:10",
                "source": "#73:0",
                "target": "#56:8"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:11",
                "source": "#73:0",
                "target": "#57:8"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:12",
                "source": "#73:0",
                "target": "#64:1"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:13",
                "source": "#73:0",
                "target": "#64:2"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:14",
                "source": "#73:0",
                "target": "#64:3"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:15",
                "source": "#73:0",
                "target": "#64:4"
            },
            {
                "type": "NetworkEdge",
                "id": "#130:16",
                "source": "#73:0",
                "target": "#64:5"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:0",
                "source": "#73:0",
                "target": "#56:0"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:1",
                "source": "#73:0",
                "target": "#56:1"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:2",
                "source": "#73:0",
                "target": "#59:0"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:3",
                "source": "#73:0",
                "target": "#59:1"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:4",
                "source": "#73:0",
                "target": "#57:2"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:5",
                "source": "#73:0",
                "target": "#57:3"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:6",
                "source": "#73:0",
                "target": "#57:4"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:7",
                "source": "#73:0",
                "target": "#57:5"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:8",
                "source": "#73:0",
                "target": "#57:6"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:9",
                "source": "#73:0",
                "target": "#57:7"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:10",
                "source": "#73:0",
                "target": "#60:1"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:11",
                "source": "#73:0",
                "target": "#65:0"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:12",
                "source": "#73:0",
                "target": "#65:1"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:13",
                "source": "#73:0",
                "target": "#65:2"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:14",
                "source": "#73:0",
                "target": "#65:3"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:15",
                "source": "#73:0",
                "target": "#65:4"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:16",
                "source": "#73:0",
                "target": "#65:5"
            },
            {
                "type": "NetworkEdge",
                "id": "#131:33",
                "source": "#73:0",
                "target": "#57:25"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:0",
                "source": "#73:0",
                "target": "#57:0"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:1",
                "source": "#73:0",
                "target": "#57:1"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:2",
                "source": "#73:0",
                "target": "#60:0"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:3",
                "source": "#73:0",
                "target": "#53:2"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:4",
                "source": "#73:0",
                "target": "#53:3"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:5",
                "source": "#73:0",
                "target": "#53:4"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:6",
                "source": "#73:0",
                "target": "#53:5"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:7",
                "source": "#73:0",
                "target": "#53:6"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:8",
                "source": "#73:0",
                "target": "#53:7"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:9",
                "source": "#73:0",
                "target": "#53:8"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:10",
                "source": "#73:0",
                "target": "#64:0"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:11",
                "source": "#73:0",
                "target": "#66:0"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:12",
                "source": "#73:0",
                "target": "#66:1"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:13",
                "source": "#73:0",
                "target": "#66:2"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:14",
                "source": "#73:0",
                "target": "#66:3"
            },
            {
                "type": "NetworkEdge",
                "id": "#132:15",
                "source": "#73:0",
                "target": "#66:4"
            }
        ]
    }
]
