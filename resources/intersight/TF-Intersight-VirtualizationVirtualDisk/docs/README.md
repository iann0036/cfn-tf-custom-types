# TF::Intersight::VirtualizationVirtualDisk

Depicts disk configuration used to be create a virtual disk on a hypervisor datastore.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::VirtualizationVirtualDisk",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#capacity" title="Capacity">Capacity</a>" : <i>String</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#cluster" title="Cluster">Cluster</a>" : <i>[ <a href="clusterdefinition.md">ClusterDefinition</a>, ... ]</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#discovered" title="Discovered">Discovered</a>" : <i>Boolean</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#inventory" title="Inventory">Inventory</a>" : <i>[ <a href="inventorydefinition.md">InventoryDefinition</a>, ... ]</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#registereddevice" title="RegisteredDevice">RegisteredDevice</a>" : <i>[ <a href="registereddevicedefinition.md">RegisteredDeviceDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#sourcecerts" title="SourceCerts">SourceCerts</a>" : <i>String</i>,
        "<a href="#sourcedisktoclone" title="SourceDiskToClone">SourceDiskToClone</a>" : <i>String</i>,
        "<a href="#sourcefilepath" title="SourceFilePath">SourceFilePath</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#waitforcompletion" title="WaitForCompletion">WaitForCompletion</a>" : <i>Boolean</i>,
        "<a href="#workflowinfo" title="WorkflowInfo">WorkflowInfo</a>" : <i>[ <a href="workflowinfodefinition.md">WorkflowInfoDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::VirtualizationVirtualDisk
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#capacity" title="Capacity">Capacity</a>: <i>String</i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#cluster" title="Cluster">Cluster</a>: <i>
      - <a href="clusterdefinition.md">ClusterDefinition</a></i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#discovered" title="Discovered">Discovered</a>: <i>Boolean</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#inventory" title="Inventory">Inventory</a>: <i>
      - <a href="inventorydefinition.md">InventoryDefinition</a></i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#registereddevice" title="RegisteredDevice">RegisteredDevice</a>: <i>
      - <a href="registereddevicedefinition.md">RegisteredDeviceDefinition</a></i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#sourcecerts" title="SourceCerts">SourceCerts</a>: <i>String</i>
    <a href="#sourcedisktoclone" title="SourceDiskToClone">SourceDiskToClone</a>: <i>String</i>
    <a href="#sourcefilepath" title="SourceFilePath">SourceFilePath</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
    <a href="#waitforcompletion" title="WaitForCompletion">WaitForCompletion</a>: <i>Boolean</i>
    <a href="#workflowinfo" title="WorkflowInfo">WorkflowInfo</a>: <i>
      - <a href="workflowinfodefinition.md">WorkflowInfoDefinition</a></i>
</pre>

## Properties

#### AccountMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ancestors

_Required_: No

_Type_: List of <a href="ancestorsdefinition.md">AncestorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cluster

_Required_: No

_Type_: List of <a href="clusterdefinition.md">ClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Discovered

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGroupMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inventory

_Required_: No

_Type_: List of <a href="inventorydefinition.md">InventoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

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

#### RegisteredDevice

_Required_: No

_Type_: List of <a href="registereddevicedefinition.md">RegisteredDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCerts

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDiskToClone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceFilePath

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
