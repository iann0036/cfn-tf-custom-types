# TF::OVH::CloudProjectContainerregistryUser

Creates a user for a container registry associated with a public cloud project.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OVH::CloudProjectContainerregistryUser",
    "Properties" : {
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#login" title="Login">Login</a>" : <i>String</i>,
        "<a href="#registryid" title="RegistryId">RegistryId</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::OVH::CloudProjectContainerregistryUser
Properties:
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#login" title="Login">Login</a>: <i>String</i>
    <a href="#registryid" title="RegistryId">RegistryId</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
</pre>

## Properties

#### Email

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Login

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryId

Registry ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The id of the public cloud project. If omitted,
the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.

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

#### Password

Returns the <code>Password</code> value.

#### User

Returns the <code>User</code> value.

