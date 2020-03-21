# Terraform::DigitalOcean::DatabaseCluster MaintenanceWindow

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#day" title="Day">Day</a>" : <i>String</i>,
    "<a href="#hour" title="Hour">Hour</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#day" title="Day">Day</a>: <i>String</i>
<a href="#hour" title="Hour">Hour</a>: <i>String</i>
</pre>

## Properties

#### Day

The day of the week on which to apply maintenance updates.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hour

The hour in UTC at which maintenance updates will be applied in 24 hour format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

