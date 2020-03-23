# Terraform::AWS::CodebuildProject CloudwatchLogs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#streamname" title="StreamName">StreamName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#streamname" title="StreamName">StreamName</a>: <i>String</i>
</pre>

## Properties

#### GroupName

The group name of the logs in CloudWatch Logs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Current status of logs in CloudWatch Logs for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `ENABLED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamName

The stream name of the logs in CloudWatch Logs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

