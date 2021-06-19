# TF::FortiOS::WirelesscontrollerWtp

Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerWtp",
    "Properties" : {
        "<a href="#admin" title="Admin">Admin</a>" : <i>String</i>,
        "<a href="#allowaccess" title="Allowaccess">Allowaccess</a>" : <i>String</i>,
        "<a href="#apcfgprofile" title="ApcfgProfile">ApcfgProfile</a>" : <i>String</i>,
        "<a href="#bonjourprofile" title="BonjourProfile">BonjourProfile</a>" : <i>String</i>,
        "<a href="#coordinatelatitude" title="CoordinateLatitude">CoordinateLatitude</a>" : <i>String</i>,
        "<a href="#coordinatelongitude" title="CoordinateLongitude">CoordinateLongitude</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#firmwareprovision" title="FirmwareProvision">FirmwareProvision</a>" : <i>String</i>,
        "<a href="#imagedownload" title="ImageDownload">ImageDownload</a>" : <i>String</i>,
        "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
        "<a href="#ipfragmentpreventing" title="IpFragmentPreventing">IpFragmentPreventing</a>" : <i>String</i>,
        "<a href="#ledstate" title="LedState">LedState</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#loginpasswd" title="LoginPasswd">LoginPasswd</a>" : <i>String</i>,
        "<a href="#loginpasswdchange" title="LoginPasswdChange">LoginPasswdChange</a>" : <i>String</i>,
        "<a href="#meshbridgeenable" title="MeshBridgeEnable">MeshBridgeEnable</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overrideallowaccess" title="OverrideAllowaccess">OverrideAllowaccess</a>" : <i>String</i>,
        "<a href="#overrideipfragment" title="OverrideIpFragment">OverrideIpFragment</a>" : <i>String</i>,
        "<a href="#overridelan" title="OverrideLan">OverrideLan</a>" : <i>String</i>,
        "<a href="#overrideledstate" title="OverrideLedState">OverrideLedState</a>" : <i>String</i>,
        "<a href="#overrideloginpasswdchange" title="OverrideLoginPasswdChange">OverrideLoginPasswdChange</a>" : <i>String</i>,
        "<a href="#overridesplittunnel" title="OverrideSplitTunnel">OverrideSplitTunnel</a>" : <i>String</i>,
        "<a href="#overridewanportmode" title="OverrideWanPortMode">OverrideWanPortMode</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#regionx" title="RegionX">RegionX</a>" : <i>String</i>,
        "<a href="#regiony" title="RegionY">RegionY</a>" : <i>String</i>,
        "<a href="#splittunnelingacllocalapsubnet" title="SplitTunnelingAclLocalApSubnet">SplitTunnelingAclLocalApSubnet</a>" : <i>String</i>,
        "<a href="#splittunnelingaclpath" title="SplitTunnelingAclPath">SplitTunnelingAclPath</a>" : <i>String</i>,
        "<a href="#tunmtudownlink" title="TunMtuDownlink">TunMtuDownlink</a>" : <i>Double</i>,
        "<a href="#tunmtuuplink" title="TunMtuUplink">TunMtuUplink</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wanportmode" title="WanPortMode">WanPortMode</a>" : <i>String</i>,
        "<a href="#wtpid" title="WtpId">WtpId</a>" : <i>String</i>,
        "<a href="#wtpmode" title="WtpMode">WtpMode</a>" : <i>String</i>,
        "<a href="#wtpprofile" title="WtpProfile">WtpProfile</a>" : <i>String</i>,
        "<a href="#lan" title="Lan">Lan</a>" : <i>[ <a href="landefinition.md">LanDefinition</a>, ... ]</i>,
        "<a href="#radio1" title="Radio1">Radio1</a>" : <i>[ <a href="radio1definition.md">Radio1Definition</a>, ... ]</i>,
        "<a href="#radio2" title="Radio2">Radio2</a>" : <i>[ <a href="radio2definition.md">Radio2Definition</a>, ... ]</i>,
        "<a href="#radio3" title="Radio3">Radio3</a>" : <i>[ <a href="radio3definition.md">Radio3Definition</a>, ... ]</i>,
        "<a href="#radio4" title="Radio4">Radio4</a>" : <i>[ <a href="radio4definition.md">Radio4Definition</a>, ... ]</i>,
        "<a href="#splittunnelingacl" title="SplitTunnelingAcl">SplitTunnelingAcl</a>" : <i>[ <a href="splittunnelingacldefinition.md">SplitTunnelingAclDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerWtp
Properties:
    <a href="#admin" title="Admin">Admin</a>: <i>String</i>
    <a href="#allowaccess" title="Allowaccess">Allowaccess</a>: <i>String</i>
    <a href="#apcfgprofile" title="ApcfgProfile">ApcfgProfile</a>: <i>String</i>
    <a href="#bonjourprofile" title="BonjourProfile">BonjourProfile</a>: <i>String</i>
    <a href="#coordinatelatitude" title="CoordinateLatitude">CoordinateLatitude</a>: <i>String</i>
    <a href="#coordinatelongitude" title="CoordinateLongitude">CoordinateLongitude</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#firmwareprovision" title="FirmwareProvision">FirmwareProvision</a>: <i>String</i>
    <a href="#imagedownload" title="ImageDownload">ImageDownload</a>: <i>String</i>
    <a href="#index" title="Index">Index</a>: <i>Double</i>
    <a href="#ipfragmentpreventing" title="IpFragmentPreventing">IpFragmentPreventing</a>: <i>String</i>
    <a href="#ledstate" title="LedState">LedState</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#loginpasswd" title="LoginPasswd">LoginPasswd</a>: <i>String</i>
    <a href="#loginpasswdchange" title="LoginPasswdChange">LoginPasswdChange</a>: <i>String</i>
    <a href="#meshbridgeenable" title="MeshBridgeEnable">MeshBridgeEnable</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overrideallowaccess" title="OverrideAllowaccess">OverrideAllowaccess</a>: <i>String</i>
    <a href="#overrideipfragment" title="OverrideIpFragment">OverrideIpFragment</a>: <i>String</i>
    <a href="#overridelan" title="OverrideLan">OverrideLan</a>: <i>String</i>
    <a href="#overrideledstate" title="OverrideLedState">OverrideLedState</a>: <i>String</i>
    <a href="#overrideloginpasswdchange" title="OverrideLoginPasswdChange">OverrideLoginPasswdChange</a>: <i>String</i>
    <a href="#overridesplittunnel" title="OverrideSplitTunnel">OverrideSplitTunnel</a>: <i>String</i>
    <a href="#overridewanportmode" title="OverrideWanPortMode">OverrideWanPortMode</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#regionx" title="RegionX">RegionX</a>: <i>String</i>
    <a href="#regiony" title="RegionY">RegionY</a>: <i>String</i>
    <a href="#splittunnelingacllocalapsubnet" title="SplitTunnelingAclLocalApSubnet">SplitTunnelingAclLocalApSubnet</a>: <i>String</i>
    <a href="#splittunnelingaclpath" title="SplitTunnelingAclPath">SplitTunnelingAclPath</a>: <i>String</i>
    <a href="#tunmtudownlink" title="TunMtuDownlink">TunMtuDownlink</a>: <i>Double</i>
    <a href="#tunmtuuplink" title="TunMtuUplink">TunMtuUplink</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wanportmode" title="WanPortMode">WanPortMode</a>: <i>String</i>
    <a href="#wtpid" title="WtpId">WtpId</a>: <i>String</i>
    <a href="#wtpmode" title="WtpMode">WtpMode</a>: <i>String</i>
    <a href="#wtpprofile" title="WtpProfile">WtpProfile</a>: <i>String</i>
    <a href="#lan" title="Lan">Lan</a>: <i>
      - <a href="landefinition.md">LanDefinition</a></i>
    <a href="#radio1" title="Radio1">Radio1</a>: <i>
      - <a href="radio1definition.md">Radio1Definition</a></i>
    <a href="#radio2" title="Radio2">Radio2</a>: <i>
      - <a href="radio2definition.md">Radio2Definition</a></i>
    <a href="#radio3" title="Radio3">Radio3</a>: <i>
      - <a href="radio3definition.md">Radio3Definition</a></i>
    <a href="#radio4" title="Radio4">Radio4</a>: <i>
      - <a href="radio4definition.md">Radio4Definition</a></i>
    <a href="#splittunnelingacl" title="SplitTunnelingAcl">SplitTunnelingAcl</a>: <i>
      - <a href="splittunnelingacldefinition.md">SplitTunnelingAclDefinition</a></i>
</pre>

## Properties

#### Admin

Configure how the FortiGate operating as a wireless controller discovers and manages this WTP, AP or FortiAP. Valid values: `discovered`, `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Allowaccess

Control management access to the managed WTP, FortiAP, or AP. Separate entries with a space.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApcfgProfile

AP local configuration profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BonjourProfile

Bonjour profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoordinateLatitude

WTP latitude coordinate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoordinateLongitude

WTP longitude coordinate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirmwareProvision

Firmware version to provision to this FortiAP on bootup (major.minor.build, i.e. 6.2.1234).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageDownload

Enable/disable WTP image download. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

Index (0 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpFragmentPreventing

Method by which IP fragmentation is prevented for CAPWAP tunneled control and data packets (default = tcp-mss-adjust). Valid values: `tcp-mss-adjust`, `icmp-unreachable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LedState

Enable to allow the FortiAPs LEDs to light. Disable to keep the LEDs off. You may want to keep the LEDs off so they are not distracting in low light areas etc. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Field for describing the physical location of the WTP, AP or FortiAP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginPasswd

Set the managed WTP, FortiAP, or AP's administrator password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginPasswdChange

Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no). Valid values: `yes`, `default`, `no`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeshBridgeEnable

