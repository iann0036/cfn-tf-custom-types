# Terraform::AWS::Ec2ClientVpnEndpoint ConnectionLogOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchloggroup" title="CloudwatchLogGroup">CloudwatchLogGroup</a>" : <i>String</i>,
    "<a href="#cloudwatchlogstream" title="CloudwatchLogStream">CloudwatchLogStream</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchloggroup" title="CloudwatchLogGroup">CloudwatchLogGroup</a>: <i>String</i>
<a href="#cloudwatchlogstream" title="CloudwatchLogStream">CloudwatchLogStream</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
</pre>

## Properties

#### CloudwatchLogGroup

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLogStream

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

