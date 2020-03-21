# Terraform::AzureRM::MonitorAutoscaleSetting Capacity

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#default" title="Default">Default</a>" : <i>Double</i>,
    "<a href="#maximum" title="Maximum">Maximum</a>" : <i>Double</i>,
    "<a href="#minimum" title="Minimum">Minimum</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#default" title="Default">Default</a>: <i>Double</i>
<a href="#maximum" title="Maximum">Maximum</a>: <i>Double</i>
<a href="#minimum" title="Minimum">Minimum</a>: <i>Double</i>
</pre>

## Properties

#### Default

The number of instances that are available for scaling if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. Valid values are between `0` and `1000`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maximum

The maximum number of instances for this resource. Valid values are between `0` and `1000`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minimum

The minimum number of instances for this resource. Valid values are between `0` and `1000`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

