# TF::TencentCloud::VodAdaptiveDynamicStreamingTemplate StreamInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#removeaudio" title="RemoveAudio">RemoveAudio</a>" : <i>Boolean</i>,
    "<a href="#audio" title="Audio">Audio</a>" : <i>[ <a href="audiodefinition.md">AudioDefinition</a>, ... ]</i>,
    "<a href="#video" title="Video">Video</a>" : <i>[ <a href="videodefinition.md">VideoDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#removeaudio" title="RemoveAudio">RemoveAudio</a>: <i>Boolean</i>
<a href="#audio" title="Audio">Audio</a>: <i>
      - <a href="audiodefinition.md">AudioDefinition</a></i>
<a href="#video" title="Video">Video</a>: <i>
      - <a href="videodefinition.md">VideoDefinition</a></i>
</pre>

## Properties

#### RemoveAudio

Whether to remove audio stream. Valid values: `false`: no, `true`: yes. `false` by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Audio

_Required_: No

_Type_: List of <a href="audiodefinition.md">AudioDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Video

_Required_: No

_Type_: List of <a href="videodefinition.md">VideoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

