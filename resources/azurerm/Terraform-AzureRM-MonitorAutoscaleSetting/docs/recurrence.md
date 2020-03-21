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

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hours

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minutes

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

