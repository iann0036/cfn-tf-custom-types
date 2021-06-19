# TF::GoogleBeta::GoogleAppEngineFlexibleAppVersion ResourcesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
    "<a href="#diskgb" title="DiskGb">DiskGb</a>" : <i>Double</i>,
    "<a href="#memorygb" title="MemoryGb">MemoryGb</a>" : <i>Double</i>,
    "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ <a href="volumesdefinition.md">VolumesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
<a href="#diskgb" title="DiskGb">DiskGb</a>: <i>Double</i>
<a href="#memorygb" title="MemoryGb">MemoryGb</a>: <i>Double</i>
<a href="#volumes" title="Volumes">Volumes</a>: <i>
      - <a href="volumesdefinition.md">VolumesDefinition</a></i>
</pre>

## Properties

#### Cpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of <a href="volumesdefinition.md">VolumesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

