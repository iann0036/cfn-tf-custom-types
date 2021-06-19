# TF::Dynatrace::Notification

CloudFormation equivalent of dynatrace_notification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::Notification",
    "Properties" : {
        "<a href="#ansibletower" title="AnsibleTower">AnsibleTower</a>" : <i>[ <a href="ansibletowerdefinition.md">AnsibleTowerDefinition</a>, ... ]</i>,
        "<a href="#config" title="Config">Config</a>" : <i>[ <a href="configdefinition.md">ConfigDefinition</a>, ... ]</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ <a href="emaildefinition.md">EmailDefinition</a>, ... ]</i>,
        "<a href="#hipchat" title="Hipchat">Hipchat</a>" : <i>[ <a href="hipchatdefinition.md">HipchatDefinition</a>, ... ]</i>,
        "<a href="#jira" title="Jira">Jira</a>" : <i>[ <a href="jiradefinition.md">JiraDefinition</a>, ... ]</i>,
        "<a href="#opsgenie" title="OpsGenie">OpsGenie</a>" : <i>[ <a href="opsgeniedefinition.md">OpsGenieDefinition</a>, ... ]</i>,
        "<a href="#pagerduty" title="PagerDuty">PagerDuty</a>" : <i>[ <a href="pagerdutydefinition.md">PagerDutyDefinition</a>, ... ]</i>,
        "<a href="#servicenow" title="ServiceNow">ServiceNow</a>" : <i>[ <a href="servicenowdefinition.md">ServiceNowDefinition</a>, ... ]</i>,
        "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slackdefinition.md">SlackDefinition</a>, ... ]</i>,
        "<a href="#trello" title="Trello">Trello</a>" : <i>[ <a href="trellodefinition.md">TrelloDefinition</a>, ... ]</i>,
        "<a href="#victorops" title="VictorOps">VictorOps</a>" : <i>[ <a href="victoropsdefinition.md">VictorOpsDefinition</a>, ... ]</i>,
        "<a href="#webhook" title="WebHook">WebHook</a>" : <i>[ <a href="webhookdefinition.md">WebHookDefinition</a>, ... ]</i>,
        "<a href="#xmatters" title="Xmatters">Xmatters</a>" : <i>[ <a href="xmattersdefinition.md">XmattersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::Notification
Properties:
    <a href="#ansibletower" title="AnsibleTower">AnsibleTower</a>: <i>
      - <a href="ansibletowerdefinition.md">AnsibleTowerDefinition</a></i>
    <a href="#config" title="Config">Config</a>: <i>
      - <a href="configdefinition.md">ConfigDefinition</a></i>
    <a href="#email" title="Email">Email</a>: <i>
      - <a href="emaildefinition.md">EmailDefinition</a></i>
    <a href="#hipchat" title="Hipchat">Hipchat</a>: <i>
      - <a href="hipchatdefinition.md">HipchatDefinition</a></i>
    <a href="#jira" title="Jira">Jira</a>: <i>
      - <a href="jiradefinition.md">JiraDefinition</a></i>
    <a href="#opsgenie" title="OpsGenie">OpsGenie</a>: <i>
      - <a href="opsgeniedefinition.md">OpsGenieDefinition</a></i>
    <a href="#pagerduty" title="PagerDuty">PagerDuty</a>: <i>
      - <a href="pagerdutydefinition.md">PagerDutyDefinition</a></i>
    <a href="#servicenow" title="ServiceNow">ServiceNow</a>: <i>
      - <a href="servicenowdefinition.md">ServiceNowDefinition</a></i>
    <a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slackdefinition.md">SlackDefinition</a></i>
    <a href="#trello" title="Trello">Trello</a>: <i>
      - <a href="trellodefinition.md">TrelloDefinition</a></i>
    <a href="#victorops" title="VictorOps">VictorOps</a>: <i>
      - <a href="victoropsdefinition.md">VictorOpsDefinition</a></i>
    <a href="#webhook" title="WebHook">WebHook</a>: <i>
      - <a href="webhookdefinition.md">WebHookDefinition</a></i>
    <a href="#xmatters" title="Xmatters">Xmatters</a>: <i>
      - <a href="xmattersdefinition.md">XmattersDefinition</a></i>
</pre>

## Properties

#### AnsibleTower

_Required_: No

_Type_: List of <a href="ansibletowerdefinition.md">AnsibleTowerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: No

_Type_: List of <a href="configdefinition.md">ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of <a href="emaildefinition.md">EmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hipchat

_Required_: No

_Type_: List of <a href="hipchatdefinition.md">HipchatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jira

_Required_: No

_Type_: List of <a href="jiradefinition.md">JiraDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpsGenie

_Required_: No

_Type_: List of <a href="opsgeniedefinition.md">OpsGenieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PagerDuty

_Required_: No

_Type_: List of <a href="pagerdutydefinition.md">PagerDutyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceNow

_Required_: No

_Type_: List of <a href="servicenowdefinition.md">ServiceNowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slack

_Required_: No

_Type_: List of <a href="slackdefinition.md">SlackDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trello

_Required_: No

_Type_: List of <a href="trellodefinition.md">TrelloDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VictorOps

_Required_: No

_Type_: List of <a href="victoropsdefinition.md">VictorOpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebHook

_Required_: No

_Type_: List of <a href="webhookdefinition.md">WebHookDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Xmatters

_Required_: No

_Type_: List of <a href="xmattersdefinition.md">XmattersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

