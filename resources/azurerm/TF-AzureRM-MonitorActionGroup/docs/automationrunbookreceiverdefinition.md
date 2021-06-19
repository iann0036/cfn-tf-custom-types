# TF::AzureRM::MonitorActionGroup AutomationRunbookReceiverDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automationaccountid" title="AutomationAccountId">AutomationAccountId</a>" : <i>String</i>,
    "<a href="#isglobalrunbook" title="IsGlobalRunbook">IsGlobalRunbook</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#runbookname" title="RunbookName">RunbookName</a>" : <i>String</i>,
    "<a href="#serviceuri" title="ServiceUri">ServiceUri</a>" : <i>String</i>,
    "<a href="#usecommonalertschema" title="UseCommonAlertSchema">UseCommonAlertSchema</a>" : <i>Boolean</i>,
    "<a href="#webhookresourceid" title="WebhookResourceId">WebhookResourceId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#automationaccountid" title="AutomationAccountId">AutomationAccountId</a>: <i>String</i>
<a href="#isglobalrunbook" title="IsGlobalRunbook">IsGlobalRunbook</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#runbookname" title="RunbookName">RunbookName</a>: <i>String</i>
<a href="#serviceuri" title="ServiceUri">ServiceUri</a>: <i>String</i>
<a href="#usecommonalertschema" title="UseCommonAlertSchema">UseCommonAlertSchema</a>: <i>Boolean</i>
<a href="#webhookresourceid" title="WebhookResourceId">WebhookResourceId</a>: <i>String</i>
</pre>

## Properties

#### AutomationAccountId

The automation account ID which holds this runbook and authenticates to Azure resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsGlobalRunbook

Indicates whether this instance is global runbook.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the automation runbook receiver.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookName

The name for this runbook.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceUri

The URI where webhooks should be sent.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCommonAlertSchema

Enables or disables the common alert schema.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookResourceId

The resource id for webhook linked to this runbook.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

