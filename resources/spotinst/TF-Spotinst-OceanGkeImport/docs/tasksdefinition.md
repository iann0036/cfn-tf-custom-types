# TF::Spotinst::OceanGkeImport TasksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#batchsizepercentage" title="BatchSizePercentage">BatchSizePercentage</a>" : <i>Double</i>,
    "<a href="#cronexpression" title="CronExpression">CronExpression</a>" : <i>String</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#tasktype" title="TaskType">TaskType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#batchsizepercentage" title="BatchSizePercentage">BatchSizePercentage</a>: <i>Double</i>
<a href="#cronexpression" title="CronExpression">CronExpression</a>: <i>String</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#tasktype" title="TaskType">TaskType</a>: <i>String</i>
</pre>

## Properties

#### BatchSizePercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CronExpression

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

