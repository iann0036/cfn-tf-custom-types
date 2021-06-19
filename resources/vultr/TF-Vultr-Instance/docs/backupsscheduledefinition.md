# TF::Vultr::Instance BackupsScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dom" title="Dom">Dom</a>" : <i>Double</i>,
    "<a href="#dow" title="Dow">Dow</a>" : <i>Double</i>,
    "<a href="#hour" title="Hour">Hour</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dom" title="Dom">Dom</a>: <i>Double</i>
<a href="#dow" title="Dow">Dow</a>: <i>Double</i>
<a href="#hour" title="Hour">Hour</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Dom

Day of month to run. Use values between 1 and 28.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dow

Day of week to run. `1 = Sunday`, `2 = Monday`, `3 = Tuesday`, `4 = Wednesday`, `5 = Thursday`, `6 = Friday`, `7 = Saturday`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hour

Hour of day to run in UTC.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of backup schedule Possible values are `daily`, `weekly`, `monthly`, `daily_alt_event`, or `daily_alt_odd`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

