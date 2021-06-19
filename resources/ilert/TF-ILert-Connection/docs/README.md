# TF::ILert::Connection

A [connection](https://docs.ilert.com/getting-started/intro#connectors-and-connections-outbond-integrations) is created at the alert source level and uses its [connector](connector.html) to perform a concrete action.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ILert::Connection",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#triggermode" title="TriggerMode">TriggerMode</a>" : <i>String</i>,
        "<a href="#triggertypes" title="TriggerTypes">TriggerTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#alertsource" title="AlertSource">AlertSource</a>" : <i>[ <a href="alertsourcedefinition.md">AlertSourceDefinition</a>, ... ]</i>,
        "<a href="#autotask" title="Autotask">Autotask</a>" : <i>[ <a href="autotaskdefinition.md">AutotaskDefinition</a>, ... ]</i>,
        "<a href="#awslambda" title="AwsLambda">AwsLambda</a>" : <i>[ <a href="awslambdadefinition.md">AwsLambdaDefinition</a>, ... ]</i>,
        "<a href="#azurefaas" title="AzureFaas">AzureFaas</a>" : <i>[ <a href="azurefaasdefinition.md">AzureFaasDefinition</a>, ... ]</i>,
        "<a href="#connector" title="Connector">Connector</a>" : <i>[ <a href="connectordefinition.md">ConnectorDefinition</a>, ... ]</i>,
        "<a href="#datadog" title="Datadog">Datadog</a>" : <i>[ <a href="datadogdefinition.md">DatadogDefinition</a>, ... ]</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ <a href="emaildefinition.md">EmailDefinition</a>, ... ]</i>,
        "<a href="#github" title="Github">Github</a>" : <i>[ <a href="githubdefinition.md">GithubDefinition</a>, ... ]</i>,
        "<a href="#googlefaas" title="GoogleFaas">GoogleFaas</a>" : <i>[ <a href="googlefaasdefinition.md">GoogleFaasDefinition</a>, ... ]</i>,
        "<a href="#jira" title="Jira">Jira</a>" : <i>[ <a href="jiradefinition.md">JiraDefinition</a>, ... ]</i>,
        "<a href="#servicenow" title="Servicenow">Servicenow</a>" : <i>[ <a href="servicenowdefinition.md">ServicenowDefinition</a>, ... ]</i>,
        "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slackdefinition.md">SlackDefinition</a>, ... ]</i>,
        "<a href="#statuspageio" title="StatusPageIo">StatusPageIo</a>" : <i>[ <a href="statuspageiodefinition.md">StatusPageIoDefinition</a>, ... ]</i>,
        "<a href="#sysdig" title="Sysdig">Sysdig</a>" : <i>[ <a href="sysdigdefinition.md">SysdigDefinition</a>, ... ]</i>,
        "<a href="#topdesk" title="Topdesk">Topdesk</a>" : <i>[ <a href="topdeskdefinition.md">TopdeskDefinition</a>, ... ]</i>,
        "<a href="#webhook" title="Webhook">Webhook</a>" : <i>[ <a href="webhookdefinition.md">WebhookDefinition</a>, ... ]</i>,
        "<a href="#zammad" title="Zammad">Zammad</a>" : <i>[ <a href="zammaddefinition.md">ZammadDefinition</a>, ... ]</i>,
        "<a href="#zapier" title="Zapier">Zapier</a>" : <i>[ <a href="zapierdefinition.md">ZapierDefinition</a>, ... ]</i>,
        "<a href="#zendesk" title="Zendesk">Zendesk</a>" : <i>[ <a href="zendeskdefinition.md">ZendeskDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ILert::Connection
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#triggermode" title="TriggerMode">TriggerMode</a>: <i>String</i>
    <a href="#triggertypes" title="TriggerTypes">TriggerTypes</a>: <i>
      - String</i>
    <a href="#alertsource" title="AlertSource">AlertSource</a>: <i>
      - <a href="alertsourcedefinition.md">AlertSourceDefinition</a></i>
    <a href="#autotask" title="Autotask">Autotask</a>: <i>
      - <a href="autotaskdefinition.md">AutotaskDefinition</a></i>
    <a href="#awslambda" title="AwsLambda">AwsLambda</a>: <i>
      - <a href="awslambdadefinition.md">AwsLambdaDefinition</a></i>
    <a href="#azurefaas" title="AzureFaas">AzureFaas</a>: <i>
      - <a href="azurefaasdefinition.md">AzureFaasDefinition</a></i>
    <a href="#connector" title="Connector">Connector</a>: <i>
      - <a href="connectordefinition.md">ConnectorDefinition</a></i>
    <a href="#datadog" title="Datadog">Datadog</a>: <i>
      - <a href="datadogdefinition.md">DatadogDefinition</a></i>
    <a href="#email" title="Email">Email</a>: <i>
      - <a href="emaildefinition.md">EmailDefinition</a></i>
    <a href="#github" title="Github">Github</a>: <i>
      - <a href="githubdefinition.md">GithubDefinition</a></i>
    <a href="#googlefaas" title="GoogleFaas">GoogleFaas</a>: <i>
      - <a href="googlefaasdefinition.md">GoogleFaasDefinition</a></i>
    <a href="#jira" title="Jira">Jira</a>: <i>
      - <a href="jiradefinition.md">JiraDefinition</a></i>
    <a href="#servicenow" title="Servicenow">Servicenow</a>: <i>
      - <a href="servicenowdefinition.md">ServicenowDefinition</a></i>
    <a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slackdefinition.md">SlackDefinition</a></i>
    <a href="#statuspageio" title="StatusPageIo">StatusPageIo</a>: <i>
      - <a href="statuspageiodefinition.md">StatusPageIoDefinition</a></i>
    <a href="#sysdig" title="Sysdig">Sysdig</a>: <i>
      - <a href="sysdigdefinition.md">SysdigDefinition</a></i>
    <a href="#topdesk" title="Topdesk">Topdesk</a>: <i>
      - <a href="topdeskdefinition.md">TopdeskDefinition</a></i>
    <a href="#webhook" title="Webhook">Webhook</a>: <i>
      - <a href="webhookdefinition.md">WebhookDefinition</a></i>
    <a href="#zammad" title="Zammad">Zammad</a>: <i>
      - <a href="zammaddefinition.md">ZammadDefinition</a></i>
    <a href="#zapier" title="Zapier">Zapier</a>: <i>
      - <a href="zapierdefinition.md">ZapierDefinition</a></i>
    <a href="#zendesk" title="Zendesk">Zendesk</a>: <i>
      - <a href="zendeskdefinition.md">ZendeskDefinition</a></i>
