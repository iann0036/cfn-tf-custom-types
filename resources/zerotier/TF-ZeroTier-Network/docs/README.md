# TF::ZeroTier::Network

CloudFormation equivalent of zerotier_network

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ZeroTier::Network",
    "Properties" : {
        "<a href="#assignipv4" title="AssignIpv4">AssignIpv4</a>" : <i>[ <a href="assignipv4definition.md">AssignIpv4Definition</a>, ... ]</i>,
        "<a href="#assignipv6" title="AssignIpv6">AssignIpv6</a>" : <i>[ <a href="assignipv6definition.md">AssignIpv6Definition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablebroadcast" title="EnableBroadcast">EnableBroadcast</a>" : <i>Boolean</i>,
        "<a href="#flowrules" title="FlowRules">FlowRules</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#multicastlimit" title="MulticastLimit">MulticastLimit</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#private" title="Private">Private</a>" : <i>Boolean</i>,
        "<a href="#assignmentpool" title="AssignmentPool">AssignmentPool</a>" : <i>[ <a href="assignmentpooldefinition.md">AssignmentPoolDefinition</a>, ... ]</i>,
        "<a href="#route" title="Route">Route</a>" : <i>[ <a href="routedefinition.md">RouteDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ZeroTier::Network
Properties:
    <a href="#assignipv4" title="AssignIpv4">AssignIpv4</a>: <i>
      - <a href="assignipv4definition.md">AssignIpv4Definition</a></i>
    <a href="#assignipv6" title="AssignIpv6">AssignIpv6</a>: <i>
      - <a href="assignipv6definition.md">AssignIpv6Definition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablebroadcast" title="EnableBroadcast">EnableBroadcast</a>: <i>Boolean</i>
    <a href="#flowrules" title="FlowRules">FlowRules</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#multicastlimit" title="MulticastLimit">MulticastLimit</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#private" title="Private">Private</a>: <i>Boolean</i>
    <a href="#assignmentpool" title="AssignmentPool">AssignmentPool</a>: <i>
      - <a href="assignmentpooldefinition.md">AssignmentPoolDefinition</a></i>
    <a href="#route" title="Route">Route</a>: <i>
      - <a href="routedefinition.md">RouteDefinition</a></i>
</pre>

## Properties

#### AssignIpv4

_Required_: No

_Type_: List of <a href="assignipv4definition.md">AssignIpv4Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignIpv6

_Required_: No

_Type_: List of <a href="assignipv6definition.md">AssignIpv6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBroadcast

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowRules

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Private

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignmentPool

_Required_: No

_Type_: List of <a href="assignmentpooldefinition.md">AssignmentPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

_Required_: No

_Type_: List of <a href="routedefinition.md">RouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTime

Returns the <code>CreationTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### TfLastUpdated

Returns the <code>TfLastUpdated</code> value.

