# Terraform::OpsGenie::NotificationPolicy DeDuplicationAction Duration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#timeamount" title="TimeAmount">TimeAmount</a>" : <i>Double</i>,
    "<a href="#timeunit" title="TimeUnit">TimeUnit</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#timeamount" title="TimeAmount">TimeAmount</a>: <i>Double</i>
<a href="#timeunit" title="TimeUnit">TimeUnit</a>: <i>String</i>
</pre>

## Properties

#### TimeAmount

A amount of time in `time_units`. This is a integer attribute.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUnit

Valid time units are: "minutes", "hours", "days". Default: minutes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

