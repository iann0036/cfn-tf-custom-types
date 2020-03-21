# Terraform::Google::CloudiotRegistry

CloudFormation equivalent of google_cloudiot_registry

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::CloudiotRegistry",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#eventnotificationconfig" title="EventNotificationConfig">EventNotificationConfig</a>" : <i>[ &lt;a href=&#34;eventnotificationconfig.md&#34;&gt;EventNotificationConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#httpconfig" title="HttpConfig">HttpConfig</a>" : <i>[ &lt;a href=&#34;httpconfig.md&#34;&gt;HttpConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#loglevel" title="LogLevel">LogLevel</a>" : <i>String</i>,
        "<a href="#mqttconfig" title="MqttConfig">MqttConfig</a>" : <i>[ &lt;a href=&#34;mqttconfig.md&#34;&gt;MqttConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#statenotificationconfig" title="StateNotificationConfig">StateNotificationConfig</a>" : <i>[ &lt;a href=&#34;statenotificationconfig.md&#34;&gt;StateNotificationConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>[ &lt;a href=&#34;credentials.md&#34;&gt;Credentials&lt;/a&gt;, ... ]</i>,
        "<a href="#eventnotificationconfigs" title="EventNotificationConfigs">EventNotificationConfigs</a>" : <i>[ &lt;a href=&#34;eventnotificationconfigs.md&#34;&gt;EventNotificationConfigs&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::CloudiotRegistry
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#eventnotificationconfig" title="EventNotificationConfig">EventNotificationConfig</a>: <i>
      - &lt;a href=&#34;eventnotificationconfig.md&#34;&gt;EventNotificationConfig&lt;/a&gt;</i>
    <a href="#httpconfig" title="HttpConfig">HttpConfig</a>: <i>
      - &lt;a href=&#34;httpconfig.md&#34;&gt;HttpConfig&lt;/a&gt;</i>
    <a href="#loglevel" title="LogLevel">LogLevel</a>: <i>String</i>
    <a href="#mqttconfig" title="MqttConfig">MqttConfig</a>: <i>
      - &lt;a href=&#34;mqttconfig.md&#34;&gt;MqttConfig&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#statenotificationconfig" title="StateNotificationConfig">StateNotificationConfig</a>: <i>
      - &lt;a href=&#34;statenotificationconfig.md&#34;&gt;StateNotificationConfig&lt;/a&gt;</i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>
      - &lt;a href=&#34;credentials.md&#34;&gt;Credentials&lt;/a&gt;</i>
    <a href="#eventnotificationconfigs" title="EventNotificationConfigs">EventNotificationConfigs</a>: <i>
      - &lt;a href=&#34;eventnotificationconfigs.md&#34;&gt;EventNotificationConfigs&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventNotificationConfig

_Required_: No

_Type_: List of &lt;a href=&#34;eventnotificationconfig.md&#34;&gt;EventNotificationConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpConfig

_Required_: No

_Type_: List of &lt;a href=&#34;httpconfig.md&#34;&gt;HttpConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MqttConfig

_Required_: No

_Type_: List of &lt;a href=&#34;mqttconfig.md&#34;&gt;MqttConfig&lt;/a&gt;

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

_Type_: List of &lt;a href=&#34;statenotificationconfig.md&#34;&gt;StateNotificationConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

_Required_: No

_Type_: List of &lt;a href=&#34;credentials.md&#34;&gt;Credentials&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventNotificationConfigs

_Required_: No

_Type_: List of &lt;a href=&#34;eventnotificationconfigs.md&#34;&gt;EventNotificationConfigs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

