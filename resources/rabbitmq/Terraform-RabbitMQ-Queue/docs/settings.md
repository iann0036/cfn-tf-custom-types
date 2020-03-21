# Terraform::RabbitMQ::Queue Settings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#arguments" title="Arguments">Arguments</a>" : <i>[ <a href="settings-arguments.md">Arguments</a>, ... ]</i>,
    "<a href="#argumentsjson" title="ArgumentsJson">ArgumentsJson</a>" : <i>String</i>,
    "<a href="#autodelete" title="AutoDelete">AutoDelete</a>" : <i>Boolean</i>,
    "<a href="#durable" title="Durable">Durable</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#arguments" title="Arguments">Arguments</a>: <i>
      - <a href="settings-arguments.md">Arguments</a></i>
<a href="#argumentsjson" title="ArgumentsJson">ArgumentsJson</a>: <i>String</i>
<a href="#autodelete" title="AutoDelete">AutoDelete</a>: <i>Boolean</i>
<a href="#durable" title="Durable">Durable</a>: <i>Boolean</i>
</pre>

## Properties

#### Arguments

Additional key/value settings for the queue.
All values will be sent to RabbitMQ as a string. If you require non-string
values, use `arguments_json`.

_Required_: No

_Type_: List of <a href="settings-arguments.md">Arguments</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArgumentsJson

A nested JSON string which contains additional
settings for the queue. This is useful for when the arguments contain
non-string values.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoDelete

Whether the queue will self-delete when all
consumers have unsubscribed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Durable

Whether the queue survives server restarts.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

