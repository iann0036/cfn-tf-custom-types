# Terraform::NS1::Notifylist Notifications

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#config" title="Config">Config</a>" : <i>[ <a href="notifications-config.md">Config</a>, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#config" title="Config">Config</a>: <i>
      - <a href="notifications-config.md">Config</a></i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Config

Configuration details for the given notifier type.

_Required_: Yes

_Type_: List of <a href="notifications-config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of notifier. Available notifiers are indicated in /notifytypes endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

