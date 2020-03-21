# Terraform::AWS::DynamodbTable

CloudFormation equivalent of aws_dynamodb_table

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DynamodbTable",
    "Properties" : {
        "<a href="#billingmode" title="BillingMode">BillingMode</a>" : <i>String</i>,
        "<a href="#hashkey" title="HashKey">HashKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rangekey" title="RangeKey">RangeKey</a>" : <i>String</i>,
        "<a href="#readcapacity" title="ReadCapacity">ReadCapacity</a>" : <i>Double</i>,
        "<a href="#streamenabled" title="StreamEnabled">StreamEnabled</a>" : <i>Boolean</i>,
        "<a href="#streamviewtype" title="StreamViewType">StreamViewType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#writecapacity" title="WriteCapacity">WriteCapacity</a>" : <i>Double</i>,
        "<a href="#attribute" title="Attribute">Attribute</a>" : <i>[ <a href="attribute.md">Attribute</a>, ... ]</i>,
        "<a href="#globalsecondaryindex" title="GlobalSecondaryIndex">GlobalSecondaryIndex</a>" : <i>[ <a href="globalsecondaryindex.md">GlobalSecondaryIndex</a>, ... ]</i>,
        "<a href="#localsecondaryindex" title="LocalSecondaryIndex">LocalSecondaryIndex</a>" : <i>[ <a href="localsecondaryindex.md">LocalSecondaryIndex</a>, ... ]</i>,
        "<a href="#pointintimerecovery" title="PointInTimeRecovery">PointInTimeRecovery</a>" : <i>[ <a href="pointintimerecovery.md">PointInTimeRecovery</a>, ... ]</i>,
        "<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>" : <i>[ <a href="serversideencryption.md">ServerSideEncryption</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>[ <a href="ttl.md">Ttl</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DynamodbTable
Properties:
    <a href="#billingmode" title="BillingMode">BillingMode</a>: <i>String</i>
    <a href="#hashkey" title="HashKey">HashKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rangekey" title="RangeKey">RangeKey</a>: <i>String</i>
    <a href="#readcapacity" title="ReadCapacity">ReadCapacity</a>: <i>Double</i>
    <a href="#streamenabled" title="StreamEnabled">StreamEnabled</a>: <i>Boolean</i>
    <a href="#streamviewtype" title="StreamViewType">StreamViewType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#writecapacity" title="WriteCapacity">WriteCapacity</a>: <i>Double</i>
    <a href="#attribute" title="Attribute">Attribute</a>: <i>
      - <a href="attribute.md">Attribute</a></i>
    <a href="#globalsecondaryindex" title="GlobalSecondaryIndex">GlobalSecondaryIndex</a>: <i>
      - <a href="globalsecondaryindex.md">GlobalSecondaryIndex</a></i>
    <a href="#localsecondaryindex" title="LocalSecondaryIndex">LocalSecondaryIndex</a>: <i>
      - <a href="localsecondaryindex.md">LocalSecondaryIndex</a></i>
    <a href="#pointintimerecovery" title="PointInTimeRecovery">PointInTimeRecovery</a>: <i>
      - <a href="pointintimerecovery.md">PointInTimeRecovery</a></i>
    <a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>: <i>
      - <a href="serversideencryption.md">ServerSideEncryption</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>
      - <a href="ttl.md">Ttl</a></i>
</pre>

## Properties

#### BillingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

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

#### StreamEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamViewType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attribute

_Required_: No

_Type_: List of <a href="attribute.md">Attribute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalSecondaryIndex

_Required_: No

_Type_: List of <a href="globalsecondaryindex.md">GlobalSecondaryIndex</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSecondaryIndex

_Required_: No

_Type_: List of <a href="localsecondaryindex.md">LocalSecondaryIndex</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PointInTimeRecovery

_Required_: No

_Type_: List of <a href="pointintimerecovery.md">PointInTimeRecovery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryption

_Required_: No

_Type_: List of <a href="serversideencryption.md">ServerSideEncryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: List of <a href="ttl.md">Ttl</a>

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

#### StreamArn

Returns the <code>StreamArn</code> value.

#### StreamLabel

Returns the <code>StreamLabel</code> value.

