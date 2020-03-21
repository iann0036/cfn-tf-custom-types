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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#videocodecoptions" title="VideoCodecOptions">VideoCodecOptions</a>" : <i>[ &lt;a href=&#34;videocodecoptions.md&#34;&gt;VideoCodecOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#audio" title="Audio">Audio</a>" : <i>[ &lt;a href=&#34;audio.md&#34;&gt;Audio&lt;/a&gt;, ... ]</i>,
        "<a href="#audiocodecoptions" title="AudioCodecOptions">AudioCodecOptions</a>" : <i>[ &lt;a href=&#34;audiocodecoptions.md&#34;&gt;AudioCodecOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#thumbnails" title="Thumbnails">Thumbnails</a>" : <i>[ &lt;a href=&#34;thumbnails.md&#34;&gt;Thumbnails&lt;/a&gt;, ... ]</i>,
        "<a href="#video" title="Video">Video</a>" : <i>[ &lt;a href=&#34;video.md&#34;&gt;Video&lt;/a&gt;, ... ]</i>,
        "<a href="#videowatermarks" title="VideoWatermarks">VideoWatermarks</a>" : <i>[ &lt;a href=&#34;videowatermarks.md&#34;&gt;VideoWatermarks&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ElastictranscoderPreset
Properties:
    <a href="#container" title="Container">Container</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#videocodecoptions" title="VideoCodecOptions">VideoCodecOptions</a>: <i>
      - &lt;a href=&#34;videocodecoptions.md&#34;&gt;VideoCodecOptions&lt;/a&gt;</i>
    <a href="#audio" title="Audio">Audio</a>: <i>
      - &lt;a href=&#34;audio.md&#34;&gt;Audio&lt;/a&gt;</i>
    <a href="#audiocodecoptions" title="AudioCodecOptions">AudioCodecOptions</a>: <i>
      - &lt;a href=&#34;audiocodecoptions.md&#34;&gt;AudioCodecOptions&lt;/a&gt;</i>
    <a href="#thumbnails" title="Thumbnails">Thumbnails</a>: <i>
      - &lt;a href=&#34;thumbnails.md&#34;&gt;Thumbnails&lt;/a&gt;</i>
    <a href="#video" title="Video">Video</a>: <i>
      - &lt;a href=&#34;video.md&#34;&gt;Video&lt;/a&gt;</i>
    <a href="#videowatermarks" title="VideoWatermarks">VideoWatermarks</a>: <i>
      - &lt;a href=&#34;videowatermarks.md&#34;&gt;VideoWatermarks&lt;/a&gt;</i>
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

#### Id

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

_Type_: List of &lt;a href=&#34;videocodecoptions.md&#34;&gt;VideoCodecOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Audio

_Required_: No

_Type_: List of &lt;a href=&#34;audio.md&#34;&gt;Audio&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AudioCodecOptions

_Required_: No

_Type_: List of &lt;a href=&#34;audiocodecoptions.md&#34;&gt;AudioCodecOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thumbnails

_Required_: No

_Type_: List of &lt;a href=&#34;thumbnails.md&#34;&gt;Thumbnails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Video

_Required_: No

_Type_: List of &lt;a href=&#34;video.md&#34;&gt;Video&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoWatermarks

_Required_: No

_Type_: List of &lt;a href=&#34;videowatermarks.md&#34;&gt;VideoWatermarks&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

