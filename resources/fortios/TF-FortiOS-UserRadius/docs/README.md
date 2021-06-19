# TF::FortiOS::UserRadius

Configure RADIUS server entries.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::UserRadius",
    "Properties" : {
        "<a href="#acctallservers" title="AcctAllServers">AcctAllServers</a>" : <i>String</i>,
        "<a href="#acctinteriminterval" title="AcctInterimInterval">AcctInterimInterval</a>" : <i>Double</i>,
        "<a href="#allusergroup" title="AllUsergroup">AllUsergroup</a>" : <i>String</i>,
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#groupoverrideattrtype" title="GroupOverrideAttrType">GroupOverrideAttrType</a>" : <i>String</i>,
        "<a href="#h3ccompatibility" title="H3cCompatibility">H3cCompatibility</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nasip" title="NasIp">NasIp</a>" : <i>String</i>,
        "<a href="#passwordencoding" title="PasswordEncoding">PasswordEncoding</a>" : <i>String</i>,
        "<a href="#passwordrenewal" title="PasswordRenewal">PasswordRenewal</a>" : <i>String</i>,
        "<a href="#radiuscoa" title="RadiusCoa">RadiusCoa</a>" : <i>String</i>,
        "<a href="#radiusport" title="RadiusPort">RadiusPort</a>" : <i>Double</i>,
        "<a href="#rsso" title="Rsso">Rsso</a>" : <i>String</i>,
        "<a href="#rssocontexttimeout" title="RssoContextTimeout">RssoContextTimeout</a>" : <i>Double</i>,
        "<a href="#rssoendpointattribute" title="RssoEndpointAttribute">RssoEndpointAttribute</a>" : <i>String</i>,
        "<a href="#rssoendpointblockattribute" title="RssoEndpointBlockAttribute">RssoEndpointBlockAttribute</a>" : <i>String</i>,
        "<a href="#rssoeponeiponly" title="RssoEpOneIpOnly">RssoEpOneIpOnly</a>" : <i>String</i>,
        "<a href="#rssoflushipsession" title="RssoFlushIpSession">RssoFlushIpSession</a>" : <i>String</i>,
        "<a href="#rssologflags" title="RssoLogFlags">RssoLogFlags</a>" : <i>String</i>,
        "<a href="#rssologperiod" title="RssoLogPeriod">RssoLogPeriod</a>" : <i>Double</i>,
        "<a href="#rssoradiusresponse" title="RssoRadiusResponse">RssoRadiusResponse</a>" : <i>String</i>,
        "<a href="#rssoradiusserverport" title="RssoRadiusServerPort">RssoRadiusServerPort</a>" : <i>Double</i>,
        "<a href="#rssosecret" title="RssoSecret">RssoSecret</a>" : <i>String</i>,
        "<a href="#rssovalidaterequestsecret" title="RssoValidateRequestSecret">RssoValidateRequestSecret</a>" : <i>String</i>,
        "<a href="#secondarysecret" title="SecondarySecret">SecondarySecret</a>" : <i>String</i>,
        "<a href="#secondaryserver" title="SecondaryServer">SecondaryServer</a>" : <i>String</i>,
        "<a href="#secret" title="Secret">Secret</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#ssoattribute" title="SsoAttribute">SsoAttribute</a>" : <i>String</i>,
        "<a href="#ssoattributekey" title="SsoAttributeKey">SsoAttributeKey</a>" : <i>String</i>,
        "<a href="#ssoattributevalueoverride" title="SsoAttributeValueOverride">SsoAttributeValueOverride</a>" : <i>String</i>,
        "<a href="#switchcontrolleracctfastframedipdetect" title="SwitchControllerAcctFastFramedipDetect">SwitchControllerAcctFastFramedipDetect</a>" : <i>Double</i>,
        "<a href="#switchcontrollerservicetype" title="SwitchControllerServiceType">SwitchControllerServiceType</a>" : <i>String</i>,
        "<a href="#tertiarysecret" title="TertiarySecret">TertiarySecret</a>" : <i>String</i>,
        "<a href="#tertiaryserver" title="TertiaryServer">TertiaryServer</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#usemanagementvdom" title="UseManagementVdom">UseManagementVdom</a>" : <i>String</i>,
        "<a href="#usernamecasesensitive" title="UsernameCaseSensitive">UsernameCaseSensitive</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#accountingserver" title="AccountingServer">AccountingServer</a>" : <i>[ <a href="accountingserverdefinition.md">AccountingServerDefinition</a>, ... ]</i>,
        "<a href="#class" title="Class">Class</a>" : <i>[ <a href="classdefinition.md">ClassDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::UserRadius
Properties:
    <a href="#acctallservers" title="AcctAllServers">AcctAllServers</a>: <i>String</i>
    <a href="#acctinteriminterval" title="AcctInterimInterval">AcctInterimInterval</a>: <i>Double</i>
    <a href="#allusergroup" title="AllUsergroup">AllUsergroup</a>: <i>String</i>
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#groupoverrideattrtype" title="GroupOverrideAttrType">GroupOverrideAttrType</a>: <i>String</i>
    <a href="#h3ccompatibility" title="H3cCompatibility">H3cCompatibility</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nasip" title="NasIp">NasIp</a>: <i>String</i>
    <a href="#passwordencoding" title="PasswordEncoding">PasswordEncoding</a>: <i>String</i>
    <a href="#passwordrenewal" title="PasswordRenewal">PasswordRenewal</a>: <i>String</i>
    <a href="#radiuscoa" title="RadiusCoa">RadiusCoa</a>: <i>String</i>
    <a href="#radiusport" title="RadiusPort">RadiusPort</a>: <i>Double</i>
    <a href="#rsso" title="Rsso">Rsso</a>: <i>String</i>
    <a href="#rssocontexttimeout" title="RssoContextTimeout">RssoContextTimeout</a>: <i>Double</i>
    <a href="#rssoendpointattribute" title="RssoEndpointAttribute">RssoEndpointAttribute</a>: <i>String</i>
    <a href="#rssoendpointblockattribute" title="RssoEndpointBlockAttribute">RssoEndpointBlockAttribute</a>: <i>String</i>
    <a href="#rssoeponeiponly" title="RssoEpOneIpOnly">RssoEpOneIpOnly</a>: <i>String</i>
    <a href="#rssoflushipsession" title="RssoFlushIpSession">RssoFlushIpSession</a>: <i>String</i>
    <a href="#rssologflags" title="RssoLogFlags">RssoLogFlags</a>: <i>String</i>
    <a href="#rssologperiod" title="RssoLogPeriod">RssoLogPeriod</a>: <i>Double</i>
    <a href="#rssoradiusresponse" title="RssoRadiusResponse">RssoRadiusResponse</a>: <i>String</i>
    <a href="#rssoradiusserverport" title="RssoRadiusServerPort">RssoRadiusServerPort</a>: <i>Double</i>
    <a href="#rssosecret" title="RssoSecret">RssoSecret</a>: <i>String</i>
    <a href="#rssovalidaterequestsecret" title="RssoValidateRequestSecret">RssoValidateRequestSecret</a>: <i>String</i>
    <a href="#secondarysecret" title="SecondarySecret">SecondarySecret</a>: <i>String</i>
    <a href="#secondaryserver" title="SecondaryServer">SecondaryServer</a>: <i>String</i>
    <a href="#secret" title="Secret">Secret</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#ssoattribute" title="SsoAttribute">SsoAttribute</a>: <i>String</i>
    <a href="#ssoattributekey" title="SsoAttributeKey">SsoAttributeKey</a>: <i>String</i>
    <a href="#ssoattributevalueoverride" title="SsoAttributeValueOverride">SsoAttributeValueOverride</a>: <i>String</i>
    <a href="#switchcontrolleracctfastframedipdetect" title="SwitchControllerAcctFastFramedipDetect">SwitchControllerAcctFastFramedipDetect</a>: <i>Double</i>
    <a href="#switchcontrollerservicetype" title="SwitchControllerServiceType">SwitchControllerServiceType</a>: <i>String</i>
    <a href="#tertiarysecret" title="TertiarySecret">TertiarySecret</a>: <i>String</i>
    <a href="#tertiaryserver" title="TertiaryServer">TertiaryServer</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#usemanagementvdom" title="UseManagementVdom">UseManagementVdom</a>: <i>String</i>
    <a href="#usernamecasesensitive" title="UsernameCaseSensitive">UsernameCaseSensitive</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#accountingserver" title="AccountingServer">AccountingServer</a>: <i>
      - <a href="accountingserverdefinition.md">AccountingServerDefinition</a></i>
    <a href="#class" title="Class">Class</a>: <i>
      - <a href="classdefinition.md">ClassDefinition</a></i>
</pre>

## Properties

#### AcctAllServers

Enable/disable sending of accounting messages to all configured servers (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcctInterimInterval

Time in seconds between each accounting interim update message.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllUsergroup

Enable/disable automatically including this RADIUS server in all user groups. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

Authentication methods/protocols permitted for this RADIUS server. Valid values: `auto`, `ms_chap_v2`, `ms_chap`, `chap`, `pap`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupOverrideAttrType

RADIUS attribute type to override user group information. Valid values: `filter-Id`, `class`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### H3cCompatibility

Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Specify outgoing interface to reach server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

RADIUS server entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NasIp

IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordEncoding

Password encoding. Valid values: `auto`, `ISO-8859-1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordRenewal

Enable/disable password renewal. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusCoa

Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after it is authenticated. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusPort

RADIUS service port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rsso

Enable/disable RADIUS based single sign on feature. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoContextTimeout

Time in seconds before the logged out user is removed from the "user context list" of logged on users.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoEndpointAttribute

RADIUS attributes used to extract the user end point identifer from the RADIUS Start record. Valid values: `User-Name`, `NAS-IP-Address`, `Framed-IP-Address`, `Framed-IP-Netmask`, `Filter-Id`, `Login-IP-Host`, `Reply-Message`, `Callback-Number`, `Callback-Id`, `Framed-Route`, `Framed-IPX-Network`, `Class`, `Called-Station-Id`, `Calling-Station-Id`, `NAS-Identifier`, `Proxy-State`, `Login-LAT-Service`, `Login-LAT-Node`, `Login-LAT-Group`, `Framed-AppleTalk-Zone`, `Acct-Session-Id`, `Acct-Multi-Session-Id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoEndpointBlockAttribute

RADIUS attributes used to block a user. Valid values: `User-Name`, `NAS-IP-Address`, `Framed-IP-Address`, `Framed-IP-Netmask`, `Filter-Id`, `Login-IP-Host`, `Reply-Message`, `Callback-Number`, `Callback-Id`, `Framed-Route`, `Framed-IPX-Network`, `Class`, `Called-Station-Id`, `Calling-Station-Id`, `NAS-Identifier`, `Proxy-State`, `Login-LAT-Service`, `Login-LAT-Node`, `Login-LAT-Group`, `Framed-AppleTalk-Zone`, `Acct-Session-Id`, `Acct-Multi-Session-Id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoEpOneIpOnly

Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoFlushIpSession

Enable/disable flushing user IP sessions on RADIUS accounting Stop messages. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoLogFlags

Events to log. Valid values: `protocol-error`, `profile-missing`, `accounting-stop-missed`, `accounting-event`, `endpoint-block`, `radiusd-other`, `none`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoLogPeriod

Time interval in seconds that group event log messages will be generated for dynamic profile events.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoRadiusResponse

Enable/disable sending RADIUS response packets after receiving Start and Stop records. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoRadiusServerPort

UDP port to listen on for RADIUS Start and Stop records.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoSecret

RADIUS secret used by the RADIUS accounting server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RssoValidateRequestSecret

Enable/disable validating the RADIUS request shared secret in the Start or End record. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondarySecret

Secret key to access the secondary server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryServer

{<name_str|ip_str>} secondary RADIUS CN domain name or IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

Pre-shared secret key used to access the primary RADIUS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

Primary RADIUS server CN domain name or IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP address for communications to the RADIUS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoAttribute

RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record. Valid values: `User-Name`, `NAS-IP-Address`, `Framed-IP-Address`, `Framed-IP-Netmask`, `Filter-Id`, `Login-IP-Host`, `Reply-Message`, `Callback-Number`, `Callback-Id`, `Framed-Route`, `Framed-IPX-Network`, `Class`, `Called-Station-Id`, `Calling-Station-Id`, `NAS-Identifier`, `Proxy-State`, `Login-LAT-Service`, `Login-LAT-Node`, `Login-LAT-Group`, `Framed-AppleTalk-Zone`, `Acct-Session-Id`, `Acct-Multi-Session-Id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoAttributeKey

Key prefix for SSO group value in the SSO attribute.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoAttributeValueOverride

Enable/disable override old attribute value with new value for the same endpoint. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchControllerAcctFastFramedipDetect

Switch controller accounting message Framed-IP detection from DHCP snooping (seconds, default=2).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchControllerServiceType

RADIUS service type. Valid values: `login`, `framed`, `callback-login`, `callback-framed`, `outbound`, `administrative`, `nas-prompt`, `authenticate-only`, `callback-nas-prompt`, `call-check`, `callback-administrative`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TertiarySecret

Secret key to access the tertiary server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TertiaryServer

{<name_str|ip_str>} tertiary RADIUS CN domain name or IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Time in seconds between re-sending authentication requests.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseManagementVdom

Enable/disable using management VDOM to send requests. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameCaseSensitive

Enable/disable case sensitive user names. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountingServer

_Required_: No

_Type_: List of <a href="accountingserverdefinition.md">AccountingServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Class

_Required_: No

_Type_: List of <a href="classdefinition.md">ClassDefinition</a>

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

