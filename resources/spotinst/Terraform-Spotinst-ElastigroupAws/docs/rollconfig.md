# Terraform::Spotinst::ElastigroupAws RollConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#batchsizepercentage" title="BatchSizePercentage">BatchSizePercentage</a>" : <i>Double</i>,
    "<a href="#graceperiod" title="GracePeriod">GracePeriod</a>" : <i>Double</i>,
    "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>,
    "<a href="#waitforrollpercentage" title="WaitForRollPercentage">WaitForRollPercentage</a>" : <i>Double</i>,
    "<a href="#waitforrolltimeout" title="WaitForRollTimeout">WaitForRollTimeout</a>" : <i>Double</i>,
    "<a href="#strategy" title="Strategy">Strategy</a>" : <i>[ <a href="rollconfig-strategy.md">Strategy</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#batchsizepercentage" title="BatchSizePercentage">BatchSizePercentage</a>: <i>Double</i>
<a href="#graceperiod" title="GracePeriod">GracePeriod</a>: <i>Double</i>
<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
<a href="#waitforrollpercentage" title="WaitForRollPercentage">WaitForRollPercentage</a>: <i>Double</i>
<a href="#waitforrolltimeout" title="WaitForRollTimeout">WaitForRollTimeout</a>: <i>Double</i>
<a href="#strategy" title="Strategy">Strategy</a>: <i>
      - <a href="rollconfig-strategy.md">Strategy</a></i>
</pre>

## Properties

#### BatchSizePercentage

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracePeriod

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForRollPercentage

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForRollTimeout

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

_Required_: No
_Type_: List of <a href="rollconfig-strategy.md">Strategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

