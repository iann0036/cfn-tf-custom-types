# Terraform::AWS::GlueCatalogTable StorageDescriptor

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
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="storagedescriptor-parameters.md">Parameters</a>, ... ]</i>,
    "<a href="#storedassubdirectories" title="StoredAsSubDirectories">StoredAsSubDirectories</a>" : <i>Boolean</i>,
    "<a href="#columns" title="Columns">Columns</a>" : <i>[ <a href="storagedescriptor-columns.md">Columns</a>, ... ]</i>,
    "<a href="#serdeinfo" title="SerDeInfo">SerDeInfo</a>" : <i>[ <a href="storagedescriptor-serdeinfo.md">SerDeInfo</a>, ... ]</i>,
    "<a href="#skewedinfo" title="SkewedInfo">SkewedInfo</a>" : <i>[ <a href="storagedescriptor-skewedinfo.md">SkewedInfo</a>, ... ]</i>,
    "<a href="#sortcolumns" title="SortColumns">SortColumns</a>" : <i>[ <a href="storagedescriptor-sortcolumns.md">SortColumns</a>, ... ]</i>
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
      - <a href="storagedescriptor-parameters.md">Parameters</a></i>
<a href="#storedassubdirectories" title="StoredAsSubDirectories">StoredAsSubDirectories</a>: <i>Boolean</i>
<a href="#columns" title="Columns">Columns</a>: <i>
      - <a href="storagedescriptor-columns.md">Columns</a></i>
<a href="#serdeinfo" title="SerDeInfo">SerDeInfo</a>: <i>
      - <a href="storagedescriptor-serdeinfo.md">SerDeInfo</a></i>
<a href="#skewedinfo" title="SkewedInfo">SkewedInfo</a>: <i>
      - <a href="storagedescriptor-skewedinfo.md">SkewedInfo</a></i>
<a href="#sortcolumns" title="SortColumns">SortColumns</a>: <i>
      - <a href="storagedescriptor-sortcolumns.md">SortColumns</a></i>
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

_Type_: List of <a href="storagedescriptor-parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoredAsSubDirectories

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Columns

_Required_: No

_Type_: List of <a href="storagedescriptor-columns.md">Columns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerDeInfo

_Required_: No

_Type_: List of <a href="storagedescriptor-serdeinfo.md">SerDeInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkewedInfo

_Required_: No

_Type_: List of <a href="storagedescriptor-skewedinfo.md">SkewedInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortColumns

_Required_: No

_Type_: List of <a href="storagedescriptor-sortcolumns.md">SortColumns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

