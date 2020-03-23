# Terraform::AWS::ElastictranscoderPreset Thumbnails

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aspectratio" title="AspectRatio">AspectRatio</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>String</i>,
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
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#interval" title="Interval">Interval</a>: <i>String</i>
<a href="#maxheight" title="MaxHeight">MaxHeight</a>: <i>String</i>
<a href="#maxwidth" title="MaxWidth">MaxWidth</a>: <i>String</i>
<a href="#paddingpolicy" title="PaddingPolicy">PaddingPolicy</a>: <i>String</i>
<a href="#resolution" title="Resolution">Resolution</a>: <i>String</i>
<a href="#sizingpolicy" title="SizingPolicy">SizingPolicy</a>: <i>String</i>
</pre>

## Properties

#### AspectRatio

The aspect ratio of thumbnails. The following values are valid: auto, 1:1, 4:3, 3:2, 16:9.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

The format of thumbnails, if any. Valid formats are jpg and png.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHeight

The maximum height of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxWidth

The maximum width of thumbnails, in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaddingPolicy

When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of thumbnails to make the total size of the thumbnails match the values that you specified for thumbnail MaxWidth and MaxHeight settings.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resolution

The width and height of thumbnail files in pixels, in the format WidthxHeight, where both values are even integers. The values cannot exceed the width and height that you specified in the Video:Resolution object. (To better control resolution and aspect ratio of thumbnails, we recommend that you use the thumbnail values `max_width`, `max_height`, `sizing_policy`, and `padding_policy` instead of `resolution` and `aspect_ratio`. The two groups of settings are mutually exclusive. Do not use them together).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizingPolicy

A value that controls scaling of thumbnails. Valid values are: `Fit`, `Fill`, `Stretch`, `Keep`, `ShrinkToFit`, and `ShrinkToFill`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

