# TF::Google::CloudiotDevice

A Google Cloud IoT Core device.


To get more information about Device, see:

* [API documentation](https://cloud.google.com/iot/docs/reference/cloudiot/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/iot/docs/)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=cloudiot_device_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::CloudiotDevice",
    "Properties" : {
        "<a href="#blocked" title="Blocked">Blocked</a>" : <i>Boolean</i>,
        "<a href="#loglevel" title="LogLevel">LogLevel</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#registry" title="Registry">Registry</a>" : <i>String</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>[ <a href="credentialsdefinition.md">CredentialsDefinition</a>, ... ]</i>,
        "<a href="#gatewayconfig" title="GatewayConfig">GatewayConfig</a>" : <i>[ <a href="gatewayconfigdefinition.md">GatewayConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::CloudiotDevice
Properties:
    <a href="#blocked" title="Blocked">Blocked</a>: <i>Boolean</i>
    <a href="#loglevel" title="LogLevel">LogLevel</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#registry" title="Registry">Registry</a>: <i>String</i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>
      - <a href="credentialsdefinition.md">CredentialsDefinition</a></i>
    <a href="#gatewayconfig" title="GatewayConfig">GatewayConfig</a>: <i>
      - <a href="gatewayconfigdefinition.md">GatewayConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Blocked

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Registry

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

_Required_: No

_Type_: List of <a href="credentialsdefinition.md">CredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayConfig

_Required_: No

_Type_: List of <a href="gatewayconfigdefinition.md">GatewayConfigDefinition</a>

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

#### Config

Returns the <code>Config</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastConfigAckTime

Returns the <code>LastConfigAckTime</code> value.

#### LastConfigSendTime

Returns the <code>LastConfigSendTime</code> value.

#### LastErrorStatus

Returns the <code>LastErrorStatus</code> value.

#### LastErrorTime

Returns the <code>LastErrorTime</code> value.

#### LastEventTime

Returns the <code>LastEventTime</code> value.

#### LastHeartbeatTime

Returns the <code>LastHeartbeatTime</code> value.

#### LastStateTime

Returns the <code>LastStateTime</code> value.

#### NumId

Returns the <code>NumId</code> value.

#### State

Returns the <code>State</code> value.

