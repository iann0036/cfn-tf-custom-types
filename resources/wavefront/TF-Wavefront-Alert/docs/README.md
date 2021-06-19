# TF::Wavefront::Alert

CloudFormation equivalent of wavefront_alert

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Wavefront::Alert",
    "Properties" : {
        "<a href="#additionalinformation" title="AdditionalInformation">AdditionalInformation</a>" : <i>String</i>,
        "<a href="#alerttype" title="AlertType">AlertType</a>" : <i>String</i>,
        "<a href="#canmodify" title="CanModify">CanModify</a>" : <i>[ String, ... ]</i>,
        "<a href="#canview" title="CanView">CanView</a>" : <i>[ String, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditionsdefinition.md">ConditionsDefinition</a>, ... ]</i>,
        "<a href="#displayexpression" title="DisplayExpression">DisplayExpression</a>" : <i>String</i>,
        "<a href="#minutes" title="Minutes">Minutes</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationresendfrequencyminutes" title="NotificationResendFrequencyMinutes">NotificationResendFrequencyMinutes</a>" : <i>Double</i>,
        "<a href="#resolveafterminutes" title="ResolveAfterMinutes">ResolveAfterMinutes</a>" : <i>Double</i>,
        "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>String</i>,
        "<a href="#thresholdtargets" title="ThresholdTargets">ThresholdTargets</a>" : <i>[ <a href="thresholdtargetsdefinition.md">ThresholdTargetsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Wavefront::Alert
Properties:
    <a href="#additionalinformation" title="AdditionalInformation">AdditionalInformation</a>: <i>String</i>
    <a href="#alerttype" title="AlertType">AlertType</a>: <i>String</i>
    <a href="#canmodify" title="CanModify">CanModify</a>: <i>
      - String</i>
    <a href="#canview" title="CanView">CanView</a>: <i>
      - String</i>
    <a href="#condition" title="Condition">Condition</a>: <i>String</i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditionsdefinition.md">ConditionsDefinition</a></i>
    <a href="#displayexpression" title="DisplayExpression">DisplayExpression</a>: <i>String</i>
    <a href="#minutes" title="Minutes">Minutes</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationresendfrequencyminutes" title="NotificationResendFrequencyMinutes">NotificationResendFrequencyMinutes</a>: <i>Double</i>
    <a href="#resolveafterminutes" title="ResolveAfterMinutes">ResolveAfterMinutes</a>: <i>Double</i>
    <a href="#severity" title="Severity">Severity</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#target" title="Target">Target</a>: <i>String</i>
    <a href="#thresholdtargets" title="ThresholdTargets">ThresholdTargets</a>: <i>
      - <a href="thresholdtargetsdefinition.md">ThresholdTargetsDefinition</a></i>
</pre>

## Properties

#### AdditionalInformation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanModify

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanView

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditionsdefinition.md">ConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayExpression

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minutes

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationResendFrequencyMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveAfterMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdTargets

_Required_: No

_Type_: List of <a href="thresholdtargetsdefinition.md">ThresholdTargetsDefinition</a>

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

