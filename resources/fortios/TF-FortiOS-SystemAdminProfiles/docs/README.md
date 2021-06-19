# TF::FortiOS::SystemAdminProfiles

Provides a resource to configure access profiles of FortiOS.

!> **Warning:** The resource will be deprecated and replaced by new resource `fortios_system_accprofile`, we recommend that you use the new resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemAdminProfiles",
    "Properties" : {
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
        "<a href="#utmgrp" title="Utmgrp">Utmgrp</a>" : <i>String</i>,
        "<a href="#vpngrp" title="Vpngrp">Vpngrp</a>" : <i>String</i>,
        "<a href="#wanoptgrp" title="Wanoptgrp">Wanoptgrp</a>" : <i>String</i>,
        "<a href="#wifi" title="Wifi">Wifi</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemAdminProfiles
Properties:
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
    <a href="#utmgrp" title="Utmgrp">Utmgrp</a>: <i>String</i>
    <a href="#vpngrp" title="Vpngrp">Vpngrp</a>: <i>String</i>
    <a href="#wanoptgrp" title="Wanoptgrp">Wanoptgrp</a>: <i>String</i>
    <a href="#wifi" title="Wifi">Wifi</a>: <i>String</i>
</pre>

## Properties

#### AdmintimeoutOverride

Enable/disable overriding the global administrator idle timeout.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authgrp

Administrator access to Users and Devices.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ftviewgrp

FortiView.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fwgrp

Administrator access to the Firewall configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Loggrp

Administrator access to Logging and Reporting including viewing log messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Profile name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netgrp

Network Configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

Scope of admin access.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secfabgrp

Security Fabric.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sysgrp

System Configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Utmgrp

Administrator access to Security Profiles.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpngrp

Administrator access to IPsec, SSL, PPTP, and L2TP VPN.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wanoptgrp

Administrator access to WAN Opt & Cache.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wifi

Administrator access to the WiFi controller and Switch controller.

_Required_: No

_Type_: String

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

