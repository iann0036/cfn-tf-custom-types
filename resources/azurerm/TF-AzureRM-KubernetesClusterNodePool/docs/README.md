# TF::AzureRM::KubernetesClusterNodePool

Manages a Node Pool within a Kubernetes Cluster

-> **Note:** Due to the fast-moving nature of AKS, we recommend using the latest version of the Azure Provider when using AKS - you can find [the latest version of the Azure Provider here](https://registry.terraform.io/providers/hashicorp/azurerm/latest).

~> **NOTE:** Multiple Node Pools are only supported when the Kubernetes Cluster is using Virtual Machine Scale Sets.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::KubernetesClusterNodePool",
    "Properties" : {
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#enableautoscaling" title="EnableAutoScaling">EnableAutoScaling</a>" : <i>Boolean</i>,
        "<a href="#enablehostencryption" title="EnableHostEncryption">EnableHostEncryption</a>" : <i>Boolean</i>,
        "<a href="#enablenodepublicip" title="EnableNodePublicIp">EnableNodePublicIp</a>" : <i>Boolean</i>,
        "<a href="#evictionpolicy" title="EvictionPolicy">EvictionPolicy</a>" : <i>String</i>,
        "<a href="#kubernetesclusterid" title="KubernetesClusterId">KubernetesClusterId</a>" : <i>String</i>,
        "<a href="#maxcount" title="MaxCount">MaxCount</a>" : <i>Double</i>,
        "<a href="#maxpods" title="MaxPods">MaxPods</a>" : <i>Double</i>,
        "<a href="#mincount" title="MinCount">MinCount</a>" : <i>Double</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
        "<a href="#nodelabels" title="NodeLabels">NodeLabels</a>" : <i>[ <a href="nodelabelsdefinition.md">NodeLabelsDefinition</a>, ... ]</i>,
        "<a href="#nodepublicipprefixid" title="NodePublicIpPrefixId">NodePublicIpPrefixId</a>" : <i>String</i>,
        "<a href="#nodetaints" title="NodeTaints">NodeTaints</a>" : <i>[ String, ... ]</i>,
        "<a href="#orchestratorversion" title="OrchestratorVersion">OrchestratorVersion</a>" : <i>String</i>,
        "<a href="#osdisksizegb" title="OsDiskSizeGb">OsDiskSizeGb</a>" : <i>Double</i>,
        "<a href="#osdisktype" title="OsDiskType">OsDiskType</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
        "<a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>" : <i>String</i>,
        "<a href="#spotmaxprice" title="SpotMaxPrice">SpotMaxPrice</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
        "<a href="#vnetsubnetid" title="VnetSubnetId">VnetSubnetId</a>" : <i>String</i>,
        "<a href="#kubeletconfig" title="KubeletConfig">KubeletConfig</a>" : <i>[ <a href="kubeletconfigdefinition.md">KubeletConfigDefinition</a>, ... ]</i>,
        "<a href="#linuxosconfig" title="LinuxOsConfig">LinuxOsConfig</a>" : <i>[ <a href="linuxosconfigdefinition.md">LinuxOsConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#upgradesettings" title="UpgradeSettings">UpgradeSettings</a>" : <i>[ <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::KubernetesClusterNodePool
Properties:
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#enableautoscaling" title="EnableAutoScaling">EnableAutoScaling</a>: <i>Boolean</i>
    <a href="#enablehostencryption" title="EnableHostEncryption">EnableHostEncryption</a>: <i>Boolean</i>
    <a href="#enablenodepublicip" title="EnableNodePublicIp">EnableNodePublicIp</a>: <i>Boolean</i>
    <a href="#evictionpolicy" title="EvictionPolicy">EvictionPolicy</a>: <i>String</i>
    <a href="#kubernetesclusterid" title="KubernetesClusterId">KubernetesClusterId</a>: <i>String</i>
    <a href="#maxcount" title="MaxCount">MaxCount</a>: <i>Double</i>
    <a href="#maxpods" title="MaxPods">MaxPods</a>: <i>Double</i>
    <a href="#mincount" title="MinCount">MinCount</a>: <i>Double</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
    <a href="#nodelabels" title="NodeLabels">NodeLabels</a>: <i>
      - <a href="nodelabelsdefinition.md">NodeLabelsDefinition</a></i>
    <a href="#nodepublicipprefixid" title="NodePublicIpPrefixId">NodePublicIpPrefixId</a>: <i>String</i>
    <a href="#nodetaints" title="NodeTaints">NodeTaints</a>: <i>
      - String</i>
    <a href="#orchestratorversion" title="OrchestratorVersion">OrchestratorVersion</a>: <i>String</i>
    <a href="#osdisksizegb" title="OsDiskSizeGb">OsDiskSizeGb</a>: <i>Double</i>
    <a href="#osdisktype" title="OsDiskType">OsDiskType</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>String</i>
    <a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>: <i>String</i>
    <a href="#spotmaxprice" title="SpotMaxPrice">SpotMaxPrice</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
    <a href="#vnetsubnetid" title="VnetSubnetId">VnetSubnetId</a>: <i>String</i>
    <a href="#kubeletconfig" title="KubeletConfig">KubeletConfig</a>: <i>
      - <a href="kubeletconfigdefinition.md">KubeletConfigDefinition</a></i>
    <a href="#linuxosconfig" title="LinuxOsConfig">LinuxOsConfig</a>: <i>
      - <a href="linuxosconfigdefinition.md">LinuxOsConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#upgradesettings" title="UpgradeSettings">UpgradeSettings</a>: <i>
      - <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a></i>
</pre>

## Properties

#### AvailabilityZones

A list of Availability Zones where the Nodes in this Node Pool should be created in. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoScaling

Whether to enable [auto-scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler). Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHostEncryption

Should the nodes in this Node Pool have host encryption enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNodePublicIp

Should each node have a Public IP Address? Defaults to `false`.  Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvictionPolicy

The Eviction Policy which should be used for Virtual Machines within the Virtual Machine Scale Set powering this Node Pool. Possible values are `Deallocate` and `Delete`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesClusterId

The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPods

The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Should this Node Pool be used for System or User resources? Possible values are `System` and `User`. Defaults to `User`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeLabels

A map of Kubernetes labels which should be applied to nodes in this Node Pool. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of <a href="nodelabelsdefinition.md">NodeLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePublicIpPrefixId

Resource ID for the Public IP Addresses Prefix for the nodes in this Node Pool. `enable_node_public_ip` should be `true`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeTaints

A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`). Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrchestratorVersion

Version of Kubernetes used for the Agents. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsDiskSizeGb

The Agent Operating System disk size in GB. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsDiskType

The type of disk which should be used for the Operating System. Possible values are `Ephemeral` and `Managed`. Defaults to `Managed`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are `Linux` and `Windows`. Defaults to `Linux`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The Priority for Virtual Machines within the Virtual Machine Scale Set that powers this Node Pool. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProximityPlacementGroupId

The ID of the Proximity Placement Group where the Virtual Machine Scale Set that powers this Node Pool will be placed. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotMaxPrice

The maximum price you're willing to pay in USD per Virtual Machine. Valid values are `-1` (the current on-demand price for a Virtual Machine) or a positive value with up to five decimal places. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetSubnetId

The ID of the Subnet where this Node Pool should exist.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeletConfig

_Required_: No

_Type_: List of <a href="kubeletconfigdefinition.md">KubeletConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxOsConfig

_Required_: No

_Type_: List of <a href="linuxosconfigdefinition.md">LinuxOsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeSettings

_Required_: No

_Type_: List of <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a>

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

