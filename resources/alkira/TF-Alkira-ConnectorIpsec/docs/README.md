# TF::Alkira::ConnectorIpsec

CloudFormation equivalent of alkira_connector_ipsec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alkira::ConnectorIpsec",
    "Properties" : {
        "<a href="#billingtags" title="BillingTags">BillingTags</a>" : <i>[ Double, ... ]</i>,
        "<a href="#cxp" title="Cxp">Cxp</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#segment" title="Segment">Segment</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#vpnmode" title="VpnMode">VpnMode</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>[ <a href="endpointdefinition.md">EndpointDefinition</a>, ... ]</i>,
        "<a href="#policyoptions" title="PolicyOptions">PolicyOptions</a>" : <i>[ <a href="policyoptionsdefinition.md">PolicyOptionsDefinition</a>, ... ]</i>,
        "<a href="#routingoptions" title="RoutingOptions">RoutingOptions</a>" : <i>[ <a href="routingoptionsdefinition.md">RoutingOptionsDefinition</a>, ... ]</i>,
        "<a href="#segmentoptions" title="SegmentOptions">SegmentOptions</a>" : <i>[ <a href="segmentoptionsdefinition.md">SegmentOptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alkira::ConnectorIpsec
Properties:
    <a href="#billingtags" title="BillingTags">BillingTags</a>: <i>
      - Double</i>
    <a href="#cxp" title="Cxp">Cxp</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#segment" title="Segment">Segment</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#vpnmode" title="VpnMode">VpnMode</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>
      - <a href="endpointdefinition.md">EndpointDefinition</a></i>
    <a href="#policyoptions" title="PolicyOptions">PolicyOptions</a>: <i>
      - <a href="policyoptionsdefinition.md">PolicyOptionsDefinition</a></i>
    <a href="#routingoptions" title="RoutingOptions">RoutingOptions</a>: <i>
      - <a href="routingoptionsdefinition.md">RoutingOptionsDefinition</a></i>
    <a href="#segmentoptions" title="SegmentOptions">SegmentOptions</a>: <i>
      - <a href="segmentoptionsdefinition.md">SegmentOptionsDefinition</a></i>
</pre>

## Properties

#### BillingTags

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cxp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Segment

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnMode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

_Required_: No

_Type_: List of <a href="endpointdefinition.md">EndpointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyOptions

_Required_: No

_Type_: List of <a href="policyoptionsdefinition.md">PolicyOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingOptions

_Required_: No

_Type_: List of <a href="routingoptionsdefinition.md">RoutingOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentOptions

_Required_: No

_Type_: List of <a href="segmentoptionsdefinition.md">SegmentOptionsDefinition</a>

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

