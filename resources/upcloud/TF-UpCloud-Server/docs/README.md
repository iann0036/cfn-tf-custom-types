# TF::UpCloud::Server

CloudFormation equivalent of upcloud_server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::UpCloud::Server",
    "Properties" : {
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
        "<a href="#firewall" title="Firewall">Firewall</a>" : <i>Boolean</i>,
        "<a href="#host" title="Host">Host</a>" : <i>Double</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#mem" title="Mem">Mem</a>" : <i>Double</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>Boolean</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#login" title="Login">Login</a>" : <i>[ <a href="logindefinition.md">LoginDefinition</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>, ... ]</i>,
        "<a href="#storagedevices" title="StorageDevices">StorageDevices</a>" : <i>[ <a href="storagedevicesdefinition.md">StorageDevicesDefinition</a>, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ <a href="templatedefinition.md">TemplateDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::UpCloud::Server
Properties:
    <a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
    <a href="#firewall" title="Firewall">Firewall</a>: <i>Boolean</i>
    <a href="#host" title="Host">Host</a>: <i>Double</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#mem" title="Mem">Mem</a>: <i>Double</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>Boolean</i>
    <a href="#plan" title="Plan">Plan</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#login" title="Login">Login</a>: <i>
      - <a href="logindefinition.md">LoginDefinition</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a></i>
    <a href="#storagedevices" title="StorageDevices">StorageDevices</a>: <i>
      - <a href="storagedevicesdefinition.md">StorageDevicesDefinition</a></i>
    <a href="#template" title="Template">Template</a>: <i>
      - <a href="templatedefinition.md">TemplateDefinition</a></i>
</pre>

## Properties

#### Cpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firewall

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mem

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Login

_Required_: No

_Type_: List of <a href="logindefinition.md">LoginDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDevices

_Required_: No

_Type_: List of <a href="storagedevicesdefinition.md">StorageDevicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of <a href="templatedefinition.md">TemplateDefinition</a>

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

#### Title

Returns the <code>Title</code> value.

