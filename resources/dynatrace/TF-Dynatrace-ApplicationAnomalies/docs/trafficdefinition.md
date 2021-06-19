# TF::Dynatrace::ApplicationAnomalies TrafficDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#drops" title="Drops">Drops</a>" : <i>[ <a href="dropsdefinition.md">DropsDefinition</a>, ... ]</i>,
    "<a href="#spikes" title="Spikes">Spikes</a>" : <i>[ <a href="spikesdefinition.md">SpikesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#drops" title="Drops">Drops</a>: <i>
      - <a href="dropsdefinition.md">DropsDefinition</a></i>
<a href="#spikes" title="Spikes">Spikes</a>: <i>
      - <a href="spikesdefinition.md">SpikesDefinition</a></i>
</pre>

## Properties

#### Drops

_Required_: No

_Type_: List of <a href="dropsdefinition.md">DropsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spikes

_Required_: No

_Type_: List of <a href="spikesdefinition.md">SpikesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

