# Terraform::Google::BigqueryTable

Creates a table resource in a dataset for Google BigQuery. For more information see
[the official documentation](https://cloud.google.com/bigquery/docs/) and
[API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables).

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
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>String</i>,
        "<a href="#tableid" title="TableId">TableId</a>" : <i>String</i>,
        "<a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>" : <i>[ <a href="encryptionconfiguration.md">EncryptionConfiguration</a>, ... ]</i>,
        "<a href="#externaldataconfiguration" title="ExternalDataConfiguration">ExternalDataConfiguration</a>" : <i>[ <a href="externaldataconfiguration.md">ExternalDataConfiguration</a>, ... ]</i>,
        "<a href="#timepartitioning" title="TimePartitioning">TimePartitioning</a>" : <i>[ <a href="timepartitioning.md">TimePartitioning</a>, ... ]</i>,
        "<a href="#view" title="View">View</a>" : <i>[ <a href="view.md">View</a>, ... ]</i>,
        "<a href="#csvoptions" title="CsvOptions">CsvOptions</a>" : <i>[ <a href="csvoptions.md">CsvOptions</a>, ... ]</i>,
        "<a href="#googlesheetsoptions" title="GoogleSheetsOptions">GoogleSheetsOptions</a>" : <i>[ <a href="googlesheetsoptions.md">GoogleSheetsOptions</a>, ... ]</i>
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
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#schema" title="Schema">Schema</a>: <i>String</i>
    <a href="#tableid" title="TableId">TableId</a>: <i>String</i>
    <a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>: <i>
      - <a href="encryptionconfiguration.md">EncryptionConfiguration</a></i>
    <a href="#externaldataconfiguration" title="ExternalDataConfiguration">ExternalDataConfiguration</a>: <i>
      - <a href="externaldataconfiguration.md">ExternalDataConfiguration</a></i>
    <a href="#timepartitioning" title="TimePartitioning">TimePartitioning</a>: <i>
      - <a href="timepartitioning.md">TimePartitioning</a></i>
    <a href="#view" title="View">View</a>: <i>
      - <a href="view.md">View</a></i>
    <a href="#csvoptions" title="CsvOptions">CsvOptions</a>: <i>
      - <a href="csvoptions.md">CsvOptions</a></i>
    <a href="#googlesheetsoptions" title="GoogleSheetsOptions">GoogleSheetsOptions</a>: <i>
      - <a href="googlesheetsoptions.md">GoogleSheetsOptions</a></i>
</pre>

## Properties

#### Clustering

Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatasetId

The dataset ID to create the table in.
Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The field description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationTime

The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FriendlyName

A descriptive name for the table.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

A mapping of labels to assign to the resource.

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
[BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
~>**NOTE**: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced `STRUCT` field type with `RECORD`
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableId

A unique ID for the resource.
Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfiguration

_Required_: No

_Type_: List of <a href="encryptionconfiguration.md">EncryptionConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalDataConfiguration

_Required_: No

_Type_: List of <a href="externaldataconfiguration.md">ExternalDataConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimePartitioning

_Required_: No

_Type_: List of <a href="timepartitioning.md">TimePartitioning</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

_Required_: No

_Type_: List of <a href="view.md">View</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvOptions

_Required_: No

_Type_: List of <a href="csvoptions.md">CsvOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleSheetsOptions

_Required_: No

_Type_: List of <a href="googlesheetsoptions.md">GoogleSheetsOptions</a>

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

Returns the <code>CreationTime</code> value.

#### Etag

Returns the <code>Etag</code> value.

#### LastModifiedTime

Returns the <code>LastModifiedTime</code> value.

#### Location

Returns the <code>Location</code> value.

#### NumBytes

Returns the <code>NumBytes</code> value.

#### NumLongTermBytes

Returns the <code>NumLongTermBytes</code> value.

#### NumRows

Returns the <code>NumRows</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### Type

Returns the <code>Type</code> value.

