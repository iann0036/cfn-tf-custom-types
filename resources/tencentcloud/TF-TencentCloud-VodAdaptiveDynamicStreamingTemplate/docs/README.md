# TF::TencentCloud::VodAdaptiveDynamicStreamingTemplate

Provide a resource to create a VOD adaptive dynamic streaming template.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::VodAdaptiveDynamicStreamingTemplate",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#disablehighervideobitrate" title="DisableHigherVideoBitrate">DisableHigherVideoBitrate</a>" : <i>Boolean</i>,
        "<a href="#disablehighervideoresolution" title="DisableHigherVideoResolution">DisableHigherVideoResolution</a>" : <i>Boolean</i>,
        "<a href="#drmtype" title="DrmType">DrmType</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#subappid" title="SubAppId">SubAppId</a>" : <i>Double</i>,
        "<a href="#streaminfo" title="StreamInfo">StreamInfo</a>" : <i>[ <a href="streaminfodefinition.md">StreamInfoDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::VodAdaptiveDynamicStreamingTemplate
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#disablehighervideobitrate" title="DisableHigherVideoBitrate">DisableHigherVideoBitrate</a>: <i>Boolean</i>
    <a href="#disablehighervideoresolution" title="DisableHigherVideoResolution">DisableHigherVideoResolution</a>: <i>Boolean</i>
    <a href="#drmtype" title="DrmType">DrmType</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#subappid" title="SubAppId">SubAppId</a>: <i>Double</i>
    <a href="#streaminfo" title="StreamInfo">StreamInfo</a>: <i>
      - <a href="streaminfodefinition.md">StreamInfoDefinition</a></i>
</pre>

## Properties

#### Comment

Template description. Length limit: 256 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableHigherVideoBitrate

Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableHigherVideoResolution

Whether to prohibit transcoding from low resolution to high resolution. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrmType

DRM scheme type. Valid values: `SimpleAES`. If this field is an empty string, DRM will not be performed on the video.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Adaptive bitstream format. Valid values: `HLS`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Template name. Length limit: 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubAppId

Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamInfo

_Required_: No

_Type_: List of <a href="streaminfodefinition.md">StreamInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

