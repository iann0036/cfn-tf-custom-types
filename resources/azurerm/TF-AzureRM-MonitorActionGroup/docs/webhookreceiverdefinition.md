# TF::AzureRM::MonitorActionGroup WebhookReceiverDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#serviceuri" title="ServiceUri">ServiceUri</a>" : <i>String</i>,
    "<a href="#usecommonalertschema" title="UseCommonAlertSchema">UseCommonAlertSchema</a>" : <i>Boolean</i>,
    "<a href="#aadauth" title="AadAuth">AadAuth</a>" : <i>[ <a href="aadauthdefinition.md">AadAuthDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#serviceuri" title="ServiceUri">ServiceUri</a>: <i>String</i>
<a href="#usecommonalertschema" title="UseCommonAlertSchema">UseCommonAlertSchema</a>: <i>Boolean</i>
<a href="#aadauth" title="AadAuth">AadAuth</a>: <i>
      - <a href="aadauthdefinition.md">AadAuthDefinition</a></i>
</pre>

## Properties

#### Name

The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.

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

#### AadAuth

_Required_: No

_Type_: List of <a href="aadauthdefinition.md">AadAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

