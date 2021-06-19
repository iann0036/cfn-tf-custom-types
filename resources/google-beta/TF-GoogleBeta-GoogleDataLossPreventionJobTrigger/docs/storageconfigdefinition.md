# TF::GoogleBeta::GoogleDataLossPreventionJobTrigger StorageConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bigqueryoptions" title="BigQueryOptions">BigQueryOptions</a>" : <i>[ <a href="bigqueryoptionsdefinition.md">BigQueryOptionsDefinition</a>, ... ]</i>,
    "<a href="#cloudstorageoptions" title="CloudStorageOptions">CloudStorageOptions</a>" : <i>[ <a href="cloudstorageoptionsdefinition.md">CloudStorageOptionsDefinition</a>, ... ]</i>,
    "<a href="#datastoreoptions" title="DatastoreOptions">DatastoreOptions</a>" : <i>[ <a href="datastoreoptionsdefinition.md">DatastoreOptionsDefinition</a>, ... ]</i>,
    "<a href="#timespanconfig" title="TimespanConfig">TimespanConfig</a>" : <i>[ <a href="timespanconfigdefinition.md">TimespanConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bigqueryoptions" title="BigQueryOptions">BigQueryOptions</a>: <i>
      - <a href="bigqueryoptionsdefinition.md">BigQueryOptionsDefinition</a></i>
<a href="#cloudstorageoptions" title="CloudStorageOptions">CloudStorageOptions</a>: <i>
      - <a href="cloudstorageoptionsdefinition.md">CloudStorageOptionsDefinition</a></i>
<a href="#datastoreoptions" title="DatastoreOptions">DatastoreOptions</a>: <i>
      - <a href="datastoreoptionsdefinition.md">DatastoreOptionsDefinition</a></i>
<a href="#timespanconfig" title="TimespanConfig">TimespanConfig</a>: <i>
      - <a href="timespanconfigdefinition.md">TimespanConfigDefinition</a></i>
</pre>

## Properties

#### BigQueryOptions

_Required_: No

_Type_: List of <a href="bigqueryoptionsdefinition.md">BigQueryOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudStorageOptions

_Required_: No

_Type_: List of <a href="cloudstorageoptionsdefinition.md">CloudStorageOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatastoreOptions

_Required_: No

_Type_: List of <a href="datastoreoptionsdefinition.md">DatastoreOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimespanConfig

_Required_: No

_Type_: List of <a href="timespanconfigdefinition.md">TimespanConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

