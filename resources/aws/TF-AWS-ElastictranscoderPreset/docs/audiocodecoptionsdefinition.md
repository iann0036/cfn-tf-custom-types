# TF::AWS::ElastictranscoderPreset AudioCodecOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bitdepth" title="BitDepth">BitDepth</a>" : <i>String</i>,
    "<a href="#bitorder" title="BitOrder">BitOrder</a>" : <i>String</i>,
    "<a href="#profile" title="Profile">Profile</a>" : <i>String</i>,
    "<a href="#signed" title="Signed">Signed</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bitdepth" title="BitDepth">BitDepth</a>: <i>String</i>
<a href="#bitorder" title="BitOrder">BitOrder</a>: <i>String</i>
<a href="#profile" title="Profile">Profile</a>: <i>String</i>
<a href="#signed" title="Signed">Signed</a>: <i>String</i>
</pre>

## Properties

#### BitDepth

The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BitOrder

The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

If you specified AAC for Audio:Codec, choose the AAC profile for the output file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signed

Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

