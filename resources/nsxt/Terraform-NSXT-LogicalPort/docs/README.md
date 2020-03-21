# Terraform::NSXT::LogicalPort

This resource provides a resource to configure a logical port on a logical switch in the NSX system. Like physical switches a logical switch can have one or more ports which can be connected to virtual machines or logical routers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LogicalPort",
    "Properties" : {
        "<a href="#adminstate" title="AdminState">AdminState</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#logicalswitchid" title="LogicalSwitchId">LogicalSwitchId</a>" : <i>String</i>,
        "<a href="#switchingprofileid" title="SwitchingProfileId">SwitchingProfileId</a>" : <i>[ <a href="switchingprofileid.md">SwitchingProfileId</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LogicalPort
Properties:
    <a href="#adminstate" title="AdminState">AdminState</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#logicalswitchid" title="LogicalSwitchId">LogicalSwitchId</a>: <i>String</i>
    <a href="#switchingprofileid" title="SwitchingProfileId">SwitchingProfileId</a>: <i>
      - <a href="switchingprofileid.md">SwitchingProfileId</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### AdminState

Admin state for the logical port. Accepted values - 'UP' or 'DOWN'. The default value is 'UP'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name, defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalSwitchId

Logical switch ID for the logical port.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchingProfileId

_Required_: No

_Type_: List of <a href="switchingprofileid.md">SwitchingProfileId</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Revision

Returns the <code>Revision</code> value.

