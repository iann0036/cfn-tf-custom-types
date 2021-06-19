# TF::Intersight::KubernetesClusterProfile

Cluster profile specifies the config profile for a Kubernetes cluster. It also depicts operations to control the life cycle of a Kubernetes cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::KubernetesClusterProfile",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#acicniprofile" title="AciCniProfile">AciCniProfile</a>" : <i>[ <a href="acicniprofiledefinition.md">AciCniProfileDefinition</a>, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#actioninfo" title="ActionInfo">ActionInfo</a>" : <i>[ <a href="actioninfodefinition.md">ActionInfoDefinition</a>, ... ]</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#associatedcluster" title="AssociatedCluster">AssociatedCluster</a>" : <i>[ <a href="associatedclusterdefinition.md">AssociatedClusterDefinition</a>, ... ]</i>,
        "<a href="#certconfig" title="CertConfig">CertConfig</a>" : <i>[ <a href="certconfigdefinition.md">CertConfigDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#clusterippools" title="ClusterIpPools">ClusterIpPools</a>" : <i>[ <a href="clusterippoolsdefinition.md">ClusterIpPoolsDefinition</a>, ... ]</i>,
        "<a href="#configcontext" title="ConfigContext">ConfigContext</a>" : <i>[ <a href="configcontextdefinition.md">ConfigContextDefinition</a>, ... ]</i>,
        "<a href="#containerruntimeconfig" title="ContainerRuntimeConfig">ContainerRuntimeConfig</a>" : <i>[ <a href="containerruntimeconfigdefinition.md">ContainerRuntimeConfigDefinition</a>, ... ]</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#essentialaddons" title="EssentialAddons">EssentialAddons</a>" : <i>[ <a href="essentialaddonsdefinition4.md">EssentialAddonsDefinition4</a>, ... ]</i>,
        "<a href="#kubeconfig" title="KubeConfig">KubeConfig</a>" : <i>[ <a href="kubeconfigdefinition.md">KubeConfigDefinition</a>, ... ]</i>,
        "<a href="#loadbalanceripleases" title="LoadbalancerIpLeases">LoadbalancerIpLeases</a>" : <i>[ <a href="loadbalanceripleasesdefinition.md">LoadbalancerIpLeasesDefinition</a>, ... ]</i>,
        "<a href="#managedmode" title="ManagedMode">ManagedMode</a>" : <i>String</i>,
        "<a href="#managementconfig" title="ManagementConfig">ManagementConfig</a>" : <i>[ <a href="managementconfigdefinition.md">ManagementConfigDefinition</a>, ... ]</i>,
        "<a href="#masterviplease" title="MasterVipLease">MasterVipLease</a>" : <i>[ <a href="mastervipleasedefinition.md">MasterVipLeaseDefinition</a>, ... ]</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netconfig" title="NetConfig">NetConfig</a>" : <i>[ <a href="netconfigdefinition.md">NetConfigDefinition</a>, ... ]</i>,
        "<a href="#nodegroups" title="NodeGroups">NodeGroups</a>" : <i>[ <a href="nodegroupsdefinition.md">NodeGroupsDefinition</a>, ... ]</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>[ <a href="organizationdefinition.md">OrganizationDefinition</a>, ... ]</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#policybucket" title="PolicyBucket">PolicyBucket</a>" : <i>[ <a href="policybucketdefinition.md">PolicyBucketDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#srctemplate" title="SrcTemplate">SrcTemplate</a>" : <i>[ <a href="srctemplatedefinition.md">SrcTemplateDefinition</a>, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#sysconfig" title="SysConfig">SysConfig</a>" : <i>[ <a href="sysconfigdefinition.md">SysConfigDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#trustedregistries" title="TrustedRegistries">TrustedRegistries</a>" : <i>[ <a href="trustedregistriesdefinition.md">TrustedRegistriesDefinition</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#waitforcompletion" title="WaitForCompletion">WaitForCompletion</a>" : <i>Boolean</i>,
        "<a href="#workflowinfo" title="WorkflowInfo">WorkflowInfo</a>" : <i>[ <a href="workflowinfodefinition.md">WorkflowInfoDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::KubernetesClusterProfile
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#acicniprofile" title="AciCniProfile">AciCniProfile</a>: <i>
      - <a href="acicniprofiledefinition.md">AciCniProfileDefinition</a></i>
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#actioninfo" title="ActionInfo">ActionInfo</a>: <i>
      - <a href="actioninfodefinition.md">ActionInfoDefinition</a></i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#associatedcluster" title="AssociatedCluster">AssociatedCluster</a>: <i>
      - <a href="associatedclusterdefinition.md">AssociatedClusterDefinition</a></i>
    <a href="#certconfig" title="CertConfig">CertConfig</a>: <i>
      - <a href="certconfigdefinition.md">CertConfigDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#clusterippools" title="ClusterIpPools">ClusterIpPools</a>: <i>
      - <a href="clusterippoolsdefinition.md">ClusterIpPoolsDefinition</a></i>
    <a href="#configcontext" title="ConfigContext">ConfigContext</a>: <i>
      - <a href="configcontextdefinition.md">ConfigContextDefinition</a></i>
    <a href="#containerruntimeconfig" title="ContainerRuntimeConfig">ContainerRuntimeConfig</a>: <i>
      - <a href="containerruntimeconfigdefinition.md">ContainerRuntimeConfigDefinition</a></i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#essentialaddons" title="EssentialAddons">EssentialAddons</a>: <i>
      - <a href="essentialaddonsdefinition4.md">EssentialAddonsDefinition4</a></i>
    <a href="#kubeconfig" title="KubeConfig">KubeConfig</a>: <i>
      - <a href="kubeconfigdefinition.md">KubeConfigDefinition</a></i>
    <a href="#loadbalanceripleases" title="LoadbalancerIpLeases">LoadbalancerIpLeases</a>: <i>
      - <a href="loadbalanceripleasesdefinition.md">LoadbalancerIpLeasesDefinition</a></i>
    <a href="#managedmode" title="ManagedMode">ManagedMode</a>: <i>String</i>
    <a href="#managementconfig" title="ManagementConfig">ManagementConfig</a>: <i>
      - <a href="managementconfigdefinition.md">ManagementConfigDefinition</a></i>
    <a href="#masterviplease" title="MasterVipLease">MasterVipLease</a>: <i>
      - <a href="mastervipleasedefinition.md">MasterVipLeaseDefinition</a></i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netconfig" title="NetConfig">NetConfig</a>: <i>
      - <a href="netconfigdefinition.md">NetConfigDefinition</a></i>
    <a href="#nodegroups" title="NodeGroups">NodeGroups</a>: <i>
      - <a href="nodegroupsdefinition.md">NodeGroupsDefinition</a></i>
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
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#srctemplate" title="SrcTemplate">SrcTemplate</a>: <i>
      - <a href="srctemplatedefinition.md">SrcTemplateDefinition</a></i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#sysconfig" title="SysConfig">SysConfig</a>: <i>
      - <a href="sysconfigdefinition.md">SysConfigDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#trustedregistries" title="TrustedRegistries">TrustedRegistries</a>: <i>
      - <a href="trustedregistriesdefinition.md">TrustedRegistriesDefinition</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
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

