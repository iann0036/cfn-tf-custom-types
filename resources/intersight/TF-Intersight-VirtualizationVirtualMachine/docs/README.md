# TF::Intersight::VirtualizationVirtualMachine

Depicts operations to control the life cycle of a virtual machine on a hypervisor.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::VirtualizationVirtualMachine",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#actioninfo" title="ActionInfo">ActionInfo</a>" : <i>[ <a href="actioninfodefinition.md">ActionInfoDefinition</a>, ... ]</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#affinityselectors" title="AffinitySelectors">AffinitySelectors</a>" : <i>[ <a href="affinityselectorsdefinition.md">AffinitySelectorsDefinition</a>, ... ]</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#antiaffinityselectors" title="AntiAffinitySelectors">AntiAffinitySelectors</a>" : <i>[ <a href="antiaffinityselectorsdefinition.md">AntiAffinitySelectorsDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#cloudinitconfig" title="CloudInitConfig">CloudInitConfig</a>" : <i>[ <a href="cloudinitconfigdefinition.md">CloudInitConfigDefinition</a>, ... ]</i>,
        "<a href="#cluster" title="Cluster">Cluster</a>" : <i>[ <a href="clusterdefinition.md">ClusterDefinition</a>, ... ]</i>,
        "<a href="#clusteresxi" title="ClusterEsxi">ClusterEsxi</a>" : <i>String</i>,
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#discovered" title="Discovered">Discovered</a>" : <i>Boolean</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="diskdefinition2.md">DiskDefinition2</a>, ... ]</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#guestos" title="GuestOs">GuestOs</a>" : <i>String</i>,
        "<a href="#host" title="Host">Host</a>" : <i>[ <a href="hostdefinition.md">HostDefinition</a>, ... ]</i>,
        "<a href="#hostesxi" title="HostEsxi">HostEsxi</a>" : <i>String</i>,
        "<a href="#hypervisortype" title="HypervisorType">HypervisorType</a>" : <i>String</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ <a href="interfacesdefinition.md">InterfacesDefinition</a>, ... ]</i>,
        "<a href="#inventory" title="Inventory">Inventory</a>" : <i>[ <a href="inventorydefinition.md">InventoryDefinition</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#powerstate" title="PowerState">PowerState</a>" : <i>String</i>,
        "<a href="#provisiontype" title="ProvisionType">ProvisionType</a>" : <i>String</i>,
        "<a href="#registereddevice" title="RegisteredDevice">RegisteredDevice</a>" : <i>[ <a href="registereddevicedefinition.md">RegisteredDeviceDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#vmconfig" title="VmConfig">VmConfig</a>" : <i>[ <a href="vmconfigdefinition.md">VmConfigDefinition</a>, ... ]</i>,
        "<a href="#waitforcompletion" title="WaitForCompletion">WaitForCompletion</a>" : <i>Boolean</i>,
        "<a href="#workflowinfo" title="WorkflowInfo">WorkflowInfo</a>" : <i>[ <a href="workflowinfodefinition.md">WorkflowInfoDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::VirtualizationVirtualMachine
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#actioninfo" title="ActionInfo">ActionInfo</a>: <i>
      - <a href="actioninfodefinition.md">ActionInfoDefinition</a></i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#affinityselectors" title="AffinitySelectors">AffinitySelectors</a>: <i>
      - <a href="affinityselectorsdefinition.md">AffinitySelectorsDefinition</a></i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#antiaffinityselectors" title="AntiAffinitySelectors">AntiAffinitySelectors</a>: <i>
      - <a href="antiaffinityselectorsdefinition.md">AntiAffinitySelectorsDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#cloudinitconfig" title="CloudInitConfig">CloudInitConfig</a>: <i>
      - <a href="cloudinitconfigdefinition.md">CloudInitConfigDefinition</a></i>
    <a href="#cluster" title="Cluster">Cluster</a>: <i>
      - <a href="clusterdefinition.md">ClusterDefinition</a></i>
    <a href="#clusteresxi" title="ClusterEsxi">ClusterEsxi</a>: <i>String</i>
    <a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#discovered" title="Discovered">Discovered</a>: <i>Boolean</i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="diskdefinition2.md">DiskDefinition2</a></i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#guestos" title="GuestOs">GuestOs</a>: <i>String</i>
    <a href="#host" title="Host">Host</a>: <i>
      - <a href="hostdefinition.md">HostDefinition</a></i>
    <a href="#hostesxi" title="HostEsxi">HostEsxi</a>: <i>String</i>
    <a href="#hypervisortype" title="HypervisorType">HypervisorType</a>: <i>String</i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - <a href="interfacesdefinition.md">InterfacesDefinition</a></i>
    <a href="#inventory" title="Inventory">Inventory</a>: <i>
      - <a href="inventorydefinition.md">InventoryDefinition</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#powerstate" title="PowerState">PowerState</a>: <i>String</i>
    <a href="#provisiontype" title="ProvisionType">ProvisionType</a>: <i>String</i>
    <a href="#registereddevice" title="RegisteredDevice">RegisteredDevice</a>: <i>
      - <a href="registereddevicedefinition.md">RegisteredDeviceDefinition</a></i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
    <a href="#vmconfig" title="VmConfig">VmConfig</a>: <i>
      - <a href="vmconfigdefinition.md">VmConfigDefinition</a></i>
    <a href="#waitforcompletion" title="WaitForCompletion">WaitForCompletion</a>: <i>Boolean</i>
    <a href="#workflowinfo" title="WorkflowInfo">WorkflowInfo</a>: <i>
      - <a href="workflowinfodefinition.md">WorkflowInfoDefinition</a></i>
</pre>

## Properties

#### AccountMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionInfo

_Required_: No

_Type_: List of <a href="actioninfodefinition.md">ActionInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AffinitySelectors

_Required_: No

_Type_: List of <a href="affinityselectorsdefinition.md">AffinitySelectorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ancestors

_Required_: No

_Type_: List of <a href="ancestorsdefinition.md">AncestorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiAffinitySelectors

_Required_: No

_Type_: List of <a href="antiaffinityselectorsdefinition.md">AntiAffinitySelectorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudInitConfig

_Required_: No

_Type_: List of <a href="cloudinitconfigdefinition.md">CloudInitConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cluster

_Required_: No

_Type_: List of <a href="clusterdefinition.md">ClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterEsxi

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Discovered

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="diskdefinition2.md">DiskDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGroupMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestOs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: List of <a href="hostdefinition.md">HostDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostEsxi

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HypervisorType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

_Required_: No

_Type_: List of <a href="interfacesdefinition.md">InterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inventory

_Required_: No

_Type_: List of <a href="inventorydefinition.md">InventoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Moid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

_Required_: No

_Type_: List of <a href="parentdefinition.md">ParentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionResources

_Required_: No

_Type_: List of <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisteredDevice

_Required_: No

_Type_: List of <a href="registereddevicedefinition.md">RegisteredDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmConfig

_Required_: No

_Type_: List of <a href="vmconfigdefinition.md">VmConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCompletion

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkflowInfo

_Required_: No

_Type_: List of <a href="workflowinfodefinition.md">WorkflowInfoDefinition</a>

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

