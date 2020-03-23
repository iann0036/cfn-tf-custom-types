# Terraform::AWS::ElastictranscoderPreset Audio

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#audiopackingmode" title="AudioPackingMode">AudioPackingMode</a>" : <i>String</i>,
    "<a href="#bitrate" title="BitRate">BitRate</a>" : <i>String</i>,
    "<a href="#channels" title="Channels">Channels</a>" : <i>String</i>,
    "<a href="#codec" title="Codec">Codec</a>" : <i>String</i>,
    "<a href="#samplerate" title="SampleRate">SampleRate</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#audiopackingmode" title="AudioPackingMode">AudioPackingMode</a>: <i>String</i>
<a href="#bitrate" title="BitRate">BitRate</a>: <i>String</i>
<a href="#channels" title="Channels">Channels</a>: <i>String</i>
<a href="#codec" title="Codec">Codec</a>: <i>String</i>
<a href="#samplerate" title="SampleRate">SampleRate</a>: <i>String</i>
</pre>

## Properties

#### AudioPackingMode

The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BitRate

The bit rate of the audio stream in the output file, in kilobits/second. Enter an integer between 64 and 320, inclusive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Channels

The number of audio channels in the output file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Codec

The audio codec for the output file. Valid values are `AAC`, `flac`, `mp2`, `mp3`, `pcm`, and `vorbis`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleRate

The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

