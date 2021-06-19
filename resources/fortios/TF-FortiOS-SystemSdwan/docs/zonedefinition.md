# TF::FortiOS::SystemSdwan ZoneDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#serviceslatiebreak" title="ServiceSlaTieBreak">ServiceSlaTieBreak</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#serviceslatiebreak" title="ServiceSlaTieBreak">ServiceSlaTieBreak</a>: <i>String</i>
</pre>

## Properties

#### Name

Zone name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceSlaTieBreak

Method of selecting member if more than one meets the SLA. Valid values: `cfg-order`, `fib-best-match`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

