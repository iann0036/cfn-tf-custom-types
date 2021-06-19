# TF::BIGIP::SysNtp

`bigip_sys_ntp` provides details about a specific bigip

This resource is helpful when configuring NTP server on the BIG-IP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::SysNtp",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#servers" title="Servers">Servers</a>" : <i>[ String, ... ]</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::SysNtp
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#servers" title="Servers">Servers</a>: <i>
      - String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
</pre>

## Properties

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servers

Adds NTP servers to or deletes NTP servers from the BIG-IP system.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Specifies the time zone that you want to use for the system time.

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

