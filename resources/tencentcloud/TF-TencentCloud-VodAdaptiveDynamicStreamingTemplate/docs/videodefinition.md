# TF::TencentCloud::VodAdaptiveDynamicStreamingTemplate VideoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bitrate" title="Bitrate">Bitrate</a>" : <i>Double</i>,
    "<a href="#codec" title="Codec">Codec</a>" : <i>String</i>,
    "<a href="#filltype" title="FillType">FillType</a>" : <i>String</i>,
    "<a href="#fps" title="Fps">Fps</a>" : <i>Double</i>,
    "<a href="#height" title="Height">Height</a>" : <i>Double</i>,
    "<a href="#resolutionadaptive" title="ResolutionAdaptive">ResolutionAdaptive</a>" : <i>Boolean</i>,
    "<a href="#width" title="Width">Width</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#bitrate" title="Bitrate">Bitrate</a>: <i>Double</i>
<a href="#codec" title="Codec">Codec</a>: <i>String</i>
<a href="#filltype" title="FillType">FillType</a>: <i>String</i>
<a href="#fps" title="Fps">Fps</a>: <i>Double</i>
<a href="#height" title="Height">Height</a>: <i>Double</i>
<a href="#resolutionadaptive" title="ResolutionAdaptive">ResolutionAdaptive</a>: <i>Boolean</i>
<a href="#width" title="Width">Width</a>: <i>Double</i>
</pre>

## Properties

#### Bitrate

Bitrate of video stream in Kbps. Value range: `0` and `[128, 35000]`. If the value is `0`, the bitrate of the video will be the same as that of the source video.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Codec

Video stream encoder. Valid values: `libx264`,`libx265`,`av1`. `libx264`: H.264, `libx265`: H.265, `av1`: AOMedia Video 1. Currently, a resolution within 640x480 must be specified for `H.265`. and the `av1` container only supports mp4.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FillType

Fill type. Fill refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported: `stretch`: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot shorter or longer; `black`: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks. Default value: black. Note: this field may return null, indicating that no valid values can be obtained.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fps

Video frame rate in Hz. Value range: `[0, 60]`. If the value is `0`, the frame rate will be the same as that of the source video.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Height

Maximum value of the height (or short side) of a video stream in px. Value range: `0` and `[128, 4096]`. If both `width` and `height` are `0`, the resolution will be the same as that of the source video; If `width` is `0`, but `height` is not `0`, `width` will be proportionally scaled; If `width` is not `0`, but `height` is `0`, `height` will be proportionally scaled; If both `width` and `height` are not `0`, the custom resolution will be used. Default value: `0`. Note: this field may return null, indicating that no valid values can be obtained.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolutionAdaptive

Resolution adaption. Valid values: `true`,`false`. `true`: enabled. In this case, `width` represents the long side of a video, while `height` the short side; `false`: disabled. In this case, `width` represents the width of a video, while `height` the height. Default value: `true`. Note: this field may return null, indicating that no valid values can be obtained.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Width

Maximum value of the width (or long side) of a video stream in px. Value range: `0` and `[128, 4096]`. If both `width` and `height` are `0`, the resolution will be the same as that of the source video; If `width` is `0`, but `height` is not `0`, `width` will be proportionally scaled; If `width` is not `0`, but `height` is `0`, `height` will be proportionally scaled; If both `width` and `height` are not `0`, the custom resolution will be used. Default value: `0`. Note: this field may return null, indicating that no valid values can be obtained.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

