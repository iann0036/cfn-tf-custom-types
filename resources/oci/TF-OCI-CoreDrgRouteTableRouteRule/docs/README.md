# TF::OCI::CoreDrgRouteTableRouteRule

This resource provides the Drg Route Table Route Rule resource in Oracle Cloud Infrastructure Core service.

Adds one static route rule to the specified DRG route table.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CoreDrgRouteTableRouteRule",
    "Properties" : {
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#destinationtype" title="DestinationType">DestinationType</a>" : <i>String</i>,
        "<a href="#drgroutetableid" title="DrgRouteTableId">DrgRouteTableId</a>" : <i>String</i>,
        "<a href="#nexthopdrgattachmentid" title="NextHopDrgAttachmentId">NextHopDrgAttachmentId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CoreDrgRouteTableRouteRule
Properties:
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#destinationtype" title="DestinationType">DestinationType</a>: <i>String</i>
    <a href="#drgroutetableid" title="DrgRouteTableId">DrgRouteTableId</a>: <i>String</i>
    <a href="#nexthopdrgattachmentid" title="NextHopDrgAttachmentId">NextHopDrgAttachmentId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Destination

(Updatable) This is the range of IP addresses used for matching when routing traffic. Only CIDR_BLOCK values are allowed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationType

(Updatable) Type of destination for the rule. Required if `direction` = `EGRESS`. Allowed values:
* `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrgRouteTableId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopDrgAttachmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG attachment is responsible for reaching the network destination.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### IsBlackhole

Returns the <code>IsBlackhole</code> value.

#### IsConflict

Returns the <code>IsConflict</code> value.

#### RouteProvenance

Returns the <code>RouteProvenance</code> value.

#### RouteType

Returns the <code>RouteType</code> value.

