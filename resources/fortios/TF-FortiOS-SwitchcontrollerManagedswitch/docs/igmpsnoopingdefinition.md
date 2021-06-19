# TF::FortiOS::SwitchcontrollerManagedswitch IgmpSnoopingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#agingtime" title="AgingTime">AgingTime</a>" : <i>Double</i>,
    "<a href="#floodunknownmulticast" title="FloodUnknownMulticast">FloodUnknownMulticast</a>" : <i>String</i>,
    "<a href="#localoverride" title="LocalOverride">LocalOverride</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#agingtime" title="AgingTime">AgingTime</a>: <i>Double</i>
<a href="#floodunknownmulticast" title="FloodUnknownMulticast">FloodUnknownMulticast</a>: <i>String</i>
<a href="#localoverride" title="LocalOverride">LocalOverride</a>: <i>String</i>
</pre>

## Properties

#### AgingTime

Maximum time to retain a multicast snooping entry for which no packets have been seen (15 - 3600 sec, default = 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloodUnknownMulticast

Enable/disable unknown multicast flooding. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalOverride

Enable/disable overriding the global IGMP snooping configuration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

