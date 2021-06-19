# TF::FortiOS::SystemSettingNtp

Provides a resource to configure Network Time Protocol (NTP) servers of FortiOS.

!> **Warning:** The resource will be deprecated and replaced by new resource `fortios_system_ntp`, we recommend that you use the new resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemSettingNtp",
    "Properties" : {
        "<a href="#ntpserver" title="Ntpserver">Ntpserver</a>" : <i>[ String, ... ]</i>,
        "<a href="#ntpsync" title="Ntpsync">Ntpsync</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemSettingNtp
Properties:
    <a href="#ntpserver" title="Ntpserver">Ntpserver</a>: <i>
      - String</i>
    <a href="#ntpsync" title="Ntpsync">Ntpsync</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Ntpserver

Configure the FortiGate to connect to any available third-party NTP server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ntpsync

Enable/disable setting the FortiGate system time by synchronizing with an NTP Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Use the FortiGuard NTP server or any other available NTP Server.

_Required_: Yes

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

