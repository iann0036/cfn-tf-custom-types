# Terraform::Google::BigtableInstance Cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
    "<a href="#numnodes" title="NumNodes">NumNodes</a>" : <i>Double</i>,
    "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
    "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
<a href="#numnodes" title="NumNodes">NumNodes</a>: <i>Double</i>
<a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
<a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### ClusterId

The ID of the Cloud Bigtable cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumNodes

The number of nodes in your Cloud Bigtable cluster.
Required, with a minimum of `3` for a `PRODUCTION` instance. Must be left unset
for a `DEVELOPMENT` instance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageType

The storage type to use. One of `"SSD"` or
`"HDD"`. Defaults to `"SSD"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The zone to create the Cloud Bigtable cluster in. Each
cluster must have a different zone in the same region. Zones that support
Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

