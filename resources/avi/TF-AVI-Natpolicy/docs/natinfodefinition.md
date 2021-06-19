# TF::AVI::Natpolicy NatInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#natip" title="NatIp">NatIp</a>" : <i>[ <a href="natipdefinition.md">NatIpDefinition</a>, ... ]</i>,
    "<a href="#natiprange" title="NatIpRange">NatIpRange</a>" : <i>[ <a href="natiprangedefinition.md">NatIpRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#natip" title="NatIp">NatIp</a>: <i>
      - <a href="natipdefinition.md">NatIpDefinition</a></i>
<a href="#natiprange" title="NatIpRange">NatIpRange</a>: <i>
      - <a href="natiprangedefinition.md">NatIpRangeDefinition</a></i>
</pre>

## Properties

#### NatIp

_Required_: No

_Type_: List of <a href="natipdefinition.md">NatIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatIpRange

_Required_: No

_Type_: List of <a href="natiprangedefinition.md">NatIpRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

