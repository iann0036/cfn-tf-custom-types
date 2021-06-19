# TF::Google::BigtableGcPolicy MaxAgeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#days" title="Days">Days</a>" : <i>Double</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#days" title="Days">Days</a>: <i>Double</i>
<a href="#duration" title="Duration">Duration</a>: <i>String</i>
</pre>

## Properties

#### Days

Number of days before applying GC policy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

Duration before applying GC policy (ex. "8h"). This is required when `days` isn't set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

