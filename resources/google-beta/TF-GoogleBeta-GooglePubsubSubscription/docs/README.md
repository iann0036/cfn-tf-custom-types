# TF::GoogleBeta::GooglePubsubSubscription

CloudFormation equivalent of google_pubsub_subscription

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GooglePubsubSubscription",
    "Properties" : {
        "<a href="#ackdeadlineseconds" title="AckDeadlineSeconds">AckDeadlineSeconds</a>" : <i>Double</i>,
        "<a href="#enablemessageordering" title="EnableMessageOrdering">EnableMessageOrdering</a>" : <i>Boolean</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#messageretentionduration" title="MessageRetentionDuration">MessageRetentionDuration</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#retainackedmessages" title="RetainAckedMessages">RetainAckedMessages</a>" : <i>Boolean</i>,
        "<a href="#topic" title="Topic">Topic</a>" : <i>String</i>,
        "<a href="#deadletterpolicy" title="DeadLetterPolicy">DeadLetterPolicy</a>" : <i>[ <a href="deadletterpolicydefinition.md">DeadLetterPolicyDefinition</a>, ... ]</i>,
        "<a href="#expirationpolicy" title="ExpirationPolicy">ExpirationPolicy</a>" : <i>[ <a href="expirationpolicydefinition.md">ExpirationPolicyDefinition</a>, ... ]</i>,
        "<a href="#pushconfig" title="PushConfig">PushConfig</a>" : <i>[ <a href="pushconfigdefinition.md">PushConfigDefinition</a>, ... ]</i>,
        "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GooglePubsubSubscription
Properties:
    <a href="#ackdeadlineseconds" title="AckDeadlineSeconds">AckDeadlineSeconds</a>: <i>Double</i>
    <a href="#enablemessageordering" title="EnableMessageOrdering">EnableMessageOrdering</a>: <i>Boolean</i>
    <a href="#filter" title="Filter">Filter</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#messageretentionduration" title="MessageRetentionDuration">MessageRetentionDuration</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#retainackedmessages" title="RetainAckedMessages">RetainAckedMessages</a>: <i>Boolean</i>
    <a href="#topic" title="Topic">Topic</a>: <i>String</i>
    <a href="#deadletterpolicy" title="DeadLetterPolicy">DeadLetterPolicy</a>: <i>
      - <a href="deadletterpolicydefinition.md">DeadLetterPolicyDefinition</a></i>
    <a href="#expirationpolicy" title="ExpirationPolicy">ExpirationPolicy</a>: <i>
      - <a href="expirationpolicydefinition.md">ExpirationPolicyDefinition</a></i>
    <a href="#pushconfig" title="PushConfig">PushConfig</a>: <i>
      - <a href="pushconfigdefinition.md">PushConfigDefinition</a></i>
    <a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="retrypolicydefinition.md">RetryPolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AckDeadlineSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMessageOrdering

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageRetentionDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainAckedMessages

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topic

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadLetterPolicy

_Required_: No

_Type_: List of <a href="deadletterpolicydefinition.md">DeadLetterPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationPolicy

_Required_: No

_Type_: List of <a href="expirationpolicydefinition.md">ExpirationPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushConfig

_Required_: No

_Type_: List of <a href="pushconfigdefinition.md">PushConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Path

Returns the <code>Path</code> value.

