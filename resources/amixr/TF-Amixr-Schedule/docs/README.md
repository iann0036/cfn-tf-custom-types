# TF::Amixr::Schedule

Manage a [schedule](https://api-docs.amixr.io/#schedules).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Amixr::Schedule",
    "Properties" : {
        "<a href="#icalurl" title="IcalUrl">IcalUrl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
        "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slackdefinition.md">SlackDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Amixr::Schedule
Properties:
    <a href="#icalurl" title="IcalUrl">IcalUrl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
    <a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slackdefinition.md">SlackDefinition</a></i>
</pre>

## Properties

#### IcalUrl

The URL of the external calendar iCal file
* `slack` - (Optional) Dictionary with slack-specific settings for a schedule. Includes:
- `channel_id` - Slack channel id. Reminder about schedule shifts will be directed to this channel in Slack.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The schedule's name
* `time_zone` - (Optional) The schedule's time zone. More information about [time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
* `ical_url` - (Optional) The URL of the external calendar iCal file
* `slack` - (Optional) Dictionary with slack-specific settings for a schedule. Includes:
- `channel_id` - Slack channel id. Reminder about schedule shifts will be directed to this channel in Slack.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

The schedule's time zone. More information about [time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
* `ical_url` - (Optional) The URL of the external calendar iCal file
* `slack` - (Optional) Dictionary with slack-specific settings for a schedule. Includes:
- `channel_id` - Slack channel id. Reminder about schedule shifts will be directed to this channel in Slack.

_Required_: No

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

