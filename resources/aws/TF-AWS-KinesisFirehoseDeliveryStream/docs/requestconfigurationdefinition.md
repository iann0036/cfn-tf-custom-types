# TF::AWS::KinesisFirehoseDeliveryStream RequestConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>" : <i>String</i>,
    "<a href="#commonattributes" title="CommonAttributes">CommonAttributes</a>" : <i>[ <a href="commonattributesdefinition.md">CommonAttributesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>: <i>String</i>
<a href="#commonattributes" title="CommonAttributes">CommonAttributes</a>: <i>
      - <a href="commonattributesdefinition.md">CommonAttributesDefinition</a></i>
</pre>

## Properties

#### ContentEncoding

Kinesis Data Firehose uses the content encoding to compress the body of a request before sending the request to the destination. Valid values are `NONE` and `GZIP`.  Default value is `NONE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonAttributes

_Required_: No

_Type_: List of <a href="commonattributesdefinition.md">CommonAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

