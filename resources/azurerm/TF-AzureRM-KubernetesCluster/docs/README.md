# TF::AzureRM::KubernetesCluster

Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)

-> **Note:** Due to the fast-moving nature of AKS, we recommend using the latest version of the Azure Provider when using AKS - you can find [the latest version of the Azure Provider here](https://registry.terraform.io/providers/hashicorp/azurerm/latest).

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text. [Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::KubernetesCluster",
    "Properties" : {
        "<a href="#apiserverauthorizedipranges" title="ApiServerAuthorizedIpRanges">ApiServerAuthorizedIpRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#automaticchannelupgrade" title="AutomaticChannelUpgrade">AutomaticChannelUpgrade</a>" : <i>String</i>,
        "<a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>" : <i>String</i>,
        "<a href="#dnsprefix" title="DnsPrefix">DnsPrefix</a>" : <i>String</i>,
        "<a href="#dnsprefixprivatecluster" title="DnsPrefixPrivateCluster">DnsPrefixPrivateCluster</a>" : <i>String</i>,
        "<a href="#enablepodsecuritypolicy" title="EnablePodSecurityPolicy">EnablePodSecurityPolicy</a>" : <i>Boolean</i>,
        "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#noderesourcegroup" title="NodeResourceGroup">NodeResourceGroup</a>" : <i>String</i>,
        "<a href="#privateclusterenabled" title="PrivateClusterEnabled">PrivateClusterEnabled</a>" : <i>Boolean</i>,
        "<a href="#privatednszoneid" title="PrivateDnsZoneId">PrivateDnsZoneId</a>" : <i>String</i>,
        "<a href="#privatelinkenabled" title="PrivateLinkEnabled">PrivateLinkEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#skutier" title="SkuTier">SkuTier</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#addonprofile" title="AddonProfile">AddonProfile</a>" : <i>[ <a href="addonprofiledefinition.md">AddonProfileDefinition</a>, ... ]</i>,
        "<a href="#autoscalerprofile" title="AutoScalerProfile">AutoScalerProfile</a>" : <i>[ <a href="autoscalerprofiledefinition.md">AutoScalerProfileDefinition</a>, ... ]</i>,
        "<a href="#defaultnodepool" title="DefaultNodePool">DefaultNodePool</a>" : <i>[ <a href="defaultnodepooldefinition.md">DefaultNodePoolDefinition</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#kubeletidentity" title="KubeletIdentity">KubeletIdentity</a>" : <i>[ <a href="kubeletidentitydefinition.md">KubeletIdentityDefinition</a>, ... ]</i>,
        "<a href="#linuxprofile" title="LinuxProfile">LinuxProfile</a>" : <i>[ <a href="linuxprofiledefinition.md">LinuxProfileDefinition</a>, ... ]</i>,
        "<a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>" : <i>[ <a href="networkprofiledefinition.md">NetworkProfileDefinition</a>, ... ]</i>,
        "<a href="#rolebasedaccesscontrol" title="RoleBasedAccessControl">RoleBasedAccessControl</a>" : <i>[ <a href="rolebasedaccesscontroldefinition.md">RoleBasedAccessControlDefinition</a>, ... ]</i>,
        "<a href="#serviceprincipal" title="ServicePrincipal">ServicePrincipal</a>" : <i>[ <a href="serviceprincipaldefinition.md">ServicePrincipalDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#windowsprofile" title="WindowsProfile">WindowsProfile</a>" : <i>[ <a href="windowsprofiledefinition.md">WindowsProfileDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::KubernetesCluster
Properties:
    <a href="#apiserverauthorizedipranges" title="ApiServerAuthorizedIpRanges">ApiServerAuthorizedIpRanges</a>: <i>
      - String</i>
    <a href="#automaticchannelupgrade" title="AutomaticChannelUpgrade">AutomaticChannelUpgrade</a>: <i>String</i>
    <a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>: <i>String</i>
    <a href="#dnsprefix" title="DnsPrefix">DnsPrefix</a>: <i>String</i>
    <a href="#dnsprefixprivatecluster" title="DnsPrefixPrivateCluster">DnsPrefixPrivateCluster</a>: <i>String</i>
    <a href="#enablepodsecuritypolicy" title="EnablePodSecurityPolicy">EnablePodSecurityPolicy</a>: <i>Boolean</i>
    <a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#noderesourcegroup" title="NodeResourceGroup">NodeResourceGroup</a>: <i>String</i>
    <a href="#privateclusterenabled" title="PrivateClusterEnabled">PrivateClusterEnabled</a>: <i>Boolean</i>
    <a href="#privatednszoneid" title="PrivateDnsZoneId">PrivateDnsZoneId</a>: <i>String</i>
    <a href="#privatelinkenabled" title="PrivateLinkEnabled">PrivateLinkEnabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#skutier" title="SkuTier">SkuTier</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#addonprofile" title="AddonProfile">AddonProfile</a>: <i>
      - <a href="addonprofiledefinition.md">AddonProfileDefinition</a></i>
    <a href="#autoscalerprofile" title="AutoScalerProfile">AutoScalerProfile</a>: <i>
      - <a href="autoscalerprofiledefinition.md">AutoScalerProfileDefinition</a></i>
    <a href="#defaultnodepool" title="DefaultNodePool">DefaultNodePool</a>: <i>
      - <a href="defaultnodepooldefinition.md">DefaultNodePoolDefinition</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#kubeletidentity" title="KubeletIdentity">KubeletIdentity</a>: <i>
      - <a href="kubeletidentitydefinition.md">KubeletIdentityDefinition</a></i>
    <a href="#linuxprofile" title="LinuxProfile">LinuxProfile</a>: <i>
      - <a href="linuxprofiledefinition.md">LinuxProfileDefinition</a></i>
    <a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>: <i>
      - <a href="networkprofiledefinition.md">NetworkProfileDefinition</a></i>
    <a href="#rolebasedaccesscontrol" title="RoleBasedAccessControl">RoleBasedAccessControl</a>: <i>
      - <a href="rolebasedaccesscontroldefinition.md">RoleBasedAccessControlDefinition</a></i>
    <a href="#serviceprincipal" title="ServicePrincipal">ServicePrincipal</a>: <i>
      - <a href="serviceprincipaldefinition.md">ServicePrincipalDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#windowsprofile" title="WindowsProfile">WindowsProfile</a>: <i>
      - <a href="windowsprofiledefinition.md">WindowsProfileDefinition</a></i>
</pre>

## Properties

#### ApiServerAuthorizedIpRanges

The IP ranges to whitelist for incoming traffic to the masters.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticChannelUpgrade

The upgrade channel for this Kubernetes Cluster. Possible values are `patch`, `rapid`, and `stable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionSetId

The ID of the Disk Encryption Set which should be used for the Nodes and Volumes. More information [can be found in the documentation](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsPrefix

DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsPrefixPrivateCluster

Specifies the DNS prefix to use with private clusters. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePodSecurityPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeResourceGroup

The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateClusterEnabled

Should this Kubernetes Cluster have its API server only exposed on internal IP addresses? This provides a Private IP Address for the Kubernetes API on the Virtual Network where the Kubernetes Cluster is located. Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateDnsZoneId

Either the ID of Private DNS Zone which should be delegated to this Cluster, `System` to have AKS manage this or `None`. In case of `None` you will need to bring your own DNS server and set up resolving, otherwise cluster will have issues after provisioning.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateLinkEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkuTier

The SKU Tier that should be used for this Kubernetes Cluster. Possible values are `Free` and `Paid` (which includes the Uptime SLA). Defaults to `Free`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddonProfile

_Required_: No

_Type_: List of <a href="addonprofiledefinition.md">AddonProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalerProfile

_Required_: No

_Type_: List of <a href="autoscalerprofiledefinition.md">AutoScalerProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultNodePool

_Required_: No

_Type_: List of <a href="defaultnodepooldefinition.md">DefaultNodePoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeletIdentity

_Required_: No

_Type_: List of <a href="kubeletidentitydefinition.md">KubeletIdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxProfile

_Required_: No

_Type_: List of <a href="linuxprofiledefinition.md">LinuxProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProfile

_Required_: No

_Type_: List of <a href="networkprofiledefinition.md">NetworkProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleBasedAccessControl

_Required_: No

_Type_: List of <a href="rolebasedaccesscontroldefinition.md">RoleBasedAccessControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipal

_Required_: No

_Type_: List of <a href="serviceprincipaldefinition.md">ServicePrincipalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsProfile

_Required_: No

_Type_: List of <a href="windowsprofiledefinition.md">WindowsProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fqdn

Returns the <code>Fqdn</code> value.

#### Id

Returns the <code>Id</code> value.

#### KubeAdminConfig

Returns the <code>KubeAdminConfig</code> value.

#### KubeAdminConfigRaw

Returns the <code>KubeAdminConfigRaw</code> value.

#### KubeConfig

Returns the <code>KubeConfig</code> value.

#### KubeConfigRaw

Returns the <code>KubeConfigRaw</code> value.

#### PrivateFqdn

Returns the <code>PrivateFqdn</code> value.

