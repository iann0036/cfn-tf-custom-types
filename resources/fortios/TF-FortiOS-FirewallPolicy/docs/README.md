# TF::FortiOS::FirewallPolicy

Configure IPv4 policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallPolicy",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#antireplay" title="AntiReplay">AntiReplay</a>" : <i>String</i>,
        "<a href="#applicationlist" title="ApplicationList">ApplicationList</a>" : <i>String</i>,
        "<a href="#authcert" title="AuthCert">AuthCert</a>" : <i>String</i>,
        "<a href="#authpath" title="AuthPath">AuthPath</a>" : <i>String</i>,
        "<a href="#authredirectaddr" title="AuthRedirectAddr">AuthRedirectAddr</a>" : <i>String</i>,
        "<a href="#autoasicoffload" title="AutoAsicOffload">AutoAsicOffload</a>" : <i>String</i>,
        "<a href="#avprofile" title="AvProfile">AvProfile</a>" : <i>String</i>,
        "<a href="#blocknotification" title="BlockNotification">BlockNotification</a>" : <i>String</i>,
        "<a href="#captiveportalexempt" title="CaptivePortalExempt">CaptivePortalExempt</a>" : <i>String</i>,
        "<a href="#capturepacket" title="CapturePacket">CapturePacket</a>" : <i>String</i>,
        "<a href="#cifsprofile" title="CifsProfile">CifsProfile</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#decryptedtrafficmirror" title="DecryptedTrafficMirror">DecryptedTrafficMirror</a>" : <i>String</i>,
        "<a href="#delaytcpnpusession" title="DelayTcpNpuSession">DelayTcpNpuSession</a>" : <i>String</i>,
        "<a href="#diffservforward" title="DiffservForward">DiffservForward</a>" : <i>String</i>,
        "<a href="#diffservreverse" title="DiffservReverse">DiffservReverse</a>" : <i>String</i>,
        "<a href="#diffservcodeforward" title="DiffservcodeForward">DiffservcodeForward</a>" : <i>String</i>,
        "<a href="#diffservcoderev" title="DiffservcodeRev">DiffservcodeRev</a>" : <i>String</i>,
        "<a href="#disclaimer" title="Disclaimer">Disclaimer</a>" : <i>String</i>,
        "<a href="#dlpsensor" title="DlpSensor">DlpSensor</a>" : <i>String</i>,
        "<a href="#dnsfilterprofile" title="DnsfilterProfile">DnsfilterProfile</a>" : <i>String</i>,
        "<a href="#dsri" title="Dsri">Dsri</a>" : <i>String</i>,
        "<a href="#dstaddrnegate" title="DstaddrNegate">DstaddrNegate</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#emailcollect" title="EmailCollect">EmailCollect</a>" : <i>String</i>,
        "<a href="#emailfilterprofile" title="EmailfilterProfile">EmailfilterProfile</a>" : <i>String</i>,
        "<a href="#filefilterprofile" title="FileFilterProfile">FileFilterProfile</a>" : <i>String</i>,
        "<a href="#firewallsessiondirty" title="FirewallSessionDirty">FirewallSessionDirty</a>" : <i>String</i>,
        "<a href="#fixedport" title="Fixedport">Fixedport</a>" : <i>String</i>,
        "<a href="#fsso" title="Fsso">Fsso</a>" : <i>String</i>,
        "<a href="#fssoagentforntlm" title="FssoAgentForNtlm">FssoAgentForNtlm</a>" : <i>String</i>,
        "<a href="#geoipanycast" title="GeoipAnycast">GeoipAnycast</a>" : <i>String</i>,
        "<a href="#geoipmatch" title="GeoipMatch">GeoipMatch</a>" : <i>String</i>,
        "<a href="#globallabel" title="GlobalLabel">GlobalLabel</a>" : <i>String</i>,
        "<a href="#httppolicyredirect" title="HttpPolicyRedirect">HttpPolicyRedirect</a>" : <i>String</i>,
        "<a href="#icapprofile" title="IcapProfile">IcapProfile</a>" : <i>String</i>,
        "<a href="#identitybasedroute" title="IdentityBasedRoute">IdentityBasedRoute</a>" : <i>String</i>,
        "<a href="#inbound" title="Inbound">Inbound</a>" : <i>String</i>,
        "<a href="#inspectionmode" title="InspectionMode">InspectionMode</a>" : <i>String</i>,
        "<a href="#internetservice" title="InternetService">InternetService</a>" : <i>String</i>,
        "<a href="#internetservicenegate" title="InternetServiceNegate">InternetServiceNegate</a>" : <i>String</i>,
        "<a href="#internetservicesrc" title="InternetServiceSrc">InternetServiceSrc</a>" : <i>String</i>,
        "<a href="#internetservicesrcnegate" title="InternetServiceSrcNegate">InternetServiceSrcNegate</a>" : <i>String</i>,
        "<a href="#ippool" title="Ippool">Ippool</a>" : <i>String</i>,
        "<a href="#ipssensor" title="IpsSensor">IpsSensor</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#learningmode" title="LearningMode">LearningMode</a>" : <i>String</i>,
        "<a href="#logtraffic" title="Logtraffic">Logtraffic</a>" : <i>String</i>,
        "<a href="#logtrafficstart" title="LogtrafficStart">LogtrafficStart</a>" : <i>String</i>,
        "<a href="#matchvip" title="MatchVip">MatchVip</a>" : <i>String</i>,
        "<a href="#matchviponly" title="MatchVipOnly">MatchVipOnly</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nat" title="Nat">Nat</a>" : <i>String</i>,
        "<a href="#natinbound" title="Natinbound">Natinbound</a>" : <i>String</i>,
        "<a href="#natip" title="Natip">Natip</a>" : <i>String</i>,
        "<a href="#natoutbound" title="Natoutbound">Natoutbound</a>" : <i>String</i>,
        "<a href="#ntlm" title="Ntlm">Ntlm</a>" : <i>String</i>,
        "<a href="#ntlmguest" title="NtlmGuest">NtlmGuest</a>" : <i>String</i>,
        "<a href="#outbound" title="Outbound">Outbound</a>" : <i>String</i>,
        "<a href="#peripshaper" title="PerIpShaper">PerIpShaper</a>" : <i>String</i>,
        "<a href="#permitanyhost" title="PermitAnyHost">PermitAnyHost</a>" : <i>String</i>,
        "<a href="#permitstunhost" title="PermitStunHost">PermitStunHost</a>" : <i>String</i>,
        "<a href="#policyid" title="Policyid">Policyid</a>" : <i>Double</i>,
        "<a href="#profilegroup" title="ProfileGroup">ProfileGroup</a>" : <i>String</i>,
        "<a href="#profileprotocoloptions" title="ProfileProtocolOptions">ProfileProtocolOptions</a>" : <i>String</i>,
        "<a href="#profiletype" title="ProfileType">ProfileType</a>" : <i>String</i>,
        "<a href="#radiusmacauthbypass" title="RadiusMacAuthBypass">RadiusMacAuthBypass</a>" : <i>String</i>,
        "<a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>" : <i>String</i>,
        "<a href="#replacemsgoverridegroup" title="ReplacemsgOverrideGroup">ReplacemsgOverrideGroup</a>" : <i>String</i>,
        "<a href="#reputationdirection" title="ReputationDirection">ReputationDirection</a>" : <i>String</i>,
        "<a href="#reputationminimum" title="ReputationMinimum">ReputationMinimum</a>" : <i>Double</i>,
        "<a href="#rsso" title="Rsso">Rsso</a>" : <i>String</i>,
        "<a href="#rtpnat" title="RtpNat">RtpNat</a>" : <i>String</i>,
        "<a href="#scanbotnetconnections" title="ScanBotnetConnections">ScanBotnetConnections</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#scheduletimeout" title="ScheduleTimeout">ScheduleTimeout</a>" : <i>String</i>,
        "<a href="#senddenypacket" title="SendDenyPacket">SendDenyPacket</a>" : <i>String</i>,
        "<a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>" : <i>String</i>,
        "<a href="#sessionttl" title="SessionTtl">SessionTtl</a>" : <i>Double</i>,
        "<a href="#spamfilterprofile" title="SpamfilterProfile">SpamfilterProfile</a>" : <i>String</i>,
        "<a href="#srcaddrnegate" title="SrcaddrNegate">SrcaddrNegate</a>" : <i>String</i>,
        "<a href="#sshfilterprofile" title="SshFilterProfile">SshFilterProfile</a>" : <i>String</i>,
        "<a href="#sshpolicyredirect" title="SshPolicyRedirect">SshPolicyRedirect</a>" : <i>String</i>,
        "<a href="#sslmirror" title="SslMirror">SslMirror</a>" : <i>String</i>,
        "<a href="#sslsshprofile" title="SslSshProfile">SslSshProfile</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tcpmssreceiver" title="TcpMssReceiver">TcpMssReceiver</a>" : <i>Double</i>,
        "<a href="#tcpmsssender" title="TcpMssSender">TcpMssSender</a>" : <i>Double</i>,
        "<a href="#tcpsessionwithoutsyn" title="TcpSessionWithoutSyn">TcpSessionWithoutSyn</a>" : <i>String</i>,
        "<a href="#timeoutsendrst" title="TimeoutSendRst">TimeoutSendRst</a>" : <i>String</i>,
        "<a href="#tos" title="Tos">Tos</a>" : <i>String</i>,
        "<a href="#tosmask" title="TosMask">TosMask</a>" : <i>String</i>,
        "<a href="#tosnegate" title="TosNegate">TosNegate</a>" : <i>String</i>,
        "<a href="#trafficshaper" title="TrafficShaper">TrafficShaper</a>" : <i>String</i>,
        "<a href="#trafficshaperreverse" title="TrafficShaperReverse">TrafficShaperReverse</a>" : <i>String</i>,
        "<a href="#utmstatus" title="UtmStatus">UtmStatus</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vlancosfwd" title="VlanCosFwd">VlanCosFwd</a>" : <i>Double</i>,
        "<a href="#vlancosrev" title="VlanCosRev">VlanCosRev</a>" : <i>Double</i>,
        "<a href="#vlanfilter" title="VlanFilter">VlanFilter</a>" : <i>String</i>,
        "<a href="#voipprofile" title="VoipProfile">VoipProfile</a>" : <i>String</i>,
        "<a href="#vpntunnel" title="Vpntunnel">Vpntunnel</a>" : <i>String</i>,
        "<a href="#wafprofile" title="WafProfile">WafProfile</a>" : <i>String</i>,
        "<a href="#wanopt" title="Wanopt">Wanopt</a>" : <i>String</i>,
        "<a href="#wanoptdetection" title="WanoptDetection">WanoptDetection</a>" : <i>String</i>,
        "<a href="#wanoptpassiveopt" title="WanoptPassiveOpt">WanoptPassiveOpt</a>" : <i>String</i>,
        "<a href="#wanoptpeer" title="WanoptPeer">WanoptPeer</a>" : <i>String</i>,
        "<a href="#wanoptprofile" title="WanoptProfile">WanoptProfile</a>" : <i>String</i>,
        "<a href="#wccp" title="Wccp">Wccp</a>" : <i>String</i>,
        "<a href="#webcache" title="Webcache">Webcache</a>" : <i>String</i>,
        "<a href="#webcachehttps" title="WebcacheHttps">WebcacheHttps</a>" : <i>String</i>,
        "<a href="#webfilterprofile" title="WebfilterProfile">WebfilterProfile</a>" : <i>String</i>,
        "<a href="#webproxyforwardserver" title="WebproxyForwardServer">WebproxyForwardServer</a>" : <i>String</i>,
        "<a href="#webproxyprofile" title="WebproxyProfile">WebproxyProfile</a>" : <i>String</i>,
        "<a href="#wsso" title="Wsso">Wsso</a>" : <i>String</i>,
        "<a href="#appcategory" title="AppCategory">AppCategory</a>" : <i>[ <a href="appcategorydefinition.md">AppCategoryDefinition</a>, ... ]</i>,
        "<a href="#appgroup" title="AppGroup">AppGroup</a>" : <i>[ <a href="appgroupdefinition.md">AppGroupDefinition</a>, ... ]</i>,
        "<a href="#application" title="Application">Application</a>" : <i>[ <a href="applicationdefinition.md">ApplicationDefinition</a>, ... ]</i>,
        "<a href="#customlogfields" title="CustomLogFields">CustomLogFields</a>" : <i>[ <a href="customlogfieldsdefinition.md">CustomLogFieldsDefinition</a>, ... ]</i>,
        "<a href="#devices" title="Devices">Devices</a>" : <i>[ <a href="devicesdefinition.md">DevicesDefinition</a>, ... ]</i>,
        "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>[ <a href="dstaddrdefinition.md">DstaddrDefinition</a>, ... ]</i>,
        "<a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>" : <i>[ <a href="dstaddr6definition.md">Dstaddr6Definition</a>, ... ]</i>,
        "<a href="#dstintf" title="Dstintf">Dstintf</a>" : <i>[ <a href="dstintfdefinition.md">DstintfDefinition</a>, ... ]</i>,
        "<a href="#fssogroups" title="FssoGroups">FssoGroups</a>" : <i>[ <a href="fssogroupsdefinition.md">FssoGroupsDefinition</a>, ... ]</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ <a href="groupsdefinition.md">GroupsDefinition</a>, ... ]</i>,
        "<a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>" : <i>[ <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>, ... ]</i>,
        "<a href="#internetservicecustomgroup" title="InternetServiceCustomGroup">InternetServiceCustomGroup</a>" : <i>[ <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a>, ... ]</i>,
        "<a href="#internetservicegroup" title="InternetServiceGroup">InternetServiceGroup</a>" : <i>[ <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a>, ... ]</i>,
        "<a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>" : <i>[ <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>, ... ]</i>,
        "<a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>" : <i>[ <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrccustom" title="InternetServiceSrcCustom">InternetServiceSrcCustom</a>" : <i>[ <a href="internetservicesrccustomdefinition.md">InternetServiceSrcCustomDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrccustomgroup" title="InternetServiceSrcCustomGroup">InternetServiceSrcCustomGroup</a>" : <i>[ <a href="internetservicesrccustomgroupdefinition.md">InternetServiceSrcCustomGroupDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrcgroup" title="InternetServiceSrcGroup">InternetServiceSrcGroup</a>" : <i>[ <a href="internetservicesrcgroupdefinition.md">InternetServiceSrcGroupDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrcid" title="InternetServiceSrcId">InternetServiceSrcId</a>" : <i>[ <a href="internetservicesrciddefinition.md">InternetServiceSrcIdDefinition</a>, ... ]</i>,
        "<a href="#internetservicesrcname" title="InternetServiceSrcName">InternetServiceSrcName</a>" : <i>[ <a href="internetservicesrcnamedefinition.md">InternetServiceSrcNameDefinition</a>, ... ]</i>,
        "<a href="#ntlmenabledbrowsers" title="NtlmEnabledBrowsers">NtlmEnabledBrowsers</a>" : <i>[ <a href="ntlmenabledbrowsersdefinition.md">NtlmEnabledBrowsersDefinition</a>, ... ]</i>,
        "<a href="#poolname" title="Poolname">Poolname</a>" : <i>[ <a href="poolnamedefinition.md">PoolnameDefinition</a>, ... ]</i>,
        "<a href="#poolname6" title="Poolname6">Poolname6</a>" : <i>[ <a href="poolname6definition.md">Poolname6Definition</a>, ... ]</i>,
        "<a href="#rtpaddr" title="RtpAddr">RtpAddr</a>" : <i>[ <a href="rtpaddrdefinition.md">RtpAddrDefinition</a>, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ <a href="servicedefinition.md">ServiceDefinition</a>, ... ]</i>,
        "<a href="#srcvendormac" title="SrcVendorMac">SrcVendorMac</a>" : <i>[ <a href="srcvendormacdefinition.md">SrcVendorMacDefinition</a>, ... ]</i>,
        "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>[ <a href="srcaddrdefinition.md">SrcaddrDefinition</a>, ... ]</i>,
        "<a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>" : <i>[ <a href="srcaddr6definition.md">Srcaddr6Definition</a>, ... ]</i>,
        "<a href="#srcintf" title="Srcintf">Srcintf</a>" : <i>[ <a href="srcintfdefinition.md">SrcintfDefinition</a>, ... ]</i>,
        "<a href="#sslmirrorintf" title="SslMirrorIntf">SslMirrorIntf</a>" : <i>[ <a href="sslmirrorintfdefinition.md">SslMirrorIntfDefinition</a>, ... ]</i>,
        "<a href="#urlcategory" title="UrlCategory">UrlCategory</a>" : <i>[ <a href="urlcategorydefinition.md">UrlCategoryDefinition</a>, ... ]</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallPolicy
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#antireplay" title="AntiReplay">AntiReplay</a>: <i>String</i>
    <a href="#applicationlist" title="ApplicationList">ApplicationList</a>: <i>String</i>
    <a href="#authcert" title="AuthCert">AuthCert</a>: <i>String</i>
    <a href="#authpath" title="AuthPath">AuthPath</a>: <i>String</i>
    <a href="#authredirectaddr" title="AuthRedirectAddr">AuthRedirectAddr</a>: <i>String</i>
    <a href="#autoasicoffload" title="AutoAsicOffload">AutoAsicOffload</a>: <i>String</i>
    <a href="#avprofile" title="AvProfile">AvProfile</a>: <i>String</i>
    <a href="#blocknotification" title="BlockNotification">BlockNotification</a>: <i>String</i>
    <a href="#captiveportalexempt" title="CaptivePortalExempt">CaptivePortalExempt</a>: <i>String</i>
    <a href="#capturepacket" title="CapturePacket">CapturePacket</a>: <i>String</i>
    <a href="#cifsprofile" title="CifsProfile">CifsProfile</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#decryptedtrafficmirror" title="DecryptedTrafficMirror">DecryptedTrafficMirror</a>: <i>String</i>
    <a href="#delaytcpnpusession" title="DelayTcpNpuSession">DelayTcpNpuSession</a>: <i>String</i>
    <a href="#diffservforward" title="DiffservForward">DiffservForward</a>: <i>String</i>
    <a href="#diffservreverse" title="DiffservReverse">DiffservReverse</a>: <i>String</i>
    <a href="#diffservcodeforward" title="DiffservcodeForward">DiffservcodeForward</a>: <i>String</i>
    <a href="#diffservcoderev" title="DiffservcodeRev">DiffservcodeRev</a>: <i>String</i>
    <a href="#disclaimer" title="Disclaimer">Disclaimer</a>: <i>String</i>
    <a href="#dlpsensor" title="DlpSensor">DlpSensor</a>: <i>String</i>
    <a href="#dnsfilterprofile" title="DnsfilterProfile">DnsfilterProfile</a>: <i>String</i>
    <a href="#dsri" title="Dsri">Dsri</a>: <i>String</i>
    <a href="#dstaddrnegate" title="DstaddrNegate">DstaddrNegate</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#emailcollect" title="EmailCollect">EmailCollect</a>: <i>String</i>
    <a href="#emailfilterprofile" title="EmailfilterProfile">EmailfilterProfile</a>: <i>String</i>
    <a href="#filefilterprofile" title="FileFilterProfile">FileFilterProfile</a>: <i>String</i>
    <a href="#firewallsessiondirty" title="FirewallSessionDirty">FirewallSessionDirty</a>: <i>String</i>
    <a href="#fixedport" title="Fixedport">Fixedport</a>: <i>String</i>
    <a href="#fsso" title="Fsso">Fsso</a>: <i>String</i>
    <a href="#fssoagentforntlm" title="FssoAgentForNtlm">FssoAgentForNtlm</a>: <i>String</i>
    <a href="#geoipanycast" title="GeoipAnycast">GeoipAnycast</a>: <i>String</i>
    <a href="#geoipmatch" title="GeoipMatch">GeoipMatch</a>: <i>String</i>
    <a href="#globallabel" title="GlobalLabel">GlobalLabel</a>: <i>String</i>
    <a href="#httppolicyredirect" title="HttpPolicyRedirect">HttpPolicyRedirect</a>: <i>String</i>
    <a href="#icapprofile" title="IcapProfile">IcapProfile</a>: <i>String</i>
    <a href="#identitybasedroute" title="IdentityBasedRoute">IdentityBasedRoute</a>: <i>String</i>
    <a href="#inbound" title="Inbound">Inbound</a>: <i>String</i>
    <a href="#inspectionmode" title="InspectionMode">InspectionMode</a>: <i>String</i>
    <a href="#internetservice" title="InternetService">InternetService</a>: <i>String</i>
    <a href="#internetservicenegate" title="InternetServiceNegate">InternetServiceNegate</a>: <i>String</i>
    <a href="#internetservicesrc" title="InternetServiceSrc">InternetServiceSrc</a>: <i>String</i>
    <a href="#internetservicesrcnegate" title="InternetServiceSrcNegate">InternetServiceSrcNegate</a>: <i>String</i>
    <a href="#ippool" title="Ippool">Ippool</a>: <i>String</i>
    <a href="#ipssensor" title="IpsSensor">IpsSensor</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#learningmode" title="LearningMode">LearningMode</a>: <i>String</i>
    <a href="#logtraffic" title="Logtraffic">Logtraffic</a>: <i>String</i>
    <a href="#logtrafficstart" title="LogtrafficStart">LogtrafficStart</a>: <i>String</i>
    <a href="#matchvip" title="MatchVip">MatchVip</a>: <i>String</i>
    <a href="#matchviponly" title="MatchVipOnly">MatchVipOnly</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nat" title="Nat">Nat</a>: <i>String</i>
    <a href="#natinbound" title="Natinbound">Natinbound</a>: <i>String</i>
    <a href="#natip" title="Natip">Natip</a>: <i>String</i>
    <a href="#natoutbound" title="Natoutbound">Natoutbound</a>: <i>String</i>
    <a href="#ntlm" title="Ntlm">Ntlm</a>: <i>String</i>
    <a href="#ntlmguest" title="NtlmGuest">NtlmGuest</a>: <i>String</i>
    <a href="#outbound" title="Outbound">Outbound</a>: <i>String</i>
    <a href="#peripshaper" title="PerIpShaper">PerIpShaper</a>: <i>String</i>
    <a href="#permitanyhost" title="PermitAnyHost">PermitAnyHost</a>: <i>String</i>
    <a href="#permitstunhost" title="PermitStunHost">PermitStunHost</a>: <i>String</i>
    <a href="#policyid" title="Policyid">Policyid</a>: <i>Double</i>
    <a href="#profilegroup" title="ProfileGroup">ProfileGroup</a>: <i>String</i>
    <a href="#profileprotocoloptions" title="ProfileProtocolOptions">ProfileProtocolOptions</a>: <i>String</i>
    <a href="#profiletype" title="ProfileType">ProfileType</a>: <i>String</i>
    <a href="#radiusmacauthbypass" title="RadiusMacAuthBypass">RadiusMacAuthBypass</a>: <i>String</i>
    <a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>: <i>String</i>
    <a href="#replacemsgoverridegroup" title="ReplacemsgOverrideGroup">ReplacemsgOverrideGroup</a>: <i>String</i>
    <a href="#reputationdirection" title="ReputationDirection">ReputationDirection</a>: <i>String</i>
    <a href="#reputationminimum" title="ReputationMinimum">ReputationMinimum</a>: <i>Double</i>
    <a href="#rsso" title="Rsso">Rsso</a>: <i>String</i>
    <a href="#rtpnat" title="RtpNat">RtpNat</a>: <i>String</i>
    <a href="#scanbotnetconnections" title="ScanBotnetConnections">ScanBotnetConnections</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#scheduletimeout" title="ScheduleTimeout">ScheduleTimeout</a>: <i>String</i>
    <a href="#senddenypacket" title="SendDenyPacket">SendDenyPacket</a>: <i>String</i>
    <a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>: <i>String</i>
    <a href="#sessionttl" title="SessionTtl">SessionTtl</a>: <i>Double</i>
    <a href="#spamfilterprofile" title="SpamfilterProfile">SpamfilterProfile</a>: <i>String</i>
    <a href="#srcaddrnegate" title="SrcaddrNegate">SrcaddrNegate</a>: <i>String</i>
    <a href="#sshfilterprofile" title="SshFilterProfile">SshFilterProfile</a>: <i>String</i>
    <a href="#sshpolicyredirect" title="SshPolicyRedirect">SshPolicyRedirect</a>: <i>String</i>
    <a href="#sslmirror" title="SslMirror">SslMirror</a>: <i>String</i>
    <a href="#sslsshprofile" title="SslSshProfile">SslSshProfile</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tcpmssreceiver" title="TcpMssReceiver">TcpMssReceiver</a>: <i>Double</i>
    <a href="#tcpmsssender" title="TcpMssSender">TcpMssSender</a>: <i>Double</i>
    <a href="#tcpsessionwithoutsyn" title="TcpSessionWithoutSyn">TcpSessionWithoutSyn</a>: <i>String</i>
    <a href="#timeoutsendrst" title="TimeoutSendRst">TimeoutSendRst</a>: <i>String</i>
    <a href="#tos" title="Tos">Tos</a>: <i>String</i>
    <a href="#tosmask" title="TosMask">TosMask</a>: <i>String</i>
    <a href="#tosnegate" title="TosNegate">TosNegate</a>: <i>String</i>
    <a href="#trafficshaper" title="TrafficShaper">TrafficShaper</a>: <i>String</i>
    <a href="#trafficshaperreverse" title="TrafficShaperReverse">TrafficShaperReverse</a>: <i>String</i>
    <a href="#utmstatus" title="UtmStatus">UtmStatus</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vlancosfwd" title="VlanCosFwd">VlanCosFwd</a>: <i>Double</i>
    <a href="#vlancosrev" title="VlanCosRev">VlanCosRev</a>: <i>Double</i>
    <a href="#vlanfilter" title="VlanFilter">VlanFilter</a>: <i>String</i>
    <a href="#voipprofile" title="VoipProfile">VoipProfile</a>: <i>String</i>
    <a href="#vpntunnel" title="Vpntunnel">Vpntunnel</a>: <i>String</i>
    <a href="#wafprofile" title="WafProfile">WafProfile</a>: <i>String</i>
    <a href="#wanopt" title="Wanopt">Wanopt</a>: <i>String</i>
    <a href="#wanoptdetection" title="WanoptDetection">WanoptDetection</a>: <i>String</i>
    <a href="#wanoptpassiveopt" title="WanoptPassiveOpt">WanoptPassiveOpt</a>: <i>String</i>
    <a href="#wanoptpeer" title="WanoptPeer">WanoptPeer</a>: <i>String</i>
    <a href="#wanoptprofile" title="WanoptProfile">WanoptProfile</a>: <i>String</i>
    <a href="#wccp" title="Wccp">Wccp</a>: <i>String</i>
    <a href="#webcache" title="Webcache">Webcache</a>: <i>String</i>
    <a href="#webcachehttps" title="WebcacheHttps">WebcacheHttps</a>: <i>String</i>
    <a href="#webfilterprofile" title="WebfilterProfile">WebfilterProfile</a>: <i>String</i>
    <a href="#webproxyforwardserver" title="WebproxyForwardServer">WebproxyForwardServer</a>: <i>String</i>
    <a href="#webproxyprofile" title="WebproxyProfile">WebproxyProfile</a>: <i>String</i>
    <a href="#wsso" title="Wsso">Wsso</a>: <i>String</i>
    <a href="#appcategory" title="AppCategory">AppCategory</a>: <i>
      - <a href="appcategorydefinition.md">AppCategoryDefinition</a></i>
    <a href="#appgroup" title="AppGroup">AppGroup</a>: <i>
      - <a href="appgroupdefinition.md">AppGroupDefinition</a></i>
    <a href="#application" title="Application">Application</a>: <i>
      - <a href="applicationdefinition.md">ApplicationDefinition</a></i>
    <a href="#customlogfields" title="CustomLogFields">CustomLogFields</a>: <i>
      - <a href="customlogfieldsdefinition.md">CustomLogFieldsDefinition</a></i>
    <a href="#devices" title="Devices">Devices</a>: <i>
      - <a href="devicesdefinition.md">DevicesDefinition</a></i>
    <a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>
      - <a href="dstaddrdefinition.md">DstaddrDefinition</a></i>
    <a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>: <i>
      - <a href="dstaddr6definition.md">Dstaddr6Definition</a></i>
    <a href="#dstintf" title="Dstintf">Dstintf</a>: <i>
      - <a href="dstintfdefinition.md">DstintfDefinition</a></i>
    <a href="#fssogroups" title="FssoGroups">FssoGroups</a>: <i>
      - <a href="fssogroupsdefinition.md">FssoGroupsDefinition</a></i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - <a href="groupsdefinition.md">GroupsDefinition</a></i>
    <a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>: <i>
      - <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a></i>
    <a href="#internetservicecustomgroup" title="InternetServiceCustomGroup">InternetServiceCustomGroup</a>: <i>
      - <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a></i>
    <a href="#internetservicegroup" title="InternetServiceGroup">InternetServiceGroup</a>: <i>
      - <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a></i>
    <a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>: <i>
      - <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a></i>
    <a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>: <i>
      - <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a></i>
    <a href="#internetservicesrccustom" title="InternetServiceSrcCustom">InternetServiceSrcCustom</a>: <i>
      - <a href="internetservicesrccustomdefinition.md">InternetServiceSrcCustomDefinition</a></i>
    <a href="#internetservicesrccustomgroup" title="InternetServiceSrcCustomGroup">InternetServiceSrcCustomGroup</a>: <i>
      - <a href="internetservicesrccustomgroupdefinition.md">InternetServiceSrcCustomGroupDefinition</a></i>
    <a href="#internetservicesrcgroup" title="InternetServiceSrcGroup">InternetServiceSrcGroup</a>: <i>
      - <a href="internetservicesrcgroupdefinition.md">InternetServiceSrcGroupDefinition</a></i>
    <a href="#internetservicesrcid" title="InternetServiceSrcId">InternetServiceSrcId</a>: <i>
      - <a href="internetservicesrciddefinition.md">InternetServiceSrcIdDefinition</a></i>
    <a href="#internetservicesrcname" title="InternetServiceSrcName">InternetServiceSrcName</a>: <i>
      - <a href="internetservicesrcnamedefinition.md">InternetServiceSrcNameDefinition</a></i>
    <a href="#ntlmenabledbrowsers" title="NtlmEnabledBrowsers">NtlmEnabledBrowsers</a>: <i>
      - <a href="ntlmenabledbrowsersdefinition.md">NtlmEnabledBrowsersDefinition</a></i>
    <a href="#poolname" title="Poolname">Poolname</a>: <i>
      - <a href="poolnamedefinition.md">PoolnameDefinition</a></i>
    <a href="#poolname6" title="Poolname6">Poolname6</a>: <i>
      - <a href="poolname6definition.md">Poolname6Definition</a></i>
    <a href="#rtpaddr" title="RtpAddr">RtpAddr</a>: <i>
      - <a href="rtpaddrdefinition.md">RtpAddrDefinition</a></i>
    <a href="#service" title="Service">Service</a>: <i>
      - <a href="servicedefinition.md">ServiceDefinition</a></i>
    <a href="#srcvendormac" title="SrcVendorMac">SrcVendorMac</a>: <i>
      - <a href="srcvendormacdefinition.md">SrcVendorMacDefinition</a></i>
    <a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>
      - <a href="srcaddrdefinition.md">SrcaddrDefinition</a></i>
    <a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>: <i>
      - <a href="srcaddr6definition.md">Srcaddr6Definition</a></i>
    <a href="#srcintf" title="Srcintf">Srcintf</a>: <i>
      - <a href="srcintfdefinition.md">SrcintfDefinition</a></i>
    <a href="#sslmirrorintf" title="SslMirrorIntf">SslMirrorIntf</a>: <i>
      - <a href="sslmirrorintfdefinition.md">SslMirrorIntfDefinition</a></i>
    <a href="#urlcategory" title="UrlCategory">UrlCategory</a>: <i>
      - <a href="urlcategorydefinition.md">UrlCategoryDefinition</a></i>
    <a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### Action

Policy action (allow/deny/ipsec). Valid values: `accept`, `deny`, `ipsec`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiReplay

Enable/disable anti-replay check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationList

Name of an existing Application list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthCert

HTTPS server certificate for policy authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPath

Enable/disable authentication-based routing. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthRedirectAddr

HTTP-to-HTTPS redirect address for firewall authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAsicOffload

Enable/disable policy traffic ASIC offloading. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvProfile

Name of an existing Antivirus profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockNotification

Enable/disable block notification. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptivePortalExempt

Enable to exempt some users from the captive portal. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapturePacket

Enable/disable capture packets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CifsProfile

Name of an existing CIFS profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DecryptedTrafficMirror

Decrypted traffic mirror.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayTcpNpuSession

Enable TCP NPU session delay to guarantee packet order of 3-way handshake. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservForward

Enable to change packet's DiffServ values to the specified diffservcode-forward value. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservReverse

Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservcodeForward

Change packet's DiffServ to this value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservcodeRev

Change packet's reverse (reply) DiffServ to this value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disclaimer

Enable/disable user authentication disclaimer. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DlpSensor

Name of an existing DLP sensor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsfilterProfile

Name of an existing DNS filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dsri

Enable DSRI to ignore HTTP server responses. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstaddrNegate

When enabled dstaddr specifies what the destination address must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailCollect

Enable/disable email collection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailfilterProfile

Name of an existing email filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileFilterProfile

Name of an existing file-filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallSessionDirty

How to handle sessions if the configuration of this firewall policy changes. Valid values: `check-all`, `check-new`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fixedport

Enable to prevent source NAT from changing a session's source port. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fsso

Enable/disable Fortinet Single Sign-On. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FssoAgentForNtlm

FSSO agent to use for NTLM authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoipAnycast

Enable/disable recognition of anycast IP addresses using the geography IP database. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoipMatch

Match geography address based either on its physical location or registered location. Valid values: `physical-location`, `registered-location`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalLabel

Label for the policy that appears when the GUI is in Global View mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpPolicyRedirect

Redirect HTTP(S) traffic to matching transparent web proxy policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcapProfile

Name of an existing ICAP profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityBasedRoute

Name of identity-based routing rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inbound

Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectionMode

Policy inspection mode (Flow/proxy). Default is Flow mode. Valid values: `proxy`, `flow`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetService

Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.  Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceNegate

When enabled internet-service specifies what the service must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrc

Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.  Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcNegate

When enabled internet-service-src specifies what the service must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ippool

Enable to use IP Pools for source NAT. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsSensor

Name of an existing IPS sensor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

Label for the policy that appears when the GUI is in Section View mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LearningMode

Enable to allow everything, but log all of the meaningful data for security information gathering. A learning report will be generated. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logtraffic

Enable or disable logging. Log all sessions or security profile sessions. Valid values: `all`, `utm`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogtrafficStart

Record logs when a session starts. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchVip

Enable to match packets that have had their destination addresses changed by a VIP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchVipOnly

Enable/disable matching of only those packets that have had their destination addresses changed by a VIP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Policy name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nat

Enable/disable source NAT. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Natinbound

Policy-based IPsec VPN: apply destination NAT to inbound traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Natip

Policy-based IPsec VPN: source NAT IP address for outgoing traffic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Natoutbound

Policy-based IPsec VPN: apply source NAT to outbound traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ntlm

Enable/disable NTLM authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtlmGuest

Enable/disable NTLM guest user access. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outbound

Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerIpShaper

Per-IP traffic shaper.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitAnyHost

Accept UDP packets from any host. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitStunHost

Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policyid

Policy ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileGroup

Name of profile group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileProtocolOptions

Name of an existing Protocol options profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileType

Determine whether the firewall policy allows security profile groups or single profiles only. Valid values: `single`, `group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusMacAuthBypass

Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUrl

URL users are directed to after seeing and accepting the disclaimer or authenticating.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacemsgOverrideGroup

Override the default replacement message group for this policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReputationDirection

Direction of the initial traffic for reputation to take effect. Valid values: `source`, `destination`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReputationMinimum

Minimum Reputation to take action.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rsso

Enable/disable RADIUS single sign-on (RSSO). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RtpNat

Enable Real Time Protocol (RTP) NAT. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanBotnetConnections

Block or monitor connections to Botnet servers or disable Botnet scanning. Valid values: `disable`, `block`, `monitor`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

Schedule name.(Default is `always`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleTimeout

Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendDenyPacket

Enable to send a reply when a session is denied or blocked by a firewall policy. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceNegate

When enabled service specifies what the service must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTtl

TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamfilterProfile

Name of an existing Spam filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcaddrNegate

When enabled srcaddr specifies what the source address must NOT be. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshFilterProfile

Name of an existing SSH filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPolicyRedirect

Redirect SSH traffic to matching transparent proxy policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMirror

Enable to copy decrypted SSL traffic to a FortiGate interface (called SSL mirroring). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSshProfile

Name of an existing SSL SSH profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable or disable this policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMssReceiver

Receiver TCP maximum segment size (MSS).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMssSender

Sender TCP maximum segment size (MSS).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSessionWithoutSyn

Enable/disable creation of TCP session without SYN flag. Valid values: `all`, `data-only`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSendRst

Enable/disable sending RST packets when TCP sessions expire. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tos

ToS (Type of Service) value used for comparison.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TosMask

Non-zero bit positions are used for comparison while zero bit positions are ignored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TosNegate

Enable negated TOS match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficShaper

Traffic shaper.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficShaperReverse

Reverse traffic shaper.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtmStatus

Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

Universally Unique Identifier (UUID; automatically assigned but can be manually reset).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanCosFwd

VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanCosRev

VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanFilter

Set VLAN filters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VoipProfile

Name of an existing VoIP profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpntunnel

Policy-based IPsec VPN: name of the IPsec VPN Phase 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafProfile

Name of an existing Web application firewall profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wanopt

Enable/disable WAN optimization. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanoptDetection

WAN optimization auto-detection mode. Valid values: `active`, `passive`, `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanoptPassiveOpt

WAN optimization passive mode options. This option decides what IP address will be used to connect server. Valid values: `default`, `transparent`, `non-transparent`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanoptPeer

WAN optimization peer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanoptProfile

WAN optimization profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wccp

Enable/disable forwarding traffic matching this policy to a configured WCCP server. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webcache

Enable/disable web cache. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebcacheHttps

Enable/disable web cache for HTTPS. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterProfile

Name of an existing Web filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebproxyForwardServer

Web proxy forward server name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebproxyProfile

Webproxy profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wsso

Enable/disable WiFi Single Sign On (WSSO). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppCategory

_Required_: No

_Type_: List of <a href="appcategorydefinition.md">AppCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppGroup

_Required_: No

_Type_: List of <a href="appgroupdefinition.md">AppGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Application

_Required_: No

_Type_: List of <a href="applicationdefinition.md">ApplicationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomLogFields

_Required_: No

_Type_: List of <a href="customlogfieldsdefinition.md">CustomLogFieldsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: No

_Type_: List of <a href="devicesdefinition.md">DevicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

_Required_: No

_Type_: List of <a href="dstaddrdefinition.md">DstaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr6

_Required_: No

_Type_: List of <a href="dstaddr6definition.md">Dstaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstintf

_Required_: No

_Type_: List of <a href="dstintfdefinition.md">DstintfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FssoGroups

_Required_: No

_Type_: List of <a href="fssogroupsdefinition.md">FssoGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of <a href="groupsdefinition.md">GroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustom

_Required_: No

_Type_: List of <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustomGroup

_Required_: No

_Type_: List of <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceGroup

_Required_: No

_Type_: List of <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceId

_Required_: No

_Type_: List of <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceName

_Required_: No

_Type_: List of <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcCustom

_Required_: No

_Type_: List of <a href="internetservicesrccustomdefinition.md">InternetServiceSrcCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcCustomGroup

_Required_: No

_Type_: List of <a href="internetservicesrccustomgroupdefinition.md">InternetServiceSrcCustomGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcGroup

_Required_: No

_Type_: List of <a href="internetservicesrcgroupdefinition.md">InternetServiceSrcGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcId

_Required_: No

_Type_: List of <a href="internetservicesrciddefinition.md">InternetServiceSrcIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcName

_Required_: No

_Type_: List of <a href="internetservicesrcnamedefinition.md">InternetServiceSrcNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtlmEnabledBrowsers

_Required_: No

_Type_: List of <a href="ntlmenabledbrowsersdefinition.md">NtlmEnabledBrowsersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Poolname

_Required_: No

_Type_: List of <a href="poolnamedefinition.md">PoolnameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Poolname6

_Required_: No

_Type_: List of <a href="poolname6definition.md">Poolname6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RtpAddr

_Required_: No

_Type_: List of <a href="rtpaddrdefinition.md">RtpAddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="servicedefinition.md">ServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcVendorMac

_Required_: No

_Type_: List of <a href="srcvendormacdefinition.md">SrcVendorMacDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

_Required_: No

_Type_: List of <a href="srcaddrdefinition.md">SrcaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr6

_Required_: No

_Type_: List of <a href="srcaddr6definition.md">Srcaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcintf

_Required_: No

_Type_: List of <a href="srcintfdefinition.md">SrcintfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMirrorIntf

_Required_: No

_Type_: List of <a href="sslmirrorintfdefinition.md">SslMirrorIntfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlCategory

_Required_: No

_Type_: List of <a href="urlcategorydefinition.md">UrlCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of <a href="usersdefinition.md">UsersDefinition</a>

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

