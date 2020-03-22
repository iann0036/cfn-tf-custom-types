# Terraform::Chef::Node

A [node](http://docs.chef.io/nodes.html) is a computer whose
configuration is managed by Chef.

Although this resource allows a node to be registered, it does not actually
configure the computer in question to interact with Chef. In most cases it
is better to use [the `chef` provisioner](/docs/provisioners/chef.html) to
configure the Chef client on a computer and have it register itself with the
Chef server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Chef::Node",
    "Properties" : {
        "<a href="#automaticattributesjson" title="AutomaticAttributesJson">AutomaticAttributesJson</a>" : <i>String</i>,
        "<a href="#defaultattributesjson" title="DefaultAttributesJson">DefaultAttributesJson</a>" : <i>String</i>,
        "<a href="#environmentname" title="EnvironmentName">EnvironmentName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#normalattributesjson" title="NormalAttributesJson">NormalAttributesJson</a>" : <i>String</i>,
        "<a href="#overrideattributesjson" title="OverrideAttributesJson">OverrideAttributesJson</a>" : <i>String</i>,
        "<a href="#runlist" title="RunList">RunList</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Chef::Node
Properties:
    <a href="#automaticattributesjson" title="AutomaticAttributesJson">AutomaticAttributesJson</a>: <i>String</i>
    <a href="#defaultattributesjson" title="DefaultAttributesJson">DefaultAttributesJson</a>: <i>String</i>
    <a href="#environmentname" title="EnvironmentName">EnvironmentName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#normalattributesjson" title="NormalAttributesJson">NormalAttributesJson</a>: <i>String</i>
    <a href="#overrideattributesjson" title="OverrideAttributesJson">OverrideAttributesJson</a>: <i>String</i>
    <a href="#runlist" title="RunList">RunList</a>: <i>
      - String</i>
</pre>

## Properties

#### AutomaticAttributesJson

String containing a JSON-serialized
object containing the automatic attributes for the node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAttributesJson

String containing a JSON-serialized
object containing the default attributes for the node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentName

the nodes environment name (default: _default).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The unique name to assign to the node.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NormalAttributesJson

String containing a JSON-serialized
object containing the normal attributes for the node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideAttributesJson

String containing a JSON-serialized
object containing the override attributes for the node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunList

List of strings to set as the
[run list](https://docs.chef.io/run_lists.html) for the node.

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

