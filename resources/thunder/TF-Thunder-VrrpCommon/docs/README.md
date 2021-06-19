# TF::Thunder::VrrpCommon

`thunder_vrrp_common` Provides details about thunder vrrp common

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::VrrpCommon",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#arpretry" title="ArpRetry">ArpRetry</a>" : <i>Double</i>,
        "<a href="#deadtimer" title="DeadTimer">DeadTimer</a>" : <i>Double</i>,
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>Double</i>,
        "<a href="#disabledefaultvrid" title="DisableDefaultVrid">DisableDefaultVrid</a>" : <i>Double</i>,
        "<a href="#forwardl4packetonstandby" title="ForwardL4PacketOnStandby">ForwardL4PacketOnStandby</a>" : <i>Double</i>,
        "<a href="#getreadytime" title="GetReadyTime">GetReadyTime</a>" : <i>Double</i>,
        "<a href="#hellointerval" title="HelloInterval">HelloInterval</a>" : <i>Double</i>,
        "<a href="#preemptiondelay" title="PreemptionDelay">PreemptionDelay</a>" : <i>Double</i>,
        "<a href="#restarttime" title="RestartTime">RestartTime</a>" : <i>Double</i>,
        "<a href="#setid" title="SetId">SetId</a>" : <i>Double</i>,
        "<a href="#trackeventdelay" title="TrackEventDelay">TrackEventDelay</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#hostidappendtovrid" title="HostidAppendToVrid">HostidAppendToVrid</a>" : <i>[ <a href="hostidappendtovriddefinition.md">HostidAppendToVridDefinition</a>, ... ]</i>,
        "<a href="#inlinemodecfg" title="InlineModeCfg">InlineModeCfg</a>" : <i>[ <a href="inlinemodecfgdefinition.md">InlineModeCfgDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::VrrpCommon
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#arpretry" title="ArpRetry">ArpRetry</a>: <i>Double</i>
    <a href="#deadtimer" title="DeadTimer">DeadTimer</a>: <i>Double</i>
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>Double</i>
    <a href="#disabledefaultvrid" title="DisableDefaultVrid">DisableDefaultVrid</a>: <i>Double</i>
    <a href="#forwardl4packetonstandby" title="ForwardL4PacketOnStandby">ForwardL4PacketOnStandby</a>: <i>Double</i>
    <a href="#getreadytime" title="GetReadyTime">GetReadyTime</a>: <i>Double</i>
    <a href="#hellointerval" title="HelloInterval">HelloInterval</a>: <i>Double</i>
    <a href="#preemptiondelay" title="PreemptionDelay">PreemptionDelay</a>: <i>Double</i>
    <a href="#restarttime" title="RestartTime">RestartTime</a>: <i>Double</i>
    <a href="#setid" title="SetId">SetId</a>: <i>Double</i>
    <a href="#trackeventdelay" title="TrackEventDelay">TrackEventDelay</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#hostidappendtovrid" title="HostidAppendToVrid">HostidAppendToVrid</a>: <i>
      - <a href="hostidappendtovriddefinition.md">HostidAppendToVridDefinition</a></i>
    <a href="#inlinemodecfg" title="InlineModeCfg">InlineModeCfg</a>: <i>
      - <a href="inlinemodecfgdefinition.md">InlineModeCfgDefinition</a></i>
</pre>

## Properties

#### Action

‘enable’: enable vrrp-a; ‘disable’: disable vrrp-a;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpRetry

Number of additional gratuitous ARPs sent out after HA failover (1-255, default is 4).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadTimer

VRRP-A dead timer in terms of how many hello messages missed, default is 5 (2-255, default is 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceId

Unique ID for each VRRP-A box (Device-id number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableDefaultVrid

Disable default vrid.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardL4PacketOnStandby

Enables Layer 2/3 forwarding of Layer 4 traffic on the Standby ACOS device.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GetReadyTime

set get ready time after ax starting up (60-1200, in unit of 100millisec, default is 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloInterval

VRRP-A Hello Interval (1-255, in unit of 100millisec, default is 2).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptionDelay

Delay before changing state from Active to Standby (1-255, in unit of 100millisec, default is 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartTime

Time between restarting ports on standby system after transition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetId

Set-ID for HA configuration (Set id from 1 to 15).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrackEventDelay

Delay before changing state after up/down event (Units of 100 milliseconds (default 30)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostidAppendToVrid

_Required_: No

_Type_: List of <a href="hostidappendtovriddefinition.md">HostidAppendToVridDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InlineModeCfg

_Required_: No

_Type_: List of <a href="inlinemodecfgdefinition.md">InlineModeCfgDefinition</a>

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

