# TF::Alicloud::ResourceManagerHandshake

Provides a Resource Manager handshake resource. You can invite accounts to join a resource directory for unified management.
For information about Resource Manager handshake and how to use it, see [What is Resource Manager handshake](https://www.alibabacloud.com/help/en/doc-detail/135287.htm).

-> **NOTE:** Available in v1.82.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ResourceManagerHandshake",
    "Properties" : {
        "<a href="#note" title="Note">Note</a>" : <i>String</i>,
        "<a href="#targetentity" title="TargetEntity">TargetEntity</a>" : <i>String</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ResourceManagerHandshake
Properties:
    <a href="#note" title="Note">Note</a>: <i>String</i>
    <a href="#targetentity" title="TargetEntity">TargetEntity</a>: <i>String</i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
</pre>

## Properties

#### Note

Remarks. The maximum length is 1024 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetEntity

Invited account ID or login email.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

Type of account being invited. Valid values: `Account`, `Email`.

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

#### ExpireTime

Returns the <code>ExpireTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### MasterAccountId

Returns the <code>MasterAccountId</code> value.

#### MasterAccountName

Returns the <code>MasterAccountName</code> value.

#### ModifyTime

Returns the <code>ModifyTime</code> value.

#### ResourceDirectoryId

Returns the <code>ResourceDirectoryId</code> value.

#### Status

Returns the <code>Status</code> value.

