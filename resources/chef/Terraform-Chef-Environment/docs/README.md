# Terraform::Chef::Environment

An [environment](http://docs.chef.io/environments.html) is a container for
Chef nodes that share a set of attribute values and may have a set of version
constraints for which cookbook versions may be used on its nodes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Chef::Environment",
    "Properties" : {
        "<a href="#cookbookconstraints" title="CookbookConstraints">CookbookConstraints</a>" : <i>[ <a href="cookbookconstraints.md">CookbookConstraints</a>, ... ]</i>,
        "<a href="#defaultattributesjson" title="DefaultAttributesJson">DefaultAttributesJson</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overrideattributesjson" title="OverrideAttributesJson">OverrideAttributesJson</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Chef::Environment
Properties:
    <a href="#cookbookconstraints" title="CookbookConstraints">CookbookConstraints</a>: <i>
      - <a href="cookbookconstraints.md">CookbookConstraints</a></i>
    <a href="#defaultattributesjson" title="DefaultAttributesJson">DefaultAttributesJson</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overrideattributesjson" title="OverrideAttributesJson">OverrideAttributesJson</a>: <i>String</i>
</pre>

## Properties

#### CookbookConstraints

Mapping of cookbook names to cookbook
version constraints that should apply for this environment.

_Required_: No

_Type_: List of <a href="cookbookconstraints.md">CookbookConstraints</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAttributesJson

String containing a JSON-serialized
object containing the default attributes for the environment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description of the environment.
If not set, a placeholder of "Managed by Terraform" will be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The unique name to assign to the environment. This name
will be used when nodes are created within the environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideAttributesJson

String containing a JSON-serialized
object containing the override attributes for the environment.

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

