# TF::GoogleBeta::GoogleCloudiotRegistry

CloudFormation equivalent of google_cloudiot_registry

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleCloudiotRegistry",
    "Properties" : {
        "<a href="#httpconfig" title="HttpConfig">HttpConfig</a>" : <i>[ <a href="httpconfigdefinition.md">HttpConfigDefinition</a>, ... ]</i>,
        "<a href="#loglevel" title="LogLevel">LogLevel</a>" : <i>String</i>,
        "<a href="#mqttconfig" title="MqttConfig">MqttConfig</a>" : <i>[ <a href="mqttconfigdefinition.md">MqttConfigDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#statenotificationconfig" title="StateNotificationConfig">StateNotificationConfig</a>" : <i>[ <a href="statenotificationconfigdefinition.md">StateNotificationConfigDefinition</a>, ... ]</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>[ <a href="credentialsdefinition.md">CredentialsDefinition</a>, ... ]</i>,
        "<a href="#eventnotificationconfigs" title="EventNotificationConfigs">EventNotificationConfigs</a>" : <i>[ <a href="eventnotificationconfigsdefinition.md">EventNotificationConfigsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleCloudiotRegistry
Properties:
    <a href="#httpconfig" title="HttpConfig">HttpConfig</a>: <i>
      - <a href="httpconfigdefinition.md">HttpConfigDefinition</a></i>
    <a href="#loglevel" title="LogLevel">LogLevel</a>: <i>String</i>
    <a href="#mqttconfig" title="MqttConfig">MqttConfig</a>: <i>
      - <a href="mqttconfigdefinition.md">MqttConfigDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#statenotificationconfig" title="StateNotificationConfig">StateNotificationConfig</a>: <i>
      - <a href="statenotificationconfigdefinition.md">StateNotificationConfigDefinition</a></i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>
      - <a href="credentialsdefinition.md">CredentialsDefinition</a></i>
    <a href="#eventnotificationconfigs" title="EventNotificationConfigs">EventNotificationConfigs</a>: <i>
      - <a href="eventnotificationconfigsdefinition.md">EventNotificationConfigsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### HttpConfig

_Required_: No

_Type_: List of <a href="httpconfigdefinition.md">HttpConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MqttConfig

_Required_: No

_Type_: List of <a href="mqttconfigdefinition.md">MqttConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateNotificationConfig

_Required_: No

_Type_: List of <a href="statenotificationconfigdefinition.md">StateNotificationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

_Required_: No

_Type_: List of <a href="credentialsdefinition.md">CredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventNotificationConfigs

_Required_: No

_Type_: List of <a href="eventnotificationconfigsdefinition.md">EventNotificationConfigsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

