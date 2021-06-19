# TF::FortiOS::WirelesscontrollerWtpprofile

Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerWtpprofile",
    "Properties" : {
        "<a href="#allowaccess" title="Allowaccess">Allowaccess</a>" : <i>String</i>,
        "<a href="#apcountry" title="ApCountry">ApCountry</a>" : <i>String</i>,
        "<a href="#aphandoff" title="ApHandoff">ApHandoff</a>" : <i>String</i>,
        "<a href="#apcfgprofile" title="ApcfgProfile">ApcfgProfile</a>" : <i>String</i>,
        "<a href="#bleprofile" title="BleProfile">BleProfile</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#controlmessageoffload" title="ControlMessageOffload">ControlMessageOffload</a>" : <i>String</i>,
        "<a href="#dtlsinkernel" title="DtlsInKernel">DtlsInKernel</a>" : <i>String</i>,
        "<a href="#dtlspolicy" title="DtlsPolicy">DtlsPolicy</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#energyefficientethernet" title="EnergyEfficientEthernet">EnergyEfficientEthernet</a>" : <i>String</i>,
        "<a href="#extinfoenable" title="ExtInfoEnable">ExtInfoEnable</a>" : <i>String</i>,
        "<a href="#frequencyhandoff" title="FrequencyHandoff">FrequencyHandoff</a>" : <i>String</i>,
        "<a href="#handoffroaming" title="HandoffRoaming">HandoffRoaming</a>" : <i>String</i>,
        "<a href="#handoffrssi" title="HandoffRssi">HandoffRssi</a>" : <i>Double</i>,
        "<a href="#handoffstathresh" title="HandoffStaThresh">HandoffStaThresh</a>" : <i>Double</i>,
        "<a href="#ipfragmentpreventing" title="IpFragmentPreventing">IpFragmentPreventing</a>" : <i>String</i>,
        "<a href="#ledstate" title="LedState">LedState</a>" : <i>String</i>,
        "<a href="#lldp" title="Lldp">Lldp</a>" : <i>String</i>,
        "<a href="#loginpasswd" title="LoginPasswd">LoginPasswd</a>" : <i>String</i>,
        "<a href="#loginpasswdchange" title="LoginPasswdChange">LoginPasswdChange</a>" : <i>String</i>,
        "<a href="#maxclients" title="MaxClients">MaxClients</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#poemode" title="PoeMode">PoeMode</a>" : <i>String</i>,
        "<a href="#splittunnelingacllocalapsubnet" title="SplitTunnelingAclLocalApSubnet">SplitTunnelingAclLocalApSubnet</a>" : <i>String</i>,
        "<a href="#splittunnelingaclpath" title="SplitTunnelingAclPath">SplitTunnelingAclPath</a>" : <i>String</i>,
        "<a href="#tunmtudownlink" title="TunMtuDownlink">TunMtuDownlink</a>" : <i>Double</i>,
        "<a href="#tunmtuuplink" title="TunMtuUplink">TunMtuUplink</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wanportmode" title="WanPortMode">WanPortMode</a>" : <i>String</i>,
        "<a href="#denymaclist" title="DenyMacList">DenyMacList</a>" : <i>[ <a href="denymaclistdefinition.md">DenyMacListDefinition</a>, ... ]</i>,
        "<a href="#lan" title="Lan">Lan</a>" : <i>[ <a href="landefinition.md">LanDefinition</a>, ... ]</i>,
        "<a href="#lbs" title="Lbs">Lbs</a>" : <i>[ <a href="lbsdefinition.md">LbsDefinition</a>, ... ]</i>,
        "<a href="#ledschedules" title="LedSchedules">LedSchedules</a>" : <i>[ <a href="ledschedulesdefinition.md">LedSchedulesDefinition</a>, ... ]</i>,
        "<a href="#platform" title="Platform">Platform</a>" : <i>[ <a href="platformdefinition.md">PlatformDefinition</a>, ... ]</i>,
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
Type: TF::FortiOS::WirelesscontrollerWtpprofile
Properties:
    <a href="#allowaccess" title="Allowaccess">Allowaccess</a>: <i>String</i>
    <a href="#apcountry" title="ApCountry">ApCountry</a>: <i>String</i>
    <a href="#aphandoff" title="ApHandoff">ApHandoff</a>: <i>String</i>
    <a href="#apcfgprofile" title="ApcfgProfile">ApcfgProfile</a>: <i>String</i>
    <a href="#bleprofile" title="BleProfile">BleProfile</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#controlmessageoffload" title="ControlMessageOffload">ControlMessageOffload</a>: <i>String</i>
    <a href="#dtlsinkernel" title="DtlsInKernel">DtlsInKernel</a>: <i>String</i>
    <a href="#dtlspolicy" title="DtlsPolicy">DtlsPolicy</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#energyefficientethernet" title="EnergyEfficientEthernet">EnergyEfficientEthernet</a>: <i>String</i>
    <a href="#extinfoenable" title="ExtInfoEnable">ExtInfoEnable</a>: <i>String</i>
    <a href="#frequencyhandoff" title="FrequencyHandoff">FrequencyHandoff</a>: <i>String</i>
    <a href="#handoffroaming" title="HandoffRoaming">HandoffRoaming</a>: <i>String</i>
    <a href="#handoffrssi" title="HandoffRssi">HandoffRssi</a>: <i>Double</i>
    <a href="#handoffstathresh" title="HandoffStaThresh">HandoffStaThresh</a>: <i>Double</i>
    <a href="#ipfragmentpreventing" title="IpFragmentPreventing">IpFragmentPreventing</a>: <i>String</i>
    <a href="#ledstate" title="LedState">LedState</a>: <i>String</i>
    <a href="#lldp" title="Lldp">Lldp</a>: <i>String</i>
    <a href="#loginpasswd" title="LoginPasswd">LoginPasswd</a>: <i>String</i>
    <a href="#loginpasswdchange" title="LoginPasswdChange">LoginPasswdChange</a>: <i>String</i>
    <a href="#maxclients" title="MaxClients">MaxClients</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#poemode" title="PoeMode">PoeMode</a>: <i>String</i>
    <a href="#splittunnelingacllocalapsubnet" title="SplitTunnelingAclLocalApSubnet">SplitTunnelingAclLocalApSubnet</a>: <i>String</i>
    <a href="#splittunnelingaclpath" title="SplitTunnelingAclPath">SplitTunnelingAclPath</a>: <i>String</i>
    <a href="#tunmtudownlink" title="TunMtuDownlink">TunMtuDownlink</a>: <i>Double</i>
    <a href="#tunmtuuplink" title="TunMtuUplink">TunMtuUplink</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wanportmode" title="WanPortMode">WanPortMode</a>: <i>String</i>
    <a href="#denymaclist" title="DenyMacList">DenyMacList</a>: <i>
      - <a href="denymaclistdefinition.md">DenyMacListDefinition</a></i>
    <a href="#lan" title="Lan">Lan</a>: <i>
      - <a href="landefinition.md">LanDefinition</a></i>
    <a href="#lbs" title="Lbs">Lbs</a>: <i>
      - <a href="lbsdefinition.md">LbsDefinition</a></i>
    <a href="#ledschedules" title="LedSchedules">LedSchedules</a>: <i>
      - <a href="ledschedulesdefinition.md">LedSchedulesDefinition</a></i>
    <a href="#platform" title="Platform">Platform</a>: <i>
      - <a href="platformdefinition.md">PlatformDefinition</a></i>
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

#### Allowaccess

Control management access to the managed WTP, FortiAP, or AP. Separate entries with a space.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApCountry

Country in which this WTP, FortiAP or AP will operate (default = NA, automatically use the country configured for the current VDOM).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApHandoff

Enable/disable AP handoff of clients to other APs (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApcfgProfile

AP local configuration profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BleProfile

Bluetooth Low Energy profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControlMessageOffload

Enable/disable CAPWAP control message data channel offload.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DtlsInKernel

Enable/disable data channel DTLS in kernel. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DtlsPolicy

WTP data channel DTLS policy (default = clear-text). Valid values: `clear-text`, `dtls-enabled`, `ipsec-vpn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnergyEfficientEthernet

Enable/disable use of energy efficient Ethernet on WTP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtInfoEnable

Enable/disable station/VAP/radio extension information. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrequencyHandoff

Enable/disable frequency handoff of clients to other channels (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandoffRoaming

Enable/disable client load balancing during roaming to avoid roaming delay (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandoffRssi

Minimum received signal strength indicator (RSSI) value for handoff (20 - 30, default = 25).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandoffStaThresh

Threshold value for AP handoff.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpFragmentPreventing

Select how to prevent IP fragmentation for CAPWAP tunneled control and data packets (default = tcp-mss-adjust). Valid values: `tcp-mss-adjust`, `icmp-unreachable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LedState

Enable/disable use of LEDs on WTP (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lldp

Enable/disable Link Layer Discovery Protocol (LLDP) for the WTP, FortiAP, or AP (default = disable). Valid values: `enable`, `disable`.

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

#### MaxClients

Maximum number of stations (STAs) supported by the WTP (default = 0, meaning no client limitation).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

WTP (or FortiAP or AP) profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoeMode

Set the WTP, FortiAP, or AP's PoE mode.

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

Downlink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunMtuUplink

Uplink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanPortMode

Enable/disable using a WAN port as a LAN port. Valid values: `wan-lan`, `wan-only`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenyMacList

_Required_: No

_Type_: List of <a href="denymaclistdefinition.md">DenyMacListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lan

_Required_: No

_Type_: List of <a href="landefinition.md">LanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lbs

_Required_: No

_Type_: List of <a href="lbsdefinition.md">LbsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LedSchedules

_Required_: No

_Type_: List of <a href="ledschedulesdefinition.md">LedSchedulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platform

_Required_: No

_Type_: List of <a href="platformdefinition.md">PlatformDefinition</a>

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

