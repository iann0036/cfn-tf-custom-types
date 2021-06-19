# TF::AzureRM::KustoCluster OptimizedAutoScaleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maximuminstances" title="MaximumInstances">MaximumInstances</a>" : <i>Double</i>,
    "<a href="#minimuminstances" title="MinimumInstances">MinimumInstances</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maximuminstances" title="MaximumInstances">MaximumInstances</a>: <i>Double</i>
<a href="#minimuminstances" title="MinimumInstances">MinimumInstances</a>: <i>Double</i>
</pre>

## Properties

#### MaximumInstances

The maximum number of allowed instances. Must between `0` and `1000`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumInstances

The minimum number of allowed instances. Must between `0` and `1000`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

