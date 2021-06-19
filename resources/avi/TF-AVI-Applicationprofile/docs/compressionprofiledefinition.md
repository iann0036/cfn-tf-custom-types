# TF::AVI::Applicationprofile CompressionProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#compressiblecontentref" title="CompressibleContentRef">CompressibleContentRef</a>" : <i>String</i>,
    "<a href="#compression" title="Compression">Compression</a>" : <i>Boolean</i>,
    "<a href="#removeacceptencodingheader" title="RemoveAcceptEncodingHeader">RemoveAcceptEncodingHeader</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#compressiblecontentref" title="CompressibleContentRef">CompressibleContentRef</a>: <i>String</i>
<a href="#compression" title="Compression">Compression</a>: <i>Boolean</i>
<a href="#removeacceptencodingheader" title="RemoveAcceptEncodingHeader">RemoveAcceptEncodingHeader</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
</pre>

## Properties

#### CompressibleContentRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compression

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveAcceptEncodingHeader

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

