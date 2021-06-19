# TF::Google::ComputeRegionUrlMap FaultInjectionPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#abort" title="Abort">Abort</a>" : <i>[ <a href="abortdefinition.md">AbortDefinition</a>, ... ]</i>,
    "<a href="#delay" title="Delay">Delay</a>" : <i>[ <a href="delaydefinition.md">DelayDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#abort" title="Abort">Abort</a>: <i>
      - <a href="abortdefinition.md">AbortDefinition</a></i>
<a href="#delay" title="Delay">Delay</a>: <i>
      - <a href="delaydefinition.md">DelayDefinition</a></i>
</pre>

## Properties

#### Abort

_Required_: No

_Type_: List of <a href="abortdefinition.md">AbortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delay

_Required_: No

_Type_: List of <a href="delaydefinition.md">DelayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