</pre>

## Properties

#### Name

The name of the connection.
- `alert_source` - (Required) A [alert_source](#alert-source-arguments) block.
- `connector` - (Required) A [connector](#connector-arguments) block.
- `trigger_mode` - (Optional) The trigger mode of the connection. Allowed values are `AUTOMATIC` or `MANUAL`. Default: `AUTOMATIC`.
- `trigger_types` - (Optional) A list of the trigger types. Allowed values are `incident-created`, `incident-assigned`, `incident-auto-escalated`, `incident-acknowledged`, `incident-raised`, `incident-comment-added`, `incident-resolved`.
- `datadog` - (Optional) A [datadog](#datadog-arguments) block.
- `jira` - (Optional) A [jira](#jira-arguments) block.
- `servicenow` - (Optional) A [servicenow](#servicenow-arguments) block.
- `slack` - (Optional) A [slack](#slack-arguments) block.
- `webhook` - (Optional) A [webhook](#webhook-arguments) block.
- `zendesk` - (Optional) A [zendesk](#zendesk-arguments) block.
- `github` - (Optional) A [github](#github-arguments) block.
- `aws_lambda` - (Optional) A [aws_lambda](#aws-lambda-arguments) block.
- `azure_faas` - (Optional) A [azure_faas](#azure-function-arguments) block.
- `google_faas` - (Optional) A [google_faas](#google-cloud-function-arguments) block.
- `email` - (Optional) A [email](#email-arguments) block.
- `sysdig` - (Optional) A [sysdig](#sysdig-arguments) block.
- `zapier` - (Optional) A [zapier](#zapier-arguments) block.
- `autotask` - (Optional) A [autotask](#autotask-arguments) block.
- `mattermost` - (Optional) A [mattermost](#mattermost-arguments) block.
- `zammad` - (Optional) A [zammad](#zammad-arguments) block.
- `status_page_io` - (Optional) A [status_page_io](#statuspage-arguments) block.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerMode

The trigger mode of the connection. Allowed values are `AUTOMATIC` or `MANUAL`. Default: `AUTOMATIC`.
- `trigger_types` - (Optional) A list of the trigger types. Allowed values are `incident-created`, `incident-assigned`, `incident-auto-escalated`, `incident-acknowledged`, `incident-raised`, `incident-comment-added`, `incident-resolved`.
- `datadog` - (Optional) A [datadog](#datadog-arguments) block.
- `jira` - (Optional) A [jira](#jira-arguments) block.
- `servicenow` - (Optional) A [servicenow](#servicenow-arguments) block.
- `slack` - (Optional) A [slack](#slack-arguments) block.
- `webhook` - (Optional) A [webhook](#webhook-arguments) block.
- `zendesk` - (Optional) A [zendesk](#zendesk-arguments) block.
- `github` - (Optional) A [github](#github-arguments) block.
- `aws_lambda` - (Optional) A [aws_lambda](#aws-lambda-arguments) block.
- `azure_faas` - (Optional) A [azure_faas](#azure-function-arguments) block.
- `google_faas` - (Optional) A [google_faas](#google-cloud-function-arguments) block.
- `email` - (Optional) A [email](#email-arguments) block.
- `sysdig` - (Optional) A [sysdig](#sysdig-arguments) block.
- `zapier` - (Optional) A [zapier](#zapier-arguments) block.
- `autotask` - (Optional) A [autotask](#autotask-arguments) block.
- `mattermost` - (Optional) A [mattermost](#mattermost-arguments) block.
- `zammad` - (Optional) A [zammad](#zammad-arguments) block.
- `status_page_io` - (Optional) A [status_page_io](#statuspage-arguments) block.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerTypes

A list of the trigger types. Allowed values are `incident-created`, `incident-assigned`, `incident-auto-escalated`, `incident-acknowledged`, `incident-raised`, `incident-comment-added`, `incident-resolved`.
- `datadog` - (Optional) A [datadog](#datadog-arguments) block.
- `jira` - (Optional) A [jira](#jira-arguments) block.
- `servicenow` - (Optional) A [servicenow](#servicenow-arguments) block.
- `slack` - (Optional) A [slack](#slack-arguments) block.
- `webhook` - (Optional) A [webhook](#webhook-arguments) block.
- `zendesk` - (Optional) A [zendesk](#zendesk-arguments) block.
- `github` - (Optional) A [github](#github-arguments) block.
- `aws_lambda` - (Optional) A [aws_lambda](#aws-lambda-arguments) block.
- `azure_faas` - (Optional) A [azure_faas](#azure-function-arguments) block.
- `google_faas` - (Optional) A [google_faas](#google-cloud-function-arguments) block.
- `email` - (Optional) A [email](#email-arguments) block.
- `sysdig` - (Optional) A [sysdig](#sysdig-arguments) block.
- `zapier` - (Optional) A [zapier](#zapier-arguments) block.
- `autotask` - (Optional) A [autotask](#autotask-arguments) block.
- `mattermost` - (Optional) A [mattermost](#mattermost-arguments) block.
- `zammad` - (Optional) A [zammad](#zammad-arguments) block.
- `status_page_io` - (Optional) A [status_page_io](#statuspage-arguments) block.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertSource

_Required_: No

_Type_: List of <a href="alertsourcedefinition.md">AlertSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autotask

_Required_: No

_Type_: List of <a href="autotaskdefinition.md">AutotaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsLambda

_Required_: No

_Type_: List of <a href="awslambdadefinition.md">AwsLambdaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFaas

_Required_: No

_Type_: List of <a href="azurefaasdefinition.md">AzureFaasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Connector

_Required_: No

_Type_: List of <a href="connectordefinition.md">ConnectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datadog

_Required_: No

_Type_: List of <a href="datadogdefinition.md">DatadogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of <a href="emaildefinition.md">EmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Github

_Required_: No

_Type_: List of <a href="githubdefinition.md">GithubDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleFaas

_Required_: No

_Type_: List of <a href="googlefaasdefinition.md">GoogleFaasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jira

_Required_: No

_Type_: List of <a href="jiradefinition.md">JiraDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servicenow

_Required_: No

_Type_: List of <a href="servicenowdefinition.md">ServicenowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slack

_Required_: No

_Type_: List of <a href="slackdefinition.md">SlackDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusPageIo

_Required_: No

_Type_: List of <a href="statuspageiodefinition.md">StatusPageIoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sysdig

_Required_: No

_Type_: List of <a href="sysdigdefinition.md">SysdigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topdesk

_Required_: No

_Type_: List of <a href="topdeskdefinition.md">TopdeskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

_Required_: No

_Type_: List of <a href="webhookdefinition.md">WebhookDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zammad

_Required_: No

_Type_: List of <a href="zammaddefinition.md">ZammadDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zapier

_Required_: No

_Type_: List of <a href="zapierdefinition.md">ZapierDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zendesk

_Required_: No

_Type_: List of <a href="zendeskdefinition.md">ZendeskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

