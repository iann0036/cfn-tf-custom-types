# TF::FortiOS::FirewallVip6

Configure virtual IP for IPv6.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallVip6",
    "Properties" : {
        "<a href="#arpreply" title="ArpReply">ArpReply</a>" : <i>String</i>,
        "<a href="#color" title="Color">Color</a>" : <i>Double</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#extip" title="Extip">Extip</a>" : <i>String</i>,
        "<a href="#extport" title="Extport">Extport</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>Double</i>,
        "<a href="#httpcookieage" title="HttpCookieAge">HttpCookieAge</a>" : <i>Double</i>,
        "<a href="#httpcookiedomain" title="HttpCookieDomain">HttpCookieDomain</a>" : <i>String</i>,
        "<a href="#httpcookiedomainfromhost" title="HttpCookieDomainFromHost">HttpCookieDomainFromHost</a>" : <i>String</i>,
        "<a href="#httpcookiegeneration" title="HttpCookieGeneration">HttpCookieGeneration</a>" : <i>Double</i>,
        "<a href="#httpcookiepath" title="HttpCookiePath">HttpCookiePath</a>" : <i>String</i>,
        "<a href="#httpcookieshare" title="HttpCookieShare">HttpCookieShare</a>" : <i>String</i>,
        "<a href="#httpipheader" title="HttpIpHeader">HttpIpHeader</a>" : <i>String</i>,
        "<a href="#httpipheadername" title="HttpIpHeaderName">HttpIpHeaderName</a>" : <i>String</i>,
        "<a href="#httpmultiplex" title="HttpMultiplex">HttpMultiplex</a>" : <i>String</i>,
        "<a href="#httpredirect" title="HttpRedirect">HttpRedirect</a>" : <i>String</i>,
        "<a href="#httpscookiesecure" title="HttpsCookieSecure">HttpsCookieSecure</a>" : <i>String</i>,
        "<a href="#ldbmethod" title="LdbMethod">LdbMethod</a>" : <i>String</i>,
        "<a href="#mappedip" title="Mappedip">Mappedip</a>" : <i>String</i>,
        "<a href="#mappedport" title="Mappedport">Mappedport</a>" : <i>String</i>,
        "<a href="#maxembryonicconnections" title="MaxEmbryonicConnections">MaxEmbryonicConnections</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#natsourcevip" title="NatSourceVip">NatSourceVip</a>" : <i>String</i>,
        "<a href="#outlookwebaccess" title="OutlookWebAccess">OutlookWebAccess</a>" : <i>String</i>,
        "<a href="#persistence" title="Persistence">Persistence</a>" : <i>String</i>,
        "<a href="#portforward" title="Portforward">Portforward</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#servertype" title="ServerType">ServerType</a>" : <i>String</i>,
        "<a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>" : <i>String</i>,
        "<a href="#sslcertificate" title="SslCertificate">SslCertificate</a>" : <i>String</i>,
        "<a href="#sslclientfallback" title="SslClientFallback">SslClientFallback</a>" : <i>String</i>,
        "<a href="#sslclientrekeycount" title="SslClientRekeyCount">SslClientRekeyCount</a>" : <i>Double</i>,
        "<a href="#sslclientrenegotiation" title="SslClientRenegotiation">SslClientRenegotiation</a>" : <i>String</i>,
        "<a href="#sslclientsessionstatemax" title="SslClientSessionStateMax">SslClientSessionStateMax</a>" : <i>Double</i>,
        "<a href="#sslclientsessionstatetimeout" title="SslClientSessionStateTimeout">SslClientSessionStateTimeout</a>" : <i>Double</i>,
        "<a href="#sslclientsessionstatetype" title="SslClientSessionStateType">SslClientSessionStateType</a>" : <i>String</i>,
        "<a href="#ssldhbits" title="SslDhBits">SslDhBits</a>" : <i>String</i>,
        "<a href="#sslhpkp" title="SslHpkp">SslHpkp</a>" : <i>String</i>,
        "<a href="#sslhpkpage" title="SslHpkpAge">SslHpkpAge</a>" : <i>Double</i>,
        "<a href="#sslhpkpbackup" title="SslHpkpBackup">SslHpkpBackup</a>" : <i>String</i>,
        "<a href="#sslhpkpincludesubdomains" title="SslHpkpIncludeSubdomains">SslHpkpIncludeSubdomains</a>" : <i>String</i>,
        "<a href="#sslhpkpprimary" title="SslHpkpPrimary">SslHpkpPrimary</a>" : <i>String</i>,
        "<a href="#sslhpkpreporturi" title="SslHpkpReportUri">SslHpkpReportUri</a>" : <i>String</i>,
        "<a href="#sslhsts" title="SslHsts">SslHsts</a>" : <i>String</i>,
        "<a href="#sslhstsage" title="SslHstsAge">SslHstsAge</a>" : <i>Double</i>,
        "<a href="#sslhstsincludesubdomains" title="SslHstsIncludeSubdomains">SslHstsIncludeSubdomains</a>" : <i>String</i>,
        "<a href="#sslhttplocationconversion" title="SslHttpLocationConversion">SslHttpLocationConversion</a>" : <i>String</i>,
        "<a href="#sslhttpmatchhost" title="SslHttpMatchHost">SslHttpMatchHost</a>" : <i>String</i>,
        "<a href="#sslmaxversion" title="SslMaxVersion">SslMaxVersion</a>" : <i>String</i>,
        "<a href="#sslminversion" title="SslMinVersion">SslMinVersion</a>" : <i>String</i>,
        "<a href="#sslmode" title="SslMode">SslMode</a>" : <i>String</i>,
        "<a href="#sslpfs" title="SslPfs">SslPfs</a>" : <i>String</i>,
        "<a href="#sslsendemptyfrags" title="SslSendEmptyFrags">SslSendEmptyFrags</a>" : <i>String</i>,
        "<a href="#sslserveralgorithm" title="SslServerAlgorithm">SslServerAlgorithm</a>" : <i>String</i>,
        "<a href="#sslservermaxversion" title="SslServerMaxVersion">SslServerMaxVersion</a>" : <i>String</i>,
        "<a href="#sslserverminversion" title="SslServerMinVersion">SslServerMinVersion</a>" : <i>String</i>,
        "<a href="#sslserversessionstatemax" title="SslServerSessionStateMax">SslServerSessionStateMax</a>" : <i>Double</i>,
        "<a href="#sslserversessionstatetimeout" title="SslServerSessionStateTimeout">SslServerSessionStateTimeout</a>" : <i>Double</i>,
        "<a href="#sslserversessionstatetype" title="SslServerSessionStateType">SslServerSessionStateType</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#weblogicserver" title="WeblogicServer">WeblogicServer</a>" : <i>String</i>,
        "<a href="#websphereserver" title="WebsphereServer">WebsphereServer</a>" : <i>String</i>,
        "<a href="#monitor" title="Monitor">Monitor</a>" : <i>[ <a href="monitordefinition.md">MonitorDefinition</a>, ... ]</i>,
        "<a href="#realservers" title="Realservers">Realservers</a>" : <i>[ <a href="realserversdefinition.md">RealserversDefinition</a>, ... ]</i>,
        "<a href="#srcfilter" title="SrcFilter">SrcFilter</a>" : <i>[ <a href="srcfilterdefinition.md">SrcFilterDefinition</a>, ... ]</i>,
        "<a href="#sslciphersuites" title="SslCipherSuites">SslCipherSuites</a>" : <i>[ <a href="sslciphersuitesdefinition.md">SslCipherSuitesDefinition</a>, ... ]</i>,
        "<a href="#sslserverciphersuites" title="SslServerCipherSuites">SslServerCipherSuites</a>" : <i>[ <a href="sslserverciphersuitesdefinition.md">SslServerCipherSuitesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallVip6
Properties:
    <a href="#arpreply" title="ArpReply">ArpReply</a>: <i>String</i>
    <a href="#color" title="Color">Color</a>: <i>Double</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#extip" title="Extip">Extip</a>: <i>String</i>
    <a href="#extport" title="Extport">Extport</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>Double</i>
    <a href="#httpcookieage" title="HttpCookieAge">HttpCookieAge</a>: <i>Double</i>
    <a href="#httpcookiedomain" title="HttpCookieDomain">HttpCookieDomain</a>: <i>String</i>
    <a href="#httpcookiedomainfromhost" title="HttpCookieDomainFromHost">HttpCookieDomainFromHost</a>: <i>String</i>
    <a href="#httpcookiegeneration" title="HttpCookieGeneration">HttpCookieGeneration</a>: <i>Double</i>
    <a href="#httpcookiepath" title="HttpCookiePath">HttpCookiePath</a>: <i>String</i>
    <a href="#httpcookieshare" title="HttpCookieShare">HttpCookieShare</a>: <i>String</i>
    <a href="#httpipheader" title="HttpIpHeader">HttpIpHeader</a>: <i>String</i>
    <a href="#httpipheadername" title="HttpIpHeaderName">HttpIpHeaderName</a>: <i>String</i>
    <a href="#httpmultiplex" title="HttpMultiplex">HttpMultiplex</a>: <i>String</i>
    <a href="#httpredirect" title="HttpRedirect">HttpRedirect</a>: <i>String</i>
    <a href="#httpscookiesecure" title="HttpsCookieSecure">HttpsCookieSecure</a>: <i>String</i>
    <a href="#ldbmethod" title="LdbMethod">LdbMethod</a>: <i>String</i>
    <a href="#mappedip" title="Mappedip">Mappedip</a>: <i>String</i>
    <a href="#mappedport" title="Mappedport">Mappedport</a>: <i>String</i>
    <a href="#maxembryonicconnections" title="MaxEmbryonicConnections">MaxEmbryonicConnections</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#natsourcevip" title="NatSourceVip">NatSourceVip</a>: <i>String</i>
    <a href="#outlookwebaccess" title="OutlookWebAccess">OutlookWebAccess</a>: <i>String</i>
    <a href="#persistence" title="Persistence">Persistence</a>: <i>String</i>
    <a href="#portforward" title="Portforward">Portforward</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#servertype" title="ServerType">ServerType</a>: <i>String</i>
    <a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>: <i>String</i>
    <a href="#sslcertificate" title="SslCertificate">SslCertificate</a>: <i>String</i>
    <a href="#sslclientfallback" title="SslClientFallback">SslClientFallback</a>: <i>String</i>
    <a href="#sslclientrekeycount" title="SslClientRekeyCount">SslClientRekeyCount</a>: <i>Double</i>
    <a href="#sslclientrenegotiation" title="SslClientRenegotiation">SslClientRenegotiation</a>: <i>String</i>
    <a href="#sslclientsessionstatemax" title="SslClientSessionStateMax">SslClientSessionStateMax</a>: <i>Double</i>
    <a href="#sslclientsessionstatetimeout" title="SslClientSessionStateTimeout">SslClientSessionStateTimeout</a>: <i>Double</i>
    <a href="#sslclientsessionstatetype" title="SslClientSessionStateType">SslClientSessionStateType</a>: <i>String</i>
    <a href="#ssldhbits" title="SslDhBits">SslDhBits</a>: <i>String</i>
    <a href="#sslhpkp" title="SslHpkp">SslHpkp</a>: <i>String</i>
    <a href="#sslhpkpage" title="SslHpkpAge">SslHpkpAge</a>: <i>Double</i>
    <a href="#sslhpkpbackup" title="SslHpkpBackup">SslHpkpBackup</a>: <i>String</i>
    <a href="#sslhpkpincludesubdomains" title="SslHpkpIncludeSubdomains">SslHpkpIncludeSubdomains</a>: <i>String</i>
    <a href="#sslhpkpprimary" title="SslHpkpPrimary">SslHpkpPrimary</a>: <i>String</i>
    <a href="#sslhpkpreporturi" title="SslHpkpReportUri">SslHpkpReportUri</a>: <i>String</i>
    <a href="#sslhsts" title="SslHsts">SslHsts</a>: <i>String</i>
    <a href="#sslhstsage" title="SslHstsAge">SslHstsAge</a>: <i>Double</i>
    <a href="#sslhstsincludesubdomains" title="SslHstsIncludeSubdomains">SslHstsIncludeSubdomains</a>: <i>String</i>
    <a href="#sslhttplocationconversion" title="SslHttpLocationConversion">SslHttpLocationConversion</a>: <i>String</i>
    <a href="#sslhttpmatchhost" title="SslHttpMatchHost">SslHttpMatchHost</a>: <i>String</i>
    <a href="#sslmaxversion" title="SslMaxVersion">SslMaxVersion</a>: <i>String</i>
    <a href="#sslminversion" title="SslMinVersion">SslMinVersion</a>: <i>String</i>
    <a href="#sslmode" title="SslMode">SslMode</a>: <i>String</i>
    <a href="#sslpfs" title="SslPfs">SslPfs</a>: <i>String</i>
    <a href="#sslsendemptyfrags" title="SslSendEmptyFrags">SslSendEmptyFrags</a>: <i>String</i>
    <a href="#sslserveralgorithm" title="SslServerAlgorithm">SslServerAlgorithm</a>: <i>String</i>
    <a href="#sslservermaxversion" title="SslServerMaxVersion">SslServerMaxVersion</a>: <i>String</i>
    <a href="#sslserverminversion" title="SslServerMinVersion">SslServerMinVersion</a>: <i>String</i>
    <a href="#sslserversessionstatemax" title="SslServerSessionStateMax">SslServerSessionStateMax</a>: <i>Double</i>
    <a href="#sslserversessionstatetimeout" title="SslServerSessionStateTimeout">SslServerSessionStateTimeout</a>: <i>Double</i>
    <a href="#sslserversessionstatetype" title="SslServerSessionStateType">SslServerSessionStateType</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#weblogicserver" title="WeblogicServer">WeblogicServer</a>: <i>String</i>
    <a href="#websphereserver" title="WebsphereServer">WebsphereServer</a>: <i>String</i>
    <a href="#monitor" title="Monitor">Monitor</a>: <i>
      - <a href="monitordefinition.md">MonitorDefinition</a></i>
    <a href="#realservers" title="Realservers">Realservers</a>: <i>
      - <a href="realserversdefinition.md">RealserversDefinition</a></i>
    <a href="#srcfilter" title="SrcFilter">SrcFilter</a>: <i>
      - <a href="srcfilterdefinition.md">SrcFilterDefinition</a></i>
    <a href="#sslciphersuites" title="SslCipherSuites">SslCipherSuites</a>: <i>
      - <a href="sslciphersuitesdefinition.md">SslCipherSuitesDefinition</a></i>
    <a href="#sslserverciphersuites" title="SslServerCipherSuites">SslServerCipherSuites</a>: <i>
      - <a href="sslserverciphersuitesdefinition.md">SslServerCipherSuitesDefinition</a></i>
</pre>

## Properties

#### ArpReply

Enable to respond to ARP requests for this virtual IP address. Enabled by default. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

Color of icon on the GUI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extip

IP address or address range on the external interface that you want to map to an address or address range on the destination network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extport

Incoming port number range that you want to map to a port number range on the destination network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

Custom defined ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCookieAge

Time in minutes that client web browsers should keep a cookie. Default is 60 seconds. 0 = no time limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCookieDomain

Domain that HTTP cookie persistence should apply to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCookieDomainFromHost

Enable/disable use of HTTP cookie domain from host field in HTTP. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCookieGeneration

Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCookiePath

Limit HTTP cookie persistence to the specified path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCookieShare

Control sharing of cookies across virtual servers. same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing. Valid values: `disable`, `same-ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpIpHeader

For HTTP multiplexing, enable to add the original client IP address in the XForwarded-For HTTP header. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpIpHeaderName

For HTTP multiplexing, enter a custom HTTPS header name. The original client IP address is added to this header. If empty, X-Forwarded-For is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMultiplex

Enable/disable HTTP multiplexing. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRedirect

Enable/disable redirection of HTTP to HTTPS Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsCookieSecure

Enable/disable verification that inserted HTTPS cookies are secure. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdbMethod

Method used to distribute sessions to real servers. Valid values: `static`, `round-robin`, `weighted`, `least-session`, `least-rtt`, `first-alive`, `http-host`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mappedip

Mapped IP address range in the format startIP-endIP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mappedport

Port number range on the destination network to which the external port number range is mapped.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxEmbryonicConnections

Maximum number of incomplete connections.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Virtual ip6 name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatSourceVip

Enable to perform SNAT on traffic from mappedip to the extip for all egress interfaces. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutlookWebAccess

Enable to add the Front-End-Https header for Microsoft Outlook Web Access. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Persistence

Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session. Valid values: `none`, `http-cookie`, `ssl-session-id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Portforward

Enable port forwarding. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol to use when forwarding packets. Valid values: `tcp`, `udp`, `sctp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

Protocol to be load balanced by the virtual server (also called the server load balance virtual IP). Valid values: `http`, `https`, `imaps`, `pop3s`, `smtps`, `ssl`, `tcp`, `udp`, `ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAlgorithm

Permitted encryption algorithms for SSL sessions according to encryption strength. Valid values: `high`, `medium`, `low`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificate

The name of the SSL certificate to use for SSL acceleration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientFallback

Enable/disable support for preventing Downgrade Attacks on client connections (RFC 7507). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientRekeyCount

Maximum length of data in MB before triggering a client rekey (0 = disable).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientRenegotiation

Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746. Valid values: `allow`, `deny`, `secure`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientSessionStateMax

Maximum number of client to FortiGate SSL session states to keep.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientSessionStateTimeout

Number of minutes to keep client to FortiGate SSL session state.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientSessionStateType

How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate. Valid values: `disable`, `time`, `count`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslDhBits

Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions. Valid values: `768`, `1024`, `1536`, `2048`, `3072`, `4096`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHpkp

Enable/disable including HPKP header in response. Valid values: `disable`, `enable`, `report-only`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHpkpAge

Number of minutes the web browser should keep HPKP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHpkpBackup

Certificate to generate backup HPKP pin from.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHpkpIncludeSubdomains

Indicate that HPKP header applies to all subdomains. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHpkpPrimary

Certificate to generate primary HPKP pin from.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHpkpReportUri

URL to report HPKP violations to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHsts

Enable/disable including HSTS header in response. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHstsAge

Number of seconds the client should honour the HSTS setting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHstsIncludeSubdomains

Indicate that HSTS header applies to all subdomains. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHttpLocationConversion

Enable to replace HTTP with HTTPS in the reply's Location HTTP header field. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHttpMatchHost

Enable/disable HTTP host matching for location conversion. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMaxVersion

Highest SSL/TLS version acceptable from a client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinVersion

Lowest SSL/TLS version acceptable from a client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMode

Apply SSL offloading between the client and the FortiGate (half) or from the client to the FortiGate and from the FortiGate to the server (full). Valid values: `half`, `full`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPfs

Select the cipher suites that can be used for SSL perfect forward secrecy (PFS). Applies to both client and server sessions. Valid values: `require`, `deny`, `allow`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSendEmptyFrags

Enable/disable sending empty fragments to avoid CBC IV attacks (SSL 3.0 & TLS 1.0 only). May need to be disabled for compatibility with older systems. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServerAlgorithm

Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength. Valid values: `high`, `medium`, `low`, `custom`, `client`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServerMaxVersion

Highest SSL/TLS version acceptable from a server. Use the client setting by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServerMinVersion

Lowest SSL/TLS version acceptable from a server. Use the client setting by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServerSessionStateMax

Maximum number of FortiGate to Server SSL session states to keep.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServerSessionStateTimeout

Number of minutes to keep FortiGate to Server SSL session state.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServerSessionStateType

How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate. Valid values: `disable`, `time`, `count`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Configure a static NAT or server load balance VIP. Valid values: `static-nat`, `server-load-balance`.

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

#### WeblogicServer

Enable to add an HTTP header to indicate SSL offloading for a WebLogic server. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsphereServer

Enable to add an HTTP header to indicate SSL offloading for a WebSphere server. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No

_Type_: List of <a href="monitordefinition.md">MonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realservers

_Required_: No

_Type_: List of <a href="realserversdefinition.md">RealserversDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcFilter

_Required_: No

_Type_: List of <a href="srcfilterdefinition.md">SrcFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCipherSuites

_Required_: No

_Type_: List of <a href="sslciphersuitesdefinition.md">SslCipherSuitesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServerCipherSuites

_Required_: No

_Type_: List of <a href="sslserverciphersuitesdefinition.md">SslServerCipherSuitesDefinition</a>

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

