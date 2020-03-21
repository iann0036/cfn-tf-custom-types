# Terraform::Google::CloudiotRegistry EventNotificationConfigs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#pubsubtopicname" title="PubsubTopicName">PubsubTopicName</a>" : <i>String</i>,
    "<a href="#subfoldermatches" title="SubfolderMatches">SubfolderMatches</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#pubsubtopicname" title="PubsubTopicName">PubsubTopicName</a>: <i>String</i>
<a href="#subfoldermatches" title="SubfolderMatches">SubfolderMatches</a>: <i>String</i>
</pre>

## Properties

#### PubsubTopicName

PubSub topic name to publish device events.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubfolderMatches

If the subfolder name matches this string
exactly, this configuration will be used. The string must not include the
leading '/' character. If empty, all strings are matched. Empty value can
only be used for the last `event_notification_configs` item.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

