# TF::Volterra::HttpLoadbalancer CompressionParamsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contentlength" title="ContentLength">ContentLength</a>" : <i>Double</i>,
    "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>[ String, ... ]</i>,
    "<a href="#disableonetagheader" title="DisableOnEtagHeader">DisableOnEtagHeader</a>" : <i>Boolean</i>,
    "<a href="#removeacceptencodingheader" title="RemoveAcceptEncodingHeader">RemoveAcceptEncodingHeader</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#contentlength" title="ContentLength">ContentLength</a>: <i>Double</i>
<a href="#contenttype" title="ContentType">ContentType</a>: <i>
      - String</i>
<a href="#disableonetagheader" title="DisableOnEtagHeader">DisableOnEtagHeader</a>: <i>Boolean</i>
<a href="#removeacceptencodingheader" title="RemoveAcceptEncodingHeader">RemoveAcceptEncodingHeader</a>: <i>Boolean</i>
</pre>

## Properties

#### ContentLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableOnEtagHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveAcceptEncodingHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

