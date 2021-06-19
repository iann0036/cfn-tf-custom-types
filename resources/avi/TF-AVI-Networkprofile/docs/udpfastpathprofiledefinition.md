# TF::AVI::Networkprofile UdpFastPathProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#perpktloadbalance" title="PerPktLoadbalance">PerPktLoadbalance</a>" : <i>Boolean</i>,
    "<a href="#sessionidletimeout" title="SessionIdleTimeout">SessionIdleTimeout</a>" : <i>Double</i>,
    "<a href="#snat" title="Snat">Snat</a>" : <i>Boolean</i>,
    "<a href="#dsrprofile" title="DsrProfile">DsrProfile</a>" : <i>[ <a href="dsrprofiledefinition.md">DsrProfileDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#perpktloadbalance" title="PerPktLoadbalance">PerPktLoadbalance</a>: <i>Boolean</i>
<a href="#sessionidletimeout" title="SessionIdleTimeout">SessionIdleTimeout</a>: <i>Double</i>
<a href="#snat" title="Snat">Snat</a>: <i>Boolean</i>
<a href="#dsrprofile" title="DsrProfile">DsrProfile</a>: <i>
      - <a href="dsrprofiledefinition.md">DsrProfileDefinition</a></i>
</pre>

## Properties

#### PerPktLoadbalance

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionIdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snat

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DsrProfile

_Required_: No

_Type_: List of <a href="dsrprofiledefinition.md">DsrProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

