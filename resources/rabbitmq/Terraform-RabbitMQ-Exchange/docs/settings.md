# Terraform::RabbitMQ::Exchange Settings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#arguments" title="Arguments">Arguments</a>" : <i>[ <a href="settings-arguments.md">Arguments</a>, ... ]</i>,
    "<a href="#autodelete" title="AutoDelete">AutoDelete</a>" : <i>Boolean</i>,
    "<a href="#durable" title="Durable">Durable</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#arguments" title="Arguments">Arguments</a>: <i>
      - <a href="settings-arguments.md">Arguments</a></i>
<a href="#autodelete" title="AutoDelete">AutoDelete</a>: <i>Boolean</i>
<a href="#durable" title="Durable">Durable</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Arguments

Additional key/value settings for the exchange.

_Required_: No

_Type_: List of <a href="settings-arguments.md">Arguments</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoDelete

Whether the exchange will self-delete when all
queues have finished using it.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Durable

Whether the exchange survives server restarts.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of exchange.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

