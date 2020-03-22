# Terraform::Linode::Sshkey

Provides a Linode SSH Key resource.  This can be used to create, modify, and delete Linodes SSH Keys.  Managed SSH Keys allow instances to be created with a list of Linode usernames, whose SSH keys will be automatically applied to the root account's `~/.ssh/authorized_keys` file.
For more information, see the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/getSSHKeys).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Linode::Sshkey",
    "Properties" : {
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Linode::Sshkey
Properties:
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#sshkey" title="SshKey">SshKey</a>: <i>String</i>
</pre>

## Properties

#### Label

A label for the SSH Key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Created

Returns the <code>Created</code> value.

#### Id

Returns the <code>Id</code> value.

