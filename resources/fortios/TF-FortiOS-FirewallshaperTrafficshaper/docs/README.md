# TF::FortiOS::FirewallshaperTrafficshaper

Configure shared traffic shaper.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallshaperTrafficshaper",
    "Properties" : {
        "<a href="#bandwidthunit" title="BandwidthUnit">BandwidthUnit</a>" : <i>String</i>,
        "<a href="#diffserv" title="Diffserv">Diffserv</a>" : <i>String</i>,
        "<a href="#diffservcode" title="Diffservcode">Diffservcode</a>" : <i>String</i>,
        "<a href="#dscpmarkingmethod" title="DscpMarkingMethod">DscpMarkingMethod</a>" : <i>String</i>,
        "<a href="#exceedbandwidth" title="ExceedBandwidth">ExceedBandwidth</a>" : <i>Double</i>,
        "<a href="#exceedclassid" title="ExceedClassId">ExceedClassId</a>" : <i>Double</i>,
        "<a href="#exceeddscp" title="ExceedDscp">ExceedDscp</a>" : <i>String</i>,
        "<a href="#guaranteedbandwidth" title="GuaranteedBandwidth">GuaranteedBandwidth</a>" : <i>Double</i>,
        "<a href="#maximumbandwidth" title="MaximumBandwidth">MaximumBandwidth</a>" : <i>Double</i>,
        "<a href="#maximumdscp" title="MaximumDscp">MaximumDscp</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overhead" title="Overhead">Overhead</a>" : <i>Double</i>,
        "<a href="#perpolicy" title="PerPolicy">PerPolicy</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallshaperTrafficshaper
Properties:
    <a href="#bandwidthunit" title="BandwidthUnit">BandwidthUnit</a>: <i>String</i>
    <a href="#diffserv" title="Diffserv">Diffserv</a>: <i>String</i>
    <a href="#diffservcode" title="Diffservcode">Diffservcode</a>: <i>String</i>
    <a href="#dscpmarkingmethod" title="DscpMarkingMethod">DscpMarkingMethod</a>: <i>String</i>
    <a href="#exceedbandwidth" title="ExceedBandwidth">ExceedBandwidth</a>: <i>Double</i>
    <a href="#exceedclassid" title="ExceedClassId">ExceedClassId</a>: <i>Double</i>
    <a href="#exceeddscp" title="ExceedDscp">ExceedDscp</a>: <i>String</i>
    <a href="#guaranteedbandwidth" title="GuaranteedBandwidth">GuaranteedBandwidth</a>: <i>Double</i>
    <a href="#maximumbandwidth" title="MaximumBandwidth">MaximumBandwidth</a>: <i>Double</i>
    <a href="#maximumdscp" title="MaximumDscp">MaximumDscp</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overhead" title="Overhead">Overhead</a>: <i>Double</i>
    <a href="#perpolicy" title="PerPolicy">PerPolicy</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### BandwidthUnit

Unit of measurement for guaranteed and maximum bandwidth for this shaper (Kbps, Mbps or Gbps). Valid values: `kbps`, `mbps`, `gbps`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Diffserv

Enable/disable changing the DiffServ setting applied to traffic accepted by this shaper. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Diffservcode

DiffServ setting to be applied to traffic accepted by this shaper.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpMarkingMethod

Select DSCP marking method. Valid values: `multi-stage`, `static`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceedBandwidth

Exceed bandwidth used for DSCP multi-stage marking. Units depend on the bandwidth-unit setting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceedClassId

Class ID for traffic in [guaranteed-bandwidth, maximum-bandwidth].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceedDscp

DSCP mark for traffic in [guaranteed-bandwidth, exceed-bandwidth].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuaranteedBandwidth

Amount of bandwidth guaranteed for this shaper (0 - 16776000). Units depend on the bandwidth-unit setting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumBandwidth

Upper bandwidth limit enforced by this shaper (0 - 16776000). 0 means no limit. Units depend on the bandwidth-unit setting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumDscp

DSCP mark for traffic in [exceed-bandwidth, maximum-bandwidth].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Traffic shaper name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overhead

Per-packet size overhead used in rate computations.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerPolicy

Enable/disable applying a separate shaper for each policy. For example, if enabled the guaranteed bandwidth is applied separately for each policy. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Higher priority traffic is more likely to be forwarded without delays and without compromising the guaranteed bandwidth. Valid values: `low`, `medium`, `high`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

