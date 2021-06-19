# TF::FortiOS::SystemSettingGlobal

Provides a resource to configure options related to the overall operation of FortiOS.

!> **Warning:** The resource will be deprecated and replaced by new resource `fortios_system_global`, we recommend that you use the new resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemSettingGlobal",
    "Properties" : {
        "<a href="#adminscp" title="AdminScp">AdminScp</a>" : <i>String</i>,
        "<a href="#adminsport" title="AdminSport">AdminSport</a>" : <i>String</i>,
        "<a href="#adminsshport" title="AdminSshPort">AdminSshPort</a>" : <i>String</i>,
        "<a href="#admintimeout" title="Admintimeout">Admintimeout</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemSettingGlobal
Properties:
    <a href="#adminscp" title="AdminScp">AdminScp</a>: <i>String</i>
    <a href="#adminsport" title="AdminSport">AdminSport</a>: <i>String</i>
    <a href="#adminsshport" title="AdminSshPort">AdminSshPort</a>: <i>String</i>
    <a href="#admintimeout" title="Admintimeout">Admintimeout</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
</pre>

## Properties

#### AdminScp

Enable SCP over SSH.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminSport

Administrative access port for HTTPS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminSshPort

Administrative access port for SSH.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Admintimeout

Number of minutes before an idle administrator session time out.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

FortiGate unit's hostname.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Number corresponding to your time zone from 00 to 86.

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

