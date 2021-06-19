# TF::FortiOS::FirewallshaperPeripshaper

Configure per-IP traffic shaper.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallshaperPeripshaper",
    "Properties" : {
        "<a href="#bandwidthunit" title="BandwidthUnit">BandwidthUnit</a>" : <i>String</i>,
        "<a href="#diffservforward" title="DiffservForward">DiffservForward</a>" : <i>String</i>,
        "<a href="#diffservreverse" title="DiffservReverse">DiffservReverse</a>" : <i>String</i>,
        "<a href="#diffservcodeforward" title="DiffservcodeForward">DiffservcodeForward</a>" : <i>String</i>,
        "<a href="#diffservcoderev" title="DiffservcodeRev">DiffservcodeRev</a>" : <i>String</i>,
        "<a href="#maxbandwidth" title="MaxBandwidth">MaxBandwidth</a>" : <i>Double</i>,
        "<a href="#maxconcurrentsession" title="MaxConcurrentSession">MaxConcurrentSession</a>" : <i>Double</i>,
        "<a href="#maxconcurrenttcpsession" title="MaxConcurrentTcpSession">MaxConcurrentTcpSession</a>" : <i>Double</i>,
        "<a href="#maxconcurrentudpsession" title="MaxConcurrentUdpSession">MaxConcurrentUdpSession</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallshaperPeripshaper
Properties:
    <a href="#bandwidthunit" title="BandwidthUnit">BandwidthUnit</a>: <i>String</i>
    <a href="#diffservforward" title="DiffservForward">DiffservForward</a>: <i>String</i>
    <a href="#diffservreverse" title="DiffservReverse">DiffservReverse</a>: <i>String</i>
    <a href="#diffservcodeforward" title="DiffservcodeForward">DiffservcodeForward</a>: <i>String</i>
    <a href="#diffservcoderev" title="DiffservcodeRev">DiffservcodeRev</a>: <i>String</i>
    <a href="#maxbandwidth" title="MaxBandwidth">MaxBandwidth</a>: <i>Double</i>
    <a href="#maxconcurrentsession" title="MaxConcurrentSession">MaxConcurrentSession</a>: <i>Double</i>
    <a href="#maxconcurrenttcpsession" title="MaxConcurrentTcpSession">MaxConcurrentTcpSession</a>: <i>Double</i>
    <a href="#maxconcurrentudpsession" title="MaxConcurrentUdpSession">MaxConcurrentUdpSession</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### BandwidthUnit

Unit of measurement for maximum bandwidth for this shaper (Kbps, Mbps or Gbps). Valid values: `kbps`, `mbps`, `gbps`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservForward

Enable/disable changing the Forward (original) DiffServ setting applied to traffic accepted by this shaper. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservReverse

Enable/disable changing the Reverse (reply) DiffServ setting applied to traffic accepted by this shaper. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservcodeForward

Forward (original) DiffServ setting to be applied to traffic accepted by this shaper.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffservcodeRev

Reverse (reply) DiffServ setting to be applied to traffic accepted by this shaper.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBandwidth

Upper bandwidth limit enforced by this shaper (0 - 16776000). 0 means no limit. Units depend on the bandwidth-unit setting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentSession

Maximum number of concurrent sessions allowed by this shaper (0 - 2097000). 0 means no limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentTcpSession

Maximum number of concurrent TCP sessions allowed by this shaper (0 - 2097000). 0 means no limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentUdpSession

Maximum number of concurrent UDP sessions allowed by this shaper (0 - 2097000). 0 means no limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Traffic shaper name.

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

