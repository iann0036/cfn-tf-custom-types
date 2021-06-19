# TF::Alicloud::LogOssShipper

CloudFormation equivalent of alicloud_log_oss_shipper

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::LogOssShipper",
    "Properties" : {
        "<a href="#bufferinterval" title="BufferInterval">BufferInterval</a>" : <i>Double</i>,
        "<a href="#buffersize" title="BufferSize">BufferSize</a>" : <i>Double</i>,
        "<a href="#compresstype" title="CompressType">CompressType</a>" : <i>String</i>,
        "<a href="#csvconfigcolumns" title="CsvConfigColumns">CsvConfigColumns</a>" : <i>[ String, ... ]</i>,
        "<a href="#csvconfigdelimiter" title="CsvConfigDelimiter">CsvConfigDelimiter</a>" : <i>String</i>,
        "<a href="#csvconfigheader" title="CsvConfigHeader">CsvConfigHeader</a>" : <i>Boolean</i>,
        "<a href="#csvconfiglinefeed" title="CsvConfigLinefeed">CsvConfigLinefeed</a>" : <i>String</i>,
        "<a href="#csvconfignullidentifier" title="CsvConfigNullidentifier">CsvConfigNullidentifier</a>" : <i>String</i>,
        "<a href="#csvconfigquote" title="CsvConfigQuote">CsvConfigQuote</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#jsonenabletag" title="JsonEnableTag">JsonEnableTag</a>" : <i>Boolean</i>,
        "<a href="#logstorename" title="LogstoreName">LogstoreName</a>" : <i>String</i>,
        "<a href="#ossbucket" title="OssBucket">OssBucket</a>" : <i>String</i>,
        "<a href="#ossprefix" title="OssPrefix">OssPrefix</a>" : <i>String</i>,
        "<a href="#pathformat" title="PathFormat">PathFormat</a>" : <i>String</i>,
        "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#shippername" title="ShipperName">ShipperName</a>" : <i>String</i>,
        "<a href="#parquetconfig" title="ParquetConfig">ParquetConfig</a>" : <i>[ <a href="parquetconfigdefinition.md">ParquetConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::LogOssShipper
Properties:
    <a href="#bufferinterval" title="BufferInterval">BufferInterval</a>: <i>Double</i>
    <a href="#buffersize" title="BufferSize">BufferSize</a>: <i>Double</i>
    <a href="#compresstype" title="CompressType">CompressType</a>: <i>String</i>
    <a href="#csvconfigcolumns" title="CsvConfigColumns">CsvConfigColumns</a>: <i>
      - String</i>
    <a href="#csvconfigdelimiter" title="CsvConfigDelimiter">CsvConfigDelimiter</a>: <i>String</i>
    <a href="#csvconfigheader" title="CsvConfigHeader">CsvConfigHeader</a>: <i>Boolean</i>
    <a href="#csvconfiglinefeed" title="CsvConfigLinefeed">CsvConfigLinefeed</a>: <i>String</i>
    <a href="#csvconfignullidentifier" title="CsvConfigNullidentifier">CsvConfigNullidentifier</a>: <i>String</i>
    <a href="#csvconfigquote" title="CsvConfigQuote">CsvConfigQuote</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#jsonenabletag" title="JsonEnableTag">JsonEnableTag</a>: <i>Boolean</i>
    <a href="#logstorename" title="LogstoreName">LogstoreName</a>: <i>String</i>
    <a href="#ossbucket" title="OssBucket">OssBucket</a>: <i>String</i>
    <a href="#ossprefix" title="OssPrefix">OssPrefix</a>: <i>String</i>
    <a href="#pathformat" title="PathFormat">PathFormat</a>: <i>String</i>
    <a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#shippername" title="ShipperName">ShipperName</a>: <i>String</i>
    <a href="#parquetconfig" title="ParquetConfig">ParquetConfig</a>: <i>
      - <a href="parquetconfigdefinition.md">ParquetConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BufferInterval

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvConfigColumns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvConfigDelimiter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvConfigHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvConfigLinefeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvConfigNullidentifier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvConfigQuote

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsonEnableTag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogstoreName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OssBucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OssPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathFormat

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShipperName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParquetConfig

_Required_: No

_Type_: List of <a href="parquetconfigdefinition.md">ParquetConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

