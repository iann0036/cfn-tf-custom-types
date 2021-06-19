# TF::Rancher2::Cluster UpgradeStrategyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#drain" title="Drain">Drain</a>" : <i>Boolean</i>,
    "<a href="#maxunavailablecontrolplane" title="MaxUnavailableControlplane">MaxUnavailableControlplane</a>" : <i>String</i>,
    "<a href="#maxunavailableworker" title="MaxUnavailableWorker">MaxUnavailableWorker</a>" : <i>String</i>,
    "<a href="#draininput" title="DrainInput">DrainInput</a>" : <i>[ <a href="draininputdefinition.md">DrainInputDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#drain" title="Drain">Drain</a>: <i>Boolean</i>
<a href="#maxunavailablecontrolplane" title="MaxUnavailableControlplane">MaxUnavailableControlplane</a>: <i>String</i>
<a href="#maxunavailableworker" title="MaxUnavailableWorker">MaxUnavailableWorker</a>: <i>String</i>
<a href="#draininput" title="DrainInput">DrainInput</a>: <i>
      - <a href="draininputdefinition.md">DrainInputDefinition</a></i>
</pre>

## Properties

#### Drain

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnavailableControlplane

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnavailableWorker

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrainInput

_Required_: No

_Type_: List of <a href="draininputdefinition.md">DrainInputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

