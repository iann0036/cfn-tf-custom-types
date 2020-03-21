# Terraform::Datadog::ServiceLevelObjective Thresholds

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#target" title="Target">Target</a>" : <i>Double</i>,
    "<a href="#targetdisplay" title="TargetDisplay">TargetDisplay</a>" : <i>String</i>,
    "<a href="#timeframe" title="Timeframe">Timeframe</a>" : <i>String</i>,
    "<a href="#warning" title="Warning">Warning</a>" : <i>Double</i>,
    "<a href="#warningdisplay" title="WarningDisplay">WarningDisplay</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#target" title="Target">Target</a>: <i>Double</i>
<a href="#targetdisplay" title="TargetDisplay">TargetDisplay</a>: <i>String</i>
<a href="#timeframe" title="Timeframe">Timeframe</a>: <i>String</i>
<a href="#warning" title="Warning">Warning</a>: <i>Double</i>
<a href="#warningdisplay" title="WarningDisplay">WarningDisplay</a>: <i>String</i>
</pre>

## Properties

#### Target

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDisplay

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeframe

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Warning

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarningDisplay

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

