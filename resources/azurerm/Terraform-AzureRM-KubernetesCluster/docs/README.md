# Terraform::AzureRM::KubernetesCluster

CloudFormation equivalent of azurerm_kubernetes_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::KubernetesCluster",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#apiserverauthorizedipranges" title="ApiServerAuthorizedIpRanges">ApiServerAuthorizedIpRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#dnsprefix" title="DnsPrefix">DnsPrefix</a>" : <i>String</i>,
        "<a href="#enablepodsecuritypolicy" title="EnablePodSecurityPolicy">EnablePodSecurityPolicy</a>" : <i>Boolean</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
        "<a href="#kubeadminconfig" title="KubeAdminConfig">KubeAdminConfig</a>" : <i>[ &lt;a href=&#34;kubeadminconfig.md&#34;&gt;KubeAdminConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#kubeadminconfigraw" title="KubeAdminConfigRaw">KubeAdminConfigRaw</a>" : <i>String</i>,
        "<a href="#kubeconfig" title="KubeConfig">KubeConfig</a>" : <i>[ &lt;a href=&#34;kubeconfig.md&#34;&gt;KubeConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#kubeconfigraw" title="KubeConfigRaw">KubeConfigRaw</a>" : <i>String</i>,
        "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#noderesourcegroup" title="NodeResourceGroup">NodeResourceGroup</a>" : <i>String</i>,
        "<a href="#privatefqdn" title="PrivateFqdn">PrivateFqdn</a>" : <i>String</i>,
        "<a href="#privatelinkenabled" title="PrivateLinkEnabled">PrivateLinkEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#addonprofile" title="AddonProfile">AddonProfile</a>" : <i>[ &lt;a href=&#34;addonprofile.md&#34;&gt;AddonProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#defaultnodepool" title="DefaultNodePool">DefaultNodePool</a>" : <i>[ &lt;a href=&#34;defaultnodepool.md&#34;&gt;DefaultNodePool&lt;/a&gt;, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;, ... ]</i>,
        "<a href="#linuxprofile" title="LinuxProfile">LinuxProfile</a>" : <i>[ &lt;a href=&#34;linuxprofile.md&#34;&gt;LinuxProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>" : <i>[ &lt;a href=&#34;networkprofile.md&#34;&gt;NetworkProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#rolebasedaccesscontrol" title="RoleBasedAccessControl">RoleBasedAccessControl</a>" : <i>[ &lt;a href=&#34;rolebasedaccesscontrol.md&#34;&gt;RoleBasedAccessControl&lt;/a&gt;, ... ]</i>,
        "<a href="#serviceprincipal" title="ServicePrincipal">ServicePrincipal</a>" : <i>[ &lt;a href=&#34;serviceprincipal.md&#34;&gt;ServicePrincipal&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#windowsprofile" title="WindowsProfile">WindowsProfile</a>" : <i>[ &lt;a href=&#34;windowsprofile.md&#34;&gt;WindowsProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#aciconnectorlinux" title="AciConnectorLinux">AciConnectorLinux</a>" : <i>[ &lt;a href=&#34;aciconnectorlinux.md&#34;&gt;AciConnectorLinux&lt;/a&gt;, ... ]</i>,
        "<a href="#azurepolicy" title="AzurePolicy">AzurePolicy</a>" : <i>[ &lt;a href=&#34;azurepolicy.md&#34;&gt;AzurePolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#httpapplicationrouting" title="HttpApplicationRouting">HttpApplicationRouting</a>" : <i>[ &lt;a href=&#34;httpapplicationrouting.md&#34;&gt;HttpApplicationRouting&lt;/a&gt;, ... ]</i>,
        "<a href="#kubedashboard" title="KubeDashboard">KubeDashboard</a>" : <i>[ &lt;a href=&#34;kubedashboard.md&#34;&gt;KubeDashboard&lt;/a&gt;, ... ]</i>,
        "<a href="#omsagent" title="OmsAgent">OmsAgent</a>" : <i>[ &lt;a href=&#34;omsagent.md&#34;&gt;OmsAgent&lt;/a&gt;, ... ]</i>,
        "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>[ &lt;a href=&#34;sshkey.md&#34;&gt;SshKey&lt;/a&gt;, ... ]</i>,
        "<a href="#loadbalancerprofile" title="LoadBalancerProfile">LoadBalancerProfile</a>" : <i>[ &lt;a href=&#34;loadbalancerprofile.md&#34;&gt;LoadBalancerProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>" : <i>[ &lt;a href=&#34;azureactivedirectory.md&#34;&gt;AzureActiveDirectory&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::KubernetesCluster
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#apiserverauthorizedipranges" title="ApiServerAuthorizedIpRanges">ApiServerAuthorizedIpRanges</a>: <i>
      - String</i>
    <a href="#dnsprefix" title="DnsPrefix">DnsPrefix</a>: <i>String</i>
    <a href="#enablepodsecuritypolicy" title="EnablePodSecurityPolicy">EnablePodSecurityPolicy</a>: <i>Boolean</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
    <a href="#kubeadminconfig" title="KubeAdminConfig">KubeAdminConfig</a>: <i>
      - &lt;a href=&#34;kubeadminconfig.md&#34;&gt;KubeAdminConfig&lt;/a&gt;</i>
    <a href="#kubeadminconfigraw" title="KubeAdminConfigRaw">KubeAdminConfigRaw</a>: <i>String</i>
    <a href="#kubeconfig" title="KubeConfig">KubeConfig</a>: <i>
      - &lt;a href=&#34;kubeconfig.md&#34;&gt;KubeConfig&lt;/a&gt;</i>
    <a href="#kubeconfigraw" title="KubeConfigRaw">KubeConfigRaw</a>: <i>String</i>
    <a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#noderesourcegroup" title="NodeResourceGroup">NodeResourceGroup</a>: <i>String</i>
    <a href="#privatefqdn" title="PrivateFqdn">PrivateFqdn</a>: <i>String</i>
    <a href="#privatelinkenabled" title="PrivateLinkEnabled">PrivateLinkEnabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#addonprofile" title="AddonProfile">AddonProfile</a>: <i>
      - &lt;a href=&#34;addonprofile.md&#34;&gt;AddonProfile&lt;/a&gt;</i>
    <a href="#defaultnodepool" title="DefaultNodePool">DefaultNodePool</a>: <i>
      - &lt;a href=&#34;defaultnodepool.md&#34;&gt;DefaultNodePool&lt;/a&gt;</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;</i>
    <a href="#linuxprofile" title="LinuxProfile">LinuxProfile</a>: <i>
      - &lt;a href=&#34;linuxprofile.md&#34;&gt;LinuxProfile&lt;/a&gt;</i>
    <a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>: <i>
      - &lt;a href=&#34;networkprofile.md&#34;&gt;NetworkProfile&lt;/a&gt;</i>
    <a href="#rolebasedaccesscontrol" title="RoleBasedAccessControl">RoleBasedAccessControl</a>: <i>
      - &lt;a href=&#34;rolebasedaccesscontrol.md&#34;&gt;RoleBasedAccessControl&lt;/a&gt;</i>
    <a href="#serviceprincipal" title="ServicePrincipal">ServicePrincipal</a>: <i>
      - &lt;a href=&#34;serviceprincipal.md&#34;&gt;ServicePrincipal&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#windowsprofile" title="WindowsProfile">WindowsProfile</a>: <i>
      - &lt;a href=&#34;windowsprofile.md&#34;&gt;WindowsProfile&lt;/a&gt;</i>
    <a href="#aciconnectorlinux" title="AciConnectorLinux">AciConnectorLinux</a>: <i>
      - &lt;a href=&#34;aciconnectorlinux.md&#34;&gt;AciConnectorLinux&lt;/a&gt;</i>
    <a href="#azurepolicy" title="AzurePolicy">AzurePolicy</a>: <i>
      - &lt;a href=&#34;azurepolicy.md&#34;&gt;AzurePolicy&lt;/a&gt;</i>
    <a href="#httpapplicationrouting" title="HttpApplicationRouting">HttpApplicationRouting</a>: <i>
      - &lt;a href=&#34;httpapplicationrouting.md&#34;&gt;HttpApplicationRouting&lt;/a&gt;</i>
    <a href="#kubedashboard" title="KubeDashboard">KubeDashboard</a>: <i>
      - &lt;a href=&#34;kubedashboard.md&#34;&gt;KubeDashboard&lt;/a&gt;</i>
    <a href="#omsagent" title="OmsAgent">OmsAgent</a>: <i>
      - &lt;a href=&#34;omsagent.md&#34;&gt;OmsAgent&lt;/a&gt;</i>
    <a href="#sshkey" title="SshKey">SshKey</a>: <i>
      - &lt;a href=&#34;sshkey.md&#34;&gt;SshKey&lt;/a&gt;</i>
    <a href="#loadbalancerprofile" title="LoadBalancerProfile">LoadBalancerProfile</a>: <i>
      - &lt;a href=&#34;loadbalancerprofile.md&#34;&gt;LoadBalancerProfile&lt;/a&gt;</i>
    <a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>: <i>
      - &lt;a href=&#34;azureactivedirectory.md&#34;&gt;AzureActiveDirectory&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiServerAuthorizedIpRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePodSecurityPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeAdminConfig

