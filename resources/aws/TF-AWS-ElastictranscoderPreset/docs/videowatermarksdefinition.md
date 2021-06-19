# TF::AWS::ElastictranscoderPreset VideoWatermarksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#horizontalalign" title="HorizontalAlign">HorizontalAlign</a>" : <i>String</i>,
    "<a href="#horizontaloffset" title="HorizontalOffset">HorizontalOffset</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#maxheight" title="MaxHeight">MaxHeight</a>" : <i>String</i>,
    "<a href="#maxwidth" title="MaxWidth">MaxWidth</a>" : <i>String</i>,
    "<a href="#opacity" title="Opacity">Opacity</a>" : <i>String</i>,
    "<a href="#sizingpolicy" title="SizingPolicy">SizingPolicy</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#verticalalign" title="VerticalAlign">VerticalAlign</a>" : <i>String</i>,
    "<a href="#verticaloffset" title="VerticalOffset">VerticalOffset</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#horizontalalign" title="HorizontalAlign">HorizontalAlign</a>: <i>String</i>
<a href="#horizontaloffset" title="HorizontalOffset">HorizontalOffset</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#maxheight" title="MaxHeight">MaxHeight</a>: <i>String</i>
<a href="#maxwidth" title="MaxWidth">MaxWidth</a>: <i>String</i>
<a href="#opacity" title="Opacity">Opacity</a>: <i>String</i>
<a href="#sizingpolicy" title="SizingPolicy">SizingPolicy</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#verticalalign" title="VerticalAlign">VerticalAlign</a>: <i>String</i>
<a href="#verticaloffset" title="VerticalOffset">VerticalOffset</a>: <i>String</i>
</pre>

## Properties

#### HorizontalAlign

The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HorizontalOffset

The amount by which you want the horizontal position of the watermark to be offset from the position specified by `horizontal_align`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHeight

The maximum height of the watermark.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxWidth

The maximum width of the watermark.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Opacity

A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizingPolicy

A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerticalAlign

The vertical position of the watermark unless you specify a nonzero value for `vertical_align`. Valid values are `Top`, `Bottom`, `Center`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerticalOffset

The amount by which you want the vertical position of the watermark to be offset from the position specified by `vertical_align`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

