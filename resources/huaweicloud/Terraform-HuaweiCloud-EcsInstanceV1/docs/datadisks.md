# Terraform::HuaweiCloud::EcsInstanceV1 DataDisks

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Size

The size of the data disk in GB. The value range is 10 to 32768.
Changing this creates a new server.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

Specifies the snapshot ID or ID of the original data disk contained in the full-ECS image.
Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The data disk type of the server. For HANA, HL1, and HL2 ECSs use co-p1 and uh-l1 disks.
Changing this creates a new server. Available options are:
* `SATA`: common I/O disk type.
* `SAS`: high I/O disk type.
* `SSD`: ultra-high I/O disk type.
* `co-p1`: high I/O(performance-optimized) disk type.
* `uh-l1`: ultra-high I/O(latency-optimized) disk type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

