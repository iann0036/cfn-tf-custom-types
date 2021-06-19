# TF::Volterra::Route MirrorPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cluster" title="Cluster">Cluster</a>" : <i>[ <a href="clusterdefinition.md">ClusterDefinition</a>, ... ]</i>,
    "<a href="#percent" title="Percent">Percent</a>" : <i>[ <a href="percentdefinition.md">PercentDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cluster" title="Cluster">Cluster</a>: <i>
      - <a href="clusterdefinition.md">ClusterDefinition</a></i>
<a href="#percent" title="Percent">Percent</a>: <i>
      - <a href="percentdefinition.md">PercentDefinition</a></i>
</pre>

## Properties

#### Cluster

_Required_: No

_Type_: List of <a href="clusterdefinition.md">ClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Percent

_Required_: No

_Type_: List of <a href="percentdefinition.md">PercentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

