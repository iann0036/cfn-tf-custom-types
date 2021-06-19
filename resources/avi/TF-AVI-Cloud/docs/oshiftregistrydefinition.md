# TF::AVI::Cloud OshiftRegistryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#registrynamespace" title="RegistryNamespace">RegistryNamespace</a>" : <i>String</i>,
    "<a href="#registryservice" title="RegistryService">RegistryService</a>" : <i>String</i>,
    "<a href="#registryvip" title="RegistryVip">RegistryVip</a>" : <i>[ <a href="registryvipdefinition.md">RegistryVipDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#registrynamespace" title="RegistryNamespace">RegistryNamespace</a>: <i>String</i>
<a href="#registryservice" title="RegistryService">RegistryService</a>: <i>String</i>
<a href="#registryvip" title="RegistryVip">RegistryVip</a>: <i>
      - <a href="registryvipdefinition.md">RegistryVipDefinition</a></i>
</pre>

## Properties

#### RegistryNamespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryVip

_Required_: No

_Type_: List of <a href="registryvipdefinition.md">RegistryVipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

