# TF::Intersight::HyperflexClusterProfile

A profile specifying configuration settings for a HyperFlex cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::HyperflexClusterProfile",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#associatedcluster" title="AssociatedCluster">AssociatedCluster</a>" : <i>[ <a href="associatedclusterdefinition.md">AssociatedClusterDefinition</a>, ... ]</i>,
        "<a href="#associatedcomputecluster" title="AssociatedComputeCluster">AssociatedComputeCluster</a>" : <i>[ <a href="associatedcomputeclusterdefinition.md">AssociatedComputeClusterDefinition</a>, ... ]</i>,
        "<a href="#autosupport" title="AutoSupport">AutoSupport</a>" : <i>[ <a href="autosupportdefinition.md">AutoSupportDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#clusternetwork" title="ClusterNetwork">ClusterNetwork</a>" : <i>[ <a href="clusternetworkdefinition.md">ClusterNetworkDefinition</a>, ... ]</i>,
        "<a href="#clusterstorage" title="ClusterStorage">ClusterStorage</a>" : <i>[ <a href="clusterstoragedefinition.md">ClusterStorageDefinition</a>, ... ]</i>,
        "<a href="#configcontext" title="ConfigContext">ConfigContext</a>" : <i>[ <a href="configcontextdefinition.md">ConfigContextDefinition</a>, ... ]</i>,
        "<a href="#configresult" title="ConfigResult">ConfigResult</a>" : <i>[ <a href="configresultdefinition.md">ConfigResultDefinition</a>, ... ]</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#dataipaddress" title="DataIpAddress">DataIpAddress</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#extfcstorage" title="ExtFcStorage">ExtFcStorage</a>" : <i>[ <a href="extfcstoragedefinition.md">ExtFcStorageDefinition</a>, ... ]</i>,
        "<a href="#extiscsistorage" title="ExtIscsiStorage">ExtIscsiStorage</a>" : <i>[ <a href="extiscsistoragedefinition.md">ExtIscsiStorageDefinition</a>, ... ]</i>,
        "<a href="#hostnameprefix" title="HostNamePrefix">HostNamePrefix</a>" : <i>String</i>,
        "<a href="#httpproxypolicy" title="Httpproxypolicy">Httpproxypolicy</a>" : <i>[ <a href="httpproxypolicydefinition.md">HttpproxypolicyDefinition</a>, ... ]</i>,
        "<a href="#hypervisorcontrolipaddress" title="HypervisorControlIpAddress">HypervisorControlIpAddress</a>" : <i>String</i>,
        "<a href="#hypervisortype" title="HypervisorType">HypervisorType</a>" : <i>String</i>,
        "<a href="#localcredential" title="LocalCredential">LocalCredential</a>" : <i>[ <a href="localcredentialdefinition.md">LocalCredentialDefinition</a>, ... ]</i>,
        "<a href="#macaddressprefix" title="MacAddressPrefix">MacAddressPrefix</a>" : <i>String</i>,
        "<a href="#mgmtipaddress" title="MgmtIpAddress">MgmtIpAddress</a>" : <i>String</i>,
        "<a href="#mgmtplatform" title="MgmtPlatform">MgmtPlatform</a>" : <i>String</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>, ... ]</i>,
        "<a href="#nodeprofileconfig" title="NodeProfileConfig">NodeProfileConfig</a>" : <i>[ <a href="nodeprofileconfigdefinition.md">NodeProfileConfigDefinition</a>, ... ]</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>[ <a href="organizationdefinition.md">OrganizationDefinition</a>, ... ]</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#policybucket" title="PolicyBucket">PolicyBucket</a>" : <i>[ <a href="policybucketdefinition.md">PolicyBucketDefinition</a>, ... ]</i>,
        "<a href="#proxysetting" title="ProxySetting">ProxySetting</a>" : <i>[ <a href="proxysettingdefinition.md">ProxySettingDefinition</a>, ... ]</i>,
        "<a href="#replication" title="Replication">Replication</a>" : <i>Double</i>,
        "<a href="#runningworkflows" title="RunningWorkflows">RunningWorkflows</a>" : <i>[ <a href="runningworkflowsdefinition.md">RunningWorkflowsDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#softwareversion" title="SoftwareVersion">SoftwareVersion</a>" : <i>[ <a href="softwareversiondefinition.md">SoftwareVersionDefinition</a>, ... ]</i>,
        "<a href="#srctemplate" title="SrcTemplate">SrcTemplate</a>" : <i>[ <a href="srctemplatedefinition.md">SrcTemplateDefinition</a>, ... ]</i>,
        "<a href="#storagedatavlan" title="StorageDataVlan">StorageDataVlan</a>" : <i>[ <a href="storagedatavlandefinition.md">StorageDataVlanDefinition</a>, ... ]</i>,
        "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
        "<a href="#sysconfig" title="SysConfig">SysConfig</a>" : <i>[ <a href="sysconfigdefinition.md">SysConfigDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#ucsmconfig" title="UcsmConfig">UcsmConfig</a>" : <i>[ <a href="ucsmconfigdefinition.md">UcsmConfigDefinition</a>, ... ]</i>,
        "<a href="#vcenterconfig" title="VcenterConfig">VcenterConfig</a>" : <i>[ <a href="vcenterconfigdefinition.md">VcenterConfigDefinition</a>, ... ]</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#waitforcompletion" title="WaitForCompletion">WaitForCompletion</a>" : <i>Boolean</i>,
        "<a href="#wwxnprefix" title="WwxnPrefix">WwxnPrefix</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::HyperflexClusterProfile
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#associatedcluster" title="AssociatedCluster">AssociatedCluster</a>: <i>
      - <a href="associatedclusterdefinition.md">AssociatedClusterDefinition</a></i>
    <a href="#associatedcomputecluster" title="AssociatedComputeCluster">AssociatedComputeCluster</a>: <i>
      - <a href="associatedcomputeclusterdefinition.md">AssociatedComputeClusterDefinition</a></i>
    <a href="#autosupport" title="AutoSupport">AutoSupport</a>: <i>
      - <a href="autosupportdefinition.md">AutoSupportDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#clusternetwork" title="ClusterNetwork">ClusterNetwork</a>: <i>
      - <a href="clusternetworkdefinition.md">ClusterNetworkDefinition</a></i>
    <a href="#clusterstorage" title="ClusterStorage">ClusterStorage</a>: <i>
      - <a href="clusterstoragedefinition.md">ClusterStorageDefinition</a></i>
    <a href="#configcontext" title="ConfigContext">ConfigContext</a>: <i>
      - <a href="configcontextdefinition.md">ConfigContextDefinition</a></i>
    <a href="#configresult" title="ConfigResult">ConfigResult</a>: <i>
      - <a href="configresultdefinition.md">ConfigResultDefinition</a></i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#dataipaddress" title="DataIpAddress">DataIpAddress</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#extfcstorage" title="ExtFcStorage">ExtFcStorage</a>: <i>
      - <a href="extfcstoragedefinition.md">ExtFcStorageDefinition</a></i>
    <a href="#extiscsistorage" title="ExtIscsiStorage">ExtIscsiStorage</a>: <i>
      - <a href="extiscsistoragedefinition.md">ExtIscsiStorageDefinition</a></i>
    <a href="#hostnameprefix" title="HostNamePrefix">HostNamePrefix</a>: <i>String</i>
    <a href="#httpproxypolicy" title="Httpproxypolicy">Httpproxypolicy</a>: <i>
      - <a href="httpproxypolicydefinition.md">HttpproxypolicyDefinition</a></i>
    <a href="#hypervisorcontrolipaddress" title="HypervisorControlIpAddress">HypervisorControlIpAddress</a>: <i>String</i>
    <a href="#hypervisortype" title="HypervisorType">HypervisorType</a>: <i>String</i>
    <a href="#localcredential" title="LocalCredential">LocalCredential</a>: <i>
      - <a href="localcredentialdefinition.md">LocalCredentialDefinition</a></i>
    <a href="#macaddressprefix" title="MacAddressPrefix">MacAddressPrefix</a>: <i>String</i>
    <a href="#mgmtipaddress" title="MgmtIpAddress">MgmtIpAddress</a>: <i>String</i>
    <a href="#mgmtplatform" title="MgmtPlatform">MgmtPlatform</a>: <i>String</i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - <a href="nodeconfigdefinition.md">NodeConfigDefinition</a></i>
    <a href="#nodeprofileconfig" title="NodeProfileConfig">NodeProfileConfig</a>: <i>
      - <a href="nodeprofileconfigdefinition.md">NodeProfileConfigDefinition</a></i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>
      - <a href="organizationdefinition.md">OrganizationDefinition</a></i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#policybucket" title="PolicyBucket">PolicyBucket</a>: <i>
      - <a href="policybucketdefinition.md">PolicyBucketDefinition</a></i>
    <a href="#proxysetting" title="ProxySetting">ProxySetting</a>: <i>
      - <a href="proxysettingdefinition.md">ProxySettingDefinition</a></i>
    <a href="#replication" title="Replication">Replication</a>: <i>Double</i>
    <a href="#runningworkflows" title="RunningWorkflows">RunningWorkflows</a>: <i>
      - <a href="runningworkflowsdefinition.md">RunningWorkflowsDefinition</a></i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#softwareversion" title="SoftwareVersion">SoftwareVersion</a>: <i>
      - <a href="softwareversiondefinition.md">SoftwareVersionDefinition</a></i>
    <a href="#srctemplate" title="SrcTemplate">SrcTemplate</a>: <i>
      - <a href="srctemplatedefinition.md">SrcTemplateDefinition</a></i>
    <a href="#storagedatavlan" title="StorageDataVlan">StorageDataVlan</a>: <i>
      - <a href="storagedatavlandefinition.md">StorageDataVlanDefinition</a></i>
    <a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
    <a href="#sysconfig" title="SysConfig">SysConfig</a>: <i>
      - <a href="sysconfigdefinition.md">SysConfigDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#ucsmconfig" title="UcsmConfig">UcsmConfig</a>: <i>
      - <a href="ucsmconfigdefinition.md">UcsmConfigDefinition</a></i>
    <a href="#vcenterconfig" title="VcenterConfig">VcenterConfig</a>: <i>
      - <a href="vcenterconfigdefinition.md">VcenterConfigDefinition</a></i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
    <a href="#waitforcompletion" title="WaitForCompletion">WaitForCompletion</a>: <i>Boolean</i>
    <a href="#wwxnprefix" title="WwxnPrefix">WwxnPrefix</a>: <i>String</i>
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

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ancestors

