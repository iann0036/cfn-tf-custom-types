# Terraform::HuaweiCloud::DisStreamV2

CloudFormation equivalent of huaweicloud_dis_stream_v2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::DisStreamV2",
    "Properties" : {
        "<a href="#autoscalemaxpartitioncount" title="AutoScaleMaxPartitionCount">AutoScaleMaxPartitionCount</a>" : <i>Double</i>,
        "<a href="#autoscaleminpartitioncount" title="AutoScaleMinPartitionCount">AutoScaleMinPartitionCount</a>" : <i>Double</i>,
        "<a href="#compressionformat" title="CompressionFormat">CompressionFormat</a>" : <i>String</i>,
        "<a href="#csvdelimiter" title="CsvDelimiter">CsvDelimiter</a>" : <i>String</i>,
        "<a href="#dataschema" title="DataSchema">DataSchema</a>" : <i>String</i>,
        "<a href="#datatype" title="DataType">DataType</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#partitioncount" title="PartitionCount">PartitionCount</a>" : <i>Double</i>,
        "<a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>" : <i>Double</i>,
        "<a href="#streamname" title="StreamName">StreamName</a>" : <i>String</i>,
        "<a href="#streamtype" title="StreamType">StreamType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::DisStreamV2
Properties:
    <a href="#autoscalemaxpartitioncount" title="AutoScaleMaxPartitionCount">AutoScaleMaxPartitionCount</a>: <i>Double</i>
    <a href="#autoscaleminpartitioncount" title="AutoScaleMinPartitionCount">AutoScaleMinPartitionCount</a>: <i>Double</i>
    <a href="#compressionformat" title="CompressionFormat">CompressionFormat</a>: <i>String</i>
    <a href="#csvdelimiter" title="CsvDelimiter">CsvDelimiter</a>: <i>String</i>
    <a href="#dataschema" title="DataSchema">DataSchema</a>: <i>String</i>
    <a href="#datatype" title="DataType">DataType</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#partitioncount" title="PartitionCount">PartitionCount</a>: <i>Double</i>
    <a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>: <i>Double</i>
    <a href="#streamname" title="StreamName">StreamName</a>: <i>String</i>
    <a href="#streamtype" title="StreamType">StreamType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### AutoScaleMaxPartitionCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScaleMinPartitionCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvDelimiter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSchema

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionCount

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Created

Returns the <code>Created</code> value.

#### ReadablePartitionCount

Returns the <code>ReadablePartitionCount</code> value.

#### WritablePartitionCount

Returns the <code>WritablePartitionCount</code> value.
