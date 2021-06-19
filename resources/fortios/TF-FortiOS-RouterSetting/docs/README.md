# TF::FortiOS::RouterSetting

Configure router settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::RouterSetting",
    "Properties" : {
        "<a href="#bgpdebugflags" title="BgpDebugFlags">BgpDebugFlags</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#igmpdebugflags" title="IgmpDebugFlags">IgmpDebugFlags</a>" : <i>String</i>,
        "<a href="#imidebugflags" title="ImiDebugFlags">ImiDebugFlags</a>" : <i>String</i>,
        "<a href="#isisdebugflags" title="IsisDebugFlags">IsisDebugFlags</a>" : <i>String</i>,
        "<a href="#ospf6debugeventsflags" title="Ospf6DebugEventsFlags">Ospf6DebugEventsFlags</a>" : <i>String</i>,
        "<a href="#ospf6debugifsmflags" title="Ospf6DebugIfsmFlags">Ospf6DebugIfsmFlags</a>" : <i>String</i>,
        "<a href="#ospf6debuglsaflags" title="Ospf6DebugLsaFlags">Ospf6DebugLsaFlags</a>" : <i>String</i>,
        "<a href="#ospf6debugnfsmflags" title="Ospf6DebugNfsmFlags">Ospf6DebugNfsmFlags</a>" : <i>String</i>,
        "<a href="#ospf6debugnsmflags" title="Ospf6DebugNsmFlags">Ospf6DebugNsmFlags</a>" : <i>String</i>,
        "<a href="#ospf6debugpacketflags" title="Ospf6DebugPacketFlags">Ospf6DebugPacketFlags</a>" : <i>String</i>,
        "<a href="#ospf6debugrouteflags" title="Ospf6DebugRouteFlags">Ospf6DebugRouteFlags</a>" : <i>String</i>,
        "<a href="#ospfdebugeventsflags" title="OspfDebugEventsFlags">OspfDebugEventsFlags</a>" : <i>String</i>,
        "<a href="#ospfdebugifsmflags" title="OspfDebugIfsmFlags">OspfDebugIfsmFlags</a>" : <i>String</i>,
        "<a href="#ospfdebuglsaflags" title="OspfDebugLsaFlags">OspfDebugLsaFlags</a>" : <i>String</i>,
        "<a href="#ospfdebugnfsmflags" title="OspfDebugNfsmFlags">OspfDebugNfsmFlags</a>" : <i>String</i>,
        "<a href="#ospfdebugnsmflags" title="OspfDebugNsmFlags">OspfDebugNsmFlags</a>" : <i>String</i>,
        "<a href="#ospfdebugpacketflags" title="OspfDebugPacketFlags">OspfDebugPacketFlags</a>" : <i>String</i>,
        "<a href="#ospfdebugrouteflags" title="OspfDebugRouteFlags">OspfDebugRouteFlags</a>" : <i>String</i>,
        "<a href="#pimdmdebugflags" title="PimdmDebugFlags">PimdmDebugFlags</a>" : <i>String</i>,
        "<a href="#pimsmdebugjoinpruneflags" title="PimsmDebugJoinpruneFlags">PimsmDebugJoinpruneFlags</a>" : <i>String</i>,
        "<a href="#pimsmdebugsimpleflags" title="PimsmDebugSimpleFlags">PimsmDebugSimpleFlags</a>" : <i>String</i>,
        "<a href="#pimsmdebugtimerflags" title="PimsmDebugTimerFlags">PimsmDebugTimerFlags</a>" : <i>String</i>,
        "<a href="#ripdebugflags" title="RipDebugFlags">RipDebugFlags</a>" : <i>String</i>,
        "<a href="#ripngdebugflags" title="RipngDebugFlags">RipngDebugFlags</a>" : <i>String</i>,
        "<a href="#showfilter" title="ShowFilter">ShowFilter</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::RouterSetting
Properties:
    <a href="#bgpdebugflags" title="BgpDebugFlags">BgpDebugFlags</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#igmpdebugflags" title="IgmpDebugFlags">IgmpDebugFlags</a>: <i>String</i>
    <a href="#imidebugflags" title="ImiDebugFlags">ImiDebugFlags</a>: <i>String</i>
    <a href="#isisdebugflags" title="IsisDebugFlags">IsisDebugFlags</a>: <i>String</i>
    <a href="#ospf6debugeventsflags" title="Ospf6DebugEventsFlags">Ospf6DebugEventsFlags</a>: <i>String</i>
    <a href="#ospf6debugifsmflags" title="Ospf6DebugIfsmFlags">Ospf6DebugIfsmFlags</a>: <i>String</i>
    <a href="#ospf6debuglsaflags" title="Ospf6DebugLsaFlags">Ospf6DebugLsaFlags</a>: <i>String</i>
    <a href="#ospf6debugnfsmflags" title="Ospf6DebugNfsmFlags">Ospf6DebugNfsmFlags</a>: <i>String</i>
    <a href="#ospf6debugnsmflags" title="Ospf6DebugNsmFlags">Ospf6DebugNsmFlags</a>: <i>String</i>
    <a href="#ospf6debugpacketflags" title="Ospf6DebugPacketFlags">Ospf6DebugPacketFlags</a>: <i>String</i>
    <a href="#ospf6debugrouteflags" title="Ospf6DebugRouteFlags">Ospf6DebugRouteFlags</a>: <i>String</i>
    <a href="#ospfdebugeventsflags" title="OspfDebugEventsFlags">OspfDebugEventsFlags</a>: <i>String</i>
    <a href="#ospfdebugifsmflags" title="OspfDebugIfsmFlags">OspfDebugIfsmFlags</a>: <i>String</i>
    <a href="#ospfdebuglsaflags" title="OspfDebugLsaFlags">OspfDebugLsaFlags</a>: <i>String</i>
    <a href="#ospfdebugnfsmflags" title="OspfDebugNfsmFlags">OspfDebugNfsmFlags</a>: <i>String</i>
    <a href="#ospfdebugnsmflags" title="OspfDebugNsmFlags">OspfDebugNsmFlags</a>: <i>String</i>
    <a href="#ospfdebugpacketflags" title="OspfDebugPacketFlags">OspfDebugPacketFlags</a>: <i>String</i>
    <a href="#ospfdebugrouteflags" title="OspfDebugRouteFlags">OspfDebugRouteFlags</a>: <i>String</i>
    <a href="#pimdmdebugflags" title="PimdmDebugFlags">PimdmDebugFlags</a>: <i>String</i>
    <a href="#pimsmdebugjoinpruneflags" title="PimsmDebugJoinpruneFlags">PimsmDebugJoinpruneFlags</a>: <i>String</i>
    <a href="#pimsmdebugsimpleflags" title="PimsmDebugSimpleFlags">PimsmDebugSimpleFlags</a>: <i>String</i>
    <a href="#pimsmdebugtimerflags" title="PimsmDebugTimerFlags">PimsmDebugTimerFlags</a>: <i>String</i>
    <a href="#ripdebugflags" title="RipDebugFlags">RipDebugFlags</a>: <i>String</i>
    <a href="#ripngdebugflags" title="RipngDebugFlags">RipngDebugFlags</a>: <i>String</i>
    <a href="#showfilter" title="ShowFilter">ShowFilter</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### BgpDebugFlags

bgp_debug_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

Hostname for this virtual domain router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgmpDebugFlags

igmp_debug_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImiDebugFlags

imi_debug_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisDebugFlags

isis_debug_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf6DebugEventsFlags

ospf6_debug_events_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf6DebugIfsmFlags

ospf6_debug_ifsm_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf6DebugLsaFlags

ospf6_debug_lsa_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf6DebugNfsmFlags

ospf6_debug_nfsm_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf6DebugNsmFlags

ospf6_debug_nsm_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf6DebugPacketFlags

ospf6_debug_packet_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf6DebugRouteFlags

ospf6_debug_route_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfDebugEventsFlags

ospf_debug_events_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfDebugIfsmFlags

ospf_debug_ifsm_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfDebugLsaFlags

ospf_debug_lsa_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfDebugNfsmFlags

ospf_debug_nfsm_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfDebugNsmFlags

ospf_debug_nsm_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfDebugPacketFlags

ospf_debug_packet_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfDebugRouteFlags

ospf_debug_route_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PimdmDebugFlags

pimdm_debug_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PimsmDebugJoinpruneFlags

pimsm_debug_joinprune_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PimsmDebugSimpleFlags

pimsm_debug_simple_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PimsmDebugTimerFlags

pimsm_debug_timer_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RipDebugFlags

rip_debug_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RipngDebugFlags

ripng_debug_flags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowFilter

Prefix-list as filter for showing routes.

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

