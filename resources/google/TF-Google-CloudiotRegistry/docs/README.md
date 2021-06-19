# TF::Google::CloudiotRegistry

A Google Cloud IoT Core device registry.


To get more information about DeviceRegistry, see:

* [API documentation](https://cloud.google.com/iot/docs/reference/cloudiot/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/iot/docs/)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=cloudiot_device_registry_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::CloudiotRegistry",
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
Type: TF::Google::CloudiotRegistry
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

Activate or deactivate HTTP.
The structure is documented below.

_Required_: No

_Type_: List of <a href="httpconfigdefinition.md">HttpConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MqttConfig

Activate or deactivate MQTT.
The structure is documented below.

_Required_: No

_Type_: List of <a href="mqttconfigdefinition.md">MqttConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateNotificationConfig

A PubSub topic to publish device state updates.
The structure is documented below.

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

