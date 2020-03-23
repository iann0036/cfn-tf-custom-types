# Terraform::AWS::EcsCluster

Provides an ECS cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EcsCluster",
    "Properties" : {
        "<a href="#capacityproviders" title="CapacityProviders">CapacityProviders</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#defaultcapacityproviderstrategy" title="DefaultCapacityProviderStrategy">DefaultCapacityProviderStrategy</a>" : <i>[ <a href="defaultcapacityproviderstrategy.md">DefaultCapacityProviderStrategy</a>, ... ]</i>,
        "<a href="#setting" title="Setting">Setting</a>" : <i>[ <a href="setting.md">Setting</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EcsCluster
Properties:
    <a href="#capacityproviders" title="CapacityProviders">CapacityProviders</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#defaultcapacityproviderstrategy" title="DefaultCapacityProviderStrategy">DefaultCapacityProviderStrategy</a>: <i>
      - <a href="defaultcapacityproviderstrategy.md">DefaultCapacityProviderStrategy</a></i>
    <a href="#setting" title="Setting">Setting</a>: <i>
      - <a href="setting.md">Setting</a></i>
</pre>

## Properties

#### CapacityProviders

List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the cluster (up to 255 letters, numbers, hyphens, and underscores).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCapacityProviderStrategy

_Required_: No

_Type_: List of <a href="defaultcapacityproviderstrategy.md">DefaultCapacityProviderStrategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Setting

_Required_: No

_Type_: List of <a href="setting.md">Setting</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

