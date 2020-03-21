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
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ &lt;a href=&#34;storagedescriptor-parameters.md&#34;&gt;Parameters&lt;/a&gt;, ... ]</i>,
    "<a href="#storedassubdirectories" title="StoredAsSubDirectories">StoredAsSubDirectories</a>" : <i>Boolean</i>,
    "<a href="#columns" title="Columns">Columns</a>" : <i>[ &lt;a href=&#34;storagedescriptor-columns.md&#34;&gt;Columns&lt;/a&gt;, ... ]</i>,
    "<a href="#serdeinfo" title="SerDeInfo">SerDeInfo</a>" : <i>[ &lt;a href=&#34;storagedescriptor-serdeinfo.md&#34;&gt;SerDeInfo&lt;/a&gt;, ... ]</i>,
    "<a href="#skewedinfo" title="SkewedInfo">SkewedInfo</a>" : <i>[ &lt;a href=&#34;storagedescriptor-skewedinfo.md&#34;&gt;SkewedInfo&lt;/a&gt;, ... ]</i>,
    "<a href="#sortcolumns" title="SortColumns">SortColumns</a>" : <i>[ &lt;a href=&#34;storagedescriptor-sortcolumns.md&#34;&gt;SortColumns&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;storagedescriptor-parameters.md&#34;&gt;Parameters&lt;/a&gt;</i>
<a href="#storedassubdirectories" title="StoredAsSubDirectories">StoredAsSubDirectories</a>: <i>Boolean</i>
<a href="#columns" title="Columns">Columns</a>: <i>
      - &lt;a href=&#34;storagedescriptor-columns.md&#34;&gt;Columns&lt;/a&gt;</i>
<a href="#serdeinfo" title="SerDeInfo">SerDeInfo</a>: <i>
      - &lt;a href=&#34;storagedescriptor-serdeinfo.md&#34;&gt;SerDeInfo&lt;/a&gt;</i>
<a href="#skewedinfo" title="SkewedInfo">SkewedInfo</a>: <i>
      - &lt;a href=&#34;storagedescriptor-skewedinfo.md&#34;&gt;SkewedInfo&lt;/a&gt;</i>
<a href="#sortcolumns" title="SortColumns">SortColumns</a>: <i>
      - &lt;a href=&#34;storagedescriptor-sortcolumns.md&#34;&gt;SortColumns&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;storagedescriptor-parameters.md&#34;&gt;Parameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoredAsSubDirectories

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Columns

_Required_: No
_Type_: List of &lt;a href=&#34;storagedescriptor-columns.md&#34;&gt;Columns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerDeInfo

_Required_: No
_Type_: List of &lt;a href=&#34;storagedescriptor-serdeinfo.md&#34;&gt;SerDeInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkewedInfo

_Required_: No
_Type_: List of &lt;a href=&#34;storagedescriptor-skewedinfo.md&#34;&gt;SkewedInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortColumns

_Required_: No
_Type_: List of &lt;a href=&#34;storagedescriptor-sortcolumns.md&#34;&gt;SortColumns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

