# Terraform::AzureRM::MonitorAutoscaleSetting FixedDate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#end" title="End">End</a>" : <i>String</i>,
    "<a href="#start" title="Start">Start</a>" : <i>String</i>,
    "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#end" title="End">End</a>: <i>String</i>
<a href="#start" title="Start">Start</a>: <i>String</i>
<a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
</pre>

## Properties

#### End

Specifies the end date for the profile, formatted as an RFC3339 date string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

Specifies the start date for the profile, formatted as an RFC3339 date string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

