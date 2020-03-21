# Terraform::Google::PubsubSubscription

A named resource representing the stream of messages from a single,
specific topic, to be delivered to the subscribing application.


To get more information about Subscription, see:

* [API documentation](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions)
* How-to Guides
    * [Managing Subscriptions](https://cloud.google.com/pubsub/docs/admin#managing_subscriptions)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::PubsubSubscription",
    "Properties" : {
        "<a href="#ackdeadlineseconds" title="AckDeadlineSeconds">AckDeadlineSeconds</a>" : <i>Double</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#messageretentionduration" title="MessageRetentionDuration">MessageRetentionDuration</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#retainackedmessages" title="RetainAckedMessages">RetainAckedMessages</a>" : <i>Boolean</i>,
        "<a href="#topic" title="Topic">Topic</a>" : <i>String</i>,
        "<a href="#expirationpolicy" title="ExpirationPolicy">ExpirationPolicy</a>" : <i>[ <a href="expirationpolicy.md">ExpirationPolicy</a>, ... ]</i>,
        "<a href="#pushconfig" title="PushConfig">PushConfig</a>" : <i>[ <a href="pushconfig.md">PushConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#oidctoken" title="OidcToken">OidcToken</a>" : <i>[ <a href="oidctoken.md">OidcToken</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::PubsubSubscription
Properties:
    <a href="#ackdeadlineseconds" title="AckDeadlineSeconds">AckDeadlineSeconds</a>: <i>Double</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#messageretentionduration" title="MessageRetentionDuration">MessageRetentionDuration</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#retainackedmessages" title="RetainAckedMessages">RetainAckedMessages</a>: <i>Boolean</i>
    <a href="#topic" title="Topic">Topic</a>: <i>String</i>
    <a href="#expirationpolicy" title="ExpirationPolicy">ExpirationPolicy</a>: <i>
      - <a href="expirationpolicy.md">ExpirationPolicy</a></i>
    <a href="#pushconfig" title="PushConfig">PushConfig</a>: <i>
      - <a href="pushconfig.md">PushConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#oidctoken" title="OidcToken">OidcToken</a>: <i>
      - <a href="oidctoken.md">OidcToken</a></i>
</pre>

## Properties

#### AckDeadlineSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

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

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

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

#### ExpirationPolicy

_Required_: No

_Type_: List of <a href="expirationpolicy.md">ExpirationPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushConfig

_Required_: No

_Type_: List of <a href="pushconfig.md">PushConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcToken

_Required_: No

_Type_: List of <a href="oidctoken.md">OidcToken</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Path

Returns the <code>Path</code> value.

