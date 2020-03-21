# Terraform::AzureRM::AppService Logs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>" : <i>[ <a href="logs-applicationlogs.md">ApplicationLogs</a>, ... ]</i>,
    "<a href="#httplogs" title="HttpLogs">HttpLogs</a>" : <i>[ <a href="logs-httplogs.md">HttpLogs</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>: <i>
      - <a href="logs-applicationlogs.md">ApplicationLogs</a></i>
<a href="#httplogs" title="HttpLogs">HttpLogs</a>: <i>
      - <a href="logs-httplogs.md">HttpLogs</a></i>
</pre>

## Properties

#### ApplicationLogs

_Required_: No

_Type_: List of <a href="logs-applicationlogs.md">ApplicationLogs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLogs

_Required_: No

_Type_: List of <a href="logs-httplogs.md">HttpLogs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

