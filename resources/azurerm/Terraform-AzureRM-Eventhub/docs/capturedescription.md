# Terraform::AzureRM::Eventhub CaptureDescription

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
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="capturedescription-destination.md">Destination</a>, ... ]</i>
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
      - <a href="capturedescription-destination.md">Destination</a></i>
</pre>

## Properties

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encoding

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeLimitInBytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipEmptyArchives

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="capturedescription-destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

