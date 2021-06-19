# TF::Rancher2::ClusterTemplate UpdateStrategyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#strategy" title="Strategy">Strategy</a>" : <i>String</i>,
    "<a href="#rollingupdate" title="RollingUpdate">RollingUpdate</a>" : <i>[ <a href="rollingupdatedefinition.md">RollingUpdateDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#strategy" title="Strategy">Strategy</a>: <i>String</i>
<a href="#rollingupdate" title="RollingUpdate">RollingUpdate</a>: <i>
      - <a href="rollingupdatedefinition.md">RollingUpdateDefinition</a></i>
</pre>

## Properties

#### Strategy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollingUpdate

_Required_: No

_Type_: List of <a href="rollingupdatedefinition.md">RollingUpdateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

