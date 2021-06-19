# TF::AzureRM::MonitorActionGroup

Manages an Action Group within Azure Monitor.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::MonitorActionGroup",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#shortname" title="ShortName">ShortName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#armrolereceiver" title="ArmRoleReceiver">ArmRoleReceiver</a>" : <i>[ <a href="armrolereceiverdefinition.md">ArmRoleReceiverDefinition</a>, ... ]</i>,
        "<a href="#automationrunbookreceiver" title="AutomationRunbookReceiver">AutomationRunbookReceiver</a>" : <i>[ <a href="automationrunbookreceiverdefinition.md">AutomationRunbookReceiverDefinition</a>, ... ]</i>,
        "<a href="#azureapppushreceiver" title="AzureAppPushReceiver">AzureAppPushReceiver</a>" : <i>[ <a href="azureapppushreceiverdefinition.md">AzureAppPushReceiverDefinition</a>, ... ]</i>,
        "<a href="#azurefunctionreceiver" title="AzureFunctionReceiver">AzureFunctionReceiver</a>" : <i>[ <a href="azurefunctionreceiverdefinition.md">AzureFunctionReceiverDefinition</a>, ... ]</i>,
        "<a href="#emailreceiver" title="EmailReceiver">EmailReceiver</a>" : <i>[ <a href="emailreceiverdefinition.md">EmailReceiverDefinition</a>, ... ]</i>,
        "<a href="#itsmreceiver" title="ItsmReceiver">ItsmReceiver</a>" : <i>[ <a href="itsmreceiverdefinition.md">ItsmReceiverDefinition</a>, ... ]</i>,
        "<a href="#logicappreceiver" title="LogicAppReceiver">LogicAppReceiver</a>" : <i>[ <a href="logicappreceiverdefinition.md">LogicAppReceiverDefinition</a>, ... ]</i>,
        "<a href="#smsreceiver" title="SmsReceiver">SmsReceiver</a>" : <i>[ <a href="smsreceiverdefinition.md">SmsReceiverDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#voicereceiver" title="VoiceReceiver">VoiceReceiver</a>" : <i>[ <a href="voicereceiverdefinition.md">VoiceReceiverDefinition</a>, ... ]</i>,
        "<a href="#webhookreceiver" title="WebhookReceiver">WebhookReceiver</a>" : <i>[ <a href="webhookreceiverdefinition.md">WebhookReceiverDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::MonitorActionGroup
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#shortname" title="ShortName">ShortName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#armrolereceiver" title="ArmRoleReceiver">ArmRoleReceiver</a>: <i>
      - <a href="armrolereceiverdefinition.md">ArmRoleReceiverDefinition</a></i>
    <a href="#automationrunbookreceiver" title="AutomationRunbookReceiver">AutomationRunbookReceiver</a>: <i>
      - <a href="automationrunbookreceiverdefinition.md">AutomationRunbookReceiverDefinition</a></i>
    <a href="#azureapppushreceiver" title="AzureAppPushReceiver">AzureAppPushReceiver</a>: <i>
      - <a href="azureapppushreceiverdefinition.md">AzureAppPushReceiverDefinition</a></i>
    <a href="#azurefunctionreceiver" title="AzureFunctionReceiver">AzureFunctionReceiver</a>: <i>
      - <a href="azurefunctionreceiverdefinition.md">AzureFunctionReceiverDefinition</a></i>
    <a href="#emailreceiver" title="EmailReceiver">EmailReceiver</a>: <i>
      - <a href="emailreceiverdefinition.md">EmailReceiverDefinition</a></i>
    <a href="#itsmreceiver" title="ItsmReceiver">ItsmReceiver</a>: <i>
      - <a href="itsmreceiverdefinition.md">ItsmReceiverDefinition</a></i>
    <a href="#logicappreceiver" title="LogicAppReceiver">LogicAppReceiver</a>: <i>
      - <a href="logicappreceiverdefinition.md">LogicAppReceiverDefinition</a></i>
    <a href="#smsreceiver" title="SmsReceiver">SmsReceiver</a>: <i>
      - <a href="smsreceiverdefinition.md">SmsReceiverDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#voicereceiver" title="VoiceReceiver">VoiceReceiver</a>: <i>
      - <a href="voicereceiverdefinition.md">VoiceReceiverDefinition</a></i>
    <a href="#webhookreceiver" title="WebhookReceiver">WebhookReceiver</a>: <i>
      - <a href="webhookreceiverdefinition.md">WebhookReceiverDefinition</a></i>
</pre>

## Properties

#### Enabled

Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Action Group. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Action Group instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortName

The short name of the action group. This will be used in SMS messages.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArmRoleReceiver

_Required_: No

_Type_: List of <a href="armrolereceiverdefinition.md">ArmRoleReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomationRunbookReceiver

_Required_: No

_Type_: List of <a href="automationrunbookreceiverdefinition.md">AutomationRunbookReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureAppPushReceiver

_Required_: No

_Type_: List of <a href="azureapppushreceiverdefinition.md">AzureAppPushReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFunctionReceiver

_Required_: No

_Type_: List of <a href="azurefunctionreceiverdefinition.md">AzureFunctionReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailReceiver

_Required_: No

_Type_: List of <a href="emailreceiverdefinition.md">EmailReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ItsmReceiver

_Required_: No

_Type_: List of <a href="itsmreceiverdefinition.md">ItsmReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicAppReceiver

_Required_: No

_Type_: List of <a href="logicappreceiverdefinition.md">LogicAppReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsReceiver

_Required_: No

_Type_: List of <a href="smsreceiverdefinition.md">SmsReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VoiceReceiver

_Required_: No

_Type_: List of <a href="voicereceiverdefinition.md">VoiceReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookReceiver

_Required_: No

_Type_: List of <a href="webhookreceiverdefinition.md">WebhookReceiverDefinition</a>

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

