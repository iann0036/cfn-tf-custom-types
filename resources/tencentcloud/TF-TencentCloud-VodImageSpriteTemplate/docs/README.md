# TF::TencentCloud::VodImageSpriteTemplate

Provide a resource to create a VOD image sprite template.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::VodImageSpriteTemplate",
    "Properties" : {
        "<a href="#columncount" title="ColumnCount">ColumnCount</a>" : <i>Double</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#filltype" title="FillType">FillType</a>" : <i>String</i>,
        "<a href="#height" title="Height">Height</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resolutionadaptive" title="ResolutionAdaptive">ResolutionAdaptive</a>" : <i>Boolean</i>,
        "<a href="#rowcount" title="RowCount">RowCount</a>" : <i>Double</i>,
        "<a href="#sampleinterval" title="SampleInterval">SampleInterval</a>" : <i>Double</i>,
        "<a href="#sampletype" title="SampleType">SampleType</a>" : <i>String</i>,
        "<a href="#subappid" title="SubAppId">SubAppId</a>" : <i>Double</i>,
        "<a href="#width" title="Width">Width</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::VodImageSpriteTemplate
Properties:
    <a href="#columncount" title="ColumnCount">ColumnCount</a>: <i>Double</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#filltype" title="FillType">FillType</a>: <i>String</i>
    <a href="#height" title="Height">Height</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resolutionadaptive" title="ResolutionAdaptive">ResolutionAdaptive</a>: <i>Boolean</i>
    <a href="#rowcount" title="RowCount">RowCount</a>: <i>Double</i>
    <a href="#sampleinterval" title="SampleInterval">SampleInterval</a>: <i>Double</i>
    <a href="#sampletype" title="SampleType">SampleType</a>: <i>String</i>
    <a href="#subappid" title="SubAppId">SubAppId</a>: <i>Double</i>
    <a href="#width" title="Width">Width</a>: <i>Double</i>
</pre>

## Properties

#### ColumnCount

Subimage column count of an image sprite.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Template description. Length limit: 256 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FillType

Fill refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported: `stretch`: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot shorter or longer; `black`: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks. Default value: `black`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Height

Maximum value of the `height` (or short side) of a screenshot in px. Value range: 0 and [128, 4,096]. If both `width` and `height` are `0`, the resolution will be the same as that of the source video; If `width` is `0`, but `height` is not `0`, `width` will be proportionally scaled; If `width` is not `0`, but `height` is `0`, `height` will be proportionally scaled; If both `width` and `height` are not `0`, the custom resolution will be used. Default value: `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of a time point screen capturing template. Length limit: 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolutionAdaptive

Resolution adaption. Valid values: `true`,`false`. `true`: enabled. In this case, `width` represents the long side of a video, while `height` the short side; `false`: disabled. In this case, `width` represents the width of a video, while `height` the height. Default value: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RowCount

Subimage row count of an image sprite.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleInterval

Sampling interval. If `sample_type` is `Percent`, sampling will be performed at an interval of the specified percentage. If `sample_type` is `Time`, sampling will be performed at the specified time interval in seconds.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleType

Sampling type. Valid values: `Percent`, `Time`. `Percent`: by percent. `Time`: by time interval.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubAppId

Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Width

Maximum value of the `width` (or long side) of a screenshot in px. Value range: 0 and [128, 4,096]. If both `width` and `height` are `0`, the resolution will be the same as that of the source video; If `width` is `0`, but `height` is not `0`, width will be proportionally scaled; If `width` is not `0`, but `height` is `0`, `height` will be proportionally scaled; If both `width` and `height` are not `0`, the custom resolution will be used. Default value: `0`.

_Required_: No

_Type_: Double

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

