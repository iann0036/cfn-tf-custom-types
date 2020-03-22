# Terraform::Scaleway::SshKey

**DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
Please use `account_ssh_key` instead.

Manages user SSH Keys to access servers provisioned on scaleway.
For additional details please refer to [API documentation](https://developer.scaleway.com/#users-user-get).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::SshKey",
    "Properties" : {
        "<a href="#key" title="Key">Key</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::SshKey
Properties:
    <a href="#key" title="Key">Key</a>: <i>String</i>
</pre>

## Properties

#### Key

public key of the SSH key to be added.

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

#### Id

Returns the <code>Id</code> value.

