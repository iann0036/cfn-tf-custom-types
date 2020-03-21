# Terraform::AzureRM::KubernetesCluster

Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text. [Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::KubernetesCluster",
    "Properties" : {
        "<a href="#apiserverauthorizedipranges" title="ApiServerAuthorizedIpRanges">ApiServerAuthorizedIpRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#dnsprefix" title="DnsPrefix">DnsPrefix</a>" : <i>String</i>,
        "<a href="#enablepodsecuritypolicy" title="EnablePodSecurityPolicy">EnablePodSecurityPolicy</a>" : <i>Boolean</i>,
        "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#noderesourcegroup" title="NodeResourceGroup">NodeResourceGroup</a>" : <i>String</i>,
        "<a href="#privatelinkenabled" title="PrivateLinkEnabled">PrivateLinkEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#addonprofile" title="AddonProfile">AddonProfile</a>" : <i>[ <a href="addonprofile.md">AddonProfile</a>, ... ]</i>,
        "<a href="#defaultnodepool" title="DefaultNodePool">DefaultNodePool</a>" : <i>[ <a href="defaultnodepool.md">DefaultNodePool</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#linuxprofile" title="LinuxProfile">LinuxProfile</a>" : <i>[ <a href="linuxprofile.md">LinuxProfile</a>, ... ]</i>,
        "<a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>" : <i>[ <a href="networkprofile.md">NetworkProfile</a>, ... ]</i>,
        "<a href="#rolebasedaccesscontrol" title="RoleBasedAccessControl">RoleBasedAccessControl</a>" : <i>[ <a href="rolebasedaccesscontrol.md">RoleBasedAccessControl</a>, ... ]</i>,
        "<a href="#serviceprincipal" title="ServicePrincipal">ServicePrincipal</a>" : <i>[ <a href="serviceprincipal.md">ServicePrincipal</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#windowsprofile" title="WindowsProfile">WindowsProfile</a>" : <i>[ <a href="windowsprofile.md">WindowsProfile</a>, ... ]</i>,
        "<a href="#aciconnectorlinux" title="AciConnectorLinux">AciConnectorLinux</a>" : <i>[ <a href="aciconnectorlinux.md">AciConnectorLinux</a>, ... ]</i>,
        "<a href="#azurepolicy" title="AzurePolicy">AzurePolicy</a>" : <i>[ <a href="azurepolicy.md">AzurePolicy</a>, ... ]</i>,
        "<a href="#httpapplicationrouting" title="HttpApplicationRouting">HttpApplicationRouting</a>" : <i>[ <a href="httpapplicationrouting.md">HttpApplicationRouting</a>, ... ]</i>,
        "<a href="#kubedashboard" title="KubeDashboard">KubeDashboard</a>" : <i>[ <a href="kubedashboard.md">KubeDashboard</a>, ... ]</i>,
        "<a href="#omsagent" title="OmsAgent">OmsAgent</a>" : <i>[ <a href="omsagent.md">OmsAgent</a>, ... ]</i>,
        "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>[ <a href="sshkey.md">SshKey</a>, ... ]</i>,
        "<a href="#loadbalancerprofile" title="LoadBalancerProfile">LoadBalancerProfile</a>" : <i>[ <a href="loadbalancerprofile.md">LoadBalancerProfile</a>, ... ]</i>,
        "<a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>" : <i>[ <a href="azureactivedirectory.md">AzureActiveDirectory</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::KubernetesCluster
Properties:
    <a href="#apiserverauthorizedipranges" title="ApiServerAuthorizedIpRanges">ApiServerAuthorizedIpRanges</a>: <i>
      - String</i>
    <a href="#dnsprefix" title="DnsPrefix">DnsPrefix</a>: <i>String</i>
    <a href="#enablepodsecuritypolicy" title="EnablePodSecurityPolicy">EnablePodSecurityPolicy</a>: <i>Boolean</i>
    <a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#noderesourcegroup" title="NodeResourceGroup">NodeResourceGroup</a>: <i>String</i>
    <a href="#privatelinkenabled" title="PrivateLinkEnabled">PrivateLinkEnabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#addonprofile" title="AddonProfile">AddonProfile</a>: <i>
      - <a href="addonprofile.md">AddonProfile</a></i>
    <a href="#defaultnodepool" title="DefaultNodePool">DefaultNodePool</a>: <i>
      - <a href="defaultnodepool.md">DefaultNodePool</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#linuxprofile" title="LinuxProfile">LinuxProfile</a>: <i>
      - <a href="linuxprofile.md">LinuxProfile</a></i>
    <a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>: <i>
      - <a href="networkprofile.md">NetworkProfile</a></i>
    <a href="#rolebasedaccesscontrol" title="RoleBasedAccessControl">RoleBasedAccessControl</a>: <i>
      - <a href="rolebasedaccesscontrol.md">RoleBasedAccessControl</a></i>
    <a href="#serviceprincipal" title="ServicePrincipal">ServicePrincipal</a>: <i>
      - <a href="serviceprincipal.md">ServicePrincipal</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#windowsprofile" title="WindowsProfile">WindowsProfile</a>: <i>
      - <a href="windowsprofile.md">WindowsProfile</a></i>
    <a href="#aciconnectorlinux" title="AciConnectorLinux">AciConnectorLinux</a>: <i>
      - <a href="aciconnectorlinux.md">AciConnectorLinux</a></i>
    <a href="#azurepolicy" title="AzurePolicy">AzurePolicy</a>: <i>
      - <a href="azurepolicy.md">AzurePolicy</a></i>
    <a href="#httpapplicationrouting" title="HttpApplicationRouting">HttpApplicationRouting</a>: <i>
      - <a href="httpapplicationrouting.md">HttpApplicationRouting</a></i>
    <a href="#kubedashboard" title="KubeDashboard">KubeDashboard</a>: <i>
      - <a href="kubedashboard.md">KubeDashboard</a></i>
    <a href="#omsagent" title="OmsAgent">OmsAgent</a>: <i>
      - <a href="omsagent.md">OmsAgent</a></i>
    <a href="#sshkey" title="SshKey">SshKey</a>: <i>
      - <a href="sshkey.md">SshKey</a></i>
    <a href="#loadbalancerprofile" title="LoadBalancerProfile">LoadBalancerProfile</a>: <i>
      - <a href="loadbalancerprofile.md">LoadBalancerProfile</a></i>
    <a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>: <i>
      - <a href="azureactivedirectory.md">AzureActiveDirectory</a></i>
</pre>

## Properties

#### ApiServerAuthorizedIpRanges

The IP ranges to whitelist for incoming traffic to the masters.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsPrefix

DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePodSecurityPolicy

Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.

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

#### PrivateLinkEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddonProfile

_Required_: No

_Type_: List of <a href="addonprofile.md">AddonProfile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultNodePool

_Required_: No

_Type_: List of <a href="defaultnodepool.md">DefaultNodePool</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxProfile

_Required_: No

_Type_: List of <a href="linuxprofile.md">LinuxProfile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProfile

_Required_: No

_Type_: List of <a href="networkprofile.md">NetworkProfile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleBasedAccessControl

_Required_: No

_Type_: List of <a href="rolebasedaccesscontrol.md">RoleBasedAccessControl</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipal

_Required_: No

_Type_: List of <a href="serviceprincipal.md">ServicePrincipal</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsProfile

_Required_: No

_Type_: List of <a href="windowsprofile.md">WindowsProfile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AciConnectorLinux

_Required_: No

_Type_: List of <a href="aciconnectorlinux.md">AciConnectorLinux</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurePolicy

_Required_: No

_Type_: List of <a href="azurepolicy.md">AzurePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpApplicationRouting

_Required_: No

_Type_: List of <a href="httpapplicationrouting.md">HttpApplicationRouting</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeDashboard

_Required_: No

_Type_: List of <a href="kubedashboard.md">KubeDashboard</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OmsAgent

_Required_: No

_Type_: List of <a href="omsagent.md">OmsAgent</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

_Required_: No

_Type_: List of <a href="sshkey.md">SshKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerProfile

_Required_: No

_Type_: List of <a href="loadbalancerprofile.md">LoadBalancerProfile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureActiveDirectory

_Required_: No

_Type_: List of <a href="azureactivedirectory.md">AzureActiveDirectory</a>

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

