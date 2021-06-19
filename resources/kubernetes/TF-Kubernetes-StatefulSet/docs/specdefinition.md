# TF::Kubernetes::StatefulSet SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accessmodes" title="AccessModes">AccessModes</a>" : <i>[ String, ... ]</i>,
    "<a href="#storageclassname" title="StorageClassName">StorageClassName</a>" : <i>String</i>,
    "<a href="#volumename" title="VolumeName">VolumeName</a>" : <i>String</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resourcesdefinition.md">ResourcesDefinition</a>, ... ]</i>,
    "<a href="#selector" title="Selector">Selector</a>" : <i>[ <a href="selectordefinition.md">SelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accessmodes" title="AccessModes">AccessModes</a>: <i>
      - String</i>
<a href="#storageclassname" title="StorageClassName">StorageClassName</a>: <i>String</i>
<a href="#volumename" title="VolumeName">VolumeName</a>: <i>String</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resourcesdefinition.md">ResourcesDefinition</a></i>
<a href="#selector" title="Selector">Selector</a>: <i>
      - <a href="selectordefinition.md">SelectorDefinition</a></i>
</pre>

## Properties

#### AccessModes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClassName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resourcesdefinition.md">ResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No

_Type_: List of <a href="selectordefinition.md">SelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

