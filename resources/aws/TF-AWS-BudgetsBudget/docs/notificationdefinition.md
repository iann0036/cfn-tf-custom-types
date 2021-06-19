# TF::AWS::BudgetsBudget NotificationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>" : <i>String</i>,
    "<a href="#notificationtype" title="NotificationType">NotificationType</a>" : <i>String</i>,
    "<a href="#subscriberemailaddresses" title="SubscriberEmailAddresses">SubscriberEmailAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#subscribersnstopicarns" title="SubscriberSnsTopicArns">SubscriberSnsTopicArns</a>" : <i>[ String, ... ]</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
    "<a href="#thresholdtype" title="ThresholdType">ThresholdType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>: <i>String</i>
<a href="#notificationtype" title="NotificationType">NotificationType</a>: <i>String</i>
<a href="#subscriberemailaddresses" title="SubscriberEmailAddresses">SubscriberEmailAddresses</a>: <i>
      - String</i>
<a href="#subscribersnstopicarns" title="SubscriberSnsTopicArns">SubscriberSnsTopicArns</a>: <i>
      - String</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
<a href="#thresholdtype" title="ThresholdType">ThresholdType</a>: <i>String</i>
</pre>

## Properties

#### ComparisonOperator

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriberEmailAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriberSnsTopicArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

