# TF::FortiOS::SystemAccprofile

Configure access profiles for system administrators.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemAccprofile",
    "Properties" : {
        "<a href="#admintimeout" title="Admintimeout">Admintimeout</a>" : <i>Double</i>,
        "<a href="#admintimeoutoverride" title="AdmintimeoutOverride">AdmintimeoutOverride</a>" : <i>String</i>,
        "<a href="#authgrp" title="Authgrp">Authgrp</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#ftviewgrp" title="Ftviewgrp">Ftviewgrp</a>" : <i>String</i>,
        "<a href="#fwgrp" title="Fwgrp">Fwgrp</a>" : <i>String</i>,
        "<a href="#loggrp" title="Loggrp">Loggrp</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netgrp" title="Netgrp">Netgrp</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#secfabgrp" title="Secfabgrp">Secfabgrp</a>" : <i>String</i>,
        "<a href="#sysgrp" title="Sysgrp">Sysgrp</a>" : <i>String</i>,
        "<a href="#systemdiagnostics" title="SystemDiagnostics">SystemDiagnostics</a>" : <i>String</i>,
        "<a href="#utmgrp" title="Utmgrp">Utmgrp</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vpngrp" title="Vpngrp">Vpngrp</a>" : <i>String</i>,
        "<a href="#wanoptgrp" title="Wanoptgrp">Wanoptgrp</a>" : <i>String</i>,
        "<a href="#wifi" title="Wifi">Wifi</a>" : <i>String</i>,
        "<a href="#fwgrppermission" title="FwgrpPermission">FwgrpPermission</a>" : <i>[ <a href="fwgrppermissiondefinition.md">FwgrpPermissionDefinition</a>, ... ]</i>,
        "<a href="#loggrppermission" title="LoggrpPermission">LoggrpPermission</a>" : <i>[ <a href="loggrppermissiondefinition.md">LoggrpPermissionDefinition</a>, ... ]</i>,
        "<a href="#netgrppermission" title="NetgrpPermission">NetgrpPermission</a>" : <i>[ <a href="netgrppermissiondefinition.md">NetgrpPermissionDefinition</a>, ... ]</i>,
        "<a href="#sysgrppermission" title="SysgrpPermission">SysgrpPermission</a>" : <i>[ <a href="sysgrppermissiondefinition.md">SysgrpPermissionDefinition</a>, ... ]</i>,
        "<a href="#utmgrppermission" title="UtmgrpPermission">UtmgrpPermission</a>" : <i>[ <a href="utmgrppermissiondefinition.md">UtmgrpPermissionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemAccprofile
Properties:
    <a href="#admintimeout" title="Admintimeout">Admintimeout</a>: <i>Double</i>
    <a href="#admintimeoutoverride" title="AdmintimeoutOverride">AdmintimeoutOverride</a>: <i>String</i>
    <a href="#authgrp" title="Authgrp">Authgrp</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#ftviewgrp" title="Ftviewgrp">Ftviewgrp</a>: <i>String</i>
    <a href="#fwgrp" title="Fwgrp">Fwgrp</a>: <i>String</i>
    <a href="#loggrp" title="Loggrp">Loggrp</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netgrp" title="Netgrp">Netgrp</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#secfabgrp" title="Secfabgrp">Secfabgrp</a>: <i>String</i>
    <a href="#sysgrp" title="Sysgrp">Sysgrp</a>: <i>String</i>
    <a href="#systemdiagnostics" title="SystemDiagnostics">SystemDiagnostics</a>: <i>String</i>
    <a href="#utmgrp" title="Utmgrp">Utmgrp</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vpngrp" title="Vpngrp">Vpngrp</a>: <i>String</i>
    <a href="#wanoptgrp" title="Wanoptgrp">Wanoptgrp</a>: <i>String</i>
    <a href="#wifi" title="Wifi">Wifi</a>: <i>String</i>
    <a href="#fwgrppermission" title="FwgrpPermission">FwgrpPermission</a>: <i>
      - <a href="fwgrppermissiondefinition.md">FwgrpPermissionDefinition</a></i>
    <a href="#loggrppermission" title="LoggrpPermission">LoggrpPermission</a>: <i>
      - <a href="loggrppermissiondefinition.md">LoggrpPermissionDefinition</a></i>
    <a href="#netgrppermission" title="NetgrpPermission">NetgrpPermission</a>: <i>
      - <a href="netgrppermissiondefinition.md">NetgrpPermissionDefinition</a></i>
    <a href="#sysgrppermission" title="SysgrpPermission">SysgrpPermission</a>: <i>
      - <a href="sysgrppermissiondefinition.md">SysgrpPermissionDefinition</a></i>
    <a href="#utmgrppermission" title="UtmgrpPermission">UtmgrpPermission</a>: <i>
      - <a href="utmgrppermissiondefinition.md">UtmgrpPermissionDefinition</a></i>
</pre>

## Properties

#### Admintimeout

Administrator timeout for this access profile (0 - 480 min, default = 10, 0 means never timeout).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdmintimeoutOverride

Enable/disable overriding the global administrator idle timeout. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authgrp

Administrator access to Users and Devices. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ftviewgrp

FortiView. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fwgrp

Administrator access to the Firewall configuration. Valid values: `none`, `read`, `read-write`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Loggrp

Administrator access to Logging and Reporting including viewing log messages. Valid values: `none`, `read`, `read-write`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Profile name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netgrp

Network Configuration. Valid values: `none`, `read`, `read-write`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

Scope of admin access: global or specific VDOM(s). Valid values: `vdom`, `global`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secfabgrp

Security Fabric. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sysgrp

System Configuration. Valid values: `none`, `read`, `read-write`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiagnostics

Enable/disable permission to run system diagnostic commands. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Utmgrp

Administrator access to Security Profiles. Valid values: `none`, `read`, `read-write`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpngrp

Administrator access to IPsec, SSL, PPTP, and L2TP VPN. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wanoptgrp

Administrator access to WAN Opt & Cache. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wifi

Administrator access to the WiFi controller and Switch controller. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwgrpPermission

_Required_: No

_Type_: List of <a href="fwgrppermissiondefinition.md">FwgrpPermissionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggrpPermission

_Required_: No

_Type_: List of <a href="loggrppermissiondefinition.md">LoggrpPermissionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetgrpPermission

_Required_: No

_Type_: List of <a href="netgrppermissiondefinition.md">NetgrpPermissionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysgrpPermission

_Required_: No

_Type_: List of <a href="sysgrppermissiondefinition.md">SysgrpPermissionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtmgrpPermission

_Required_: No

_Type_: List of <a href="utmgrppermissiondefinition.md">UtmgrpPermissionDefinition</a>

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

