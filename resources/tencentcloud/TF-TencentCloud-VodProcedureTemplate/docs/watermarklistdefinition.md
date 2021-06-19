# TF::TencentCloud::VodProcedureTemplate WatermarkListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#definition" title="Definition">Definition</a>" : <i>String</i>,
    "<a href="#endtimeoffset" title="EndTimeOffset">EndTimeOffset</a>" : <i>Double</i>,
    "<a href="#starttimeoffset" title="StartTimeOffset">StartTimeOffset</a>" : <i>Double</i>,
    "<a href="#svgcontent" title="SvgContent">SvgContent</a>" : <i>String</i>,
    "<a href="#textcontent" title="TextContent">TextContent</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#definition" title="Definition">Definition</a>: <i>String</i>
<a href="#endtimeoffset" title="EndTimeOffset">EndTimeOffset</a>: <i>Double</i>
<a href="#starttimeoffset" title="StartTimeOffset">StartTimeOffset</a>: <i>Double</i>
<a href="#svgcontent" title="SvgContent">SvgContent</a>: <i>String</i>
<a href="#textcontent" title="TextContent">TextContent</a>: <i>String</i>
</pre>

## Properties

#### Definition

Watermarking template ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTimeOffset

End time offset of a watermark in seconds. If this parameter is left blank or `0` is entered, the watermark will exist till the last video frame; If this value is greater than `0` (e.g., n), the watermark will exist till second n; If this value is smaller than `0` (e.g., -n), the watermark will exist till second n before the last video frame.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTimeOffset

Start time offset of a watermark in seconds. If this parameter is left blank or `0` is entered, the watermark will appear upon the first video frame. If this parameter is left blank or `0` is entered, the watermark will appear upon the first video frame; If this value is greater than `0` (e.g., n), the watermark will appear at second n after the first video frame; If this value is smaller than `0` (e.g., -n), the watermark will appear at second n before the last video frame.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvgContent

SVG content of up to `2000000` characters. This needs to be entered only when the watermark type is `SVG`. Note: this field may return null, indicating that no valid values can be obtained.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextContent

Text content of up to `100` characters. This needs to be entered only when the watermark type is text. Note: this field may return null, indicating that no valid values can be obtained.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

