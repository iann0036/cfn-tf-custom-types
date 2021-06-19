# TF::Vultr::SshKey

Provides a Vultr SSH key resource. This can be used to create, read, modify, and delete SSH keys.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::SshKey",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::SshKey
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sshkey" title="SshKey">SshKey</a>: <i>String</i>
</pre>

## Properties

#### Name

The name/label of the SSH key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

The public SSH key.

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

#### DateCreated

Returns the <code>DateCreated</code> value.

#### Id

Returns the <code>Id</code> value.