Enable/disable mesh Ethernet bridge when WTP is configured as a mesh branch/leaf AP. Valid values: `default`, `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

WTP, AP or FortiAP configuration name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideAllowaccess

Enable to override the WTP profile management access configuration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideIpFragment

Enable/disable overriding the WTP profile IP fragment prevention setting. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideLan

Enable to override the WTP profile LAN port setting. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideLedState

Enable to override the profile LED state setting for this FortiAP. You must enable this option to use the led-state command to turn off the FortiAP's LEDs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideLoginPasswdChange

Enable to override the WTP profile login-password (administrator password) setting. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideSplitTunnel

Enable/disable overriding the WTP profile split tunneling setting. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideWanPortMode

Enable/disable overriding the wan-port-mode in the WTP profile. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Region name WTP is associated with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionX

Relative horizontal region coordinate (between 0 and 1).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionY

Relative vertical region coordinate (between 0 and 1).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunnelingAclLocalApSubnet

Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunnelingAclPath

Split tunneling ACL path is local/tunnel. Valid values: `tunnel`, `local`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunMtuDownlink

Downlink tunnel MTU in octets. Set the value to either 0 (by default), 576, or 1500.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunMtuUplink

Uplink tunnel maximum transmission unit (MTU) in octets (eight-bit bytes). Set the value to either 0 (by default), 576, or 1500.

_Required_: No

_Type_: Double

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

#### WanPortMode

Enable/disable using the FortiAP WAN port as a LAN port. Valid values: `wan-lan`, `wan-only`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WtpId

WTP ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WtpMode

WTP, AP, or FortiAP operating mode; normal (by default) or remote. A tunnel mode SSID can be assigned to an AP in normal mode but not remote mode, while a local-bridge mode SSID can be assigned to an AP in either normal mode or remote mode. Valid values: `normal`, `remote`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WtpProfile

WTP profile name to apply to this WTP, AP or FortiAP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lan

_Required_: No

_Type_: List of <a href="landefinition.md">LanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Radio1

_Required_: No

_Type_: List of <a href="radio1definition.md">Radio1Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Radio2

_Required_: No

_Type_: List of <a href="radio2definition.md">Radio2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Radio3

_Required_: No

_Type_: List of <a href="radio3definition.md">Radio3Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Radio4

_Required_: No

_Type_: List of <a href="radio4definition.md">Radio4Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunnelingAcl

_Required_: No

_Type_: List of <a href="splittunnelingacldefinition.md">SplitTunnelingAclDefinition</a>

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

