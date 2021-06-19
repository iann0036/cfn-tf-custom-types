# TF::Panos::OspfArea

Manages an OSPF area config.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::OspfArea",
    "Properties" : {
        "<a href="#acceptsummary" title="AcceptSummary">AcceptSummary</a>" : <i>Boolean</i>,
        "<a href="#advertisemetric" title="AdvertiseMetric">AdvertiseMetric</a>" : <i>Double</i>,
        "<a href="#advertisetype" title="AdvertiseType">AdvertiseType</a>" : <i>String</i>,
        "<a href="#defaultrouteadvertise" title="DefaultRouteAdvertise">DefaultRouteAdvertise</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>,
        "<a href="#extrange" title="ExtRange">ExtRange</a>" : <i>[ <a href="extrangedefinition.md">ExtRangeDefinition</a>, ... ]</i>,
        "<a href="#range" title="Range">Range</a>" : <i>[ <a href="rangedefinition.md">RangeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::OspfArea
Properties:
    <a href="#acceptsummary" title="AcceptSummary">AcceptSummary</a>: <i>Boolean</i>
    <a href="#advertisemetric" title="AdvertiseMetric">AdvertiseMetric</a>: <i>Double</i>
    <a href="#advertisetype" title="AdvertiseType">AdvertiseType</a>: <i>String</i>
    <a href="#defaultrouteadvertise" title="DefaultRouteAdvertise">DefaultRouteAdvertise</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
    <a href="#extrange" title="ExtRange">ExtRange</a>: <i>
      - <a href="extrangedefinition.md">ExtRangeDefinition</a></i>
    <a href="#range" title="Range">Range</a>: <i>
      - <a href="rangedefinition.md">RangeDefinition</a></i>
</pre>

## Properties

#### AcceptSummary

(stub/nssa) Accept summary.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseMetric

(stub/nssa) Advertise metric.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseType

Advertise type.  Valid values are `ext-2` or `ext-1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRouteAdvertise

(stub/nssa) Default route advertise.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template location.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Area type.  Valid values are `normal` (default), `stub`, or `nssa`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

The virtual router name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtRange

_Required_: No

_Type_: List of <a href="extrangedefinition.md">ExtRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

_Required_: No

_Type_: List of <a href="rangedefinition.md">RangeDefinition</a>

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

