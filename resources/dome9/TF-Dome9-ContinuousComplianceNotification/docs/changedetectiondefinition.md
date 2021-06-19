# TF::Dome9::ContinuousComplianceNotification ChangeDetectionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#awssecurityhubintegrationstate" title="AwsSecurityHubIntegrationState">AwsSecurityHubIntegrationState</a>" : <i>String</i>,
    "<a href="#emailperfindingsendingstate" title="EmailPerFindingSendingState">EmailPerFindingSendingState</a>" : <i>String</i>,
    "<a href="#emailsendingstate" title="EmailSendingState">EmailSendingState</a>" : <i>String</i>,
    "<a href="#externalticketcreatingstate" title="ExternalTicketCreatingState">ExternalTicketCreatingState</a>" : <i>String</i>,
    "<a href="#snssendingstate" title="SnsSendingState">SnsSendingState</a>" : <i>String</i>,
    "<a href="#webhookintegrationstate" title="WebhookIntegrationState">WebhookIntegrationState</a>" : <i>String</i>,
    "<a href="#awssecurityhubintegration" title="AwsSecurityHubIntegration">AwsSecurityHubIntegration</a>" : <i>[ <a href="awssecurityhubintegrationdefinition.md">AwsSecurityHubIntegrationDefinition</a>, ... ]</i>,
    "<a href="#emaildata" title="EmailData">EmailData</a>" : <i>[ <a href="emaildatadefinition.md">EmailDataDefinition</a>, ... ]</i>,
    "<a href="#emailperfindingdata" title="EmailPerFindingData">EmailPerFindingData</a>" : <i>[ <a href="emailperfindingdatadefinition.md">EmailPerFindingDataDefinition</a>, ... ]</i>,
    "<a href="#snsdata" title="SnsData">SnsData</a>" : <i>[ <a href="snsdatadefinition.md">SnsDataDefinition</a>, ... ]</i>,
    "<a href="#ticketingsystemdata" title="TicketingSystemData">TicketingSystemData</a>" : <i>[ <a href="ticketingsystemdatadefinition.md">TicketingSystemDataDefinition</a>, ... ]</i>,
    "<a href="#webhookdata" title="WebhookData">WebhookData</a>" : <i>[ <a href="webhookdatadefinition.md">WebhookDataDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#awssecurityhubintegrationstate" title="AwsSecurityHubIntegrationState">AwsSecurityHubIntegrationState</a>: <i>String</i>
<a href="#emailperfindingsendingstate" title="EmailPerFindingSendingState">EmailPerFindingSendingState</a>: <i>String</i>
<a href="#emailsendingstate" title="EmailSendingState">EmailSendingState</a>: <i>String</i>
<a href="#externalticketcreatingstate" title="ExternalTicketCreatingState">ExternalTicketCreatingState</a>: <i>String</i>
<a href="#snssendingstate" title="SnsSendingState">SnsSendingState</a>: <i>String</i>
<a href="#webhookintegrationstate" title="WebhookIntegrationState">WebhookIntegrationState</a>: <i>String</i>
<a href="#awssecurityhubintegration" title="AwsSecurityHubIntegration">AwsSecurityHubIntegration</a>: <i>
      - <a href="awssecurityhubintegrationdefinition.md">AwsSecurityHubIntegrationDefinition</a></i>
<a href="#emaildata" title="EmailData">EmailData</a>: <i>
      - <a href="emaildatadefinition.md">EmailDataDefinition</a></i>
<a href="#emailperfindingdata" title="EmailPerFindingData">EmailPerFindingData</a>: <i>
      - <a href="emailperfindingdatadefinition.md">EmailPerFindingDataDefinition</a></i>
<a href="#snsdata" title="SnsData">SnsData</a>: <i>
      - <a href="snsdatadefinition.md">SnsDataDefinition</a></i>
<a href="#ticketingsystemdata" title="TicketingSystemData">TicketingSystemData</a>: <i>
      - <a href="ticketingsystemdatadefinition.md">TicketingSystemDataDefinition</a></i>
<a href="#webhookdata" title="WebhookData">WebhookData</a>: <i>
      - <a href="webhookdatadefinition.md">WebhookDataDefinition</a></i>
</pre>

## Properties

#### AwsSecurityHubIntegrationState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailPerFindingSendingState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailSendingState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalTicketCreatingState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsSendingState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookIntegrationState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsSecurityHubIntegration

_Required_: No

_Type_: List of <a href="awssecurityhubintegrationdefinition.md">AwsSecurityHubIntegrationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailData

_Required_: No

_Type_: List of <a href="emaildatadefinition.md">EmailDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailPerFindingData

_Required_: No

_Type_: List of <a href="emailperfindingdatadefinition.md">EmailPerFindingDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsData

_Required_: No

_Type_: List of <a href="snsdatadefinition.md">SnsDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TicketingSystemData

_Required_: No

_Type_: List of <a href="ticketingsystemdatadefinition.md">TicketingSystemDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookData

_Required_: No

_Type_: List of <a href="webhookdatadefinition.md">WebhookDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

