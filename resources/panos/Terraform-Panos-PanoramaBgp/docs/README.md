# Terraform::Panos::PanoramaBgp

This resource allows you to add/update/delete a Panorama virtual
router BGP configuration.

**Important Note:**  When it comes to BGP configuration, PAN-OS requires that
BGP itself first be configured before you can add other BGP sub-config, such
as dampening profiles or peer groups.  Since every BGP resource must reference a
virtual router, the key to accomplishing this is by pointing the `virtual_router`
param for each BGP sub-config to `panos_panorama_bgp.foo.virtual_router` instead
of `panos_panorama_virtual_router.bar.name`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaBgp",
    "Properties" : {
        "<a href="#aggregatemed" title="AggregateMed">AggregateMed</a>" : <i>Boolean</i>,
        "<a href="#allowredistributedefaultroute" title="AllowRedistributeDefaultRoute">AllowRedistributeDefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#alwayscomparemed" title="AlwaysCompareMed">AlwaysCompareMed</a>" : <i>Boolean</i>,
        "<a href="#asformat" title="AsFormat">AsFormat</a>" : <i>String</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>String</i>,
        "<a href="#bfdprofile" title="BfdProfile">BfdProfile</a>" : <i>String</i>,
        "<a href="#confederationmemberas" title="ConfederationMemberAs">ConfederationMemberAs</a>" : <i>String</i>,
        "<a href="#defaultlocalpreference" title="DefaultLocalPreference">DefaultLocalPreference</a>" : <i>String</i>,
        "<a href="#deterministicmedcomparison" title="DeterministicMedComparison">DeterministicMedComparison</a>" : <i>Boolean</i>,
        "<a href="#ecmpmultias" title="EcmpMultiAs">EcmpMultiAs</a>" : <i>Boolean</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#enablegracefulrestart" title="EnableGracefulRestart">EnableGracefulRestart</a>" : <i>Boolean</i>,
        "<a href="#enforcefirstas" title="EnforceFirstAs">EnforceFirstAs</a>" : <i>Boolean</i>,
        "<a href="#installroute" title="InstallRoute">InstallRoute</a>" : <i>Boolean</i>,
        "<a href="#localrestarttime" title="LocalRestartTime">LocalRestartTime</a>" : <i>Double</i>,
        "<a href="#maxpeerrestarttime" title="MaxPeerRestartTime">MaxPeerRestartTime</a>" : <i>Double</i>,
        "<a href="#reflectorclusterid" title="ReflectorClusterId">ReflectorClusterId</a>" : <i>String</i>,
        "<a href="#rejectdefaultroute" title="RejectDefaultRoute">RejectDefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>String</i>,
        "<a href="#staleroutetime" title="StaleRouteTime">StaleRouteTime</a>" : <i>Double</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaBgp
Properties:
    <a href="#aggregatemed" title="AggregateMed">AggregateMed</a>: <i>Boolean</i>
    <a href="#allowredistributedefaultroute" title="AllowRedistributeDefaultRoute">AllowRedistributeDefaultRoute</a>: <i>Boolean</i>
    <a href="#alwayscomparemed" title="AlwaysCompareMed">AlwaysCompareMed</a>: <i>Boolean</i>
    <a href="#asformat" title="AsFormat">AsFormat</a>: <i>String</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>String</i>
    <a href="#bfdprofile" title="BfdProfile">BfdProfile</a>: <i>String</i>
    <a href="#confederationmemberas" title="ConfederationMemberAs">ConfederationMemberAs</a>: <i>String</i>
    <a href="#defaultlocalpreference" title="DefaultLocalPreference">DefaultLocalPreference</a>: <i>String</i>
    <a href="#deterministicmedcomparison" title="DeterministicMedComparison">DeterministicMedComparison</a>: <i>Boolean</i>
    <a href="#ecmpmultias" title="EcmpMultiAs">EcmpMultiAs</a>: <i>Boolean</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#enablegracefulrestart" title="EnableGracefulRestart">EnableGracefulRestart</a>: <i>Boolean</i>
    <a href="#enforcefirstas" title="EnforceFirstAs">EnforceFirstAs</a>: <i>Boolean</i>
    <a href="#installroute" title="InstallRoute">InstallRoute</a>: <i>Boolean</i>
    <a href="#localrestarttime" title="LocalRestartTime">LocalRestartTime</a>: <i>Double</i>
    <a href="#maxpeerrestarttime" title="MaxPeerRestartTime">MaxPeerRestartTime</a>: <i>Double</i>
    <a href="#reflectorclusterid" title="ReflectorClusterId">ReflectorClusterId</a>: <i>String</i>
    <a href="#rejectdefaultroute" title="RejectDefaultRoute">RejectDefaultRoute</a>: <i>Boolean</i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>String</i>
    <a href="#staleroutetime" title="StaleRouteTime">StaleRouteTime</a>: <i>Double</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
</pre>

## Properties

#### AggregateMed

Aggregate route only if they have
same MED attributes (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowRedistributeDefaultRoute

Allow redistribute
default route to BGP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlwaysCompareMed

Always compare MEDs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsFormat

AS format.  Valid values are `"2-byte"` (default)
or `"4-byte"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsNumber

Local AS number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdProfile

BFD configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfederationMemberAs

Confederation requires
member-AS number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLocalPreference

Default local preference (default:
`"100"`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeterministicMedComparison

Deterministic MED
comparison (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpMultiAs

Support multiple AS in ECMP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Enable BGP or not (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableGracefulRestart

Enable graceful restart
(default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceFirstAs

Enforce First AS for EBGP (default:
`true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallRoute

Populate BGP learned route to global
route table.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalRestartTime

Local restart time to advertise to
peer, in seconds (default: `120`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPeerRestartTime

Maximum of peer restart time
accepted, in seconds (default: `120`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReflectorClusterId

Route reflector cluster ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectDefaultRoute

Do not learn default route from
BGP (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

Router ID of this BGP instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaleRouteTime

Time to remove stale routes after
peer restart, in seconds (default: `120`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

The template stack name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

The virtual router to add this BGP
configuration to.

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

