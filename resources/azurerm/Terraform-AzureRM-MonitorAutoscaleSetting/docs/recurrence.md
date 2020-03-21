# Terraform::AzureRM::MonitorAutoscaleSetting Recurrence

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#days" title="Days">Days</a>" : <i>[ String, ... ]</i>,
    "<a href="#hours" title="Hours">Hours</a>" : <i>[ Double, ... ]</i>,
    "<a href="#minutes" title="Minutes">Minutes</a>" : <i>[ Double, ... ]</i>,
    "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#days" title="Days">Days</a>: <i>
      - String</i>
<a href="#hours" title="Hours">Hours</a>: <i>
      - Double</i>
<a href="#minutes" title="Minutes">Minutes</a>: <i>
      - Double</i>
<a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
</pre>

## Properties

#### Days

A list of days that this profile takes effect on. Possible values include `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` and `Sunday`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hours

A list containing a single item, which specifies the Hour interval at which this recurrence should be triggered (in 24-hour time). Possible values are from `0` to `23`.

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minutes

A list containing a single item which specifies the Minute interval at which this recurrence should be triggered.

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

The Time Zone used for the `hours` field. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

