# TF::TencentCloud::VodProcedureTemplate TranscodeTaskListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#definition" title="Definition">Definition</a>" : <i>String</i>,
    "<a href="#mosaiclist" title="MosaicList">MosaicList</a>" : <i>[ <a href="mosaiclistdefinition.md">MosaicListDefinition</a>, ... ]</i>,
    "<a href="#watermarklist" title="WatermarkList">WatermarkList</a>" : <i>[ <a href="watermarklistdefinition.md">WatermarkListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#definition" title="Definition">Definition</a>: <i>String</i>
<a href="#mosaiclist" title="MosaicList">MosaicList</a>: <i>
      - <a href="mosaiclistdefinition.md">MosaicListDefinition</a></i>
<a href="#watermarklist" title="WatermarkList">WatermarkList</a>: <i>
      - <a href="watermarklistdefinition.md">WatermarkListDefinition</a></i>
</pre>

## Properties

#### Definition

Video transcoding template ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MosaicList

_Required_: No

_Type_: List of <a href="mosaiclistdefinition.md">MosaicListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatermarkList

_Required_: No

_Type_: List of <a href="watermarklistdefinition.md">WatermarkListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

