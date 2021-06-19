# TF::Google::DataLossPreventionDeidentifyTemplate NewValueDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#booleanvalue" title="BooleanValue">BooleanValue</a>" : <i>Boolean</i>,
    "<a href="#dayofweekvalue" title="DayOfWeekValue">DayOfWeekValue</a>" : <i>String</i>,
    "<a href="#floatvalue" title="FloatValue">FloatValue</a>" : <i>Double</i>,
    "<a href="#integervalue" title="IntegerValue">IntegerValue</a>" : <i>Double</i>,
    "<a href="#stringvalue" title="StringValue">StringValue</a>" : <i>String</i>,
    "<a href="#timestampvalue" title="TimestampValue">TimestampValue</a>" : <i>String</i>,
    "<a href="#datevalue" title="DateValue">DateValue</a>" : <i>[ <a href="datevaluedefinition.md">DateValueDefinition</a>, ... ]</i>,
    "<a href="#timevalue" title="TimeValue">TimeValue</a>" : <i>[ <a href="timevaluedefinition.md">TimeValueDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#booleanvalue" title="BooleanValue">BooleanValue</a>: <i>Boolean</i>
<a href="#dayofweekvalue" title="DayOfWeekValue">DayOfWeekValue</a>: <i>String</i>
<a href="#floatvalue" title="FloatValue">FloatValue</a>: <i>Double</i>
<a href="#integervalue" title="IntegerValue">IntegerValue</a>: <i>Double</i>
<a href="#stringvalue" title="StringValue">StringValue</a>: <i>String</i>
<a href="#timestampvalue" title="TimestampValue">TimestampValue</a>: <i>String</i>
<a href="#datevalue" title="DateValue">DateValue</a>: <i>
      - <a href="datevaluedefinition.md">DateValueDefinition</a></i>
<a href="#timevalue" title="TimeValue">TimeValue</a>: <i>
      - <a href="timevaluedefinition.md">TimeValueDefinition</a></i>
</pre>

## Properties

#### BooleanValue

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DayOfWeekValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegerValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimestampValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateValue

_Required_: No

_Type_: List of <a href="datevaluedefinition.md">DateValueDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeValue

_Required_: No

_Type_: List of <a href="timevaluedefinition.md">TimeValueDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

