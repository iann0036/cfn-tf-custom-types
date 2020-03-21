# Terraform::Google::LoggingProjectSink BigqueryOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#usepartitionedtables" title="UsePartitionedTables">UsePartitionedTables</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#usepartitionedtables" title="UsePartitionedTables">UsePartitionedTables</a>: <i>Boolean</i>
</pre>

## Properties

#### UsePartitionedTables

Whether to use [BigQuery's partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables).
By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and [special query syntax](https://cloud.google.com/bigquery/docs/querying-partitioned-tables)
has to be used instead. In both cases, tables are sharded based on UTC timezone.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

