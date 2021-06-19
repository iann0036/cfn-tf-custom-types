# TF::OPC::ComputeOrchestratedInstance InstanceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bootorder" title="BootOrder">BootOrder</a>" : <i>[ Double, ... ]</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#imagelist" title="ImageList">ImageList</a>" : <i>String</i>,
    "<a href="#instanceattributes" title="InstanceAttributes">InstanceAttributes</a>" : <i>String</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#persistent" title="Persistent">Persistent</a>" : <i>Boolean</i>,
    "<a href="#reversedns" title="ReverseDns">ReverseDns</a>" : <i>Boolean</i>,
    "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
    "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#networkinginfo" title="NetworkingInfo">NetworkingInfo</a>" : <i>[ <a href="networkinginfodefinition.md">NetworkingInfoDefinition</a>, ... ]</i>,
    "<a href="#storage" title="Storage">Storage</a>" : <i>[ <a href="storagedefinition.md">StorageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bootorder" title="BootOrder">BootOrder</a>: <i>
      - Double</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#imagelist" title="ImageList">ImageList</a>: <i>String</i>
<a href="#instanceattributes" title="InstanceAttributes">InstanceAttributes</a>: <i>String</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#persistent" title="Persistent">Persistent</a>: <i>Boolean</i>
<a href="#reversedns" title="ReverseDns">ReverseDns</a>: <i>Boolean</i>
<a href="#shape" title="Shape">Shape</a>: <i>String</i>
<a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#networkinginfo" title="NetworkingInfo">NetworkingInfo</a>: <i>
      - <a href="networkinginfodefinition.md">NetworkingInfoDefinition</a></i>
<a href="#storage" title="Storage">Storage</a>: <i>
      - <a href="storagedefinition.md">StorageDefinition</a></i>
</pre>

## Properties

#### BootOrder

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageList

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceAttributes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Persistent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseDns

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkingInfo

_Required_: No

_Type_: List of <a href="networkinginfodefinition.md">NetworkingInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

_Required_: No

_Type_: List of <a href="storagedefinition.md">StorageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

