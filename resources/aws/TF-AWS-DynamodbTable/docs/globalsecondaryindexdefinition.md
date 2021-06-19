# TF::AWS::DynamodbTable GlobalSecondaryIndexDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hashkey" title="HashKey">HashKey</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nonkeyattributes" title="NonKeyAttributes">NonKeyAttributes</a>" : <i>[ String, ... ]</i>,
    "<a href="#projectiontype" title="ProjectionType">ProjectionType</a>" : <i>String</i>,
    "<a href="#rangekey" title="RangeKey">RangeKey</a>" : <i>String</i>,
    "<a href="#readcapacity" title="ReadCapacity">ReadCapacity</a>" : <i>Double</i>,
    "<a href="#writecapacity" title="WriteCapacity">WriteCapacity</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#hashkey" title="HashKey">HashKey</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nonkeyattributes" title="NonKeyAttributes">NonKeyAttributes</a>: <i>
      - String</i>
<a href="#projectiontype" title="ProjectionType">ProjectionType</a>: <i>String</i>
<a href="#rangekey" title="RangeKey">RangeKey</a>: <i>String</i>
<a href="#readcapacity" title="ReadCapacity">ReadCapacity</a>: <i>Double</i>
<a href="#writecapacity" title="WriteCapacity">WriteCapacity</a>: <i>Double</i>
</pre>

## Properties

#### HashKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NonKeyAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectionType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

