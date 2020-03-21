# Terraform::Spotinst::ElastigroupGcp ScheduledTask

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cronexpression" title="CronExpression">CronExpression</a>" : <i>String</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>" : <i>String</i>,
    "<a href="#mincapacity" title="MinCapacity">MinCapacity</a>" : <i>String</i>,
    "<a href="#targetcapacity" title="TargetCapacity">TargetCapacity</a>" : <i>String</i>,
    "<a href="#tasktype" title="TaskType">TaskType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cronexpression" title="CronExpression">CronExpression</a>: <i>String</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>: <i>String</i>
<a href="#mincapacity" title="MinCapacity">MinCapacity</a>: <i>String</i>
<a href="#targetcapacity" title="TargetCapacity">TargetCapacity</a>: <i>String</i>
<a href="#tasktype" title="TaskType">TaskType</a>: <i>String</i>
</pre>

## Properties

#### CronExpression

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCapacity

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCapacity

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetCapacity

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

