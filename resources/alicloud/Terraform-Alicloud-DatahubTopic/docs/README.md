# Terraform::Alicloud::DatahubTopic

The topic is the basic unit of Datahub data source and is used to define one kind of data or stream. It contains a set of subscriptions. You can manage the datahub source of an application by using topics. [Refer to details](https://help.aliyun.com/document_detail/47440.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::DatahubTopic",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#lifecycle" title="LifeCycle">LifeCycle</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
        "<a href="#recordschema" title="RecordSchema">RecordSchema</a>" : <i>[ <a href="recordschema.md">RecordSchema</a>, ... ]</i>,
        "<a href="#recordtype" title="RecordType">RecordType</a>" : <i>String</i>,
        "<a href="#shardcount" title="ShardCount">ShardCount</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::DatahubTopic
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#lifecycle" title="LifeCycle">LifeCycle</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
    <a href="#recordschema" title="RecordSchema">RecordSchema</a>: <i>
      - <a href="recordschema.md">RecordSchema</a></i>
    <a href="#recordtype" title="RecordType">RecordType</a>: <i>String</i>
    <a href="#shardcount" title="ShardCount">ShardCount</a>: <i>Double</i>
</pre>

## Properties

#### Comment

Comment of the datahub topic. It cannot be longer than 255 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifeCycle

How many days this topic lives. The permitted range of values is [1, 7]. The default value is 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the datahub topic. Its length is limited to 1-128 and only characters such as letters, digits and '_' are allowed. It is case-insensitive.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

The name of the datahub project that this topic belongs to. It is case-insensitive.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordSchema

Schema of this topic, required only for TUPLE topic. Supported data types (case-insensitive) are:
- BIGINT
- STRING
- BOOLEAN
- DOUBLE
- TIMESTAMP.

_Required_: No

_Type_: List of <a href="recordschema.md">RecordSchema</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordType

The type of this topic. Its value must be one of {BLOB, TUPLE}. For BLOB topic, data will be organized as binary and encoded by BASE64. For TUPLE topic, data has fixed schema. The default value is "TUPLE" with a schema {STRING}.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShardCount

The number of shards this topic contains. The permitted range of values is [1, 10]. The default value is 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### LastModifyTime

Returns the <code>LastModifyTime</code> value.

