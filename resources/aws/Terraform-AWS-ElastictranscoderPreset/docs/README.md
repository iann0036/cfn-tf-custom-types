# Terraform::AWS::ElastictranscoderPreset

CloudFormation equivalent of aws_elastictranscoder_preset

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ElastictranscoderPreset",
    "Properties" : {
        "<a href="#container" title="Container">Container</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#videocodecoptions" title="VideoCodecOptions">VideoCodecOptions</a>" : <i>[ <a href="videocodecoptions.md">VideoCodecOptions</a>, ... ]</i>,
        "<a href="#audio" title="Audio">Audio</a>" : <i>[ <a href="audio.md">Audio</a>, ... ]</i>,
        "<a href="#audiocodecoptions" title="AudioCodecOptions">AudioCodecOptions</a>" : <i>[ <a href="audiocodecoptions.md">AudioCodecOptions</a>, ... ]</i>,
        "<a href="#thumbnails" title="Thumbnails">Thumbnails</a>" : <i>[ <a href="thumbnails.md">Thumbnails</a>, ... ]</i>,
        "<a href="#video" title="Video">Video</a>" : <i>[ <a href="video.md">Video</a>, ... ]</i>,
        "<a href="#videowatermarks" title="VideoWatermarks">VideoWatermarks</a>" : <i>[ <a href="videowatermarks.md">VideoWatermarks</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ElastictranscoderPreset
Properties:
    <a href="#container" title="Container">Container</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#videocodecoptions" title="VideoCodecOptions">VideoCodecOptions</a>: <i>
      - <a href="videocodecoptions.md">VideoCodecOptions</a></i>
    <a href="#audio" title="Audio">Audio</a>: <i>
      - <a href="audio.md">Audio</a></i>
    <a href="#audiocodecoptions" title="AudioCodecOptions">AudioCodecOptions</a>: <i>
      - <a href="audiocodecoptions.md">AudioCodecOptions</a></i>
    <a href="#thumbnails" title="Thumbnails">Thumbnails</a>: <i>
      - <a href="thumbnails.md">Thumbnails</a></i>
    <a href="#video" title="Video">Video</a>: <i>
      - <a href="video.md">Video</a></i>
    <a href="#videowatermarks" title="VideoWatermarks">VideoWatermarks</a>: <i>
      - <a href="videowatermarks.md">VideoWatermarks</a></i>
</pre>

## Properties

#### Container

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoCodecOptions

_Required_: No

_Type_: List of <a href="videocodecoptions.md">VideoCodecOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Audio

_Required_: No

_Type_: List of <a href="audio.md">Audio</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AudioCodecOptions

_Required_: No

_Type_: List of <a href="audiocodecoptions.md">AudioCodecOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thumbnails

_Required_: No

_Type_: List of <a href="thumbnails.md">Thumbnails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Video

_Required_: No

_Type_: List of <a href="video.md">Video</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoWatermarks

_Required_: No

_Type_: List of <a href="videowatermarks.md">VideoWatermarks</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

