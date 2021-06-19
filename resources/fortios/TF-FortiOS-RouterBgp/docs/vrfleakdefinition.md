# TF::FortiOS::RouterBgp VrfLeakDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#vrf" title="Vrf">Vrf</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>[ <a href="targetdefinition.md">TargetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#vrf" title="Vrf">Vrf</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>
      - <a href="targetdefinition.md">TargetDefinition</a></i>
</pre>

## Properties

#### Vrf

Origin VRF ID <0 - 31>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="targetdefinition.md">TargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

