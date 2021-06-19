# TF::ZeroTier::Member

CloudFormation equivalent of zerotier_member

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ZeroTier::Member",
    "Properties" : {
        "<a href="#allowethernetbridging" title="AllowEthernetBridging">AllowEthernetBridging</a>" : <i>Boolean</i>,
        "<a href="#authorized" title="Authorized">Authorized</a>" : <i>Boolean</i>,
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ Double, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#hidden" title="Hidden">Hidden</a>" : <i>Boolean</i>,
        "<a href="#ipassignments" title="IpAssignments">IpAssignments</a>" : <i>[ String, ... ]</i>,
        "<a href="#memberid" title="MemberId">MemberId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#noautoassignips" title="NoAutoAssignIps">NoAutoAssignIps</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ZeroTier::Member
Properties:
    <a href="#allowethernetbridging" title="AllowEthernetBridging">AllowEthernetBridging</a>: <i>Boolean</i>
    <a href="#authorized" title="Authorized">Authorized</a>: <i>Boolean</i>
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#hidden" title="Hidden">Hidden</a>: <i>Boolean</i>
    <a href="#ipassignments" title="IpAssignments">IpAssignments</a>: <i>
      - String</i>
    <a href="#memberid" title="MemberId">MemberId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#noautoassignips" title="NoAutoAssignIps">NoAutoAssignIps</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowEthernetBridging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorized

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capabilities

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hidden

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAssignments

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAutoAssignIps

_Required_: No

_Type_: Boolean

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

