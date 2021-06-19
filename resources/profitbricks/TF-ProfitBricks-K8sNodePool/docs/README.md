# TF::ProfitBricks::K8sNodePool

Manages a Kubernetes Node Pool, part of a managed Kubernetes cluster on ProfitBricks.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ProfitBricks::K8sNodePool",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#corescount" title="CoresCount">CoresCount</a>" : <i>Double</i>,
        "<a href="#cpufamily" title="CpuFamily">CpuFamily</a>" : <i>String</i>,
        "<a href="#datacenterid" title="DatacenterId">DatacenterId</a>" : <i>String</i>,
        "<a href="#k8sclusterid" title="K8sClusterId">K8sClusterId</a>" : <i>String</i>,
        "<a href="#k8sversion" title="K8sVersion">K8sVersion</a>" : <i>String</i>,
        "<a href="#lans" title="Lans">Lans</a>" : <i>[ Double, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
        "<a href="#publicips" title="PublicIps">PublicIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#ramsize" title="RamSize">RamSize</a>" : <i>Double</i>,
        "<a href="#storagesize" title="StorageSize">StorageSize</a>" : <i>Double</i>,
        "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
        "<a href="#autoscaling" title="AutoScaling">AutoScaling</a>" : <i>[ <a href="autoscalingdefinition.md">AutoScalingDefinition</a>, ... ]</i>,
        "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>[ <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ProfitBricks::K8sNodePool
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#corescount" title="CoresCount">CoresCount</a>: <i>Double</i>
    <a href="#cpufamily" title="CpuFamily">CpuFamily</a>: <i>String</i>
    <a href="#datacenterid" title="DatacenterId">DatacenterId</a>: <i>String</i>
    <a href="#k8sclusterid" title="K8sClusterId">K8sClusterId</a>: <i>String</i>
    <a href="#k8sversion" title="K8sVersion">K8sVersion</a>: <i>String</i>
    <a href="#lans" title="Lans">Lans</a>: <i>
      - Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
    <a href="#publicips" title="PublicIps">PublicIps</a>: <i>
      - String</i>
    <a href="#ramsize" title="RamSize">RamSize</a>: <i>Double</i>
    <a href="#storagesize" title="StorageSize">StorageSize</a>: <i>Double</i>
    <a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
    <a href="#autoscaling" title="AutoScaling">AutoScaling</a>: <i>
      - <a href="autoscalingdefinition.md">AutoScalingDefinition</a></i>
    <a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>
      - <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailabilityZone

