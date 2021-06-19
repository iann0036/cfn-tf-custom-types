# TF::Rancher2::ClusterTemplate EventRateLimitDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configuration" title="Configuration">Configuration</a>" : <i>[ <a href="configurationdefinition.md">ConfigurationDefinition</a>, ... ]</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#configuration" title="Configuration">Configuration</a>: <i>
      - <a href="configurationdefinition.md">ConfigurationDefinition</a></i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
</pre>

## Properties

#### Configuration

_Required_: No

_Type_: List of <a href="configurationdefinition.md">ConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

