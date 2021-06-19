# TF::AWS::DynamodbTable

Provides a DynamoDB table resource

~> **Note:** It is recommended to use `lifecycle` [`ignore_changes`](https://www.terraform.io/docs/configuration/meta-arguments/lifecycle.html#ignore_changes) for `read_capacity` and/or `write_capacity` if there's [autoscaling policy](/docs/providers/aws/r/appautoscaling_policy.html) attached to the table.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DynamodbTable",
    "Properties" : {
        "<a href="#billingmode" title="BillingMode">BillingMode</a>" : <i>String</i>,
        "<a href="#hashkey" title="HashKey">HashKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rangekey" title="RangeKey">RangeKey</a>" : <i>String</i>,
        "<a href="#readcapacity" title="ReadCapacity">ReadCapacity</a>" : <i>Double</i>,
        "<a href="#streamenabled" title="StreamEnabled">StreamEnabled</a>" : <i>Boolean</i>,
        "<a href="#streamviewtype" title="StreamViewType">StreamViewType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#writecapacity" title="WriteCapacity">WriteCapacity</a>" : <i>Double</i>,
        "<a href="#attribute" title="Attribute">Attribute</a>" : <i>[ <a href="attributedefinition.md">AttributeDefinition</a>, ... ]</i>,
        "<a href="#globalsecondaryindex" title="GlobalSecondaryIndex">GlobalSecondaryIndex</a>" : <i>[ <a href="globalsecondaryindexdefinition.md">GlobalSecondaryIndexDefinition</a>, ... ]</i>,
        "<a href="#localsecondaryindex" title="LocalSecondaryIndex">LocalSecondaryIndex</a>" : <i>[ <a href="localsecondaryindexdefinition.md">LocalSecondaryIndexDefinition</a>, ... ]</i>,
        "<a href="#pointintimerecovery" title="PointInTimeRecovery">PointInTimeRecovery</a>" : <i>[ <a href="pointintimerecoverydefinition.md">PointInTimeRecoveryDefinition</a>, ... ]</i>,
        "<a href="#replica" title="Replica">Replica</a>" : <i>[ <a href="replicadefinition.md">ReplicaDefinition</a>, ... ]</i>,
        "<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>" : <i>[ <a href="serversideencryptiondefinition.md">ServerSideEncryptionDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>[ <a href="ttldefinition.md">TtlDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DynamodbTable
Properties:
    <a href="#billingmode" title="BillingMode">BillingMode</a>: <i>String</i>
    <a href="#hashkey" title="HashKey">HashKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rangekey" title="RangeKey">RangeKey</a>: <i>String</i>
    <a href="#readcapacity" title="ReadCapacity">ReadCapacity</a>: <i>Double</i>
    <a href="#streamenabled" title="StreamEnabled">StreamEnabled</a>: <i>Boolean</i>
    <a href="#streamviewtype" title="StreamViewType">StreamViewType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#writecapacity" title="WriteCapacity">WriteCapacity</a>: <i>Double</i>
    <a href="#attribute" title="Attribute">Attribute</a>: <i>
      - <a href="attributedefinition.md">AttributeDefinition</a></i>
    <a href="#globalsecondaryindex" title="GlobalSecondaryIndex">GlobalSecondaryIndex</a>: <i>
      - <a href="globalsecondaryindexdefinition.md">GlobalSecondaryIndexDefinition</a></i>
    <a href="#localsecondaryindex" title="LocalSecondaryIndex">LocalSecondaryIndex</a>: <i>
      - <a href="localsecondaryindexdefinition.md">LocalSecondaryIndexDefinition</a></i>
    <a href="#pointintimerecovery" title="PointInTimeRecovery">PointInTimeRecovery</a>: <i>
      - <a href="pointintimerecoverydefinition.md">PointInTimeRecoveryDefinition</a></i>
    <a href="#replica" title="Replica">Replica</a>: <i>
      - <a href="replicadefinition.md">ReplicaDefinition</a></i>
    <a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>: <i>
      - <a href="serversideencryptiondefinition.md">ServerSideEncryptionDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>
      - <a href="ttldefinition.md">TtlDefinition</a></i>
</pre>

## Properties

#### BillingMode

Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashKey

The attribute to use as the hash (partition) key. Must also be defined as an `attribute`, see below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the attribute
* `type` - (Required) Attribute type, which must be a scalar type: `S`, `N`, or `B` for (S)tring, (N)umber or (B)inary data.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeKey

The attribute to use as the range (sort) key. Must also be defined as an `attribute`, see below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadCapacity

The number of read units for this table. If the `billing_mode` is `PROVISIONED`, this field is required.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamEnabled

Indicates whether Streams are to be enabled (true) or disabled (false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamViewType

When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to populate on the created table. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteCapacity

The number of write units for this table. If the `billing_mode` is `PROVISIONED`, this field is required.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attribute

_Required_: No

_Type_: List of <a href="attributedefinition.md">AttributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalSecondaryIndex

_Required_: No

_Type_: List of <a href="globalsecondaryindexdefinition.md">GlobalSecondaryIndexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSecondaryIndex

_Required_: No

_Type_: List of <a href="localsecondaryindexdefinition.md">LocalSecondaryIndexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PointInTimeRecovery

_Required_: No

_Type_: List of <a href="pointintimerecoverydefinition.md">PointInTimeRecoveryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replica

_Required_: No

_Type_: List of <a href="replicadefinition.md">ReplicaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryption

_Required_: No

_Type_: List of <a href="serversideencryptiondefinition.md">ServerSideEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: List of <a href="ttldefinition.md">TtlDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### StreamArn

Returns the <code>StreamArn</code> value.

#### StreamLabel

Returns the <code>StreamLabel</code> value.

