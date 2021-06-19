# TF::Google::BigqueryTable ExternalDataConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autodetect" title="Autodetect">Autodetect</a>" : <i>Boolean</i>,
    "<a href="#compression" title="Compression">Compression</a>" : <i>String</i>,
    "<a href="#ignoreunknownvalues" title="IgnoreUnknownValues">IgnoreUnknownValues</a>" : <i>Boolean</i>,
    "<a href="#maxbadrecords" title="MaxBadRecords">MaxBadRecords</a>" : <i>Double</i>,
    "<a href="#schema" title="Schema">Schema</a>" : <i>String</i>,
    "<a href="#sourceformat" title="SourceFormat">SourceFormat</a>" : <i>String</i>,
    "<a href="#sourceuris" title="SourceUris">SourceUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#csvoptions" title="CsvOptions">CsvOptions</a>" : <i>[ <a href="csvoptionsdefinition.md">CsvOptionsDefinition</a>, ... ]</i>,
    "<a href="#googlesheetsoptions" title="GoogleSheetsOptions">GoogleSheetsOptions</a>" : <i>[ <a href="googlesheetsoptionsdefinition.md">GoogleSheetsOptionsDefinition</a>, ... ]</i>,
    "<a href="#hivepartitioningoptions" title="HivePartitioningOptions">HivePartitioningOptions</a>" : <i>[ <a href="hivepartitioningoptionsdefinition.md">HivePartitioningOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autodetect" title="Autodetect">Autodetect</a>: <i>Boolean</i>
<a href="#compression" title="Compression">Compression</a>: <i>String</i>
<a href="#ignoreunknownvalues" title="IgnoreUnknownValues">IgnoreUnknownValues</a>: <i>Boolean</i>
<a href="#maxbadrecords" title="MaxBadRecords">MaxBadRecords</a>: <i>Double</i>
<a href="#schema" title="Schema">Schema</a>: <i>String</i>
<a href="#sourceformat" title="SourceFormat">SourceFormat</a>: <i>String</i>
<a href="#sourceuris" title="SourceUris">SourceUris</a>: <i>
      - String</i>
<a href="#csvoptions" title="CsvOptions">CsvOptions</a>: <i>
      - <a href="csvoptionsdefinition.md">CsvOptionsDefinition</a></i>
<a href="#googlesheetsoptions" title="GoogleSheetsOptions">GoogleSheetsOptions</a>: <i>
      - <a href="googlesheetsoptionsdefinition.md">GoogleSheetsOptionsDefinition</a></i>
<a href="#hivepartitioningoptions" title="HivePartitioningOptions">HivePartitioningOptions</a>: <i>
      - <a href="hivepartitioningoptionsdefinition.md">HivePartitioningOptionsDefinition</a></i>
</pre>

## Properties

#### Autodetect

- Let BigQuery try to autodetect the schema
and format of the table.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compression

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreUnknownValues

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBadRecords

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

A JSON schema for the external table. Schema is required
for CSV and JSON formats if autodetect is not on. Schema is disallowed
for Google Cloud Bigtable, Cloud Datastore backups, Avro, ORC and Parquet formats.
~>**NOTE:** Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
Furthermore drift for this field cannot not be detected because BigQuery
only uses this schema to compute the effective schema for the table, therefore
any changes on the configured value will force the table to be recreated.
This schema is effectively only applied when creating a table from an external
datasource, after creation the computed schema will be stored in
`google_bigquery_table.schema`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceFormat

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUris

A list of the fully-qualified URIs that point to
your data in Google Cloud.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvOptions

_Required_: No

_Type_: List of <a href="csvoptionsdefinition.md">CsvOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleSheetsOptions

_Required_: No

_Type_: List of <a href="googlesheetsoptionsdefinition.md">GoogleSheetsOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HivePartitioningOptions

_Required_: No

_Type_: List of <a href="hivepartitioningoptionsdefinition.md">HivePartitioningOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

