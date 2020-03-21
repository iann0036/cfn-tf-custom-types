# Terraform::InfluxDB::Database RetentionPolicies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#default" title="Default">Default</a>" : <i>Boolean</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#replication" title="Replication">Replication</a>" : <i>Double</i>,
    "<a href="#shardgroupduration" title="Shardgroupduration">Shardgroupduration</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#default" title="Default">Default</a>: <i>Boolean</i>
<a href="#duration" title="Duration">Duration</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#replication" title="Replication">Replication</a>: <i>Double</i>
<a href="#shardgroupduration" title="Shardgroupduration">Shardgroupduration</a>: <i>String</i>
</pre>

## Properties

#### Default

Marks current retention policy as default. Default value is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

The duration for retention policy, format of duration can be found at InfluxDB Documentation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the retention policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replication

Determines how many copies of data points are stored in a cluster. Not applicable for single node / Open Source version of InfluxDB. Default value of 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shardgroupduration

Determines how much time each shard group spans. How and why to modify can be found at InfluxDB Documentation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

