# TF::Volterra::HttpLoadbalancer MirrorPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#originpool" title="OriginPool">OriginPool</a>" : <i>[ <a href="originpooldefinition.md">OriginPoolDefinition</a>, ... ]</i>,
    "<a href="#percent" title="Percent">Percent</a>" : <i>[ <a href="percentdefinition.md">PercentDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#originpool" title="OriginPool">OriginPool</a>: <i>
      - <a href="originpooldefinition.md">OriginPoolDefinition</a></i>
<a href="#percent" title="Percent">Percent</a>: <i>
      - <a href="percentdefinition.md">PercentDefinition</a></i>
</pre>

## Properties

#### OriginPool

_Required_: No

_Type_: List of <a href="originpooldefinition.md">OriginPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Percent

_Required_: No

_Type_: List of <a href="percentdefinition.md">PercentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

