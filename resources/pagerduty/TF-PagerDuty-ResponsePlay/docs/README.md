# TF::PagerDuty::ResponsePlay

A [response play](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/get_services) allows you to create packages of Incident Actions that can be applied during an Incident's life cycle.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PagerDuty::ResponsePlay",
    "Properties" : {
        "<a href="#conferencenumber" title="ConferenceNumber">ConferenceNumber</a>" : <i>String</i>,
        "<a href="#conferenceurl" title="ConferenceUrl">ConferenceUrl</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#from" title="From">From</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#respondersmessage" title="RespondersMessage">RespondersMessage</a>" : <i>String</i>,
        "<a href="#runnability" title="Runnability">Runnability</a>" : <i>String</i>,
        "<a href="#subscribersmessage" title="SubscribersMessage">SubscribersMessage</a>" : <i>String</i>,
        "<a href="#team" title="Team">Team</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#responder" title="Responder">Responder</a>" : <i>[ <a href="responderdefinition.md">ResponderDefinition</a>, ... ]</i>,
        "<a href="#subscriber" title="Subscriber">Subscriber</a>" : <i>[ <a href="subscriberdefinition.md">SubscriberDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PagerDuty::ResponsePlay
Properties:
    <a href="#conferencenumber" title="ConferenceNumber">ConferenceNumber</a>: <i>String</i>
    <a href="#conferenceurl" title="ConferenceUrl">ConferenceUrl</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#from" title="From">From</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#respondersmessage" title="RespondersMessage">RespondersMessage</a>: <i>String</i>
    <a href="#runnability" title="Runnability">Runnability</a>: <i>String</i>
    <a href="#subscribersmessage" title="SubscribersMessage">SubscribersMessage</a>: <i>String</i>
    <a href="#team" title="Team">Team</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#responder" title="Responder">Responder</a>: <i>
      - <a href="responderdefinition.md">ResponderDefinition</a></i>
    <a href="#subscriber" title="Subscriber">Subscriber</a>: <i>
      - <a href="subscriberdefinition.md">SubscriberDefinition</a></i>
</pre>

## Properties

#### ConferenceNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConferenceUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description of the response play.
If not set, a placeholder of "Managed by Terraform" will be set.
* `type` - (Optional)  A string that determines the schema of the object. If not set, the default value is "response_play".
* `team` - (Optional) The ID of the team associated with the response play.
* `subscriber` - (Required) A user and/or team to be added as a subscriber to any incident on which this response play is run. There can be multiple subscribers defined on a single response play.
* `subscribers_message` - (Optional) The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
* `responder` - (Required) A user and/or escalation policy to be requested as a responder to any incident on which this response play is run. There can be multiple responders defined on a single response play.
* `responders_message` - (Optional) The message body of the notification that will be sent to this response play's set of responders. If empty, a default response request notification will be sent.
* `runnability` - (Optional) String representing how this response play is allowed to be run. Valid options are:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### From

The email of the user attributed to the request. Needs to be a valid email address of a user in the PagerDuty account.
* `description` - (Optional) A human-friendly description of the response play.
If not set, a placeholder of "Managed by Terraform" will be set.
* `type` - (Optional)  A string that determines the schema of the object. If not set, the default value is "response_play".
* `team` - (Optional) The ID of the team associated with the response play.
* `subscriber` - (Required) A user and/or team to be added as a subscriber to any incident on which this response play is run. There can be multiple subscribers defined on a single response play.
* `subscribers_message` - (Optional) The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
* `responder` - (Required) A user and/or escalation policy to be requested as a responder to any incident on which this response play is run. There can be multiple responders defined on a single response play.
* `responders_message` - (Optional) The message body of the notification that will be sent to this response play's set of responders. If empty, a default response request notification will be sent.
* `runnability` - (Optional) String representing how this response play is allowed to be run. Valid options are:.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the response play.
* `from` - (Required) The email of the user attributed to the request. Needs to be a valid email address of a user in the PagerDuty account.
* `description` - (Optional) A human-friendly description of the response play.
If not set, a placeholder of "Managed by Terraform" will be set.
* `type` - (Optional)  A string that determines the schema of the object. If not set, the default value is "response_play".
* `team` - (Optional) The ID of the team associated with the response play.
* `subscriber` - (Required) A user and/or team to be added as a subscriber to any incident on which this response play is run. There can be multiple subscribers defined on a single response play.
* `subscribers_message` - (Optional) The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
* `responder` - (Required) A user and/or escalation policy to be requested as a responder to any incident on which this response play is run. There can be multiple responders defined on a single response play.
* `responders_message` - (Optional) The message body of the notification that will be sent to this response play's set of responders. If empty, a default response request notification will be sent.
* `runnability` - (Optional) String representing how this response play is allowed to be run. Valid options are:.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RespondersMessage

The message body of the notification that will be sent to this response play's set of responders. If empty, a default response request notification will be sent.
* `runnability` - (Optional) String representing how this response play is allowed to be run. Valid options are:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runnability

String representing how this response play is allowed to be run. Valid options are:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscribersMessage

The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
* `responder` - (Required) A user and/or escalation policy to be requested as a responder to any incident on which this response play is run. There can be multiple responders defined on a single response play.
* `responders_message` - (Optional) The message body of the notification that will be sent to this response play's set of responders. If empty, a default response request notification will be sent.
* `runnability` - (Optional) String representing how this response play is allowed to be run. Valid options are:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Team

The ID of the team associated with the response play.
* `subscriber` - (Required) A user and/or team to be added as a subscriber to any incident on which this response play is run. There can be multiple subscribers defined on a single response play.
* `subscribers_message` - (Optional) The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
* `responder` - (Required) A user and/or escalation policy to be requested as a responder to any incident on which this response play is run. There can be multiple responders defined on a single response play.
* `responders_message` - (Optional) The message body of the notification that will be sent to this response play's set of responders. If empty, a default response request notification will be sent.
* `runnability` - (Optional) String representing how this response play is allowed to be run. Valid options are:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

A string that determines the schema of the object. If not set, the default value is "response_play".
* `team` - (Optional) The ID of the team associated with the response play.
* `subscriber` - (Required) A user and/or team to be added as a subscriber to any incident on which this response play is run. There can be multiple subscribers defined on a single response play.
* `subscribers_message` - (Optional) The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent.
* `responder` - (Required) A user and/or escalation policy to be requested as a responder to any incident on which this response play is run. There can be multiple responders defined on a single response play.
* `responders_message` - (Optional) The message body of the notification that will be sent to this response play's set of responders. If empty, a default response request notification will be sent.
* `runnability` - (Optional) String representing how this response play is allowed to be run. Valid options are:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Responder

_Required_: No

_Type_: List of <a href="responderdefinition.md">ResponderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subscriber

_Required_: No

_Type_: List of <a href="subscriberdefinition.md">SubscriberDefinition</a>

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

