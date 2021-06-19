# TF::AWS::GluePartition StorageDescriptorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketcolumns" title="BucketColumns">BucketColumns</a>" : <i>[ String, ... ]</i>,
    "<a href="#compressed" title="Compressed">Compressed</a>" : <i>Boolean</i>,
    "<a href="#inputformat" title="InputFormat">InputFormat</a>" : <i>String</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#numberofbuckets" title="NumberOfBuckets">NumberOfBuckets</a>" : <i>Double</i>,
    "<a href="#outputformat" title="OutputFormat">OutputFormat</a>" : <i>String</i>,
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
    "<a href="#storedassubdirectories" title="StoredAsSubDirectories">StoredAsSubDirectories</a>" : <i>Boolean</i>,
    "<a href="#columns" title="Columns">Columns</a>" : <i>[ <a href="columnsdefinition.md">ColumnsDefinition</a>, ... ]</i>,
    "<a href="#serdeinfo" title="SerDeInfo">SerDeInfo</a>" : <i>[ <a href="serdeinfodefinition.md">SerDeInfoDefinition</a>, ... ]</i>,
    "<a href="#skewedinfo" title="SkewedInfo">SkewedInfo</a>" : <i>[ <a href="skewedinfodefinition.md">SkewedInfoDefinition</a>, ... ]</i>,
    "<a href="#sortcolumns" title="SortColumns">SortColumns</a>" : <i>[ <a href="sortcolumnsdefinition.md">SortColumnsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bucketcolumns" title="BucketColumns">BucketColumns</a>: <i>
      - String</i>
<a href="#compressed" title="Compressed">Compressed</a>: <i>Boolean</i>
<a href="#inputformat" title="InputFormat">InputFormat</a>: <i>String</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#numberofbuckets" title="NumberOfBuckets">NumberOfBuckets</a>: <i>Double</i>
<a href="#outputformat" title="OutputFormat">OutputFormat</a>: <i>String</i>
<a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
<a href="#storedassubdirectories" title="StoredAsSubDirectories">StoredAsSubDirectories</a>: <i>Boolean</i>
<a href="#columns" title="Columns">Columns</a>: <i>
      - <a href="columnsdefinition.md">ColumnsDefinition</a></i>
<a href="#serdeinfo" title="SerDeInfo">SerDeInfo</a>: <i>
      - <a href="serdeinfodefinition.md">SerDeInfoDefinition</a></i>
<a href="#skewedinfo" title="SkewedInfo">SkewedInfo</a>: <i>
      - <a href="skewedinfodefinition.md">SkewedInfoDefinition</a></i>
<a href="#sortcolumns" title="SortColumns">SortColumns</a>: <i>
      - <a href="sortcolumnsdefinition.md">SortColumnsDefinition</a></i>
</pre>

## Properties

#### BucketColumns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compressed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfBuckets

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoredAsSubDirectories

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Columns

_Required_: No

_Type_: List of <a href="columnsdefinition.md">ColumnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerDeInfo

_Required_: No

_Type_: List of <a href="serdeinfodefinition.md">SerDeInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkewedInfo

_Required_: No

_Type_: List of <a href="skewedinfodefinition.md">SkewedInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortColumns

_Required_: No

_Type_: List of <a href="sortcolumnsdefinition.md">SortColumnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