[string] - The desired Compute availability zone - See the API documentation for more information
- `storage_type` -(Required)[string] - The desired storage type - SSD/HDD
- `node_count` -(Required)[int] - The desired number of nodes in the node pool
- `cores_count` -(Required)[int] - The CPU cores count for each node of the node pool
- `ram_size` -(Required)[int] - The desired amount of RAM, in MB
- `storage_size` -(Required)[int] - The desired amount of storage for each node, in GB
- `public_ips` - (Optional)[list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements;.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoresCount

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuFamily

[string] The desired CPU Family - See the API documentation for more information
- `availability_zone` - (Required)[string] - The desired Compute availability zone - See the API documentation for more information
- `storage_type` -(Required)[string] - The desired storage type - SSD/HDD
- `node_count` -(Required)[int] - The desired number of nodes in the node pool
- `cores_count` -(Required)[int] - The CPU cores count for each node of the node pool
- `ram_size` -(Required)[int] - The desired amount of RAM, in MB
- `storage_size` -(Required)[int] - The desired amount of storage for each node, in GB
- `public_ips` - (Optional)[list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements;.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatacenterId

[string] A Datacenter's UUID
- `k8s_cluster_id`- (Required)[string] A k8s cluster's UUID
- `cpu_family` - (Required)[string] The desired CPU Family - See the API documentation for more information
- `availability_zone` - (Required)[string] - The desired Compute availability zone - See the API documentation for more information
- `storage_type` -(Required)[string] - The desired storage type - SSD/HDD
- `node_count` -(Required)[int] - The desired number of nodes in the node pool
- `cores_count` -(Required)[int] - The CPU cores count for each node of the node pool
- `ram_size` -(Required)[int] - The desired amount of RAM, in MB
- `storage_size` -(Required)[int] - The desired amount of storage for each node, in GB
- `public_ips` - (Optional)[list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements;.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### K8sClusterId

[string] A k8s cluster's UUID
- `cpu_family` - (Required)[string] The desired CPU Family - See the API documentation for more information
- `availability_zone` - (Required)[string] - The desired Compute availability zone - See the API documentation for more information
- `storage_type` -(Required)[string] - The desired storage type - SSD/HDD
- `node_count` -(Required)[int] - The desired number of nodes in the node pool
- `cores_count` -(Required)[int] - The CPU cores count for each node of the node pool
- `ram_size` -(Required)[int] - The desired amount of RAM, in MB
- `storage_size` -(Required)[int] - The desired amount of storage for each node, in GB
- `public_ips` - (Optional)[list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements;.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### K8sVersion

[string] The desired Kubernetes Version. for supported values, please check the API documentation.
- `auto_scaling` - (Optional)[string] Wether the Node Pool should autoscale. For more details, please check the API documentation
- `lans` - (Optional)[list] A list of numeric LAN id's you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
- `maintenance_window` - (Optional) See the **maintenance_window** section in the example above
- `datacenter_id` - (Required)[string] A Datacenter's UUID
- `k8s_cluster_id`- (Required)[string] A k8s cluster's UUID
- `cpu_family` - (Required)[string] The desired CPU Family - See the API documentation for more information
- `availability_zone` - (Required)[string] - The desired Compute availability zone - See the API documentation for more information
- `storage_type` -(Required)[string] - The desired storage type - SSD/HDD
- `node_count` -(Required)[int] - The desired number of nodes in the node pool
- `cores_count` -(Required)[int] - The CPU cores count for each node of the node pool
- `ram_size` -(Required)[int] - The desired amount of RAM, in MB
- `storage_size` -(Required)[int] - The desired amount of storage for each node, in GB
- `public_ips` - (Optional)[list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements;.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lans

[list] A list of numeric LAN id's you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
- `maintenance_window` - (Optional) See the **maintenance_window** section in the example above
- `datacenter_id` - (Required)[string] A Datacenter's UUID
- `k8s_cluster_id`- (Required)[string] A k8s cluster's UUID
- `cpu_family` - (Required)[string] The desired CPU Family - See the API documentation for more information
- `availability_zone` - (Required)[string] - The desired Compute availability zone - See the API documentation for more information
- `storage_type` -(Required)[string] - The desired storage type - SSD/HDD
- `node_count` -(Required)[int] - The desired number of nodes in the node pool
- `cores_count` -(Required)[int] - The CPU cores count for each node of the node pool
- `ram_size` -(Required)[int] - The desired amount of RAM, in MB
- `storage_size` -(Required)[int] - The desired amount of storage for each node, in GB
- `public_ips` - (Optional)[list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements;.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

[string] The name of the Kubernetes Cluster.
- `k8s_version` - (Optional)[string] The desired Kubernetes Version. for supported values, please check the API documentation.
- `auto_scaling` - (Optional)[string] Wether the Node Pool should autoscale. For more details, please check the API documentation
- `lans` - (Optional)[list] A list of numeric LAN id's you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
- `maintenance_window` - (Optional) See the **maintenance_window** section in the example above
- `datacenter_id` - (Required)[string] A Datacenter's UUID
- `k8s_cluster_id`- (Required)[string] A k8s cluster's UUID
- `cpu_family` - (Required)[string] The desired CPU Family - See the API documentation for more information
- `availability_zone` - (Required)[string] - The desired Compute availability zone - See the API documentation for more information
- `storage_type` -(Required)[string] - The desired storage type - SSD/HDD
- `node_count` -(Required)[int] - The desired number of nodes in the node pool
- `cores_count` -(Required)[int] - The CPU cores count for each node of the node pool
- `ram_size` -(Required)[int] - The desired amount of RAM, in MB
- `storage_size` -(Required)[int] - The desired amount of storage for each node, in GB
- `public_ips` - (Optional)[list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements;.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIps

[list] A list of public IPs associated with the node pool; must have at least `node_count + 1` elements;.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RamSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScaling

_Required_: No

_Type_: List of <a href="autoscalingdefinition.md">AutoScalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: No

_Type_: List of <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

