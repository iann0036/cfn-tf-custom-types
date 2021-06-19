# TF::SumoLogic::ScheduledView

Provides a [Sumologic Scheduled View][1].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SumoLogic::ScheduledView",
    "Properties" : {
        "<a href="#dataforwardingid" title="DataForwardingId">DataForwardingId</a>" : <i>String</i>,
        "<a href="#indexname" title="IndexName">IndexName</a>" : <i>String</i>,
        "<a href="#parsingmode" title="ParsingMode">ParsingMode</a>" : <i>String</i>,
        "<a href="#query" title="Query">Query</a>" : <i>String</i>,
        "<a href="#reduceretentionperiodimmediately" title="ReduceRetentionPeriodImmediately">ReduceRetentionPeriodImmediately</a>" : <i>Boolean</i>,
        "<a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>" : <i>Double</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SumoLogic::ScheduledView
Properties:
    <a href="#dataforwardingid" title="DataForwardingId">DataForwardingId</a>: <i>String</i>
    <a href="#indexname" title="IndexName">IndexName</a>: <i>String</i>
    <a href="#parsingmode" title="ParsingMode">ParsingMode</a>: <i>String</i>
    <a href="#query" title="Query">Query</a>: <i>String</i>
    <a href="#reduceretentionperiodimmediately" title="ReduceRetentionPeriodImmediately">ReduceRetentionPeriodImmediately</a>: <i>Boolean</i>
    <a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>: <i>Double</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
</pre>

## Properties

#### DataForwardingId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParsingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReduceRetentionPeriodImmediately

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

