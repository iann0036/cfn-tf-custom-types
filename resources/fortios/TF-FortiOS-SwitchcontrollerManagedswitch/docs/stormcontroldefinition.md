# TF::FortiOS::SwitchcontrollerManagedswitch StormControlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#broadcast" title="Broadcast">Broadcast</a>" : <i>String</i>,
    "<a href="#localoverride" title="LocalOverride">LocalOverride</a>" : <i>String</i>,
    "<a href="#rate" title="Rate">Rate</a>" : <i>Double</i>,
    "<a href="#unknownmulticast" title="UnknownMulticast">UnknownMulticast</a>" : <i>String</i>,
    "<a href="#unknownunicast" title="UnknownUnicast">UnknownUnicast</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#broadcast" title="Broadcast">Broadcast</a>: <i>String</i>
<a href="#localoverride" title="LocalOverride">LocalOverride</a>: <i>String</i>
<a href="#rate" title="Rate">Rate</a>: <i>Double</i>
<a href="#unknownmulticast" title="UnknownMulticast">UnknownMulticast</a>: <i>String</i>
<a href="#unknownunicast" title="UnknownUnicast">UnknownUnicast</a>: <i>String</i>
</pre>

## Properties

#### Broadcast

Enable/disable storm control to drop broadcast traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalOverride

Enable to override global FortiSwitch storm control settings for this FortiSwitch. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rate

Rate in packets per second at which storm traffic is controlled (1 - 10000000, default = 500). Storm control drops excess traffic data rates beyond this threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnknownMulticast

Enable/disable storm control to drop unknown multicast traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnknownUnicast

Enable/disable storm control to drop unknown unicast traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

