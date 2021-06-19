# TF::OpsGenie::ApiIntegration

Manages an API Integration within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::ApiIntegration",
    "Properties" : {
        "<a href="#allowwriteaccess" title="AllowWriteAccess">AllowWriteAccess</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
        "<a href="#ignorerespondersfrompayload" title="IgnoreRespondersFromPayload">IgnoreRespondersFromPayload</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ownerteamid" title="OwnerTeamId">OwnerTeamId</a>" : <i>String</i>,
        "<a href="#suppressnotifications" title="SuppressNotifications">SuppressNotifications</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#webhookurl" title="WebhookUrl">WebhookUrl</a>" : <i>String</i>,
        "<a href="#responders" title="Responders">Responders</a>" : <i>[ <a href="respondersdefinition.md">RespondersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::ApiIntegration
Properties:
    <a href="#allowwriteaccess" title="AllowWriteAccess">AllowWriteAccess</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
    <a href="#ignorerespondersfrompayload" title="IgnoreRespondersFromPayload">IgnoreRespondersFromPayload</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ownerteamid" title="OwnerTeamId">OwnerTeamId</a>: <i>String</i>
    <a href="#suppressnotifications" title="SuppressNotifications">SuppressNotifications</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#webhookurl" title="WebhookUrl">WebhookUrl</a>: <i>String</i>
    <a href="#responders" title="Responders">Responders</a>: <i>
      - <a href="respondersdefinition.md">RespondersDefinition</a></i>
</pre>

## Properties

#### AllowWriteAccess

This parameter is for configuring the write access of integration. If write access is restricted, the integration will not be authorized to write within any domain. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

This parameter is for specifying whether the integration will be enabled or not. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreRespondersFromPayload

If enabled, the integration will ignore recipients sent in request payloads. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the integration. Name must be unique for each integration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerTeamId

Owner team id of the integration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuppressNotifications

If enabled, notifications that come from alerts will be suppressed. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the integration (API, Marid, Prometheus, etc). The full list of options can be found [here](https://docs.opsgenie.com/docs/integration-types-to-use-with-api).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookUrl

It is required if type is `Webhook`. This is the url Opsgenie will be sending request to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Responders

_Required_: No

_Type_: List of <a href="respondersdefinition.md">RespondersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiKey

Returns the <code>ApiKey</code> value.

#### Id

Returns the <code>Id</code> value.

