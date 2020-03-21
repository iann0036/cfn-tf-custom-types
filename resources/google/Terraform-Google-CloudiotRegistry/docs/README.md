# Terraform::Google::CloudiotRegistry

Creates a device registry in Google's Cloud IoT Core platform. For more information see
[the official documentation](https://cloud.google.com/iot/docs/) and
[API](https://cloud.google.com/iot/docs/reference/cloudiot/rest/v1/projects.locations.registries).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::CloudiotRegistry",
    "Properties" : {
        "<a href="#eventnotificationconfig" title="EventNotificationConfig">EventNotificationConfig</a>" : <i>[ <a href="eventnotificationconfig.md">EventNotificationConfig</a>, ... ]</i>,
        "<a href="#httpconfig" title="HttpConfig">HttpConfig</a>" : <i>[ <a href="httpconfig.md">HttpConfig</a>, ... ]</i>,
        "<a href="#loglevel" title="LogLevel">LogLevel</a>" : <i>String</i>,
        "<a href="#mqttconfig" title="MqttConfig">MqttConfig</a>" : <i>[ <a href="mqttconfig.md">MqttConfig</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#statenotificationconfig" title="StateNotificationConfig">StateNotificationConfig</a>" : <i>[ <a href="statenotificationconfig.md">StateNotificationConfig</a>, ... ]</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>[ <a href="credentials.md">Credentials</a>, ... ]</i>,
        "<a href="#eventnotificationconfigs" title="EventNotificationConfigs">EventNotificationConfigs</a>" : <i>[ <a href="eventnotificationconfigs.md">EventNotificationConfigs</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::CloudiotRegistry
Properties:
    <a href="#eventnotificationconfig" title="EventNotificationConfig">EventNotificationConfig</a>: <i>
      - <a href="eventnotificationconfig.md">EventNotificationConfig</a></i>
    <a href="#httpconfig" title="HttpConfig">HttpConfig</a>: <i>
      - <a href="httpconfig.md">HttpConfig</a></i>
    <a href="#loglevel" title="LogLevel">LogLevel</a>: <i>String</i>
    <a href="#mqttconfig" title="MqttConfig">MqttConfig</a>: <i>
      - <a href="mqttconfig.md">MqttConfig</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#statenotificationconfig" title="StateNotificationConfig">StateNotificationConfig</a>: <i>
      - <a href="statenotificationconfig.md">StateNotificationConfig</a></i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>
      - <a href="credentials.md">Credentials</a></i>
    <a href="#eventnotificationconfigs" title="EventNotificationConfigs">EventNotificationConfigs</a>: <i>
      - <a href="eventnotificationconfigs.md">EventNotificationConfigs</a></i>
</pre>

## Properties

#### EventNotificationConfig

_Required_: No

_Type_: List of <a href="eventnotificationconfig.md">EventNotificationConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpConfig

Activate or deactivate HTTP. Structure is documented below.

_Required_: No

_Type_: List of <a href="httpconfig.md">HttpConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MqttConfig

Activate or deactivate MQTT. Structure is documented below.

_Required_: No

_Type_: List of <a href="mqttconfig.md">MqttConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The project in which the resource belongs. If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The Region in which the created address should reside. If it is not provided, the provider region is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateNotificationConfig

A PubSub topic to publish device state updates. Structure is documented below.

_Required_: No

_Type_: List of <a href="statenotificationconfig.md">StateNotificationConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

_Required_: No

_Type_: List of <a href="credentials.md">Credentials</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventNotificationConfigs

_Required_: No

_Type_: List of <a href="eventnotificationconfigs.md">EventNotificationConfigs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