_Required_: No

_Type_: List of <a href="ancestorsdefinition.md">AncestorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedCluster

_Required_: No

_Type_: List of <a href="associatedclusterdefinition.md">AssociatedClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedComputeCluster

_Required_: No

_Type_: List of <a href="associatedcomputeclusterdefinition.md">AssociatedComputeClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSupport

_Required_: No

_Type_: List of <a href="autosupportdefinition.md">AutoSupportDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterNetwork

_Required_: No

_Type_: List of <a href="clusternetworkdefinition.md">ClusterNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterStorage

_Required_: No

_Type_: List of <a href="clusterstoragedefinition.md">ClusterStorageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigContext

_Required_: No

_Type_: List of <a href="configcontextdefinition.md">ConfigContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigResult

_Required_: No

_Type_: List of <a href="configresultdefinition.md">ConfigResultDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataIpAddress

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

#### ExtFcStorage

_Required_: No

_Type_: List of <a href="extfcstoragedefinition.md">ExtFcStorageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtIscsiStorage

_Required_: No

_Type_: List of <a href="extiscsistoragedefinition.md">ExtIscsiStorageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostNamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Httpproxypolicy

_Required_: No

_Type_: List of <a href="httpproxypolicydefinition.md">HttpproxypolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HypervisorControlIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HypervisorType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalCredential

