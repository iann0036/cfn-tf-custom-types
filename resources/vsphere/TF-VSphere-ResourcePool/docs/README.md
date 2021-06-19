# TF::VSphere::ResourcePool

The `vsphere_resource_pool` resource can be used to create and manage
resource pools in standalone hosts or on compute clusters.

For more information on vSphere resource pools, see [this
page][ref-vsphere-resource_pools].

[ref-vsphere-resource_pools]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VSphere::ResourcePool",
    "Properties" : {
        "<a href="#cpuexpandable" title="CpuExpandable">CpuExpandable</a>" : <i>Boolean</i>,
        "<a href="#cpulimit" title="CpuLimit">CpuLimit</a>" : <i>Double</i>,
        "<a href="#cpureservation" title="CpuReservation">CpuReservation</a>" : <i>Double</i>,
        "<a href="#cpusharelevel" title="CpuShareLevel">CpuShareLevel</a>" : <i>String</i>,
        "<a href="#cpushares" title="CpuShares">CpuShares</a>" : <i>Double</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributesdefinition.md">CustomAttributesDefinition</a>, ... ]</i>,
        "<a href="#memoryexpandable" title="MemoryExpandable">MemoryExpandable</a>" : <i>Boolean</i>,
        "<a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>" : <i>Double</i>,
        "<a href="#memoryreservation" title="MemoryReservation">MemoryReservation</a>" : <i>Double</i>,
        "<a href="#memorysharelevel" title="MemoryShareLevel">MemoryShareLevel</a>" : <i>String</i>,
        "<a href="#memoryshares" title="MemoryShares">MemoryShares</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentresourcepoolid" title="ParentResourcePoolId">ParentResourcePoolId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VSphere::ResourcePool
Properties:
    <a href="#cpuexpandable" title="CpuExpandable">CpuExpandable</a>: <i>Boolean</i>
    <a href="#cpulimit" title="CpuLimit">CpuLimit</a>: <i>Double</i>
    <a href="#cpureservation" title="CpuReservation">CpuReservation</a>: <i>Double</i>
    <a href="#cpusharelevel" title="CpuShareLevel">CpuShareLevel</a>: <i>String</i>
    <a href="#cpushares" title="CpuShares">CpuShares</a>: <i>Double</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributesdefinition.md">CustomAttributesDefinition</a></i>
    <a href="#memoryexpandable" title="MemoryExpandable">MemoryExpandable</a>: <i>Boolean</i>
    <a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>: <i>Double</i>
    <a href="#memoryreservation" title="MemoryReservation">MemoryReservation</a>: <i>Double</i>
    <a href="#memorysharelevel" title="MemoryShareLevel">MemoryShareLevel</a>: <i>String</i>
    <a href="#memoryshares" title="MemoryShares">MemoryShares</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentresourcepoolid" title="ParentResourcePoolId">ParentResourcePoolId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### CpuExpandable

Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuLimit

The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuReservation

Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShareLevel

The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `cpu_shares` will be
ignored.  Default: `normal`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShares

The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`cpu_share_level` must be `custom`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: List of <a href="customattributesdefinition.md">CustomAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryExpandable

Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryLimit

The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryReservation

Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryShareLevel

The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `memory_shares` will be
ignored.  Default: `normal`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryShares

The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`memory_share_level` must be `custom`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the resource pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentResourcePoolId

The [managed object ID][docs-about-morefs]
of the parent resource pool. This can be the root resource pool for a cluster
or standalone host, or a resource pool itself. When moving a resource pool
from one parent resource pool to another, both must share a common root
resource pool or the move will fail.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

_Required_: No

_Type_: List of String

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

