# Terraform::Scaleway::UserData

**DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
Please use `scaleway_instance_server` instead.

Provides user data for servers.
For additional details please refer to [API documentation](https://developer.scaleway.com/#user-data).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::UserData",
    "Properties" : {
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::UserData
Properties:
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### Key

The key of the user data object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

ID of server to associate the user data with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value of the user data object.

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

