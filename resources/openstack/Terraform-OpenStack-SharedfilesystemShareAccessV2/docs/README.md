# Terraform::OpenStack::SharedfilesystemShareAccessV2

Use this resource to control the share access lists.

~> **Important Security Notice** The access key retrieved by this resource will
be stored *unencrypted* in your Terraform state file. If you use this resource
in production, please make sure your state file is sufficiently protected.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::SharedfilesystemShareAccessV2",
    "Properties" : {
        "<a href="#accesslevel" title="AccessLevel">AccessLevel</a>" : <i>String</i>,
        "<a href="#accessto" title="AccessTo">AccessTo</a>" : <i>String</i>,
        "<a href="#accesstype" title="AccessType">AccessType</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#shareid" title="ShareId">ShareId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::SharedfilesystemShareAccessV2
Properties:
    <a href="#accesslevel" title="AccessLevel">AccessLevel</a>: <i>String</i>
    <a href="#accessto" title="AccessTo">AccessTo</a>: <i>String</i>
    <a href="#accesstype" title="AccessType">AccessType</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#shareid" title="ShareId">ShareId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AccessLevel

The access level to the share. Can either be `rw` or `ro`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessTo

The value that defines the access. Can either be an IP
address or a username verified by configured Security Service of the Share Network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessType

The access rule type. Can either be an ip, user,
cert, or cephx. cephx support requires an OpenStack environment that supports
Shared Filesystem microversion 2.13 (Mitaka) or later.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share access. Changing this
creates a new share access.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareId

The UUID of the share to which you are granted access.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccessKey

Returns the <code>AccessKey</code> value.

#### Id

Returns the <code>Id</code> value.

