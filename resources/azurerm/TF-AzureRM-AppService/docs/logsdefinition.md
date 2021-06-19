# TF::AzureRM::AppService LogsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#detailederrormessagesenabled" title="DetailedErrorMessagesEnabled">DetailedErrorMessagesEnabled</a>" : <i>Boolean</i>,
    "<a href="#failedrequesttracingenabled" title="FailedRequestTracingEnabled">FailedRequestTracingEnabled</a>" : <i>Boolean</i>,
    "<a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>" : <i>[ <a href="applicationlogsdefinition.md">ApplicationLogsDefinition</a>, ... ]</i>,
    "<a href="#httplogs" title="HttpLogs">HttpLogs</a>" : <i>[ <a href="httplogsdefinition.md">HttpLogsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#detailederrormessagesenabled" title="DetailedErrorMessagesEnabled">DetailedErrorMessagesEnabled</a>: <i>Boolean</i>
<a href="#failedrequesttracingenabled" title="FailedRequestTracingEnabled">FailedRequestTracingEnabled</a>: <i>Boolean</i>
<a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>: <i>
      - <a href="applicationlogsdefinition.md">ApplicationLogsDefinition</a></i>
<a href="#httplogs" title="HttpLogs">HttpLogs</a>: <i>
      - <a href="httplogsdefinition.md">HttpLogsDefinition</a></i>
</pre>

## Properties

#### DetailedErrorMessagesEnabled

Should `Detailed error messages` be enabled on this App Service? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedRequestTracingEnabled

Should `Failed request tracing` be enabled on this App Service? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationLogs

_Required_: No

_Type_: List of <a href="applicationlogsdefinition.md">ApplicationLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLogs

_Required_: No

_Type_: List of <a href="httplogsdefinition.md">HttpLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

