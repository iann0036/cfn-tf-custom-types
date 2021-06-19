# TF::Amixr::Route

[Routes](https://api-docs.amixr.io/#routes) allow to direct different alerts to different messenger channels and Escalation Policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Amixr::Route",
    "Properties" : {
        "<a href="#integrationid" title="IntegrationId">IntegrationId</a>" : <i>String</i>,
        "<a href="#position" title="Position">Position</a>" : <i>Double</i>,
        "<a href="#routingregex" title="RoutingRegex">RoutingRegex</a>" : <i>String</i>,
        "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slackdefinition.md">SlackDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Amixr::Route
Properties:
    <a href="#integrationid" title="IntegrationId">IntegrationId</a>: <i>String</i>
    <a href="#position" title="Position">Position</a>: <i>Double</i>
    <a href="#routingregex" title="RoutingRegex">RoutingRegex</a>: <i>String</i>
    <a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slackdefinition.md">SlackDefinition</a></i>
</pre>

## Properties

#### IntegrationId

The ID of the integration.
* `routing_regex` - (Required) Python Regex query. Amixr choose the route for an alert in case there is a match inside the whole alert payload.
* `position` - (Required) The position of the route (starts from 0)
* `slack` - (Optional) Dictionary with slack-specific settings for a route. Includes:
- `channel_id` - Slack channel id. Alerts will be directed to this channel in Slack.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

The position of the route (starts from 0)
* `slack` - (Optional) Dictionary with slack-specific settings for a route. Includes:
- `channel_id` - Slack channel id. Alerts will be directed to this channel in Slack.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingRegex

Python Regex query. Amixr choose the route for an alert in case there is a match inside the whole alert payload.
* `position` - (Required) The position of the route (starts from 0)
* `slack` - (Optional) Dictionary with slack-specific settings for a route. Includes:
- `channel_id` - Slack channel id. Alerts will be directed to this channel in Slack.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slack

_Required_: No

_Type_: List of <a href="slackdefinition.md">SlackDefinition</a>

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

