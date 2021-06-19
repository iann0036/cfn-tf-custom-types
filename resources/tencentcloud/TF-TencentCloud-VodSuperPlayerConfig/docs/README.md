# TF::TencentCloud::VodSuperPlayerConfig

Provide a resource to create a VOD super player config.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::VodSuperPlayerConfig",
    "Properties" : {
        "<a href="#adaptivedynamicstreamingdefinition" title="AdaptiveDynamicStreamingDefinition">AdaptiveDynamicStreamingDefinition</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#drmswitch" title="DrmSwitch">DrmSwitch</a>" : <i>Boolean</i>,
        "<a href="#imagespritedefinition" title="ImageSpriteDefinition">ImageSpriteDefinition</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#scheme" title="Scheme">Scheme</a>" : <i>String</i>,
        "<a href="#subappid" title="SubAppId">SubAppId</a>" : <i>Double</i>,
        "<a href="#drmstreaminginfo" title="DrmStreamingInfo">DrmStreamingInfo</a>" : <i>[ <a href="drmstreaminginfodefinition.md">DrmStreamingInfoDefinition</a>, ... ]</i>,
        "<a href="#resolutionnames" title="ResolutionNames">ResolutionNames</a>" : <i>[ <a href="resolutionnamesdefinition.md">ResolutionNamesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::VodSuperPlayerConfig
Properties:
    <a href="#adaptivedynamicstreamingdefinition" title="AdaptiveDynamicStreamingDefinition">AdaptiveDynamicStreamingDefinition</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#drmswitch" title="DrmSwitch">DrmSwitch</a>: <i>Boolean</i>
    <a href="#imagespritedefinition" title="ImageSpriteDefinition">ImageSpriteDefinition</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#scheme" title="Scheme">Scheme</a>: <i>String</i>
    <a href="#subappid" title="SubAppId">SubAppId</a>: <i>Double</i>
    <a href="#drmstreaminginfo" title="DrmStreamingInfo">DrmStreamingInfo</a>: <i>
      - <a href="drmstreaminginfodefinition.md">DrmStreamingInfoDefinition</a></i>
    <a href="#resolutionnames" title="ResolutionNames">ResolutionNames</a>: <i>
      - <a href="resolutionnamesdefinition.md">ResolutionNamesDefinition</a></i>
</pre>

## Properties

#### AdaptiveDynamicStreamingDefinition

ID of the unencrypted adaptive bitrate streaming template that allows output, which is required if `drm_switch` is `false`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Template description. Length limit: 256 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Domain name used for playback. If it is left empty or set to `Default`, the domain name configured in [Default Distribution Configuration](https://cloud.tencent.com/document/product/266/33373) will be used. `Default` by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrmSwitch

Switch of DRM-protected adaptive bitstream playback: `true`: enabled, indicating to play back only output adaptive bitstreams protected by DRM; `false`: disabled, indicating to play back unencrypted output adaptive bitstreams. Default value: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageSpriteDefinition

ID of the image sprite template that allows output.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Player configuration name, which can contain up to 64 letters, digits, underscores, and hyphens (such as test_ABC-123) and must be unique under a user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheme

Scheme used for playback. If it is left empty or set to `Default`, the scheme configured in [Default Distribution Configuration](https://cloud.tencent.com/document/product/266/33373) will be used. Other valid values: `HTTP`; `HTTPS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubAppId

Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrmStreamingInfo

_Required_: No

_Type_: List of <a href="drmstreaminginfodefinition.md">DrmStreamingInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolutionNames

_Required_: No

_Type_: List of <a href="resolutionnamesdefinition.md">ResolutionNamesDefinition</a>

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

