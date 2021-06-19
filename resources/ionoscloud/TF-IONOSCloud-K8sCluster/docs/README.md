# TF::IONOSCloud::K8sCluster

Manages a Managed Kubernetes cluster on IonosCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::IONOSCloud::K8sCluster",
    "Properties" : {
        "<a href="#availableupgradeversions" title="AvailableUpgradeVersions">AvailableUpgradeVersions</a>" : <i>[ String, ... ]</i>,
        "<a href="#gatewayip" title="GatewayIp">GatewayIp</a>" : <i>String</i>,
        "<a href="#k8sversion" title="K8sVersion">K8sVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#public" title="Public">Public</a>" : <i>Boolean</i>,
        "<a href="#viablenodepoolversions" title="ViableNodePoolVersions">ViableNodePoolVersions</a>" : <i>[ String, ... ]</i>,
        "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>[ <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::IONOSCloud::K8sCluster
Properties:
    <a href="#availableupgradeversions" title="AvailableUpgradeVersions">AvailableUpgradeVersions</a>: <i>
      - String</i>
    <a href="#gatewayip" title="GatewayIp">GatewayIp</a>: <i>String</i>
    <a href="#k8sversion" title="K8sVersion">K8sVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#public" title="Public">Public</a>: <i>Boolean</i>
    <a href="#viablenodepoolversions" title="ViableNodePoolVersions">ViableNodePoolVersions</a>: <i>
      - String</i>
    <a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>
      - <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailableUpgradeVersions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp

The IP address of the gateway used by the cluster. This is mandatory when `public` is set to `false` and should not be provided otherwise.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### K8sVersion

[string] The desired Kubernetes Version. For supported values, please check the API documentation.
- `maintenance_window` - (Optional) See the **maintenance_window** section in the example above
- `public` - The indicator if the cluster is public or private. Be aware that setting it to false is currently in beta phase.
- `gateway_ip` - The IP address of the gateway used by the cluster. This is mandatory when `public` is set to `false` and should not be provided otherwise.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

[string] The name of the Kubernetes Cluster.
- `k8s_version` - (Optional)[string] The desired Kubernetes Version. For supported values, please check the API documentation.
- `maintenance_window` - (Optional) See the **maintenance_window** section in the example above
- `public` - The indicator if the cluster is public or private. Be aware that setting it to false is currently in beta phase.
- `gateway_ip` - The IP address of the gateway used by the cluster. This is mandatory when `public` is set to `false` and should not be provided otherwise.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Public

The indicator if the cluster is public or private. Be aware that setting it to false is currently in beta phase.
- `gateway_ip` - The IP address of the gateway used by the cluster. This is mandatory when `public` is set to `false` and should not be provided otherwise.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViableNodePoolVersions

_Required_: No

_Type_: List of String

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

