# Terraform::AWS::DynamodbTable

CloudFormation equivalent of aws_dynamodb_table

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DynamodbTable",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#billingmode" title="BillingMode">BillingMode</a>" : <i>String</i>,
        "<a href="#hashkey" title="HashKey">HashKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rangekey" title="RangeKey">RangeKey</a>" : <i>String</i>,
        "<a href="#readcapacity" title="ReadCapacity">ReadCapacity</a>" : <i>Double</i>,
        "<a href="#streamarn" title="StreamArn">StreamArn</a>" : <i>String</i>,
        "<a href="#streamenabled" title="StreamEnabled">StreamEnabled</a>" : <i>Boolean</i>,
        "<a href="#streamlabel" title="StreamLabel">StreamLabel</a>" : <i>String</i>,
        "<a href="#streamviewtype" title="StreamViewType">StreamViewType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#writecapacity" title="WriteCapacity">WriteCapacity</a>" : <i>Double</i>,
        "<a href="#attribute" title="Attribute">Attribute</a>" : <i>[ &lt;a href=&#34;attribute.md&#34;&gt;Attribute&lt;/a&gt;, ... ]</i>,
        "<a href="#globalsecondaryindex" title="GlobalSecondaryIndex">GlobalSecondaryIndex</a>" : <i>[ &lt;a href=&#34;globalsecondaryindex.md&#34;&gt;GlobalSecondaryIndex&lt;/a&gt;, ... ]</i>,
        "<a href="#localsecondaryindex" title="LocalSecondaryIndex">LocalSecondaryIndex</a>" : <i>[ &lt;a href=&#34;localsecondaryindex.md&#34;&gt;LocalSecondaryIndex&lt;/a&gt;, ... ]</i>,
        "<a href="#pointintimerecovery" title="PointInTimeRecovery">PointInTimeRecovery</a>" : <i>[ &lt;a href=&#34;pointintimerecovery.md&#34;&gt;PointInTimeRecovery&lt;/a&gt;, ... ]</i>,
        "<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>" : <i>[ &lt;a href=&#34;serversideencryption.md&#34;&gt;ServerSideEncryption&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>[ &lt;a href=&#34;ttl.md&#34;&gt;Ttl&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DynamodbTable
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#billingmode" title="BillingMode">BillingMode</a>: <i>String</i>
    <a href="#hashkey" title="HashKey">HashKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rangekey" title="RangeKey">RangeKey</a>: <i>String</i>
    <a href="#readcapacity" title="ReadCapacity">ReadCapacity</a>: <i>Double</i>
    <a href="#streamarn" title="StreamArn">StreamArn</a>: <i>String</i>
    <a href="#streamenabled" title="StreamEnabled">StreamEnabled</a>: <i>Boolean</i>
    <a href="#streamlabel" title="StreamLabel">StreamLabel</a>: <i>String</i>
    <a href="#streamviewtype" title="StreamViewType">StreamViewType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#writecapacity" title="WriteCapacity">WriteCapacity</a>: <i>Double</i>
    <a href="#attribute" title="Attribute">Attribute</a>: <i>
      - &lt;a href=&#34;attribute.md&#34;&gt;Attribute&lt;/a&gt;</i>
    <a href="#globalsecondaryindex" title="GlobalSecondaryIndex">GlobalSecondaryIndex</a>: <i>
      - &lt;a href=&#34;globalsecondaryindex.md&#34;&gt;GlobalSecondaryIndex&lt;/a&gt;</i>
    <a href="#localsecondaryindex" title="LocalSecondaryIndex">LocalSecondaryIndex</a>: <i>
      - &lt;a href=&#34;localsecondaryindex.md&#34;&gt;LocalSecondaryIndex&lt;/a&gt;</i>
    <a href="#pointintimerecovery" title="PointInTimeRecovery">PointInTimeRecovery</a>: <i>
      - &lt;a href=&#34;pointintimerecovery.md&#34;&gt;PointInTimeRecovery&lt;/a&gt;</i>
    <a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>: <i>
      - &lt;a href=&#34;serversideencryption.md&#34;&gt;ServerSideEncryption&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>
      - &lt;a href=&#34;ttl.md&#34;&gt;Ttl&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### StreamArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamViewType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attribute

_Required_: No

_Type_: List of &lt;a href=&#34;attribute.md&#34;&gt;Attribute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalSecondaryIndex

_Required_: No

_Type_: List of &lt;a href=&#34;globalsecondaryindex.md&#34;&gt;GlobalSecondaryIndex&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSecondaryIndex

_Required_: No

_Type_: List of &lt;a href=&#34;localsecondaryindex.md&#34;&gt;LocalSecondaryIndex&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PointInTimeRecovery

_Required_: No

_Type_: List of &lt;a href=&#34;pointintimerecovery.md&#34;&gt;PointInTimeRecovery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryption

_Required_: No

_Type_: List of &lt;a href=&#34;serversideencryption.md&#34;&gt;ServerSideEncryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: List of &lt;a href=&#34;ttl.md&#34;&gt;Ttl&lt;/a&gt;

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

#### StreamArn

Returns the &lt;code&gt;StreamArn&lt;/code&gt; value.

#### StreamLabel

Returns the &lt;code&gt;StreamLabel&lt;/code&gt; value.

