# TF::AzureRM::MonitorAutoscaleSetting EmailDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customemails" title="CustomEmails">CustomEmails</a>" : <i>[ String, ... ]</i>,
    "<a href="#sendtosubscriptionadministrator" title="SendToSubscriptionAdministrator">SendToSubscriptionAdministrator</a>" : <i>Boolean</i>,
    "<a href="#sendtosubscriptioncoadministrator" title="SendToSubscriptionCoAdministrator">SendToSubscriptionCoAdministrator</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#customemails" title="CustomEmails">CustomEmails</a>: <i>
      - String</i>
<a href="#sendtosubscriptionadministrator" title="SendToSubscriptionAdministrator">SendToSubscriptionAdministrator</a>: <i>Boolean</i>
<a href="#sendtosubscriptioncoadministrator" title="SendToSubscriptionCoAdministrator">SendToSubscriptionCoAdministrator</a>: <i>Boolean</i>
</pre>

## Properties

#### CustomEmails

Specifies a list of custom email addresses to which the email notifications will be sent.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendToSubscriptionAdministrator

Should email notifications be sent to the subscription administrator? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendToSubscriptionCoAdministrator

Should email notifications be sent to the subscription co-administrator? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

