# TF::FortiOS::SystemGlobal

Configure global attributes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemGlobal",
    "Properties" : {
        "<a href="#adminconcurrent" title="AdminConcurrent">AdminConcurrent</a>" : <i>String</i>,
        "<a href="#adminconsoletimeout" title="AdminConsoleTimeout">AdminConsoleTimeout</a>" : <i>Double</i>,
        "<a href="#adminhstsmaxage" title="AdminHstsMaxAge">AdminHstsMaxAge</a>" : <i>Double</i>,
        "<a href="#adminhttpspkirequired" title="AdminHttpsPkiRequired">AdminHttpsPkiRequired</a>" : <i>String</i>,
        "<a href="#adminhttpsredirect" title="AdminHttpsRedirect">AdminHttpsRedirect</a>" : <i>String</i>,
        "<a href="#adminhttpssslversions" title="AdminHttpsSslVersions">AdminHttpsSslVersions</a>" : <i>String</i>,
        "<a href="#adminlockoutduration" title="AdminLockoutDuration">AdminLockoutDuration</a>" : <i>Double</i>,
        "<a href="#adminlockoutthreshold" title="AdminLockoutThreshold">AdminLockoutThreshold</a>" : <i>Double</i>,
        "<a href="#adminloginmax" title="AdminLoginMax">AdminLoginMax</a>" : <i>Double</i>,
        "<a href="#adminmaintainer" title="AdminMaintainer">AdminMaintainer</a>" : <i>String</i>,
        "<a href="#adminport" title="AdminPort">AdminPort</a>" : <i>Double</i>,
        "<a href="#adminrestrictlocal" title="AdminRestrictLocal">AdminRestrictLocal</a>" : <i>String</i>,
        "<a href="#adminscp" title="AdminScp">AdminScp</a>" : <i>String</i>,
        "<a href="#adminservercert" title="AdminServerCert">AdminServerCert</a>" : <i>String</i>,
        "<a href="#adminsport" title="AdminSport">AdminSport</a>" : <i>Double</i>,
        "<a href="#adminsshgracetime" title="AdminSshGraceTime">AdminSshGraceTime</a>" : <i>Double</i>,
        "<a href="#adminsshpassword" title="AdminSshPassword">AdminSshPassword</a>" : <i>String</i>,
        "<a href="#adminsshport" title="AdminSshPort">AdminSshPort</a>" : <i>Double</i>,
        "<a href="#adminsshv1" title="AdminSshV1">AdminSshV1</a>" : <i>String</i>,
        "<a href="#admintelnet" title="AdminTelnet">AdminTelnet</a>" : <i>String</i>,
        "<a href="#admintelnetport" title="AdminTelnetPort">AdminTelnetPort</a>" : <i>Double</i>,
        "<a href="#admintimeout" title="Admintimeout">Admintimeout</a>" : <i>Double</i>,
        "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
        "<a href="#allowtrafficredirect" title="AllowTrafficRedirect">AllowTrafficRedirect</a>" : <i>String</i>,
        "<a href="#antireplay" title="AntiReplay">AntiReplay</a>" : <i>String</i>,
        "<a href="#arpmaxentry" title="ArpMaxEntry">ArpMaxEntry</a>" : <i>Double</i>,
        "<a href="#asymroute" title="Asymroute">Asymroute</a>" : <i>String</i>,
        "<a href="#authcert" title="AuthCert">AuthCert</a>" : <i>String</i>,
        "<a href="#authhttpport" title="AuthHttpPort">AuthHttpPort</a>" : <i>Double</i>,
        "<a href="#authhttpsport" title="AuthHttpsPort">AuthHttpsPort</a>" : <i>Double</i>,
        "<a href="#authkeepalive" title="AuthKeepalive">AuthKeepalive</a>" : <i>String</i>,
        "<a href="#authsessionlimit" title="AuthSessionLimit">AuthSessionLimit</a>" : <i>String</i>,
        "<a href="#autoauthextensiondevice" title="AutoAuthExtensionDevice">AutoAuthExtensionDevice</a>" : <i>String</i>,
        "<a href="#autorunlogfsck" title="AutorunLogFsck">AutorunLogFsck</a>" : <i>String</i>,
        "<a href="#avaffinity" title="AvAffinity">AvAffinity</a>" : <i>String</i>,
        "<a href="#avfailopen" title="AvFailopen">AvFailopen</a>" : <i>String</i>,
        "<a href="#avfailopensession" title="AvFailopenSession">AvFailopenSession</a>" : <i>String</i>,
        "<a href="#batchcmdb" title="BatchCmdb">BatchCmdb</a>" : <i>String</i>,
        "<a href="#blocksessiontimer" title="BlockSessionTimer">BlockSessionTimer</a>" : <i>Double</i>,
        "<a href="#brfdbmaxentry" title="BrFdbMaxEntry">BrFdbMaxEntry</a>" : <i>Double</i>,
        "<a href="#certchainmax" title="CertChainMax">CertChainMax</a>" : <i>Double</i>,
        "<a href="#cfgreverttimeout" title="CfgRevertTimeout">CfgRevertTimeout</a>" : <i>Double</i>,
        "<a href="#cfgsave" title="CfgSave">CfgSave</a>" : <i>String</i>,
        "<a href="#checkprotocolheader" title="CheckProtocolHeader">CheckProtocolHeader</a>" : <i>String</i>,
        "<a href="#checkresetrange" title="CheckResetRange">CheckResetRange</a>" : <i>String</i>,
        "<a href="#cliauditlog" title="CliAuditLog">CliAuditLog</a>" : <i>String</i>,
        "<a href="#cloudcommunication" title="CloudCommunication">CloudCommunication</a>" : <i>String</i>,
        "<a href="#cltcertreq" title="CltCertReq">CltCertReq</a>" : <i>String</i>,
        "<a href="#compliancecheck" title="ComplianceCheck">ComplianceCheck</a>" : <i>String</i>,
        "<a href="#compliancechecktime" title="ComplianceCheckTime">ComplianceCheckTime</a>" : <i>String</i>,
        "<a href="#cpuusethreshold" title="CpuUseThreshold">CpuUseThreshold</a>" : <i>Double</i>,
        "<a href="#csrcaattribute" title="CsrCaAttribute">CsrCaAttribute</a>" : <i>String</i>,
        "<a href="#dailyrestart" title="DailyRestart">DailyRestart</a>" : <i>String</i>,
        "<a href="#defaultservicesourceport" title="DefaultServiceSourcePort">DefaultServiceSourcePort</a>" : <i>String</i>,
        "<a href="#deviceidentificationactivescandelay" title="DeviceIdentificationActiveScanDelay">DeviceIdentificationActiveScanDelay</a>" : <i>Double</i>,
        "<a href="#deviceidletimeout" title="DeviceIdleTimeout">DeviceIdleTimeout</a>" : <i>Double</i>,
        "<a href="#dhparams" title="DhParams">DhParams</a>" : <i>String</i>,
        "<a href="#dnsproxyworkercount" title="DnsproxyWorkerCount">DnsproxyWorkerCount</a>" : <i>Double</i>,
        "<a href="#dst" title="Dst">Dst</a>" : <i>String</i>,
        "<a href="#endpointcontrolfdsaccess" title="EndpointControlFdsAccess">EndpointControlFdsAccess</a>" : <i>String</i>,
        "<a href="#endpointcontrolportalport" title="EndpointControlPortalPort">EndpointControlPortalPort</a>" : <i>Double</i>,
        "<a href="#failtime" title="Failtime">Failtime</a>" : <i>Double</i>,
        "<a href="#fazdiskbuffersize" title="FazDiskBufferSize">FazDiskBufferSize</a>" : <i>Double</i>,
        "<a href="#fdsstatistics" title="FdsStatistics">FdsStatistics</a>" : <i>String</i>,
        "<a href="#fdsstatisticsperiod" title="FdsStatisticsPeriod">FdsStatisticsPeriod</a>" : <i>Double</i>,
        "<a href="#fecport" title="FecPort">FecPort</a>" : <i>Double</i>,
        "<a href="#fgdalertsubscription" title="FgdAlertSubscription">FgdAlertSubscription</a>" : <i>String</i>,
        "<a href="#fortiextender" title="Fortiextender">Fortiextender</a>" : <i>String</i>,
        "<a href="#fortiextenderdataport" title="FortiextenderDataPort">FortiextenderDataPort</a>" : <i>Double</i>,
        "<a href="#fortiextendervlanmode" title="FortiextenderVlanMode">FortiextenderVlanMode</a>" : <i>String</i>,
        "<a href="#fortiipamintegration" title="FortiipamIntegration">FortiipamIntegration</a>" : <i>String</i>,
        "<a href="#fortiserviceport" title="FortiservicePort">FortiservicePort</a>" : <i>Double</i>,
        "<a href="#fortitokencloud" title="FortitokenCloud">FortitokenCloud</a>" : <i>String</i>,
        "<a href="#guiallowdefaulthostname" title="GuiAllowDefaultHostname">GuiAllowDefaultHostname</a>" : <i>String</i>,
        "<a href="#guicertificates" title="GuiCertificates">GuiCertificates</a>" : <i>String</i>,
        "<a href="#guicustomlanguage" title="GuiCustomLanguage">GuiCustomLanguage</a>" : <i>String</i>,
        "<a href="#guidateformat" title="GuiDateFormat">GuiDateFormat</a>" : <i>String</i>,
        "<a href="#guidatetimesource" title="GuiDateTimeSource">GuiDateTimeSource</a>" : <i>String</i>,
        "<a href="#guidevicelatitude" title="GuiDeviceLatitude">GuiDeviceLatitude</a>" : <i>String</i>,
        "<a href="#guidevicelongitude" title="GuiDeviceLongitude">GuiDeviceLongitude</a>" : <i>String</i>,
        "<a href="#guidisplayhostname" title="GuiDisplayHostname">GuiDisplayHostname</a>" : <i>String</i>,
        "<a href="#guifirmwareupgradesetupwarning" title="GuiFirmwareUpgradeSetupWarning">GuiFirmwareUpgradeSetupWarning</a>" : <i>String</i>,
        "<a href="#guifirmwareupgradewarning" title="GuiFirmwareUpgradeWarning">GuiFirmwareUpgradeWarning</a>" : <i>String</i>,
        "<a href="#guiforticareregistrationsetupwarning" title="GuiForticareRegistrationSetupWarning">GuiForticareRegistrationSetupWarning</a>" : <i>String</i>,
        "<a href="#guifortigatecloudsandbox" title="GuiFortigateCloudSandbox">GuiFortigateCloudSandbox</a>" : <i>String</i>,
        "<a href="#guifortisandboxcloud" title="GuiFortisandboxCloud">GuiFortisandboxCloud</a>" : <i>String</i>,
        "<a href="#guiipv6" title="GuiIpv6">GuiIpv6</a>" : <i>String</i>,
        "<a href="#guilinesperpage" title="GuiLinesPerPage">GuiLinesPerPage</a>" : <i>Double</i>,
        "<a href="#guitheme" title="GuiTheme">GuiTheme</a>" : <i>String</i>,
        "<a href="#guiwirelessopensecurity" title="GuiWirelessOpensecurity">GuiWirelessOpensecurity</a>" : <i>String</i>,
        "<a href="#honordf" title="HonorDf">HonorDf</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#igmpstatelimit" title="IgmpStateLimit">IgmpStateLimit</a>" : <i>Double</i>,
        "<a href="#ikeembryoniclimit" title="IkeEmbryonicLimit">IkeEmbryonicLimit</a>" : <i>Double</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#ipsrcportrange" title="IpSrcPortRange">IpSrcPortRange</a>" : <i>String</i>,
        "<a href="#ipsaffinity" title="IpsAffinity">IpsAffinity</a>" : <i>String</i>,
        "<a href="#ipsecasicoffload" title="IpsecAsicOffload">IpsecAsicOffload</a>" : <i>String</i>,
        "<a href="#ipsechmacoffload" title="IpsecHmacOffload">IpsecHmacOffload</a>" : <i>String</i>,
        "<a href="#ipsecsoftdecasync" title="IpsecSoftDecAsync">IpsecSoftDecAsync</a>" : <i>String</i>,
        "<a href="#ipv6acceptdad" title="Ipv6AcceptDad">Ipv6AcceptDad</a>" : <i>Double</i>,
        "<a href="#ipv6allowanycastprobe" title="Ipv6AllowAnycastProbe">Ipv6AllowAnycastProbe</a>" : <i>String</i>,
        "<a href="#ipv6allowtrafficredirect" title="Ipv6AllowTrafficRedirect">Ipv6AllowTrafficRedirect</a>" : <i>String</i>,
        "<a href="#irqtimeaccounting" title="IrqTimeAccounting">IrqTimeAccounting</a>" : <i>String</i>,
        "<a href="#language" title="Language">Language</a>" : <i>String</i>,
        "<a href="#ldapconntimeout" title="Ldapconntimeout">Ldapconntimeout</a>" : <i>Double</i>,
        "<a href="#lldpreception" title="LldpReception">LldpReception</a>" : <i>String</i>,
        "<a href="#lldptransmission" title="LldpTransmission">LldpTransmission</a>" : <i>String</i>,
        "<a href="#logsslconnection" title="LogSslConnection">LogSslConnection</a>" : <i>String</i>,
        "<a href="#loguuidaddress" title="LogUuidAddress">LogUuidAddress</a>" : <i>String</i>,
        "<a href="#loguuidpolicy" title="LogUuidPolicy">LogUuidPolicy</a>" : <i>String</i>,
        "<a href="#logintimestamp" title="LoginTimestamp">LoginTimestamp</a>" : <i>String</i>,
        "<a href="#longvdomname" title="LongVdomName">LongVdomName</a>" : <i>String</i>,
        "<a href="#managementvdom" title="ManagementVdom">ManagementVdom</a>" : <i>String</i>,
        "<a href="#maxdlpstatmemory" title="MaxDlpstatMemory">MaxDlpstatMemory</a>" : <i>Double</i>,
        "<a href="#maxroutecachesize" title="MaxRouteCacheSize">MaxRouteCacheSize</a>" : <i>Double</i>,
        "<a href="#mcttlnotchange" title="McTtlNotchange">McTtlNotchange</a>" : <i>String</i>,
        "<a href="#memoryusethresholdextreme" title="MemoryUseThresholdExtreme">MemoryUseThresholdExtreme</a>" : <i>Double</i>,
        "<a href="#memoryusethresholdgreen" title="MemoryUseThresholdGreen">MemoryUseThresholdGreen</a>" : <i>Double</i>,
        "<a href="#memoryusethresholdred" title="MemoryUseThresholdRed">MemoryUseThresholdRed</a>" : <i>Double</i>,
        "<a href="#miglogaffinity" title="MiglogAffinity">MiglogAffinity</a>" : <i>String</i>,
        "<a href="#miglogdchildren" title="MiglogdChildren">MiglogdChildren</a>" : <i>Double</i>,
        "<a href="#multifactorauthentication" title="MultiFactorAuthentication">MultiFactorAuthentication</a>" : <i>String</i>,
        "<a href="#multicastforward" title="MulticastForward">MulticastForward</a>" : <i>String</i>,
        "<a href="#ndpmaxentry" title="NdpMaxEntry">NdpMaxEntry</a>" : <i>Double</i>,
        "<a href="#peruserbal" title="PerUserBal">PerUserBal</a>" : <i>String</i>,
        "<a href="#peruserbwl" title="PerUserBwl">PerUserBwl</a>" : <i>String</i>,
        "<a href="#policyauthconcurrent" title="PolicyAuthConcurrent">PolicyAuthConcurrent</a>" : <i>Double</i>,
        "<a href="#postloginbanner" title="PostLoginBanner">PostLoginBanner</a>" : <i>String</i>,
        "<a href="#preloginbanner" title="PreLoginBanner">PreLoginBanner</a>" : <i>String</i>,
        "<a href="#privatedataencryption" title="PrivateDataEncryption">PrivateDataEncryption</a>" : <i>String</i>,
        "<a href="#proxyauthlifetime" title="ProxyAuthLifetime">ProxyAuthLifetime</a>" : <i>String</i>,
        "<a href="#proxyauthlifetimetimeout" title="ProxyAuthLifetimeTimeout">ProxyAuthLifetimeTimeout</a>" : <i>Double</i>,
        "<a href="#proxyauthtimeout" title="ProxyAuthTimeout">ProxyAuthTimeout</a>" : <i>Double</i>,
        "<a href="#proxycipherhardwareacceleration" title="ProxyCipherHardwareAcceleration">ProxyCipherHardwareAcceleration</a>" : <i>String</i>,
        "<a href="#proxykxphardwareacceleration" title="ProxyKxpHardwareAcceleration">ProxyKxpHardwareAcceleration</a>" : <i>String</i>,
        "<a href="#proxyreauthenticationmode" title="ProxyReAuthenticationMode">ProxyReAuthenticationMode</a>" : <i>String</i>,
        "<a href="#proxyworkercount" title="ProxyWorkerCount">ProxyWorkerCount</a>" : <i>Double</i>,
        "<a href="#radiusport" title="RadiusPort">RadiusPort</a>" : <i>Double</i>,
        "<a href="#rebootuponconfigrestore" title="RebootUponConfigRestore">RebootUponConfigRestore</a>" : <i>String</i>,
        "<a href="#refresh" title="Refresh">Refresh</a>" : <i>Double</i>,
        "<a href="#remoteauthtimeout" title="Remoteauthtimeout">Remoteauthtimeout</a>" : <i>Double</i>,
        "<a href="#resetsessionlesstcp" title="ResetSessionlessTcp">ResetSessionlessTcp</a>" : <i>String</i>,
        "<a href="#restarttime" title="RestartTime">RestartTime</a>" : <i>String</i>,
        "<a href="#revisionbackuponlogout" title="RevisionBackupOnLogout">RevisionBackupOnLogout</a>" : <i>String</i>,
        "<a href="#revisionimageautobackup" title="RevisionImageAutoBackup">RevisionImageAutoBackup</a>" : <i>String</i>,
        "<a href="#scanunitcount" title="ScanunitCount">ScanunitCount</a>" : <i>Double</i>,
        "<a href="#securityratingresultsubmission" title="SecurityRatingResultSubmission">SecurityRatingResultSubmission</a>" : <i>String</i>,
        "<a href="#securityratingrunonschedule" title="SecurityRatingRunOnSchedule">SecurityRatingRunOnSchedule</a>" : <i>String</i>,
        "<a href="#sendpmtuicmp" title="SendPmtuIcmp">SendPmtuIcmp</a>" : <i>String</i>,
        "<a href="#snatroutechange" title="SnatRouteChange">SnatRouteChange</a>" : <i>String</i>,
        "<a href="#specialfile23support" title="SpecialFile23Support">SpecialFile23Support</a>" : <i>String</i>,
        "<a href="#ssdtrimdate" title="SsdTrimDate">SsdTrimDate</a>" : <i>Double</i>,
        "<a href="#ssdtrimfreq" title="SsdTrimFreq">SsdTrimFreq</a>" : <i>String</i>,
        "<a href="#ssdtrimhour" title="SsdTrimHour">SsdTrimHour</a>" : <i>Double</i>,
        "<a href="#ssdtrimmin" title="SsdTrimMin">SsdTrimMin</a>" : <i>Double</i>,
        "<a href="#ssdtrimweekday" title="SsdTrimWeekday">SsdTrimWeekday</a>" : <i>String</i>,
        "<a href="#sshcbccipher" title="SshCbcCipher">SshCbcCipher</a>" : <i>String</i>,
        "<a href="#sshhmacmd5" title="SshHmacMd5">SshHmacMd5</a>" : <i>String</i>,
        "<a href="#sshkexsha1" title="SshKexSha1">SshKexSha1</a>" : <i>String</i>,
        "<a href="#sshmacweak" title="SshMacWeak">SshMacWeak</a>" : <i>String</i>,
        "<a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>" : <i>String</i>,
        "<a href="#sslstatickeyciphers" title="SslStaticKeyCiphers">SslStaticKeyCiphers</a>" : <i>String</i>,
        "<a href="#sslvpncipherhardwareacceleration" title="SslvpnCipherHardwareAcceleration">SslvpnCipherHardwareAcceleration</a>" : <i>String</i>,
        "<a href="#sslvpnemssncheck" title="SslvpnEmsSnCheck">SslvpnEmsSnCheck</a>" : <i>String</i>,
        "<a href="#sslvpnkxphardwareacceleration" title="SslvpnKxpHardwareAcceleration">SslvpnKxpHardwareAcceleration</a>" : <i>String</i>,
        "<a href="#sslvpnmaxworkercount" title="SslvpnMaxWorkerCount">SslvpnMaxWorkerCount</a>" : <i>Double</i>,
        "<a href="#sslvpnpluginversioncheck" title="SslvpnPluginVersionCheck">SslvpnPluginVersionCheck</a>" : <i>String</i>,
        "<a href="#strictdirtysessioncheck" title="StrictDirtySessionCheck">StrictDirtySessionCheck</a>" : <i>String</i>,
        "<a href="#strongcrypto" title="StrongCrypto">StrongCrypto</a>" : <i>String</i>,
        "<a href="#switchcontroller" title="SwitchController">SwitchController</a>" : <i>String</i>,
        "<a href="#switchcontrollerreservednetwork" title="SwitchControllerReservedNetwork">SwitchControllerReservedNetwork</a>" : <i>String</i>,
        "<a href="#sysperfloginterval" title="SysPerfLogInterval">SysPerfLogInterval</a>" : <i>Double</i>,
        "<a href="#tcphalfclosetimer" title="TcpHalfcloseTimer">TcpHalfcloseTimer</a>" : <i>Double</i>,
        "<a href="#tcphalfopentimer" title="TcpHalfopenTimer">TcpHalfopenTimer</a>" : <i>Double</i>,
        "<a href="#tcpoption" title="TcpOption">TcpOption</a>" : <i>String</i>,
        "<a href="#tcptimewaittimer" title="TcpTimewaitTimer">TcpTimewaitTimer</a>" : <i>Double</i>,
        "<a href="#tftp" title="Tftp">Tftp</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#tpmcskippolicy" title="TpMcSkipPolicy">TpMcSkipPolicy</a>" : <i>String</i>,
        "<a href="#trafficpriority" title="TrafficPriority">TrafficPriority</a>" : <i>String</i>,
        "<a href="#trafficprioritylevel" title="TrafficPriorityLevel">TrafficPriorityLevel</a>" : <i>String</i>,
        "<a href="#twofactoremailexpiry" title="TwoFactorEmailExpiry">TwoFactorEmailExpiry</a>" : <i>Double</i>,
        "<a href="#twofactorfacexpiry" title="TwoFactorFacExpiry">TwoFactorFacExpiry</a>" : <i>Double</i>,
        "<a href="#twofactorftkexpiry" title="TwoFactorFtkExpiry">TwoFactorFtkExpiry</a>" : <i>Double</i>,
        "<a href="#twofactorftmexpiry" title="TwoFactorFtmExpiry">TwoFactorFtmExpiry</a>" : <i>Double</i>,
        "<a href="#twofactorsmsexpiry" title="TwoFactorSmsExpiry">TwoFactorSmsExpiry</a>" : <i>Double</i>,
        "<a href="#udpidletimer" title="UdpIdleTimer">UdpIdleTimer</a>" : <i>Double</i>,
        "<a href="#urlfilteraffinity" title="UrlFilterAffinity">UrlFilterAffinity</a>" : <i>String</i>,
        "<a href="#urlfiltercount" title="UrlFilterCount">UrlFilterCount</a>" : <i>Double</i>,
        "<a href="#userdevicestoremaxdevices" title="UserDeviceStoreMaxDevices">UserDeviceStoreMaxDevices</a>" : <i>Double</i>,
        "<a href="#userdevicestoremaxusers" title="UserDeviceStoreMaxUsers">UserDeviceStoreMaxUsers</a>" : <i>Double</i>,
        "<a href="#userservercert" title="UserServerCert">UserServerCert</a>" : <i>String</i>,
        "<a href="#vdomadmin" title="VdomAdmin">VdomAdmin</a>" : <i>String</i>,
        "<a href="#vdommode" title="VdomMode">VdomMode</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#viparprange" title="VipArpRange">VipArpRange</a>" : <i>String</i>,
        "<a href="#virtualservercount" title="VirtualServerCount">VirtualServerCount</a>" : <i>Double</i>,
        "<a href="#virtualserverhardwareacceleration" title="VirtualServerHardwareAcceleration">VirtualServerHardwareAcceleration</a>" : <i>String</i>,
        "<a href="#wadaffinity" title="WadAffinity">WadAffinity</a>" : <i>String</i>,
        "<a href="#wadcsvccscount" title="WadCsvcCsCount">WadCsvcCsCount</a>" : <i>Double</i>,
        "<a href="#wadcsvcdbcount" title="WadCsvcDbCount">WadCsvcDbCount</a>" : <i>Double</i>,
        "<a href="#wadmemorychangegranularity" title="WadMemoryChangeGranularity">WadMemoryChangeGranularity</a>" : <i>Double</i>,
        "<a href="#wadsourceaffinity" title="WadSourceAffinity">WadSourceAffinity</a>" : <i>String</i>,
        "<a href="#wadworkercount" title="WadWorkerCount">WadWorkerCount</a>" : <i>Double</i>,
        "<a href="#wificacertificate" title="WifiCaCertificate">WifiCaCertificate</a>" : <i>String</i>,
        "<a href="#wificertificate" title="WifiCertificate">WifiCertificate</a>" : <i>String</i>,
        "<a href="#wimax4gusb" title="Wimax4gUsb">Wimax4gUsb</a>" : <i>String</i>,
        "<a href="#wirelesscontroller" title="WirelessController">WirelessController</a>" : <i>String</i>,
        "<a href="#wirelesscontrollerport" title="WirelessControllerPort">WirelessControllerPort</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemGlobal
Properties:
    <a href="#adminconcurrent" title="AdminConcurrent">AdminConcurrent</a>: <i>String</i>
    <a href="#adminconsoletimeout" title="AdminConsoleTimeout">AdminConsoleTimeout</a>: <i>Double</i>
    <a href="#adminhstsmaxage" title="AdminHstsMaxAge">AdminHstsMaxAge</a>: <i>Double</i>
    <a href="#adminhttpspkirequired" title="AdminHttpsPkiRequired">AdminHttpsPkiRequired</a>: <i>String</i>
    <a href="#adminhttpsredirect" title="AdminHttpsRedirect">AdminHttpsRedirect</a>: <i>String</i>
    <a href="#adminhttpssslversions" title="AdminHttpsSslVersions">AdminHttpsSslVersions</a>: <i>String</i>
    <a href="#adminlockoutduration" title="AdminLockoutDuration">AdminLockoutDuration</a>: <i>Double</i>
    <a href="#adminlockoutthreshold" title="AdminLockoutThreshold">AdminLockoutThreshold</a>: <i>Double</i>
    <a href="#adminloginmax" title="AdminLoginMax">AdminLoginMax</a>: <i>Double</i>
    <a href="#adminmaintainer" title="AdminMaintainer">AdminMaintainer</a>: <i>String</i>
    <a href="#adminport" title="AdminPort">AdminPort</a>: <i>Double</i>
    <a href="#adminrestrictlocal" title="AdminRestrictLocal">AdminRestrictLocal</a>: <i>String</i>
    <a href="#adminscp" title="AdminScp">AdminScp</a>: <i>String</i>
    <a href="#adminservercert" title="AdminServerCert">AdminServerCert</a>: <i>String</i>
    <a href="#adminsport" title="AdminSport">AdminSport</a>: <i>Double</i>
    <a href="#adminsshgracetime" title="AdminSshGraceTime">AdminSshGraceTime</a>: <i>Double</i>
    <a href="#adminsshpassword" title="AdminSshPassword">AdminSshPassword</a>: <i>String</i>
    <a href="#adminsshport" title="AdminSshPort">AdminSshPort</a>: <i>Double</i>
    <a href="#adminsshv1" title="AdminSshV1">AdminSshV1</a>: <i>String</i>
    <a href="#admintelnet" title="AdminTelnet">AdminTelnet</a>: <i>String</i>
    <a href="#admintelnetport" title="AdminTelnetPort">AdminTelnetPort</a>: <i>Double</i>
    <a href="#admintimeout" title="Admintimeout">Admintimeout</a>: <i>Double</i>
    <a href="#alias" title="Alias">Alias</a>: <i>String</i>
    <a href="#allowtrafficredirect" title="AllowTrafficRedirect">AllowTrafficRedirect</a>: <i>String</i>
    <a href="#antireplay" title="AntiReplay">AntiReplay</a>: <i>String</i>
    <a href="#arpmaxentry" title="ArpMaxEntry">ArpMaxEntry</a>: <i>Double</i>
    <a href="#asymroute" title="Asymroute">Asymroute</a>: <i>String</i>
    <a href="#authcert" title="AuthCert">AuthCert</a>: <i>String</i>
    <a href="#authhttpport" title="AuthHttpPort">AuthHttpPort</a>: <i>Double</i>
    <a href="#authhttpsport" title="AuthHttpsPort">AuthHttpsPort</a>: <i>Double</i>
    <a href="#authkeepalive" title="AuthKeepalive">AuthKeepalive</a>: <i>String</i>
    <a href="#authsessionlimit" title="AuthSessionLimit">AuthSessionLimit</a>: <i>String</i>
    <a href="#autoauthextensiondevice" title="AutoAuthExtensionDevice">AutoAuthExtensionDevice</a>: <i>String</i>
    <a href="#autorunlogfsck" title="AutorunLogFsck">AutorunLogFsck</a>: <i>String</i>
    <a href="#avaffinity" title="AvAffinity">AvAffinity</a>: <i>String</i>
    <a href="#avfailopen" title="AvFailopen">AvFailopen</a>: <i>String</i>
    <a href="#avfailopensession" title="AvFailopenSession">AvFailopenSession</a>: <i>String</i>
    <a href="#batchcmdb" title="BatchCmdb">BatchCmdb</a>: <i>String</i>
    <a href="#blocksessiontimer" title="BlockSessionTimer">BlockSessionTimer</a>: <i>Double</i>
    <a href="#brfdbmaxentry" title="BrFdbMaxEntry">BrFdbMaxEntry</a>: <i>Double</i>
    <a href="#certchainmax" title="CertChainMax">CertChainMax</a>: <i>Double</i>
    <a href="#cfgreverttimeout" title="CfgRevertTimeout">CfgRevertTimeout</a>: <i>Double</i>
    <a href="#cfgsave" title="CfgSave">CfgSave</a>: <i>String</i>
    <a href="#checkprotocolheader" title="CheckProtocolHeader">CheckProtocolHeader</a>: <i>String</i>
    <a href="#checkresetrange" title="CheckResetRange">CheckResetRange</a>: <i>String</i>
    <a href="#cliauditlog" title="CliAuditLog">CliAuditLog</a>: <i>String</i>
    <a href="#cloudcommunication" title="CloudCommunication">CloudCommunication</a>: <i>String</i>
    <a href="#cltcertreq" title="CltCertReq">CltCertReq</a>: <i>String</i>
    <a href="#compliancecheck" title="ComplianceCheck">ComplianceCheck</a>: <i>String</i>
    <a href="#compliancechecktime" title="ComplianceCheckTime">ComplianceCheckTime</a>: <i>String</i>
    <a href="#cpuusethreshold" title="CpuUseThreshold">CpuUseThreshold</a>: <i>Double</i>
    <a href="#csrcaattribute" title="CsrCaAttribute">CsrCaAttribute</a>: <i>String</i>
    <a href="#dailyrestart" title="DailyRestart">DailyRestart</a>: <i>String</i>
    <a href="#defaultservicesourceport" title="DefaultServiceSourcePort">DefaultServiceSourcePort</a>: <i>String</i>
    <a href="#deviceidentificationactivescandelay" title="DeviceIdentificationActiveScanDelay">DeviceIdentificationActiveScanDelay</a>: <i>Double</i>
    <a href="#deviceidletimeout" title="DeviceIdleTimeout">DeviceIdleTimeout</a>: <i>Double</i>
    <a href="#dhparams" title="DhParams">DhParams</a>: <i>String</i>
    <a href="#dnsproxyworkercount" title="DnsproxyWorkerCount">DnsproxyWorkerCount</a>: <i>Double</i>
    <a href="#dst" title="Dst">Dst</a>: <i>String</i>
    <a href="#endpointcontrolfdsaccess" title="EndpointControlFdsAccess">EndpointControlFdsAccess</a>: <i>String</i>
    <a href="#endpointcontrolportalport" title="EndpointControlPortalPort">EndpointControlPortalPort</a>: <i>Double</i>
    <a href="#failtime" title="Failtime">Failtime</a>: <i>Double</i>
    <a href="#fazdiskbuffersize" title="FazDiskBufferSize">FazDiskBufferSize</a>: <i>Double</i>
    <a href="#fdsstatistics" title="FdsStatistics">FdsStatistics</a>: <i>String</i>
    <a href="#fdsstatisticsperiod" title="FdsStatisticsPeriod">FdsStatisticsPeriod</a>: <i>Double</i>
    <a href="#fecport" title="FecPort">FecPort</a>: <i>Double</i>
    <a href="#fgdalertsubscription" title="FgdAlertSubscription">FgdAlertSubscription</a>: <i>String</i>
    <a href="#fortiextender" title="Fortiextender">Fortiextender</a>: <i>String</i>
    <a href="#fortiextenderdataport" title="FortiextenderDataPort">FortiextenderDataPort</a>: <i>Double</i>
    <a href="#fortiextendervlanmode" title="FortiextenderVlanMode">FortiextenderVlanMode</a>: <i>String</i>
    <a href="#fortiipamintegration" title="FortiipamIntegration">FortiipamIntegration</a>: <i>String</i>
    <a href="#fortiserviceport" title="FortiservicePort">FortiservicePort</a>: <i>Double</i>
    <a href="#fortitokencloud" title="FortitokenCloud">FortitokenCloud</a>: <i>String</i>
    <a href="#guiallowdefaulthostname" title="GuiAllowDefaultHostname">GuiAllowDefaultHostname</a>: <i>String</i>
    <a href="#guicertificates" title="GuiCertificates">GuiCertificates</a>: <i>String</i>
    <a href="#guicustomlanguage" title="GuiCustomLanguage">GuiCustomLanguage</a>: <i>String</i>
    <a href="#guidateformat" title="GuiDateFormat">GuiDateFormat</a>: <i>String</i>
    <a href="#guidatetimesource" title="GuiDateTimeSource">GuiDateTimeSource</a>: <i>String</i>
    <a href="#guidevicelatitude" title="GuiDeviceLatitude">GuiDeviceLatitude</a>: <i>String</i>
    <a href="#guidevicelongitude" title="GuiDeviceLongitude">GuiDeviceLongitude</a>: <i>String</i>
    <a href="#guidisplayhostname" title="GuiDisplayHostname">GuiDisplayHostname</a>: <i>String</i>
    <a href="#guifirmwareupgradesetupwarning" title="GuiFirmwareUpgradeSetupWarning">GuiFirmwareUpgradeSetupWarning</a>: <i>String</i>
    <a href="#guifirmwareupgradewarning" title="GuiFirmwareUpgradeWarning">GuiFirmwareUpgradeWarning</a>: <i>String</i>
    <a href="#guiforticareregistrationsetupwarning" title="GuiForticareRegistrationSetupWarning">GuiForticareRegistrationSetupWarning</a>: <i>String</i>
    <a href="#guifortigatecloudsandbox" title="GuiFortigateCloudSandbox">GuiFortigateCloudSandbox</a>: <i>String</i>
    <a href="#guifortisandboxcloud" title="GuiFortisandboxCloud">GuiFortisandboxCloud</a>: <i>String</i>
    <a href="#guiipv6" title="GuiIpv6">GuiIpv6</a>: <i>String</i>
    <a href="#guilinesperpage" title="GuiLinesPerPage">GuiLinesPerPage</a>: <i>Double</i>
    <a href="#guitheme" title="GuiTheme">GuiTheme</a>: <i>String</i>
    <a href="#guiwirelessopensecurity" title="GuiWirelessOpensecurity">GuiWirelessOpensecurity</a>: <i>String</i>
    <a href="#honordf" title="HonorDf">HonorDf</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#igmpstatelimit" title="IgmpStateLimit">IgmpStateLimit</a>: <i>Double</i>
    <a href="#ikeembryoniclimit" title="IkeEmbryonicLimit">IkeEmbryonicLimit</a>: <i>Double</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#ipsrcportrange" title="IpSrcPortRange">IpSrcPortRange</a>: <i>String</i>
    <a href="#ipsaffinity" title="IpsAffinity">IpsAffinity</a>: <i>String</i>
    <a href="#ipsecasicoffload" title="IpsecAsicOffload">IpsecAsicOffload</a>: <i>String</i>
    <a href="#ipsechmacoffload" title="IpsecHmacOffload">IpsecHmacOffload</a>: <i>String</i>
    <a href="#ipsecsoftdecasync" title="IpsecSoftDecAsync">IpsecSoftDecAsync</a>: <i>String</i>
    <a href="#ipv6acceptdad" title="Ipv6AcceptDad">Ipv6AcceptDad</a>: <i>Double</i>
    <a href="#ipv6allowanycastprobe" title="Ipv6AllowAnycastProbe">Ipv6AllowAnycastProbe</a>: <i>String</i>
    <a href="#ipv6allowtrafficredirect" title="Ipv6AllowTrafficRedirect">Ipv6AllowTrafficRedirect</a>: <i>String</i>
    <a href="#irqtimeaccounting" title="IrqTimeAccounting">IrqTimeAccounting</a>: <i>String</i>
    <a href="#language" title="Language">Language</a>: <i>String</i>
    <a href="#ldapconntimeout" title="Ldapconntimeout">Ldapconntimeout</a>: <i>Double</i>
    <a href="#lldpreception" title="LldpReception">LldpReception</a>: <i>String</i>
    <a href="#lldptransmission" title="LldpTransmission">LldpTransmission</a>: <i>String</i>
    <a href="#logsslconnection" title="LogSslConnection">LogSslConnection</a>: <i>String</i>
    <a href="#loguuidaddress" title="LogUuidAddress">LogUuidAddress</a>: <i>String</i>
    <a href="#loguuidpolicy" title="LogUuidPolicy">LogUuidPolicy</a>: <i>String</i>
    <a href="#logintimestamp" title="LoginTimestamp">LoginTimestamp</a>: <i>String</i>
    <a href="#longvdomname" title="LongVdomName">LongVdomName</a>: <i>String</i>
    <a href="#managementvdom" title="ManagementVdom">ManagementVdom</a>: <i>String</i>
    <a href="#maxdlpstatmemory" title="MaxDlpstatMemory">MaxDlpstatMemory</a>: <i>Double</i>
    <a href="#maxroutecachesize" title="MaxRouteCacheSize">MaxRouteCacheSize</a>: <i>Double</i>
    <a href="#mcttlnotchange" title="McTtlNotchange">McTtlNotchange</a>: <i>String</i>
    <a href="#memoryusethresholdextreme" title="MemoryUseThresholdExtreme">MemoryUseThresholdExtreme</a>: <i>Double</i>
    <a href="#memoryusethresholdgreen" title="MemoryUseThresholdGreen">MemoryUseThresholdGreen</a>: <i>Double</i>
    <a href="#memoryusethresholdred" title="MemoryUseThresholdRed">MemoryUseThresholdRed</a>: <i>Double</i>
    <a href="#miglogaffinity" title="MiglogAffinity">MiglogAffinity</a>: <i>String</i>
    <a href="#miglogdchildren" title="MiglogdChildren">MiglogdChildren</a>: <i>Double</i>
    <a href="#multifactorauthentication" title="MultiFactorAuthentication">MultiFactorAuthentication</a>: <i>String</i>
    <a href="#multicastforward" title="MulticastForward">MulticastForward</a>: <i>String</i>
    <a href="#ndpmaxentry" title="NdpMaxEntry">NdpMaxEntry</a>: <i>Double</i>
    <a href="#peruserbal" title="PerUserBal">PerUserBal</a>: <i>String</i>
    <a href="#peruserbwl" title="PerUserBwl">PerUserBwl</a>: <i>String</i>
    <a href="#policyauthconcurrent" title="PolicyAuthConcurrent">PolicyAuthConcurrent</a>: <i>Double</i>
    <a href="#postloginbanner" title="PostLoginBanner">PostLoginBanner</a>: <i>String</i>
    <a href="#preloginbanner" title="PreLoginBanner">PreLoginBanner</a>: <i>String</i>
    <a href="#privatedataencryption" title="PrivateDataEncryption">PrivateDataEncryption</a>: <i>String</i>
    <a href="#proxyauthlifetime" title="ProxyAuthLifetime">ProxyAuthLifetime</a>: <i>String</i>
    <a href="#proxyauthlifetimetimeout" title="ProxyAuthLifetimeTimeout">ProxyAuthLifetimeTimeout</a>: <i>Double</i>
    <a href="#proxyauthtimeout" title="ProxyAuthTimeout">ProxyAuthTimeout</a>: <i>Double</i>
    <a href="#proxycipherhardwareacceleration" title="ProxyCipherHardwareAcceleration">ProxyCipherHardwareAcceleration</a>: <i>String</i>
    <a href="#proxykxphardwareacceleration" title="ProxyKxpHardwareAcceleration">ProxyKxpHardwareAcceleration</a>: <i>String</i>
    <a href="#proxyreauthenticationmode" title="ProxyReAuthenticationMode">ProxyReAuthenticationMode</a>: <i>String</i>
    <a href="#proxyworkercount" title="ProxyWorkerCount">ProxyWorkerCount</a>: <i>Double</i>
    <a href="#radiusport" title="RadiusPort">RadiusPort</a>: <i>Double</i>
    <a href="#rebootuponconfigrestore" title="RebootUponConfigRestore">RebootUponConfigRestore</a>: <i>String</i>
    <a href="#refresh" title="Refresh">Refresh</a>: <i>Double</i>
    <a href="#remoteauthtimeout" title="Remoteauthtimeout">Remoteauthtimeout</a>: <i>Double</i>
    <a href="#resetsessionlesstcp" title="ResetSessionlessTcp">ResetSessionlessTcp</a>: <i>String</i>
    <a href="#restarttime" title="RestartTime">RestartTime</a>: <i>String</i>
    <a href="#revisionbackuponlogout" title="RevisionBackupOnLogout">RevisionBackupOnLogout</a>: <i>String</i>
    <a href="#revisionimageautobackup" title="RevisionImageAutoBackup">RevisionImageAutoBackup</a>: <i>String</i>
    <a href="#scanunitcount" title="ScanunitCount">ScanunitCount</a>: <i>Double</i>
    <a href="#securityratingresultsubmission" title="SecurityRatingResultSubmission">SecurityRatingResultSubmission</a>: <i>String</i>
    <a href="#securityratingrunonschedule" title="SecurityRatingRunOnSchedule">SecurityRatingRunOnSchedule</a>: <i>String</i>
    <a href="#sendpmtuicmp" title="SendPmtuIcmp">SendPmtuIcmp</a>: <i>String</i>
    <a href="#snatroutechange" title="SnatRouteChange">SnatRouteChange</a>: <i>String</i>
    <a href="#specialfile23support" title="SpecialFile23Support">SpecialFile23Support</a>: <i>String</i>
    <a href="#ssdtrimdate" title="SsdTrimDate">SsdTrimDate</a>: <i>Double</i>
    <a href="#ssdtrimfreq" title="SsdTrimFreq">SsdTrimFreq</a>: <i>String</i>
    <a href="#ssdtrimhour" title="SsdTrimHour">SsdTrimHour</a>: <i>Double</i>
    <a href="#ssdtrimmin" title="SsdTrimMin">SsdTrimMin</a>: <i>Double</i>
    <a href="#ssdtrimweekday" title="SsdTrimWeekday">SsdTrimWeekday</a>: <i>String</i>
    <a href="#sshcbccipher" title="SshCbcCipher">SshCbcCipher</a>: <i>String</i>
    <a href="#sshhmacmd5" title="SshHmacMd5">SshHmacMd5</a>: <i>String</i>
    <a href="#sshkexsha1" title="SshKexSha1">SshKexSha1</a>: <i>String</i>
    <a href="#sshmacweak" title="SshMacWeak">SshMacWeak</a>: <i>String</i>
    <a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>: <i>String</i>
    <a href="#sslstatickeyciphers" title="SslStaticKeyCiphers">SslStaticKeyCiphers</a>: <i>String</i>
    <a href="#sslvpncipherhardwareacceleration" title="SslvpnCipherHardwareAcceleration">SslvpnCipherHardwareAcceleration</a>: <i>String</i>
    <a href="#sslvpnemssncheck" title="SslvpnEmsSnCheck">SslvpnEmsSnCheck</a>: <i>String</i>
    <a href="#sslvpnkxphardwareacceleration" title="SslvpnKxpHardwareAcceleration">SslvpnKxpHardwareAcceleration</a>: <i>String</i>
    <a href="#sslvpnmaxworkercount" title="SslvpnMaxWorkerCount">SslvpnMaxWorkerCount</a>: <i>Double</i>
    <a href="#sslvpnpluginversioncheck" title="SslvpnPluginVersionCheck">SslvpnPluginVersionCheck</a>: <i>String</i>
    <a href="#strictdirtysessioncheck" title="StrictDirtySessionCheck">StrictDirtySessionCheck</a>: <i>String</i>
    <a href="#strongcrypto" title="StrongCrypto">StrongCrypto</a>: <i>String</i>
    <a href="#switchcontroller" title="SwitchController">SwitchController</a>: <i>String</i>
    <a href="#switchcontrollerreservednetwork" title="SwitchControllerReservedNetwork">SwitchControllerReservedNetwork</a>: <i>String</i>
    <a href="#sysperfloginterval" title="SysPerfLogInterval">SysPerfLogInterval</a>: <i>Double</i>
    <a href="#tcphalfclosetimer" title="TcpHalfcloseTimer">TcpHalfcloseTimer</a>: <i>Double</i>
    <a href="#tcphalfopentimer" title="TcpHalfopenTimer">TcpHalfopenTimer</a>: <i>Double</i>
    <a href="#tcpoption" title="TcpOption">TcpOption</a>: <i>String</i>
    <a href="#tcptimewaittimer" title="TcpTimewaitTimer">TcpTimewaitTimer</a>: <i>Double</i>
    <a href="#tftp" title="Tftp">Tftp</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#tpmcskippolicy" title="TpMcSkipPolicy">TpMcSkipPolicy</a>: <i>String</i>
    <a href="#trafficpriority" title="TrafficPriority">TrafficPriority</a>: <i>String</i>
    <a href="#trafficprioritylevel" title="TrafficPriorityLevel">TrafficPriorityLevel</a>: <i>String</i>
    <a href="#twofactoremailexpiry" title="TwoFactorEmailExpiry">TwoFactorEmailExpiry</a>: <i>Double</i>
    <a href="#twofactorfacexpiry" title="TwoFactorFacExpiry">TwoFactorFacExpiry</a>: <i>Double</i>
    <a href="#twofactorftkexpiry" title="TwoFactorFtkExpiry">TwoFactorFtkExpiry</a>: <i>Double</i>
    <a href="#twofactorftmexpiry" title="TwoFactorFtmExpiry">TwoFactorFtmExpiry</a>: <i>Double</i>
    <a href="#twofactorsmsexpiry" title="TwoFactorSmsExpiry">TwoFactorSmsExpiry</a>: <i>Double</i>
    <a href="#udpidletimer" title="UdpIdleTimer">UdpIdleTimer</a>: <i>Double</i>
    <a href="#urlfilteraffinity" title="UrlFilterAffinity">UrlFilterAffinity</a>: <i>String</i>
    <a href="#urlfiltercount" title="UrlFilterCount">UrlFilterCount</a>: <i>Double</i>
    <a href="#userdevicestoremaxdevices" title="UserDeviceStoreMaxDevices">UserDeviceStoreMaxDevices</a>: <i>Double</i>
    <a href="#userdevicestoremaxusers" title="UserDeviceStoreMaxUsers">UserDeviceStoreMaxUsers</a>: <i>Double</i>
    <a href="#userservercert" title="UserServerCert">UserServerCert</a>: <i>String</i>
    <a href="#vdomadmin" title="VdomAdmin">VdomAdmin</a>: <i>String</i>
    <a href="#vdommode" title="VdomMode">VdomMode</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#viparprange" title="VipArpRange">VipArpRange</a>: <i>String</i>
    <a href="#virtualservercount" title="VirtualServerCount">VirtualServerCount</a>: <i>Double</i>
    <a href="#virtualserverhardwareacceleration" title="VirtualServerHardwareAcceleration">VirtualServerHardwareAcceleration</a>: <i>String</i>
    <a href="#wadaffinity" title="WadAffinity">WadAffinity</a>: <i>String</i>
    <a href="#wadcsvccscount" title="WadCsvcCsCount">WadCsvcCsCount</a>: <i>Double</i>
    <a href="#wadcsvcdbcount" title="WadCsvcDbCount">WadCsvcDbCount</a>: <i>Double</i>
    <a href="#wadmemorychangegranularity" title="WadMemoryChangeGranularity">WadMemoryChangeGranularity</a>: <i>Double</i>
    <a href="#wadsourceaffinity" title="WadSourceAffinity">WadSourceAffinity</a>: <i>String</i>
    <a href="#wadworkercount" title="WadWorkerCount">WadWorkerCount</a>: <i>Double</i>
    <a href="#wificacertificate" title="WifiCaCertificate">WifiCaCertificate</a>: <i>String</i>
    <a href="#wificertificate" title="WifiCertificate">WifiCertificate</a>: <i>String</i>
    <a href="#wimax4gusb" title="Wimax4gUsb">Wimax4gUsb</a>: <i>String</i>
    <a href="#wirelesscontroller" title="WirelessController">WirelessController</a>: <i>String</i>
    <a href="#wirelesscontrollerport" title="WirelessControllerPort">WirelessControllerPort</a>: <i>Double</i>
</pre>

## Properties

#### AdminConcurrent

Enable/disable concurrent administrator logins. (Use policy-auth-concurrent for firewall authenticated users.) Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminConsoleTimeout

Console login timeout that overrides the admintimeout value. (15 - 300 seconds) (15 seconds to 5 minutes). 0 the default, disables this timeout.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminHstsMaxAge

HTTPS Strict-Transport-Security header max-age in seconds. A value of 0 will reset any HSTS records in the browser.When admin-https-redirect is disabled the header max-age will be 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminHttpsPkiRequired

Enable/disable admin login method. Enable to force administrators to provide a valid certificate to log in if PKI is enabled. Disable to allow administrators to log in with a certificate or password. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminHttpsRedirect

Enable/disable redirection of HTTP administration access to HTTPS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminHttpsSslVersions

Allowed TLS versions for web administration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminLockoutDuration

Amount of time in seconds that an administrator account is locked out after reaching the admin-lockout-threshold for repeated failed login attempts.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminLockoutThreshold

Number of failed login attempts before an administrator account is locked out for the admin-lockout-duration.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminLoginMax

Maximum number of administrators who can be logged in at the same time (1 - 100, default = 100).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminMaintainer

Enable/disable maintainer administrator login. When enabled, the maintainer account can be used to log in from the console after a hard reboot. The password is "bcpb" followed by the FortiGate unit serial number. You have limited time to complete this login. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminPort

Administrative access port for HTTP. (1 - 65535, default = 80).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminRestrictLocal

Enable/disable local admin authentication restriction when remote authenticator is up and running. (default = disable) Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminScp

Enable/disable using SCP to download the system configuration. You can use SCP as an alternative method for backing up the configuration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminServerCert

Server certificate that the FortiGate uses for HTTPS administrative connections.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminSport

Administrative access port for HTTPS. (1 - 65535, default = 443).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminSshGraceTime

Maximum time in seconds permitted between making an SSH connection to the FortiGate unit and authenticating (10 - 3600 sec (1 hour), default 120).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminSshPassword

Enable/disable password authentication for SSH admin access. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminSshPort

Administrative access port for SSH. (1 - 65535, default = 22).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminSshV1

Enable/disable SSH v1 compatibility. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminTelnet

Enable/disable TELNET service. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminTelnetPort

Administrative access port for TELNET. (1 - 65535, default = 23).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Admintimeout

Number of minutes before an idle administrator session times out (5 - 480 minutes (8 hours), default = 5). A shorter idle timeout is more secure.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alias

Alias for your FortiGate unit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowTrafficRedirect

Disable to allow traffic to be routed back on a different interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiReplay

Level of checking for packet replay and TCP sequence checking. Valid values: `disable`, `loose`, `strict`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpMaxEntry

Maximum number of dynamically learned MAC addresses that can be added to the ARP table (131072 - 2147483647, default = 131072).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Asymroute

Enable/disable asymmetric route. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthCert

Server certificate that the FortiGate uses for HTTPS firewall authentication connections.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthHttpPort

User authentication HTTP port. (1 - 65535, default = 80).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthHttpsPort

User authentication HTTPS port. (1 - 65535, default = 443).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthKeepalive

Enable to prevent user authentication sessions from timing out when idle. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSessionLimit

Action to take when the number of allowed user authenticated sessions is reached. Valid values: `block-new`, `logout-inactive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAuthExtensionDevice

Enable/disable automatic authorization of dedicated Fortinet extension devices. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutorunLogFsck

Enable/disable automatic log partition check after ungraceful shutdown. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvAffinity

Affinity setting for AV scanning (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvFailopen

Set the action to take if the FortiGate is running low on memory or the proxy connection limit has been reached. Valid values: `pass`, `off`, `one-shot`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvFailopenSession

When enabled and a proxy for a protocol runs out of room in its session table, that protocol goes into failopen mode and enacts the action specified by av-failopen. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BatchCmdb

Enable/disable batch mode, allowing you to enter a series of CLI commands that will execute as a group once they are loaded. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockSessionTimer

Duration in seconds for blocked sessions (1 - 300 sec  (5 minutes), default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrFdbMaxEntry

Maximum number of bridge forwarding database (FDB) entries.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertChainMax

Maximum number of certificates that can be traversed in a certificate chain.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CfgRevertTimeout

Time-out for reverting to the last saved configuration.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CfgSave

Configuration file save mode for CLI changes. Valid values: `automatic`, `manual`, `revert`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckProtocolHeader

Level of checking performed on protocol headers. Strict checking is more thorough but may affect performance. Loose checking is ok in most cases. Valid values: `loose`, `strict`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckResetRange

Configure ICMP error message verification. You can either apply strict RST range checking or disable it. Valid values: `strict`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CliAuditLog

Enable/disable CLI audit log. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudCommunication

Enable/disable all cloud communication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CltCertReq

Enable/disable requiring administrators to have a client certificate to log into the GUI using HTTPS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceCheck

Enable/disable global PCI DSS compliance check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceCheckTime

Time of day to run scheduled PCI DSS compliance checks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuUseThreshold

Threshold at which CPU usage is reported. (% of total CPU, default = 90).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsrCaAttribute

Enable/disable the CA attribute in certificates. Some CA servers reject CSRs that have the CA attribute. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailyRestart

Enable/disable daily restart of FortiGate unit. Use the restart-time option to set the time of day for the restart. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultServiceSourcePort

Default service source port range. (default=1-65535).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceIdentificationActiveScanDelay

Number of seconds to passively scan a device before performing an active scan. (20 - 3600 sec, (20 sec to 1 hour), default = 90).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceIdleTimeout

Time in seconds that a device must be idle to automatically log the device user out. (30 - 31536000 sec (30 sec to 1 year), default = 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhParams

Number of bits to use in the Diffie-Hellman exchange for HTTPS/SSH protocols. Valid values: `1024`, `1536`, `2048`, `3072`, `4096`, `6144`, `8192`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsproxyWorkerCount

DNS proxy worker count.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dst

Enable/disable daylight saving time. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointControlFdsAccess

Enable/disable access to the FortiGuard network for non-compliant endpoints. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointControlPortalPort

Endpoint control portal port (1 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Failtime

Fail-time for server lost.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FazDiskBufferSize

Maximum disk buffer size to temporarily store logs destined for FortiAnalyzer. To be used in the event that FortiAnalyzer is unavailalble.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FdsStatistics

Enable/disable sending IPS, Application Control, and AntiVirus data to FortiGuard. This data is used to improve FortiGuard services and is not shared with external parties and is protected by Fortinet's privacy policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FdsStatisticsPeriod

FortiGuard statistics collection period in minutes. (1 - 1440 min (1 min to 24 hours), default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecPort

Local UDP port for Forward Error Correction (49152 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FgdAlertSubscription

Type of alert to retrieve from FortiGuard. Valid values: `advisory`, `latest-threat`, `latest-virus`, `latest-attack`, `new-antivirus-db`, `new-attack-db`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fortiextender

Enable/disable FortiExtender. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiextenderDataPort

FortiExtender data port (1024 - 49150, default = 25246).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiextenderVlanMode

Enable/disable FortiExtender VLAN mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiipamIntegration

Enable/disable integration with the FortiIPAM cloud service. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiservicePort

FortiService port (1 - 65535, default = 8013). Used by FortiClient endpoint compliance. Older versions of FortiClient used a different port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortitokenCloud

Enable/disable FortiToken Cloud service. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiAllowDefaultHostname

Enable/disable the GUI warning about using a default hostname Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiCertificates

Enable/disable the System > Certificate GUI page, allowing you to add and configure certificates from the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiCustomLanguage

Enable/disable custom languages in GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDateFormat

Default date format used throughout GUI. Valid values: `yyyy/MM/dd`, `dd/MM/yyyy`, `MM/dd/yyyy`, `yyyy-MM-dd`, `dd-MM-yyyy`, `MM-dd-yyyy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDateTimeSource

Source from which the FortiGate GUI uses to display date and time entries. Valid values: `system`, `browser`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDeviceLatitude

Add the latitude of the location of this FortiGate to position it on the Threat Map.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDeviceLongitude

Add the longitude of the location of this FortiGate to position it on the Threat Map.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDisplayHostname

Enable/disable displaying the FortiGate's hostname on the GUI login page. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiFirmwareUpgradeSetupWarning

Enable/disable the firmware upgrade warning on GUI setup wizard. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiFirmwareUpgradeWarning

Enable/disable the firmware upgrade warning on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiForticareRegistrationSetupWarning

Enable/disable the FortiCare registration setup warning on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiFortigateCloudSandbox

Enable/disable displaying FortiGate Cloud Sandbox on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiFortisandboxCloud

Enable/disable displaying FortiSandbox Cloud on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiIpv6

Enable/disable IPv6 settings on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiLinesPerPage

Number of lines to display per page for web administration.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiTheme

Color scheme for the administration GUI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiWirelessOpensecurity

Enable/disable wireless open security option on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HonorDf

Enable/disable honoring of Don't-Fragment (DF) flag. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

FortiGate unit's hostname. Most models will truncate names longer than 24 characters. Some models support hostnames up to 35 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgmpStateLimit

Maximum number of IGMP memberships (96 - 64000, default = 3200).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeEmbryonicLimit

Maximum number of IPsec tunnels to negotiate simultaneously.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

Dead gateway detection interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSrcPortRange

IP source port range used for traffic originating from the FortiGate unit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsAffinity

Affinity setting for IPS (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx; allowed CPUs must be less than total number of IPS engine daemons).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecAsicOffload

Enable/disable ASIC offloading (hardware acceleration) for IPsec VPN traffic. Hardware acceleration can offload IPsec VPN sessions and accelerate encryption and decryption. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecHmacOffload

Enable/disable offloading (hardware acceleration) of HMAC processing for IPsec VPN. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecSoftDecAsync

Enable/disable software decryption asynchronization (using multiple CPUs to do decryption) for IPsec VPN traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6AcceptDad

Enable/disable acceptance of IPv6 Duplicate Address Detection (DAD).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6AllowAnycastProbe

Enable/disable IPv6 address probe through Anycast. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6AllowTrafficRedirect

Disable to prevent IPv6 traffic with same local ingress and egress interface from being forwarded without policy check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IrqTimeAccounting

Configure CPU IRQ time accounting mode. Valid values: `auto`, `force`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Language

GUI display language. Valid values: `english`, `french`, `spanish`, `portuguese`, `japanese`, `trach`, `simch`, `korean`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ldapconntimeout

Global timeout for connections with remote LDAP servers in milliseconds (1 - 300000, default 500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpReception

Enable/disable Link Layer Discovery Protocol (LLDP) reception. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpTransmission

Enable/disable Link Layer Discovery Protocol (LLDP) transmission. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSslConnection

Enable/disable logging of SSL connection events. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogUuidAddress

Enable/disable insertion of address UUIDs to traffic logs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogUuidPolicy

Enable/disable insertion of policy UUIDs to traffic logs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginTimestamp

Enable/disable login time recording. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongVdomName

Enable/disable long VDOM name support. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementVdom

Management virtual domain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDlpstatMemory

Maximum DLP stat memory (0 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRouteCacheSize

Maximum number of IP route cache entries (0 - 2147483647).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McTtlNotchange

Enable/disable no modification of multicast TTL. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryUseThresholdExtreme

Threshold at which memory usage is considered extreme (new sessions are dropped) (% of total RAM, default = 95).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryUseThresholdGreen

Threshold at which memory usage forces the FortiGate to exit conserve mode (% of total RAM, default = 82).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryUseThresholdRed

Threshold at which memory usage forces the FortiGate to enter conserve mode (% of total RAM, default = 88).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MiglogAffinity

Affinity setting for logging (64-bit hexadecimal value in the format of xxxxxxxxxxxxxxxx).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MiglogdChildren

Number of logging (miglogd) processes to be allowed to run. Higher number can reduce performance; lower number can slow log processing time. No logs will be dropped or lost if the number is changed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiFactorAuthentication

Enforce all login methods to require an additional authentication factor (default = optional). Valid values: `optional`, `mandatory`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastForward

Enable/disable multicast forwarding. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NdpMaxEntry

Maximum number of NDP table entries (set to 65,536 or higher; if set to 0, kernel holds 65,536 entries).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerUserBal

Enable/disable per-user block/allow list filter. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerUserBwl

Enable/disable per-user black/white list filter. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyAuthConcurrent

Number of concurrent firewall use logins from the same user (1 - 100, default = 0 means no limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostLoginBanner

Enable/disable displaying the administrator access disclaimer message after an administrator successfully logs in. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreLoginBanner

Enable/disable displaying the administrator access disclaimer message on the login page before an administrator logs in. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateDataEncryption

Enable/disable private data encryption using an AES 128-bit key. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyAuthLifetime

Enable/disable authenticated users lifetime control.  This is a cap on the total time a proxy user can be authenticated for after which re-authentication will take place. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyAuthLifetimeTimeout

Lifetime timeout in minutes for authenticated users (5  - 65535 min, default=480 (8 hours)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyAuthTimeout

Authentication timeout in minutes for authenticated users (1 - 300 min, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyCipherHardwareAcceleration

Enable/disable using content processor (CP8 or CP9) hardware acceleration to encrypt and decrypt IPsec and SSL traffic. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyKxpHardwareAcceleration

Enable/disable using the content processor to accelerate KXP traffic. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyReAuthenticationMode

Control if users must re-authenticate after a session is closed, traffic has been idle, or from the point at which the user was first created. Valid values: `session`, `traffic`, `absolute`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyWorkerCount

Proxy worker count.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusPort

RADIUS service port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RebootUponConfigRestore

Enable/disable reboot of system upon restoring configuration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Refresh

Statistics refresh interval in GUI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remoteauthtimeout

Number of seconds that the FortiGate waits for responses from remote RADIUS, LDAP, or TACACS+ authentication servers. (0-300 sec, default = 5, 0 means no timeout).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetSessionlessTcp

Action to perform if the FortiGate receives a TCP packet but cannot find a corresponding session in its session table. NAT/Route mode only. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartTime

Daily restart time (hh:mm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevisionBackupOnLogout

Enable/disable back-up of the latest configuration revision when an administrator logs out of the CLI or GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevisionImageAutoBackup

Enable/disable back-up of the latest configuration revision after the firmware is upgraded. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanunitCount

Number of scanunits. The range and the default depend on the number of CPUs. Only available on FortiGate units with multiple CPUs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityRatingResultSubmission

Enable/disable the submission of Security Rating results to FortiGuard. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityRatingRunOnSchedule

Enable/disable scheduled runs of Security Rating. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendPmtuIcmp

Enable/disable sending of path maximum transmission unit (PMTU) - ICMP destination unreachable packet and to support PMTUD protocol on your network to reduce fragmentation of packets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatRouteChange

Enable/disable the ability to change the static NAT route. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecialFile23Support

Enable/disable IPS detection of HIBUN format files when using Data Leak Protection. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsdTrimDate

Date within a month to run ssd trim.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsdTrimFreq

How often to run SSD Trim (default = weekly). SSD Trim prevents SSD drive data loss by finding and isolating errors. Valid values: `never`, `hourly`, `daily`, `weekly`, `monthly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsdTrimHour

Hour of the day on which to run SSD Trim (0 - 23, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsdTrimMin

Minute of the hour on which to run SSD Trim (0 - 59, 60 for random).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsdTrimWeekday

Day of week to run SSD Trim. Valid values: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshCbcCipher

Enable/disable CBC cipher for SSH access. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshHmacMd5

Enable/disable HMAC-MD5 for SSH access. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKexSha1

Enable/disable SHA1 key exchange for SSH access. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshMacWeak

Enable/disable HMAC-SHA1 and UMAC-64-ETM for SSH access. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinProtoVersion

Minimum supported protocol version for SSL/TLS connections (default = TLSv1.2).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslStaticKeyCiphers

Enable/disable static key ciphers in SSL/TLS connections (e.g. AES128-SHA, AES256-SHA, AES128-SHA256, AES256-SHA256). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslvpnCipherHardwareAcceleration

Enable/disable SSL VPN hardware acceleration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslvpnEmsSnCheck

Enable/disable verification of EMS serial number in SSL-VPN connection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslvpnKxpHardwareAcceleration

Enable/disable SSL VPN KXP hardware acceleration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslvpnMaxWorkerCount

Maximum number of SSL VPN processes. Upper limit for this value is the number of CPUs and depends on the model.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslvpnPluginVersionCheck

Enable/disable checking browser's plugin version by SSL VPN. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictDirtySessionCheck

Enable to check the session against the original policy when revalidating. This can prevent dropping of redirected sessions when web-filtering and authentication are enabled together. If this option is enabled, the FortiGate unit deletes a session if a routing or policy change causes the session to no longer match the policy that originally allowed the session. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrongCrypto

Enable to use strong encryption and only allow strong ciphers (AES, 3DES) and digest (SHA1) for HTTPS/SSH/TLS/SSL functions. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchController

Enable/disable switch controller feature. Switch controller allows you to manage FortiSwitch from the FortiGate itself. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchControllerReservedNetwork

Enable reserved network subnet for controlled switches. This is available when the switch controller is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysPerfLogInterval

Time in minutes between updates of performance statistics logging. (1 - 15 min, default = 5, 0 = disabled).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpHalfcloseTimer

Number of seconds the FortiGate unit should wait to close a session after one peer has sent a FIN packet but the other has not responded (1 - 86400 sec (1 day), default = 120).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpHalfopenTimer

Number of seconds the FortiGate unit should wait to close a session after one peer has sent an open session packet but the other has not responded (1 - 86400 sec (1 day), default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpOption

Enable SACK, timestamp and MSS TCP options. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpTimewaitTimer

Length of the TCP TIME-WAIT state in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tftp

Enable/disable TFTP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Number corresponding to your time zone from 00 to 86. Enter set timezone ? to view the list of time zones and the numbers that represent them. Valid values: `01`, `02`, `03`, `04`, `05`, `81`, `06`, `07`, `08`, `09`, `10`, `11`, `12`, `13`, `74`, `14`, `77`, `15`, `87`, `16`, `17`, `18`, `19`, `20`, `75`, `21`, `22`, `23`, `24`, `80`, `79`, `25`, `26`, `27`, `28`, `78`, `29`, `30`, `31`, `32`, `33`, `34`, `35`, `36`, `37`, `38`, `83`, `84`, `40`, `85`, `41`, `42`, `43`, `39`, `44`, `46`, `47`, `51`, `48`, `45`, `49`, `50`, `52`, `53`, `54`, `55`, `56`, `57`, `58`, `59`, `60`, `62`, `63`, `61`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, `71`, `72`, `00`, `82`, `73`, `86`, `76`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TpMcSkipPolicy

Enable/disable skip policy check and allow multicast through. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficPriority

Choose Type of Service (ToS) or Differentiated Services Code Point (DSCP) for traffic prioritization in traffic shaping. Valid values: `tos`, `dscp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficPriorityLevel

Default system-wide level of priority for traffic prioritization. Valid values: `low`, `medium`, `high`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactorEmailExpiry

Email-based two-factor authentication session timeout (30 - 300 seconds (5 minutes), default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactorFacExpiry

FortiAuthenticator token authentication session timeout (10 - 3600 seconds (1 hour), default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactorFtkExpiry

FortiToken authentication session timeout (60 - 600 sec (10 minutes), default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactorFtmExpiry

FortiToken Mobile session timeout (1 - 168 hours (7 days), default = 72).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactorSmsExpiry

SMS-based two-factor authentication session timeout (30 - 300 sec, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpIdleTimer

UDP connection session timeout. This command can be useful in managing CPU and memory resources (1 - 86400 seconds (1 day), default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFilterAffinity

URL filter CPU affinity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFilterCount

URL filter daemon count.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDeviceStoreMaxDevices

Maximum number of devices allowed in user device store.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDeviceStoreMaxUsers

Maximum number of users allowed in user device store.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserServerCert

Certificate to use for https user authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VdomAdmin

Enable/disable support for multiple virtual domains (VDOMs). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VdomMode

Enable/disable support for split/multiple virtual domains (VDOMs). no-vdom:Disable split/multiple VDOMs mode. split-vdom:Enable split VDOMs mode. multi-vdom:Enable multiple VDOMs mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipArpRange

Controls the number of ARPs that the FortiGate sends for a Virtual IP (VIP) address range. Valid values: `unlimited`, `restricted`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualServerCount

Maximum number of virtual server processes to create. The maximum is the number of CPU cores. This is not available on single-core CPUs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualServerHardwareAcceleration

Enable/disable virtual server hardware acceleration. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WadAffinity

Affinity setting for wad (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WadCsvcCsCount

Number of concurrent WAD-cache-service object-cache processes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WadCsvcDbCount

Number of concurrent WAD-cache-service byte-cache processes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WadMemoryChangeGranularity

Minimum percentage change in system memory usage detected by the wad daemon prior to adjusting TCP window size for any active connection.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WadSourceAffinity

Enable/disable dispatching traffic to WAD workers based on source affinity. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WadWorkerCount

Number of explicit proxy WAN optimization daemon (WAD) processes. By default WAN optimization, explicit proxy, and web caching is handled by all of the CPU cores in a FortiGate unit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WifiCaCertificate

CA certificate that verifies the WiFi certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WifiCertificate

Certificate to use for WiFi authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wimax4gUsb

Enable/disable comparability with WiMAX 4G USB devices. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WirelessController

Enable/disable the wireless controller feature to use the FortiGate unit to manage FortiAPs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WirelessControllerPort

Port used for the control channel in wireless controller mode (wireless-mode is ac). The data channel port is the control channel port number plus one (1024 - 49150, default = 5246).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

