# TF::AzureRM::Eventhub CaptureDescriptionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#encoding" title="Encoding">Encoding</a>" : <i>String</i>,
    "<a href="#intervalinseconds" title="IntervalInSeconds">IntervalInSeconds</a>" : <i>Double</i>,
    "<a href="#sizelimitinbytes" title="SizeLimitInBytes">SizeLimitInBytes</a>" : <i>Double</i>,
    "<a href="#skipemptyarchives" title="SkipEmptyArchives">SkipEmptyArchives</a>" : <i>Boolean</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destinationdefinition.md">DestinationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#encoding" title="Encoding">Encoding</a>: <i>String</i>
<a href="#intervalinseconds" title="IntervalInSeconds">IntervalInSeconds</a>: <i>Double</i>
<a href="#sizelimitinbytes" title="SizeLimitInBytes">SizeLimitInBytes</a>: <i>Double</i>
<a href="#skipemptyarchives" title="SkipEmptyArchives">SkipEmptyArchives</a>: <i>Boolean</i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destinationdefinition.md">DestinationDefinition</a></i>
</pre>

## Properties

#### Enabled

Specifies if the Capture Description is Enabled.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encoding

Specifies the Encoding used for the Capture Description. Possible values are `Avro` and `AvroDeflate`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalInSeconds

Specifies the time interval in seconds at which the capture will happen. Values can be between `60` and `900` seconds. Defaults to `300` seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeLimitInBytes

Specifies the amount of data built up in your EventHub before a Capture Operation occurs. Value should be between `10485760` and `524288000`  bytes. Defaults to `314572800` bytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipEmptyArchives

Specifies if empty files should not be emitted if no events occur during the Capture time window.  Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destinationdefinition.md">DestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