_Required_: No

_Type_: List of &lt;a href=&#34;kubeadminconfig.md&#34;&gt;KubeAdminConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeAdminConfigRaw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeConfig

_Required_: No

_Type_: List of &lt;a href=&#34;kubeconfig.md&#34;&gt;KubeConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeConfigRaw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeResourceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateFqdn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateLinkEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddonProfile

_Required_: No

_Type_: List of &lt;a href=&#34;addonprofile.md&#34;&gt;AddonProfile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultNodePool

_Required_: No

_Type_: List of &lt;a href=&#34;defaultnodepool.md&#34;&gt;DefaultNodePool&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxProfile

_Required_: No

_Type_: List of &lt;a href=&#34;linuxprofile.md&#34;&gt;LinuxProfile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProfile

_Required_: No

_Type_: List of &lt;a href=&#34;networkprofile.md&#34;&gt;NetworkProfile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleBasedAccessControl

_Required_: No

_Type_: List of &lt;a href=&#34;rolebasedaccesscontrol.md&#34;&gt;RoleBasedAccessControl&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipal

_Required_: No

_Type_: List of &lt;a href=&#34;serviceprincipal.md&#34;&gt;ServicePrincipal&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsProfile

_Required_: No

_Type_: List of &lt;a href=&#34;windowsprofile.md&#34;&gt;WindowsProfile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AciConnectorLinux