_Required_: No

_Type_: List of <a href="localcredentialdefinition.md">LocalCredentialDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddressPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtPlatform

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

#### NodeConfig

_Required_: No

_Type_: List of <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeProfileConfig

_Required_: No

_Type_: List of <a href="nodeprofileconfigdefinition.md">NodeProfileConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: No

_Type_: List of <a href="organizationdefinition.md">OrganizationDefinition</a>

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

#### PolicyBucket

_Required_: No

_Type_: List of <a href="policybucketdefinition.md">PolicyBucketDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxySetting

_Required_: No

_Type_: List of <a href="proxysettingdefinition.md">ProxySettingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replication

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunningWorkflows

_Required_: No

_Type_: List of <a href="runningworkflowsdefinition.md">RunningWorkflowsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareVersion

_Required_: No

_Type_: List of <a href="softwareversiondefinition.md">SoftwareVersionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcTemplate

_Required_: No

_Type_: List of <a href="srctemplatedefinition.md">SrcTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDataVlan

_Required_: No

_Type_: List of <a href="storagedatavlandefinition.md">StorageDataVlanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysConfig

_Required_: No

_Type_: List of <a href="sysconfigdefinition.md">SysConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcsmConfig

_Required_: No

_Type_: List of <a href="ucsmconfigdefinition.md">UcsmConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterConfig

_Required_: No

_Type_: List of <a href="vcenterconfigdefinition.md">VcenterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCompletion

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WwxnPrefix

_Required_: No

_Type_: String

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

