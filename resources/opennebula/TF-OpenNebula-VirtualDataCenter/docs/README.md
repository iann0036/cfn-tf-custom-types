# TF::OpenNebula::VirtualDataCenter

Provides an OpenNebula virtual data center resource.

This resource allows you to manage virtual data centers on your OpenNebula organization. When applied,
a new virtual data center is created. When destroyed, this virtual data center is removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpenNebula::VirtualDataCenter",
    "Properties" : {
        "<a href="#groupids" title="GroupIds">GroupIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ <a href="zonesdefinition.md">ZonesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpenNebula::VirtualDataCenter
Properties:
    <a href="#groupids" title="GroupIds">GroupIds</a>: <i>
      - Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - <a href="zonesdefinition.md">ZonesDefinition</a></i>
</pre>

## Properties

#### GroupIds

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the virtual data center.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: No

_Type_: List of <a href="zonesdefinition.md">ZonesDefinition</a>

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

