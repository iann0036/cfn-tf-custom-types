# TF::FortiOS::SystemSpeedtestschedule

Speed test schedule for each interface. Applies to FortiOS Version `>= 7.0.0`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemSpeedtestschedule",
    "Properties" : {
        "<a href="#diffserv" title="Diffserv">Diffserv</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#updateinbandwidth" title="UpdateInbandwidth">UpdateInbandwidth</a>" : <i>String</i>,
        "<a href="#updateinbandwidthmaximum" title="UpdateInbandwidthMaximum">UpdateInbandwidthMaximum</a>" : <i>Double</i>,
        "<a href="#updateinbandwidthminimum" title="UpdateInbandwidthMinimum">UpdateInbandwidthMinimum</a>" : <i>Double</i>,
        "<a href="#updateoutbandwidth" title="UpdateOutbandwidth">UpdateOutbandwidth</a>" : <i>String</i>,
        "<a href="#updateoutbandwidthmaximum" title="UpdateOutbandwidthMaximum">UpdateOutbandwidthMaximum</a>" : <i>Double</i>,
        "<a href="#updateoutbandwidthminimum" title="UpdateOutbandwidthMinimum">UpdateOutbandwidthMinimum</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#schedules" title="Schedules">Schedules</a>" : <i>[ <a href="schedulesdefinition.md">SchedulesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemSpeedtestschedule
Properties:
    <a href="#diffserv" title="Diffserv">Diffserv</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#updateinbandwidth" title="UpdateInbandwidth">UpdateInbandwidth</a>: <i>String</i>
    <a href="#updateinbandwidthmaximum" title="UpdateInbandwidthMaximum">UpdateInbandwidthMaximum</a>: <i>Double</i>
    <a href="#updateinbandwidthminimum" title="UpdateInbandwidthMinimum">UpdateInbandwidthMinimum</a>: <i>Double</i>
    <a href="#updateoutbandwidth" title="UpdateOutbandwidth">UpdateOutbandwidth</a>: <i>String</i>
    <a href="#updateoutbandwidthmaximum" title="UpdateOutbandwidthMaximum">UpdateOutbandwidthMaximum</a>: <i>Double</i>
    <a href="#updateoutbandwidthminimum" title="UpdateOutbandwidthMinimum">UpdateOutbandwidthMinimum</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#schedules" title="Schedules">Schedules</a>: <i>
      - <a href="schedulesdefinition.md">SchedulesDefinition</a></i>
</pre>

## Properties

#### Diffserv

DSCP used for speed test.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

Speed test server name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable scheduled speed test. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateInbandwidth

Enable/disable bypassing interface's inbound bandwidth setting. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateInbandwidthMaximum

Maximum downloading bandwidth (kbps) to be used in a speed test.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateInbandwidthMinimum

Minimum downloading bandwidth (kbps) to be considered effective.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateOutbandwidth

Enable/disable bypassing interface's outbound bandwidth setting. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateOutbandwidthMaximum

Maximum uploading bandwidth (kbps) to be used in a speed test.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateOutbandwidthMinimum

Minimum uploading bandwidth (kbps) to be considered effective.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedules

_Required_: No

_Type_: List of <a href="schedulesdefinition.md">SchedulesDefinition</a>

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

