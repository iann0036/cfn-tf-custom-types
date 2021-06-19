# TF::Tfe::NotificationConfiguration

Terraform Cloud can be configured to send notifications for run state transitions. 
Notification configurations allow you to specify a URL, destination type, and what events will trigger the notification. 
Each workspace can have up to 20 notification configurations, and they apply to all runs for that workspace.

~> **NOTE:** Using `destination_type` of `email` requires using the provider with Terraform Cloud or an instance of 
  Terraform Enterprise at least as recent as v202005-1.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Tfe::NotificationConfiguration",
    "Properties" : {
        "<a href="#destinationtype" title="DestinationType">DestinationType</a>" : <i>String</i>,
        "<a href="#emailaddresses" title="EmailAddresses">EmailAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#emailuserids" title="EmailUserIds">EmailUserIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ String, ... ]</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Tfe::NotificationConfiguration
Properties:
    <a href="#destinationtype" title="DestinationType">DestinationType</a>: <i>String</i>
    <a href="#emailaddresses" title="EmailAddresses">EmailAddresses</a>: <i>
      - String</i>
    <a href="#emailuserids" title="EmailUserIds">EmailUserIds</a>: <i>
      - String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>: <i>String</i>
</pre>

## Properties

#### DestinationType

The type of notification configuration payload to send.
Valid values are `email`, `generic` or `slack`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailAddresses

**TFE only** A list of email addresses. This value
_must not_ be provided if `destination_type` is `generic` or `slack`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailUserIds

A list of user IDs. This value _must not_ be provided
if `destination_type` is `generic` or `slack`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the notification configuration should be enabled or not.
Disabled configurations will not send any notifications. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the notification configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

A write-only secure token for the notification configuration, which can
be used by the receiving server to verify request authenticity when configured for notification
configurations with a destination type of `generic`. Defaults to `null`.
This value _must not_ be provided if `destination_type` is `email` or `slack`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

The array of triggers for which this notification configuration will
send notifications. Valid values are `run:created`, `run:planning`, `run:needs_attention`, `run:applying`
`run:completed`, `run:errored`. If omitted, no notification triggers are configured.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The HTTP or HTTPS URL of the notification
configuration where notification requests will be made. This value _must not_ be provided if `destination_type`
is `email`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceId

The id of the workspace that owns the notification configuration.

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

#### Id

Returns the <code>Id</code> value.

