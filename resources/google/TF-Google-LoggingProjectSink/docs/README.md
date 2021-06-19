# TF::Google::LoggingProjectSink

Manages a project-level logging sink. For more information see:

* [API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks)
* How-to Guides
    * [Exporting Logs](https://cloud.google.com/logging/docs/export)

~> You can specify exclusions for log sinks created by terraform by using the exclusions field of `google_logging_folder_sink`

~> **Note:** You must have [granted the "Logs Configuration Writer"](https://cloud.google.com/logging/docs/access-control) IAM role (`roles/logging.configWriter`) to the credentials used with terraform.

~> **Note** You must [enable the Cloud Resource Manager API](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::LoggingProjectSink",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#uniquewriteridentity" title="UniqueWriterIdentity">UniqueWriterIdentity</a>" : <i>Boolean</i>,
        "<a href="#bigqueryoptions" title="BigqueryOptions">BigqueryOptions</a>" : <i>[ <a href="bigqueryoptionsdefinition.md">BigqueryOptionsDefinition</a>, ... ]</i>,
        "<a href="#exclusions" title="Exclusions">Exclusions</a>" : <i>[ <a href="exclusionsdefinition.md">ExclusionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::LoggingProjectSink
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#filter" title="Filter">Filter</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#uniquewriteridentity" title="UniqueWriterIdentity">UniqueWriterIdentity</a>: <i>Boolean</i>
    <a href="#bigqueryoptions" title="BigqueryOptions">BigqueryOptions</a>: <i>
      - <a href="bigqueryoptionsdefinition.md">BigqueryOptionsDefinition</a></i>
    <a href="#exclusions" title="Exclusions">Exclusions</a>: <i>
      - <a href="exclusionsdefinition.md">ExclusionsDefinition</a></i>
</pre>

## Properties

#### Description

A description of this sink. The maximum length of the description is 8000 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, a BigQuery dataset or a Cloud Logging bucket . Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
"logging.googleapis.com/projects/[PROJECT_ID]]/locations/global/buckets/[BUCKET_ID]"
```
The writer associated with the sink must have access to write to the above resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

If set to True, then this sink is disabled and it does not export any log entries.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the logging sink.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UniqueWriterIdentity

Whether or not to create a unique identity associated with this sink. If `false`
(the default), then the `writer_identity` used is `serviceAccount:cloud-logs@system.gserviceaccount.com`. If `true`,
then a unique service account is created and used for this sink. If you wish to publish logs across projects or utilize
`bigquery_options`, you must set `unique_writer_identity` to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigqueryOptions

_Required_: No

_Type_: List of <a href="bigqueryoptionsdefinition.md">BigqueryOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusions

_Required_: No

_Type_: List of <a href="exclusionsdefinition.md">ExclusionsDefinition</a>

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

#### WriterIdentity

Returns the <code>WriterIdentity</code> value.

