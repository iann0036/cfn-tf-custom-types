# Terraform::Spotinst::ElastigroupAwsBeanstalk DeploymentPreferences

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automaticroll" title="AutomaticRoll">AutomaticRoll</a>" : <i>Boolean</i>,
    "<a href="#batchsizepercentage" title="BatchSizePercentage">BatchSizePercentage</a>" : <i>Double</i>,
    "<a href="#graceperiod" title="GracePeriod">GracePeriod</a>" : <i>Double</i>,
    "<a href="#strategy" title="Strategy">Strategy</a>" : <i>[ <a href="deploymentpreferences-strategy.md">Strategy</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#automaticroll" title="AutomaticRoll">AutomaticRoll</a>: <i>Boolean</i>
<a href="#batchsizepercentage" title="BatchSizePercentage">BatchSizePercentage</a>: <i>Double</i>
<a href="#graceperiod" title="GracePeriod">GracePeriod</a>: <i>Double</i>
<a href="#strategy" title="Strategy">Strategy</a>: <i>
      - <a href="deploymentpreferences-strategy.md">Strategy</a></i>
</pre>

## Properties

#### AutomaticRoll

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BatchSizePercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracePeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

_Required_: No

_Type_: List of <a href="deploymentpreferences-strategy.md">Strategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