_Required_: No

_Type_: List of &lt;a href=&#34;aciconnectorlinux.md&#34;&gt;AciConnectorLinux&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;azurepolicy.md&#34;&gt;AzurePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpApplicationRouting

_Required_: No

_Type_: List of &lt;a href=&#34;httpapplicationrouting.md&#34;&gt;HttpApplicationRouting&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeDashboard

_Required_: No

_Type_: List of &lt;a href=&#34;kubedashboard.md&#34;&gt;KubeDashboard&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OmsAgent

_Required_: No

_Type_: List of &lt;a href=&#34;omsagent.md&#34;&gt;OmsAgent&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

_Required_: No

_Type_: List of &lt;a href=&#34;sshkey.md&#34;&gt;SshKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerProfile

_Required_: No

_Type_: List of &lt;a href=&#34;loadbalancerprofile.md&#34;&gt;LoadBalancerProfile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureActiveDirectory

_Required_: No

_Type_: List of &lt;a href=&#34;azureactivedirectory.md&#34;&gt;AzureActiveDirectory&lt;/a&gt;

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

Returns the &lt;code&gt;Fqdn&lt;/code&gt; value.

#### KubeAdminConfig

Returns the &lt;code&gt;KubeAdminConfig&lt;/code&gt; value.

#### KubeAdminConfigRaw

Returns the &lt;code&gt;KubeAdminConfigRaw&lt;/code&gt; value.

#### KubeConfig

Returns the &lt;code&gt;KubeConfig&lt;/code&gt; value.

#### KubeConfigRaw

Returns the &lt;code&gt;KubeConfigRaw&lt;/code&gt; value.

#### PrivateFqdn

Returns the &lt;code&gt;PrivateFqdn&lt;/code&gt; value.

