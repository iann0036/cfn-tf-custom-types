# TF::Alicloud::CsKubernetesNodePool ManagementDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autorepair" title="AutoRepair">AutoRepair</a>" : <i>Boolean</i>,
    "<a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>" : <i>Boolean</i>,
    "<a href="#maxunavailable" title="MaxUnavailable">MaxUnavailable</a>" : <i>Double</i>,
    "<a href="#surge" title="Surge">Surge</a>" : <i>Double</i>,
    "<a href="#surgepercentage" title="SurgePercentage">SurgePercentage</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#autorepair" title="AutoRepair">AutoRepair</a>: <i>Boolean</i>
<a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>: <i>Boolean</i>
<a href="#maxunavailable" title="MaxUnavailable">MaxUnavailable</a>: <i>Double</i>
<a href="#surge" title="Surge">Surge</a>: <i>Double</i>
<a href="#surgepercentage" title="SurgePercentage">SurgePercentage</a>: <i>Double</i>
</pre>

## Properties

#### AutoRepair

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoUpgrade

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnavailable

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Surge

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SurgePercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

