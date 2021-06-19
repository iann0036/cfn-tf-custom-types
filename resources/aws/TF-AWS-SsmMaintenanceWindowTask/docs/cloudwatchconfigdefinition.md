# TF::AWS::SsmMaintenanceWindowTask CloudwatchConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchloggroupname" title="CloudwatchLogGroupName">CloudwatchLogGroupName</a>" : <i>String</i>,
    "<a href="#cloudwatchoutputenabled" title="CloudwatchOutputEnabled">CloudwatchOutputEnabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchloggroupname" title="CloudwatchLogGroupName">CloudwatchLogGroupName</a>: <i>String</i>
<a href="#cloudwatchoutputenabled" title="CloudwatchOutputEnabled">CloudwatchOutputEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### CloudwatchLogGroupName

The name of the CloudWatch log group where you want to send command output. If you don't specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchOutputEnabled

Enables Systems Manager to send command output to CloudWatch Logs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

