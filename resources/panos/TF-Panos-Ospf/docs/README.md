# TF::Panos::Ospf

Manages OSPF config attached to a virtual router.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::Ospf",
    "Properties" : {
        "<a href="#allowredistributedefaultroute" title="AllowRedistributeDefaultRoute">AllowRedistributeDefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#bfdprofile" title="BfdProfile">BfdProfile</a>" : <i>String</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#enablegracefulrestart" title="EnableGracefulRestart">EnableGracefulRestart</a>" : <i>Boolean</i>,
        "<a href="#graceperiod" title="GracePeriod">GracePeriod</a>" : <i>Double</i>,
        "<a href="#helperenable" title="HelperEnable">HelperEnable</a>" : <i>Boolean</i>,
        "<a href="#lsainterval" title="LsaInterval">LsaInterval</a>" : <i>Double</i>,
        "<a href="#maxneighborrestarttime" title="MaxNeighborRestartTime">MaxNeighborRestartTime</a>" : <i>Double</i>,
        "<a href="#rejectdefaultroute" title="RejectDefaultRoute">RejectDefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#rfc1583" title="Rfc1583">Rfc1583</a>" : <i>Boolean</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>String</i>,
        "<a href="#spfcalculationdelay" title="SpfCalculationDelay">SpfCalculationDelay</a>" : <i>Double</i>,
        "<a href="#strictlsachecking" title="StrictLsaChecking">StrictLsaChecking</a>" : <i>Boolean</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::Ospf
Properties:
    <a href="#allowredistributedefaultroute" title="AllowRedistributeDefaultRoute">AllowRedistributeDefaultRoute</a>: <i>Boolean</i>
    <a href="#bfdprofile" title="BfdProfile">BfdProfile</a>: <i>String</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#enablegracefulrestart" title="EnableGracefulRestart">EnableGracefulRestart</a>: <i>Boolean</i>
    <a href="#graceperiod" title="GracePeriod">GracePeriod</a>: <i>Double</i>
    <a href="#helperenable" title="HelperEnable">HelperEnable</a>: <i>Boolean</i>
    <a href="#lsainterval" title="LsaInterval">LsaInterval</a>: <i>Double</i>
    <a href="#maxneighborrestarttime" title="MaxNeighborRestartTime">MaxNeighborRestartTime</a>: <i>Double</i>
    <a href="#rejectdefaultroute" title="RejectDefaultRoute">RejectDefaultRoute</a>: <i>Boolean</i>
    <a href="#rfc1583" title="Rfc1583">Rfc1583</a>: <i>Boolean</i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>String</i>
    <a href="#spfcalculationdelay" title="SpfCalculationDelay">SpfCalculationDelay</a>: <i>Double</i>
    <a href="#strictlsachecking" title="StrictLsaChecking">StrictLsaChecking</a>: <i>Boolean</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
</pre>

## Properties

#### AllowRedistributeDefaultRoute

Allow redistribute default route.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdProfile

BFD profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Enable flag.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableGracefulRestart

Enable graceful restart.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracePeriod

Grace period.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelperEnable

Helper enable.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LsaInterval

LSA interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNeighborRestartTime

Max neighbor restart time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectDefaultRoute

Reject default route.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rfc1583

RFC 1583.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

Router ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpfCalculationDelay

SPF calculation delay.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictLsaChecking

Strict LSA checking.

_Required_: No

_Type_: Boolean

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

#### VirtualRouter

The virtual router name.

_Required_: Yes

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

