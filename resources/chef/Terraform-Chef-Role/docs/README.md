# Terraform::Chef::Role

A [role](http://docs.chef.io/roles.html) is a set of standard configuration
that can apply across multiple nodes that perform the same function.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Chef::Role",
    "Properties" : {
        "<a href="#defaultattributesjson" title="DefaultAttributesJson">DefaultAttributesJson</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overrideattributesjson" title="OverrideAttributesJson">OverrideAttributesJson</a>" : <i>String</i>,
        "<a href="#runlist" title="RunList">RunList</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Chef::Role
Properties:
    <a href="#defaultattributesjson" title="DefaultAttributesJson">DefaultAttributesJson</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overrideattributesjson" title="OverrideAttributesJson">OverrideAttributesJson</a>: <i>String</i>
    <a href="#runlist" title="RunList">RunList</a>: <i>
      - String</i>
</pre>

## Properties

#### DefaultAttributesJson

String containing a JSON-serialized
object containing the default attributes for the role.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description of the role.
If not set, a placeholder of "Managed by Terraform" will be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The unique name to assign to the role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideAttributesJson

String containing a JSON-serialized
object containing the override attributes for the role.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunList

List of strings to set as the
[run list](https://docs.chef.io/run_lists.html) for any nodes that belong
to this role.

_Required_: No

_Type_: List of String

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

