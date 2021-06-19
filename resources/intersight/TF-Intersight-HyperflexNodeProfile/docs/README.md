# TF::Intersight::HyperflexNodeProfile

A configuration profile per node in the HyperFlex cluster.
It defines node settings such as IP address configuration for hypervisor management network, storage data network, HyperFlex management network, and the assigned physical server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::HyperflexNodeProfile",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#assignedserver" title="AssignedServer">AssignedServer</a>" : <i>[ <a href="assignedserverdefinition.md">AssignedServerDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#clusterprofile" title="ClusterProfile">ClusterProfile</a>" : <i>[ <a href="clusterprofiledefinition.md">ClusterProfileDefinition</a>, ... ]</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#hxdpdataip" title="HxdpDataIp">HxdpDataIp</a>" : <i>String</i>,
        "<a href="#hxdpmgmtip" title="HxdpMgmtIp">HxdpMgmtIp</a>" : <i>String</i>,
        "<a href="#hypervisorcontrolip" title="HypervisorControlIp">HypervisorControlIp</a>" : <i>String</i>,
        "<a href="#hypervisordataip" title="HypervisorDataIp">HypervisorDataIp</a>" : <i>String</i>,
        "<a href="#hypervisormgmtip" title="HypervisorMgmtIp">HypervisorMgmtIp</a>" : <i>String</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#srctemplate" title="SrcTemplate">SrcTemplate</a>" : <i>[ <a href="srctemplatedefinition.md">SrcTemplateDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::HyperflexNodeProfile
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#assignedserver" title="AssignedServer">AssignedServer</a>: <i>
      - <a href="assignedserverdefinition.md">AssignedServerDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#clusterprofile" title="ClusterProfile">ClusterProfile</a>: <i>
      - <a href="clusterprofiledefinition.md">ClusterProfileDefinition</a></i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#hxdpdataip" title="HxdpDataIp">HxdpDataIp</a>: <i>String</i>
    <a href="#hxdpmgmtip" title="HxdpMgmtIp">HxdpMgmtIp</a>: <i>String</i>
    <a href="#hypervisorcontrolip" title="HypervisorControlIp">HypervisorControlIp</a>: <i>String</i>
    <a href="#hypervisordataip" title="HypervisorDataIp">HypervisorDataIp</a>: <i>String</i>
    <a href="#hypervisormgmtip" title="HypervisorMgmtIp">HypervisorMgmtIp</a>: <i>String</i>
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
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#srctemplate" title="SrcTemplate">SrcTemplate</a>: <i>
      - <a href="srctemplatedefinition.md">SrcTemplateDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
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

#### AssignedServer

_Required_: No

_Type_: List of <a href="assignedserverdefinition.md">AssignedServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterProfile

_Required_: No

_Type_: List of <a href="clusterprofiledefinition.md">ClusterProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGroupMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HxdpDataIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HxdpMgmtIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HypervisorControlIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HypervisorDataIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HypervisorMgmtIp

_Required_: No

_Type_: String

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

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcTemplate

_Required_: No

_Type_: List of <a href="srctemplatedefinition.md">SrcTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

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

