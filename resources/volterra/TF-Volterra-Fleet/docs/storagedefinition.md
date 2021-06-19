# TF::Volterra::Fleet StorageDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
    "<a href="#volumedefaults" title="VolumeDefaults">VolumeDefaults</a>" : <i>[ <a href="volumedefaultsdefinition.md">VolumeDefaultsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#zone" title="Zone">Zone</a>: <i>String</i>
<a href="#volumedefaults" title="VolumeDefaults">VolumeDefaults</a>: <i>
      - <a href="volumedefaultsdefinition.md">VolumeDefaultsDefinition</a></i>
</pre>

## Properties

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeDefaults

_Required_: No

_Type_: List of <a href="volumedefaultsdefinition.md">VolumeDefaultsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

