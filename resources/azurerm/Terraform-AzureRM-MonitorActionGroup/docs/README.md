# Terraform::AzureRM::MonitorActionGroup

CloudFormation equivalent of azurerm_monitor_action_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::MonitorActionGroup",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#shortname" title="ShortName">ShortName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#armrolereceiver" title="ArmRoleReceiver">ArmRoleReceiver</a>" : <i>[ &lt;a href=&#34;armrolereceiver.md&#34;&gt;ArmRoleReceiver&lt;/a&gt;, ... ]</i>,
        "<a href="#automationrunbookreceiver" title="AutomationRunbookReceiver">AutomationRunbookReceiver</a>" : <i>[ &lt;a href=&#34;automationrunbookreceiver.md&#34;&gt;AutomationRunbookReceiver&lt;/a&gt;, ... ]</i>,
        "<a href="#azureapppushreceiver" title="AzureAppPushReceiver">AzureAppPushReceiver</a>" : <i>[ &lt;a href=&#34;azureapppushreceiver.md&#34;&gt;AzureAppPushReceiver&lt;/a&gt;, ... ]</i>,
        "<a href="#azurefunctionreceiver" title="AzureFunctionReceiver">AzureFunctionReceiver</a>" : <i>[ &lt;a href=&#34;azurefunctionreceiver.md&#34;&gt;AzureFunctionReceiver&lt;/a&gt;, ... ]</i>,
        "<a href="#emailreceiver" title="EmailReceiver">EmailReceiver</a>" : <i>[ &lt;a href=&#34;emailreceiver.md&#34;&gt;EmailReceiver&lt;/a&gt;, ... ]</i>,
        "<a href="#itsmreceiver" title="ItsmReceiver">ItsmReceiver</a>" : <i>[ &lt;a href=&#34;itsmreceiver.md&#34;&gt;ItsmReceiver&lt;/a&gt;, ... ]</i>,
        "<a href="#logicappreceiver" title="LogicAppReceiver">LogicAppReceiver</a>" : <i>[ &lt;a href=&#34;logicappreceiver.md&#34;&gt;LogicAppReceiver&lt;/a&gt;, ... ]</i>,
        "<a href="#smsreceiver" title="SmsReceiver">SmsReceiver</a>" : <i>[ &lt;a href=&#34;smsreceiver.md&#34;&gt;SmsReceiver&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#voicereceiver" title="VoiceReceiver">VoiceReceiver</a>" : <i>[ &lt;a href=&#34;voicereceiver.md&#34;&gt;VoiceReceiver&lt;/a&gt;, ... ]</i>,
        "<a href="#webhookreceiver" title="WebhookReceiver">WebhookReceiver</a>" : <i>[ &lt;a href=&#34;webhookreceiver.md&#34;&gt;WebhookReceiver&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::MonitorActionGroup
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#shortname" title="ShortName">ShortName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#armrolereceiver" title="ArmRoleReceiver">ArmRoleReceiver</a>: <i>
      - &lt;a href=&#34;armrolereceiver.md&#34;&gt;ArmRoleReceiver&lt;/a&gt;</i>
    <a href="#automationrunbookreceiver" title="AutomationRunbookReceiver">AutomationRunbookReceiver</a>: <i>
      - &lt;a href=&#34;automationrunbookreceiver.md&#34;&gt;AutomationRunbookReceiver&lt;/a&gt;</i>
    <a href="#azureapppushreceiver" title="AzureAppPushReceiver">AzureAppPushReceiver</a>: <i>
      - &lt;a href=&#34;azureapppushreceiver.md&#34;&gt;AzureAppPushReceiver&lt;/a&gt;</i>
    <a href="#azurefunctionreceiver" title="AzureFunctionReceiver">AzureFunctionReceiver</a>: <i>
      - &lt;a href=&#34;azurefunctionreceiver.md&#34;&gt;AzureFunctionReceiver&lt;/a&gt;</i>
    <a href="#emailreceiver" title="EmailReceiver">EmailReceiver</a>: <i>
      - &lt;a href=&#34;emailreceiver.md&#34;&gt;EmailReceiver&lt;/a&gt;</i>
    <a href="#itsmreceiver" title="ItsmReceiver">ItsmReceiver</a>: <i>
      - &lt;a href=&#34;itsmreceiver.md&#34;&gt;ItsmReceiver&lt;/a&gt;</i>
    <a href="#logicappreceiver" title="LogicAppReceiver">LogicAppReceiver</a>: <i>
      - &lt;a href=&#34;logicappreceiver.md&#34;&gt;LogicAppReceiver&lt;/a&gt;</i>
    <a href="#smsreceiver" title="SmsReceiver">SmsReceiver</a>: <i>
      - &lt;a href=&#34;smsreceiver.md&#34;&gt;SmsReceiver&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#voicereceiver" title="VoiceReceiver">VoiceReceiver</a>: <i>
      - &lt;a href=&#34;voicereceiver.md&#34;&gt;VoiceReceiver&lt;/a&gt;</i>
    <a href="#webhookreceiver" title="WebhookReceiver">WebhookReceiver</a>: <i>
      - &lt;a href=&#34;webhookreceiver.md&#34;&gt;WebhookReceiver&lt;/a&gt;</i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArmRoleReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;armrolereceiver.md&#34;&gt;ArmRoleReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomationRunbookReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;automationrunbookreceiver.md&#34;&gt;AutomationRunbookReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureAppPushReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;azureapppushreceiver.md&#34;&gt;AzureAppPushReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFunctionReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;azurefunctionreceiver.md&#34;&gt;AzureFunctionReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;emailreceiver.md&#34;&gt;EmailReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ItsmReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;itsmreceiver.md&#34;&gt;ItsmReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicAppReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;logicappreceiver.md&#34;&gt;LogicAppReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;smsreceiver.md&#34;&gt;SmsReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VoiceReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;voicereceiver.md&#34;&gt;VoiceReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookReceiver

_Required_: No

_Type_: List of &lt;a href=&#34;webhookreceiver.md&#34;&gt;WebhookReceiver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

