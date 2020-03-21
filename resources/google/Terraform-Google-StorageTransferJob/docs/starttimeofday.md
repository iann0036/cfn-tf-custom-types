# Terraform::Google::StorageTransferJob StartTimeOfDay

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hours" title="Hours">Hours</a>" : <i>Double</i>,
    "<a href="#minutes" title="Minutes">Minutes</a>" : <i>Double</i>,
    "<a href="#nanos" title="Nanos">Nanos</a>" : <i>Double</i>,
    "<a href="#seconds" title="Seconds">Seconds</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#hours" title="Hours">Hours</a>: <i>Double</i>
<a href="#minutes" title="Minutes">Minutes</a>: <i>Double</i>
<a href="#nanos" title="Nanos">Nanos</a>: <i>Double</i>
<a href="#seconds" title="Seconds">Seconds</a>: <i>Double</i>
</pre>

## Properties

#### Hours

Hours of day in 24 hour format. Should be from 0 to 23.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minutes

Minutes of hour of day. Must be from 0 to 59.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nanos

Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Seconds

Seconds of minutes of the time. Must normally be from 0 to 59.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

