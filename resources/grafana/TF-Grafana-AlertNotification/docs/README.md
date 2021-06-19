# TF::Grafana::AlertNotification

CloudFormation equivalent of grafana_alert_notification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Grafana::AlertNotification",
    "Properties" : {
        "<a href="#disableresolvemessage" title="DisableResolveMessage">DisableResolveMessage</a>" : <i>Boolean</i>,
        "<a href="#frequency" title="Frequency">Frequency</a>" : <i>String</i>,
        "<a href="#isdefault" title="IsDefault">IsDefault</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#securesettings" title="SecureSettings">SecureSettings</a>" : <i>[ <a href="securesettingsdefinition.md">SecureSettingsDefinition</a>, ... ]</i>,
        "<a href="#sendreminder" title="SendReminder">SendReminder</a>" : <i>Boolean</i>,
        "<a href="#settings" title="Settings">Settings</a>" : <i>[ <a href="settingsdefinition.md">SettingsDefinition</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uid" title="Uid">Uid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Grafana::AlertNotification
Properties:
    <a href="#disableresolvemessage" title="DisableResolveMessage">DisableResolveMessage</a>: <i>Boolean</i>
    <a href="#frequency" title="Frequency">Frequency</a>: <i>String</i>
    <a href="#isdefault" title="IsDefault">IsDefault</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#securesettings" title="SecureSettings">SecureSettings</a>: <i>
      - <a href="securesettingsdefinition.md">SecureSettingsDefinition</a></i>
    <a href="#sendreminder" title="SendReminder">SendReminder</a>: <i>Boolean</i>
    <a href="#settings" title="Settings">Settings</a>: <i>
      - <a href="settingsdefinition.md">SettingsDefinition</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uid" title="Uid">Uid</a>: <i>String</i>
</pre>

## Properties

#### DisableResolveMessage

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Frequency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDefault

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureSettings

_Required_: No

_Type_: List of <a href="securesettingsdefinition.md">SecureSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendReminder

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

_Required_: No

_Type_: List of <a href="settingsdefinition.md">SettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uid

_Required_: No

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

