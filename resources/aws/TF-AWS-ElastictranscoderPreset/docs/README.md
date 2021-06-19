# TF::AWS::ElastictranscoderPreset

Provides an Elastic Transcoder preset resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ElastictranscoderPreset",
    "Properties" : {
        "<a href="#container" title="Container">Container</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#videocodecoptions" title="VideoCodecOptions">VideoCodecOptions</a>" : <i>[ <a href="videocodecoptionsdefinition.md">VideoCodecOptionsDefinition</a>, ... ]</i>,
        "<a href="#audio" title="Audio">Audio</a>" : <i>[ <a href="audiodefinition.md">AudioDefinition</a>, ... ]</i>,
        "<a href="#audiocodecoptions" title="AudioCodecOptions">AudioCodecOptions</a>" : <i>[ <a href="audiocodecoptionsdefinition.md">AudioCodecOptionsDefinition</a>, ... ]</i>,
        "<a href="#thumbnails" title="Thumbnails">Thumbnails</a>" : <i>[ <a href="thumbnailsdefinition.md">ThumbnailsDefinition</a>, ... ]</i>,
        "<a href="#video" title="Video">Video</a>" : <i>[ <a href="videodefinition.md">VideoDefinition</a>, ... ]</i>,
        "<a href="#videowatermarks" title="VideoWatermarks">VideoWatermarks</a>" : <i>[ <a href="videowatermarksdefinition.md">VideoWatermarksDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ElastictranscoderPreset
Properties:
    <a href="#container" title="Container">Container</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#videocodecoptions" title="VideoCodecOptions">VideoCodecOptions</a>: <i>
      - <a href="videocodecoptionsdefinition.md">VideoCodecOptionsDefinition</a></i>
    <a href="#audio" title="Audio">Audio</a>: <i>
      - <a href="audiodefinition.md">AudioDefinition</a></i>
    <a href="#audiocodecoptions" title="AudioCodecOptions">AudioCodecOptions</a>: <i>
      - <a href="audiocodecoptionsdefinition.md">AudioCodecOptionsDefinition</a></i>
    <a href="#thumbnails" title="Thumbnails">Thumbnails</a>: <i>
      - <a href="thumbnailsdefinition.md">ThumbnailsDefinition</a></i>
    <a href="#video" title="Video">Video</a>: <i>
      - <a href="videodefinition.md">VideoDefinition</a></i>
    <a href="#videowatermarks" title="VideoWatermarks">VideoWatermarks</a>: <i>
      - <a href="videowatermarksdefinition.md">VideoWatermarksDefinition</a></i>
</pre>

## Properties

#### Container

The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the preset (maximum 255 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the preset. (maximum 40 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoCodecOptions

_Required_: No

_Type_: List of <a href="videocodecoptionsdefinition.md">VideoCodecOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Audio

_Required_: No

_Type_: List of <a href="audiodefinition.md">AudioDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AudioCodecOptions

_Required_: No

_Type_: List of <a href="audiocodecoptionsdefinition.md">AudioCodecOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thumbnails

_Required_: No

_Type_: List of <a href="thumbnailsdefinition.md">ThumbnailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Video

_Required_: No

_Type_: List of <a href="videodefinition.md">VideoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoWatermarks

_Required_: No

_Type_: List of <a href="videowatermarksdefinition.md">VideoWatermarksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

