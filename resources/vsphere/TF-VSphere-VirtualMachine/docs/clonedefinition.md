# TF::VSphere::VirtualMachine CloneDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#linkedclone" title="LinkedClone">LinkedClone</a>" : <i>Boolean</i>,
    "<a href="#ovfnetworkmap" title="OvfNetworkMap">OvfNetworkMap</a>" : <i>[ <a href="ovfnetworkmapdefinition.md">OvfNetworkMapDefinition</a>, ... ]</i>,
    "<a href="#ovfstoragemap" title="OvfStorageMap">OvfStorageMap</a>" : <i>[ <a href="ovfstoragemapdefinition.md">OvfStorageMapDefinition</a>, ... ]</i>,
    "<a href="#templateuuid" title="TemplateUuid">TemplateUuid</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#customize" title="Customize">Customize</a>" : <i>[ <a href="customizedefinition.md">CustomizeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#linkedclone" title="LinkedClone">LinkedClone</a>: <i>Boolean</i>
<a href="#ovfnetworkmap" title="OvfNetworkMap">OvfNetworkMap</a>: <i>
      - <a href="ovfnetworkmapdefinition.md">OvfNetworkMapDefinition</a></i>
<a href="#ovfstoragemap" title="OvfStorageMap">OvfStorageMap</a>: <i>
      - <a href="ovfstoragemapdefinition.md">OvfStorageMapDefinition</a></i>
<a href="#templateuuid" title="TemplateUuid">TemplateUuid</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#customize" title="Customize">Customize</a>: <i>
      - <a href="customizedefinition.md">CustomizeDefinition</a></i>
</pre>

## Properties

#### LinkedClone

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvfNetworkMap

_Required_: No

_Type_: List of <a href="ovfnetworkmapdefinition.md">OvfNetworkMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvfStorageMap

_Required_: No

_Type_: List of <a href="ovfstoragemapdefinition.md">OvfStorageMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUuid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Customize

_Required_: No

_Type_: List of <a href="customizedefinition.md">CustomizeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

