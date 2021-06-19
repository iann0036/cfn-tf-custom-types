# TF::TencentCloud::VodProcedureTemplate SnapshotByTimeOffsetTaskListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#definition" title="Definition">Definition</a>" : <i>String</i>,
    "<a href="#exttimeoffsetlist" title="ExtTimeOffsetList">ExtTimeOffsetList</a>" : <i>[ String, ... ]</i>,
    "<a href="#watermarklist" title="WatermarkList">WatermarkList</a>" : <i>[ <a href="watermarklistdefinition.md">WatermarkListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#definition" title="Definition">Definition</a>: <i>String</i>
<a href="#exttimeoffsetlist" title="ExtTimeOffsetList">ExtTimeOffsetList</a>: <i>
      - String</i>
<a href="#watermarklist" title="WatermarkList">WatermarkList</a>: <i>
      - <a href="watermarklistdefinition.md">WatermarkListDefinition</a></i>
</pre>

## Properties

#### Definition

Time point screen capturing template ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtTimeOffsetList

The list of screenshot time points. `s` and `%` formats are supported: When a time point string ends with `s`, its unit is second. For example, `3.5s` means the 3.5th second of the video; When a time point string ends with `%`, it is marked with corresponding percentage of the video duration. For example, `10%` means that the time point is at the 10% of the video entire duration.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatermarkList

_Required_: No

_Type_: List of <a href="watermarklistdefinition.md">WatermarkListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

