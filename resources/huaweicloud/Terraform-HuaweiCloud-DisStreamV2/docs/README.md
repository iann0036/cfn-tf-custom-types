# Terraform::HuaweiCloud::DisStreamV2

CloudFormation equivalent of huaweicloud_dis_stream_v2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::DisStreamV2",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#autoscalemaxpartitioncount" title="AutoScaleMaxPartitionCount">AutoScaleMaxPartitionCount</a>" : <i>Double</i>,
        "<a href="#autoscaleminpartitioncount" title="AutoScaleMinPartitionCount">AutoScaleMinPartitionCount</a>" : <i>Double</i>,
        "<a href="#compressionformat" title="CompressionFormat">CompressionFormat</a>" : <i>String</i>,
        "<a href="#created" title="Created">Created</a>" : <i>Double</i>,
        "<a href="#csvdelimiter" title="CsvDelimiter">CsvDelimiter</a>" : <i>String</i>,
        "<a href="#dataschema" title="DataSchema">DataSchema</a>" : <i>String</i>,
        "<a href="#datatype" title="DataType">DataType</a>" : <i>String</i>,
        "<a href="#partitioncount" title="PartitionCount">PartitionCount</a>" : <i>Double</i>,
        "<a href="#readablepartitioncount" title="ReadablePartitionCount">ReadablePartitionCount</a>" : <i>Double</i>,
        "<a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>" : <i>Double</i>,
        "<a href="#streamname" title="StreamName">StreamName</a>" : <i>String</i>,
        "<a href="#streamtype" title="StreamType">StreamType</a>" : <i>String</i>,
        "<a href="#writablepartitioncount" title="WritablePartitionCount">WritablePartitionCount</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::DisStreamV2
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#autoscalemaxpartitioncount" title="AutoScaleMaxPartitionCount">AutoScaleMaxPartitionCount</a>: <i>Double</i>
    <a href="#autoscaleminpartitioncount" title="AutoScaleMinPartitionCount">AutoScaleMinPartitionCount</a>: <i>Double</i>
    <a href="#compressionformat" title="CompressionFormat">CompressionFormat</a>: <i>String</i>
    <a href="#created" title="Created">Created</a>: <i>Double</i>
    <a href="#csvdelimiter" title="CsvDelimiter">CsvDelimiter</a>: <i>String</i>
    <a href="#dataschema" title="DataSchema">DataSchema</a>: <i>String</i>
    <a href="#datatype" title="DataType">DataType</a>: <i>String</i>
    <a href="#partitioncount" title="PartitionCount">PartitionCount</a>: <i>Double</i>
    <a href="#readablepartitioncount" title="ReadablePartitionCount">ReadablePartitionCount</a>: <i>Double</i>
    <a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>: <i>Double</i>
    <a href="#streamname" title="StreamName">StreamName</a>: <i>String</i>
    <a href="#streamtype" title="StreamType">StreamType</a>: <i>String</i>
    <a href="#writablepartitioncount" title="WritablePartitionCount">WritablePartitionCount</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Created

_Required_: No

_Type_: Double

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

#### PartitionCount

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadablePartitionCount

_Required_: No

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

#### WritablePartitionCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

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

Returns the &lt;code&gt;Created&lt;/code&gt; value.

#### ReadablePartitionCount

Returns the &lt;code&gt;ReadablePartitionCount&lt;/code&gt; value.

#### WritablePartitionCount

Returns the &lt;code&gt;WritablePartitionCount&lt;/code&gt; value.

