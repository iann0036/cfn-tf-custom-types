# Terraform::Google::BigqueryTable TimePartitioning

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expirationms" title="ExpirationMs">ExpirationMs</a>" : <i>Double</i>,
    "<a href="#field" title="Field">Field</a>" : <i>String</i>,
    "<a href="#requirepartitionfilter" title="RequirePartitionFilter">RequirePartitionFilter</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#expirationms" title="ExpirationMs">ExpirationMs</a>: <i>Double</i>
<a href="#field" title="Field">Field</a>: <i>String</i>
<a href="#requirepartitionfilter" title="RequirePartitionFilter">RequirePartitionFilter</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### ExpirationMs

Number of milliseconds for which to keep the
storage for a partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Field

The field used to determine how to create a time-based
partition. If time-based partitioning is enabled without this value, the
table is partitioned based on the load time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequirePartitionFilter

If set to true, queries over this table
require a partition filter that can be used for partition elimination to be
specified.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The only type supported is DAY, which will generate
one partition per day based on data loading time.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

