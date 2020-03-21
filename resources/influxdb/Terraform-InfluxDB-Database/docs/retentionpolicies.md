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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replication

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shardgroupduration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

