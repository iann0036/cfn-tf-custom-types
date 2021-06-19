# TF::Thunder::InterfaceEthernetIpv6 RouterAdverDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#advermtu" title="AdverMtu">AdverMtu</a>" : <i>Double</i>,
    "<a href="#advermtudisable" title="AdverMtuDisable">AdverMtuDisable</a>" : <i>Double</i>,
    "<a href="#advervrid" title="AdverVrid">AdverVrid</a>" : <i>Double</i>,
    "<a href="#advervriddefault" title="AdverVridDefault">AdverVridDefault</a>" : <i>Double</i>,
    "<a href="#defaultlifetime" title="DefaultLifetime">DefaultLifetime</a>" : <i>Double</i>,
    "<a href="#floatingip" title="FloatingIp">FloatingIp</a>" : <i>String</i>,
    "<a href="#floatingipdefaultvrid" title="FloatingIpDefaultVrid">FloatingIpDefaultVrid</a>" : <i>String</i>,
    "<a href="#hoplimit" title="HopLimit">HopLimit</a>" : <i>Double</i>,
    "<a href="#managedconfigaction" title="ManagedConfigAction">ManagedConfigAction</a>" : <i>String</i>,
    "<a href="#maxinterval" title="MaxInterval">MaxInterval</a>" : <i>Double</i>,
    "<a href="#mininterval" title="MinInterval">MinInterval</a>" : <i>Double</i>,
    "<a href="#otherconfigaction" title="OtherConfigAction">OtherConfigAction</a>" : <i>String</i>,
    "<a href="#ratelimit" title="RateLimit">RateLimit</a>" : <i>Double</i>,
    "<a href="#reachabletime" title="ReachableTime">ReachableTime</a>" : <i>Double</i>,
    "<a href="#retransmittimer" title="RetransmitTimer">RetransmitTimer</a>" : <i>Double</i>,
    "<a href="#usefloatingip" title="UseFloatingIp">UseFloatingIp</a>" : <i>Double</i>,
    "<a href="#usefloatingipdefaultvrid" title="UseFloatingIpDefaultVrid">UseFloatingIpDefaultVrid</a>" : <i>Double</i>,
    "<a href="#prefixlist" title="PrefixList">PrefixList</a>" : <i>[ <a href="prefixlistdefinition.md">PrefixListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#advermtu" title="AdverMtu">AdverMtu</a>: <i>Double</i>
<a href="#advermtudisable" title="AdverMtuDisable">AdverMtuDisable</a>: <i>Double</i>
<a href="#advervrid" title="AdverVrid">AdverVrid</a>: <i>Double</i>
<a href="#advervriddefault" title="AdverVridDefault">AdverVridDefault</a>: <i>Double</i>
<a href="#defaultlifetime" title="DefaultLifetime">DefaultLifetime</a>: <i>Double</i>
<a href="#floatingip" title="FloatingIp">FloatingIp</a>: <i>String</i>
<a href="#floatingipdefaultvrid" title="FloatingIpDefaultVrid">FloatingIpDefaultVrid</a>: <i>String</i>
<a href="#hoplimit" title="HopLimit">HopLimit</a>: <i>Double</i>
<a href="#managedconfigaction" title="ManagedConfigAction">ManagedConfigAction</a>: <i>String</i>
<a href="#maxinterval" title="MaxInterval">MaxInterval</a>: <i>Double</i>
<a href="#mininterval" title="MinInterval">MinInterval</a>: <i>Double</i>
<a href="#otherconfigaction" title="OtherConfigAction">OtherConfigAction</a>: <i>String</i>
<a href="#ratelimit" title="RateLimit">RateLimit</a>: <i>Double</i>
<a href="#reachabletime" title="ReachableTime">ReachableTime</a>: <i>Double</i>
<a href="#retransmittimer" title="RetransmitTimer">RetransmitTimer</a>: <i>Double</i>
<a href="#usefloatingip" title="UseFloatingIp">UseFloatingIp</a>: <i>Double</i>
<a href="#usefloatingipdefaultvrid" title="UseFloatingIpDefaultVrid">UseFloatingIpDefaultVrid</a>: <i>Double</i>
<a href="#prefixlist" title="PrefixList">PrefixList</a>: <i>
      - <a href="prefixlistdefinition.md">PrefixListDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdverMtu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdverMtuDisable

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdverVrid

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdverVridDefault

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLifetime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIpDefaultVrid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HopLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedConfigAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OtherConfigAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReachableTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetransmitTimer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseFloatingIp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseFloatingIpDefaultVrid

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixList

_Required_: No

_Type_: List of <a href="prefixlistdefinition.md">PrefixListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

