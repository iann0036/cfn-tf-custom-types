# TF::FortiOS::Wirelesscontrollerhotspot20H2qpwanmetric

Configure WAN metrics.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::Wirelesscontrollerhotspot20H2qpwanmetric",
    "Properties" : {
        "<a href="#downlinkload" title="DownlinkLoad">DownlinkLoad</a>" : <i>Double</i>,
        "<a href="#downlinkspeed" title="DownlinkSpeed">DownlinkSpeed</a>" : <i>Double</i>,
        "<a href="#linkatcapacity" title="LinkAtCapacity">LinkAtCapacity</a>" : <i>String</i>,
        "<a href="#linkstatus" title="LinkStatus">LinkStatus</a>" : <i>String</i>,
        "<a href="#loadmeasurementduration" title="LoadMeasurementDuration">LoadMeasurementDuration</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#symmetricwanlink" title="SymmetricWanLink">SymmetricWanLink</a>" : <i>String</i>,
        "<a href="#uplinkload" title="UplinkLoad">UplinkLoad</a>" : <i>Double</i>,
        "<a href="#uplinkspeed" title="UplinkSpeed">UplinkSpeed</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::Wirelesscontrollerhotspot20H2qpwanmetric
Properties:
    <a href="#downlinkload" title="DownlinkLoad">DownlinkLoad</a>: <i>Double</i>
    <a href="#downlinkspeed" title="DownlinkSpeed">DownlinkSpeed</a>: <i>Double</i>
    <a href="#linkatcapacity" title="LinkAtCapacity">LinkAtCapacity</a>: <i>String</i>
    <a href="#linkstatus" title="LinkStatus">LinkStatus</a>: <i>String</i>
    <a href="#loadmeasurementduration" title="LoadMeasurementDuration">LoadMeasurementDuration</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#symmetricwanlink" title="SymmetricWanLink">SymmetricWanLink</a>: <i>String</i>
    <a href="#uplinkload" title="UplinkLoad">UplinkLoad</a>: <i>Double</i>
    <a href="#uplinkspeed" title="UplinkSpeed">UplinkSpeed</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### DownlinkLoad

Downlink load.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownlinkSpeed

Downlink speed (in kilobits/s).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkAtCapacity

Link at capacity. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkStatus

Link status. Valid values: `up`, `down`, `in-test`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadMeasurementDuration

Load measurement duration (in tenths of a second).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

WAN metric name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SymmetricWanLink

WAN link symmetry. Valid values: `symmetric`, `asymmetric`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UplinkLoad

Uplink load.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UplinkSpeed

Uplink speed (in kilobits/s).

_Required_: No

_Type_: Double

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

