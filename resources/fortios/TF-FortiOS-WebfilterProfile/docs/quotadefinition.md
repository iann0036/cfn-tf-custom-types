# TF::FortiOS::WebfilterProfile QuotaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#category" title="Category">Category</a>" : <i>String</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#overridereplacemsg" title="OverrideReplacemsg">OverrideReplacemsg</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#category" title="Category">Category</a>: <i>String</i>
<a href="#duration" title="Duration">Duration</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#overridereplacemsg" title="OverrideReplacemsg">OverrideReplacemsg</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#unit" title="Unit">Unit</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>Double</i>
</pre>

## Properties

#### Category

FortiGuard categories to apply quota to (category action must be set to monitor).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

Duration of quota.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideReplacemsg

Override replacement message.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Quota type. Valid values: `time`, `traffic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

Traffic quota unit of measurement. Valid values: `B`, `KB`, `MB`, `GB`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

Traffic quota value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

