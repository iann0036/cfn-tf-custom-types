# TF::Lacework::AlertChannelMicrosoftTeams

You can configure Lacework to forward alerts to a Microsoft Teams channel through an incoming webhook.
[Create a incoming webhook](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)

To find more information about the alert payload, see the [Lacework support documentation](https://support.lacework.com/hc/en-us/articles/360051656053-Microsoft-Teams).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Lacework::AlertChannelMicrosoftTeams",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#webhookurl" title="WebhookUrl">WebhookUrl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Lacework::AlertChannelMicrosoftTeams
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#webhookurl" title="WebhookUrl">WebhookUrl</a>: <i>String</i>
</pre>

## Properties

#### Enabled

The state of the external integration. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Alert Channel integration name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookUrl

The URL of your Microsoft Teams incoming webhook.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedOrUpdatedBy

Returns the <code>CreatedOrUpdatedBy</code> value.

#### CreatedOrUpdatedTime

Returns the <code>CreatedOrUpdatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntgGuid

Returns the <code>IntgGuid</code> value.

#### OrgLevel

Returns the <code>OrgLevel</code> value.

#### TypeName

Returns the <code>TypeName</code> value.

