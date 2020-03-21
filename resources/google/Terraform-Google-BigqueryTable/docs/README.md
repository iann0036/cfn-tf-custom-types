# Terraform::Google::BigqueryTable

CloudFormation equivalent of google_bigquery_table

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::BigqueryTable",
    "Properties" : {
        "<a href="#clustering" title="Clustering">Clustering</a>" : <i>[ String, ... ]</i>,
        "<a href="#datasetid" title="DatasetId">DatasetId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#expirationtime" title="ExpirationTime">ExpirationTime</a>" : <i>Double</i>,
        "<a href="#friendlyname" title="FriendlyName">FriendlyName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>String</i>,
        "<a href="#tableid" title="TableId">TableId</a>" : <i>String</i>,
        "<a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>" : <i>[ &lt;a href=&#34;encryptionconfiguration.md&#34;&gt;EncryptionConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#externaldataconfiguration" title="ExternalDataConfiguration">ExternalDataConfiguration</a>" : <i>[ &lt;a href=&#34;externaldataconfiguration.md&#34;&gt;ExternalDataConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#timepartitioning" title="TimePartitioning">TimePartitioning</a>" : <i>[ &lt;a href=&#34;timepartitioning.md&#34;&gt;TimePartitioning&lt;/a&gt;, ... ]</i>,
        "<a href="#view" title="View">View</a>" : <i>[ &lt;a href=&#34;view.md&#34;&gt;View&lt;/a&gt;, ... ]</i>,
        "<a href="#csvoptions" title="CsvOptions">CsvOptions</a>" : <i>[ &lt;a href=&#34;csvoptions.md&#34;&gt;CsvOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#googlesheetsoptions" title="GoogleSheetsOptions">GoogleSheetsOptions</a>" : <i>[ &lt;a href=&#34;googlesheetsoptions.md&#34;&gt;GoogleSheetsOptions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::BigqueryTable
Properties:
    <a href="#clustering" title="Clustering">Clustering</a>: <i>
      - String</i>
    <a href="#datasetid" title="DatasetId">DatasetId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#expirationtime" title="ExpirationTime">ExpirationTime</a>: <i>Double</i>
    <a href="#friendlyname" title="FriendlyName">FriendlyName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#schema" title="Schema">Schema</a>: <i>String</i>
    <a href="#tableid" title="TableId">TableId</a>: <i>String</i>
    <a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>: <i>
      - &lt;a href=&#34;encryptionconfiguration.md&#34;&gt;EncryptionConfiguration&lt;/a&gt;</i>
    <a href="#externaldataconfiguration" title="ExternalDataConfiguration">ExternalDataConfiguration</a>: <i>
      - &lt;a href=&#34;externaldataconfiguration.md&#34;&gt;ExternalDataConfiguration&lt;/a&gt;</i>
    <a href="#timepartitioning" title="TimePartitioning">TimePartitioning</a>: <i>
      - &lt;a href=&#34;timepartitioning.md&#34;&gt;TimePartitioning&lt;/a&gt;</i>
    <a href="#view" title="View">View</a>: <i>
      - &lt;a href=&#34;view.md&#34;&gt;View&lt;/a&gt;</i>
    <a href="#csvoptions" title="CsvOptions">CsvOptions</a>: <i>
      - &lt;a href=&#34;csvoptions.md&#34;&gt;CsvOptions&lt;/a&gt;</i>
    <a href="#googlesheetsoptions" title="GoogleSheetsOptions">GoogleSheetsOptions</a>: <i>
      - &lt;a href=&#34;googlesheetsoptions.md&#34;&gt;GoogleSheetsOptions&lt;/a&gt;</i>
</pre>

## Properties

#### Clustering

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatasetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FriendlyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;encryptionconfiguration.md&#34;&gt;EncryptionConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalDataConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;externaldataconfiguration.md&#34;&gt;ExternalDataConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimePartitioning

_Required_: No

_Type_: List of &lt;a href=&#34;timepartitioning.md&#34;&gt;TimePartitioning&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

_Required_: No

_Type_: List of &lt;a href=&#34;view.md&#34;&gt;View&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvOptions

_Required_: No

_Type_: List of &lt;a href=&#34;csvoptions.md&#34;&gt;CsvOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleSheetsOptions

_Required_: No

_Type_: List of &lt;a href=&#34;googlesheetsoptions.md&#34;&gt;GoogleSheetsOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTime

Returns the &lt;code&gt;CreationTime&lt;/code&gt; value.

#### Etag

Returns the &lt;code&gt;Etag&lt;/code&gt; value.

#### LastModifiedTime

Returns the &lt;code&gt;LastModifiedTime&lt;/code&gt; value.

#### Location

Returns the &lt;code&gt;Location&lt;/code&gt; value.

#### NumBytes

Returns the &lt;code&gt;NumBytes&lt;/code&gt; value.

#### NumLongTermBytes

Returns the &lt;code&gt;NumLongTermBytes&lt;/code&gt; value.

#### NumRows

Returns the &lt;code&gt;NumRows&lt;/code&gt; value.

#### SelfLink

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

#### Type

Returns the &lt;code&gt;Type&lt;/code&gt; value.