#### AciCniProfile

_Required_: No

_Type_: List of <a href="acicniprofiledefinition.md">AciCniProfileDefinition</a>

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

#### Ancestors

_Required_: No

_Type_: List of <a href="ancestorsdefinition.md">AncestorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedCluster

_Required_: No

_Type_: List of <a href="associatedclusterdefinition.md">AssociatedClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertConfig

_Required_: No

_Type_: List of <a href="certconfigdefinition.md">CertConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIpPools

_Required_: No

_Type_: List of <a href="clusterippoolsdefinition.md">ClusterIpPoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigContext

_Required_: No

_Type_: List of <a href="configcontextdefinition.md">ConfigContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerRuntimeConfig

_Required_: No

_Type_: List of <a href="containerruntimeconfigdefinition.md">ContainerRuntimeConfigDefinition</a>

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

#### EssentialAddons

_Required_: No

_Type_: List of <a href="essentialaddonsdefinition4.md">EssentialAddonsDefinition4</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeConfig

_Required_: No

_Type_: List of <a href="kubeconfigdefinition.md">KubeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadbalancerIpLeases

_Required_: No

_Type_: List of <a href="loadbalanceripleasesdefinition.md">LoadbalancerIpLeasesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementConfig

_Required_: No

_Type_: List of <a href="managementconfigdefinition.md">ManagementConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterVipLease

_Required_: No

_Type_: List of <a href="mastervipleasedefinition.md">MasterVipLeaseDefinition</a>

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

#### NetConfig

_Required_: No

_Type_: List of <a href="netconfigdefinition.md">NetConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeGroups

_Required_: No

_Type_: List of <a href="nodegroupsdefinition.md">NodeGroupsDefinition</a>

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

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcTemplate

_Required_: No

_Type_: List of <a href="srctemplatedefinition.md">SrcTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

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

#### TrustedRegistries

_Required_: No

_Type_: List of <a href="trustedregistriesdefinition.md">TrustedRegistriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

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

