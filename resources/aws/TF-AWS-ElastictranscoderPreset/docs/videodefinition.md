# TF::AWS::ElastictranscoderPreset VideoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aspectratio" title="AspectRatio">AspectRatio</a>" : <i>String</i>,
    "<a href="#bitrate" title="BitRate">BitRate</a>" : <i>String</i>,
    "<a href="#codec" title="Codec">Codec</a>" : <i>String</i>,
    "<a href="#displayaspectratio" title="DisplayAspectRatio">DisplayAspectRatio</a>" : <i>String</i>,
    "<a href="#fixedgop" title="FixedGop">FixedGop</a>" : <i>String</i>,
    "<a href="#framerate" title="FrameRate">FrameRate</a>" : <i>String</i>,
    "<a href="#keyframesmaxdist" title="KeyframesMaxDist">KeyframesMaxDist</a>" : <i>String</i>,
    "<a href="#maxframerate" title="MaxFrameRate">MaxFrameRate</a>" : <i>String</i>,
    "<a href="#maxheight" title="MaxHeight">MaxHeight</a>" : <i>String</i>,
    "<a href="#maxwidth" title="MaxWidth">MaxWidth</a>" : <i>String</i>,
    "<a href="#paddingpolicy" title="PaddingPolicy">PaddingPolicy</a>" : <i>String</i>,
    "<a href="#resolution" title="Resolution">Resolution</a>" : <i>String</i>,
    "<a href="#sizingpolicy" title="SizingPolicy">SizingPolicy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#aspectratio" title="AspectRatio">AspectRatio</a>: <i>String</i>
<a href="#bitrate" title="BitRate">BitRate</a>: <i>String</i>
<a href="#codec" title="Codec">Codec</a>: <i>String</i>
<a href="#displayaspectratio" title="DisplayAspectRatio">DisplayAspectRatio</a>: <i>String</i>
<a href="#fixedgop" title="FixedGop">FixedGop</a>: <i>String</i>
<a href="#framerate" title="FrameRate">FrameRate</a>: <i>String</i>
<a href="#keyframesmaxdist" title="KeyframesMaxDist">KeyframesMaxDist</a>: <i>String</i>
<a href="#maxframerate" title="MaxFrameRate">MaxFrameRate</a>: <i>String</i>
<a href="#maxheight" title="MaxHeight">MaxHeight</a>: <i>String</i>
<a href="#maxwidth" title="MaxWidth">MaxWidth</a>: <i>String</i>
<a href="#paddingpolicy" title="PaddingPolicy">PaddingPolicy</a>: <i>String</i>
<a href="#resolution" title="Resolution">Resolution</a>: <i>String</i>
<a href="#sizingpolicy" title="SizingPolicy">SizingPolicy</a>: <i>String</i>
</pre>

## Properties

#### AspectRatio

The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BitRate

The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Codec

The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayAspectRatio

The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedGop

Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrameRate

The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyframesMaxDist

The maximum number of frames between key frames. Not applicable for containers of type gif.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxFrameRate

If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHeight

The maximum height of the output video in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 96 and 3072, inclusive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxWidth

The maximum width of the output video in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 128 and 4096, inclusive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaddingPolicy

When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resolution

The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizingPolicy

A value that controls scaling of the output video. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, `ShrinkToFill`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

