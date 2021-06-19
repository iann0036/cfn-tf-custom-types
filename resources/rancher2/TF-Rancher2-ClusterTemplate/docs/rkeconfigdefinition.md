# TF::Rancher2::ClusterTemplate RkeConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addonjobtimeout" title="AddonJobTimeout">AddonJobTimeout</a>" : <i>Double</i>,
    "<a href="#addons" title="Addons">Addons</a>" : <i>String</i>,
    "<a href="#addonsinclude" title="AddonsInclude">AddonsInclude</a>" : <i>[ String, ... ]</i>,
    "<a href="#ignoredockerversion" title="IgnoreDockerVersion">IgnoreDockerVersion</a>" : <i>Boolean</i>,
    "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
    "<a href="#prefixpath" title="PrefixPath">PrefixPath</a>" : <i>String</i>,
    "<a href="#sshagentauth" title="SshAgentAuth">SshAgentAuth</a>" : <i>Boolean</i>,
    "<a href="#sshcertpath" title="SshCertPath">SshCertPath</a>" : <i>String</i>,
    "<a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>" : <i>String</i>,
    "<a href="#winprefixpath" title="WinPrefixPath">WinPrefixPath</a>" : <i>String</i>,
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>[ <a href="authenticationdefinition.md">AuthenticationDefinition</a>, ... ]</i>,
    "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorizationdefinition.md">AuthorizationDefinition</a>, ... ]</i>,
    "<a href="#bastionhost" title="BastionHost">BastionHost</a>" : <i>[ <a href="bastionhostdefinition.md">BastionHostDefinition</a>, ... ]</i>,
    "<a href="#cloudprovider" title="CloudProvider">CloudProvider</a>" : <i>[ <a href="cloudproviderdefinition.md">CloudProviderDefinition</a>, ... ]</i>,
    "<a href="#dns" title="Dns">Dns</a>" : <i>[ <a href="dnsdefinition.md">DnsDefinition</a>, ... ]</i>,
    "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ <a href="ingressdefinition.md">IngressDefinition</a>, ... ]</i>,
    "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>[ <a href="monitoringdefinition.md">MonitoringDefinition</a>, ... ]</i>,
    "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
    "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ <a href="nodesdefinition.md">NodesDefinition</a>, ... ]</i>,
    "<a href="#privateregistries" title="PrivateRegistries">PrivateRegistries</a>" : <i>[ <a href="privateregistriesdefinition.md">PrivateRegistriesDefinition</a>, ... ]</i>,
    "<a href="#services" title="Services">Services</a>" : <i>[ <a href="servicesdefinition.md">ServicesDefinition</a>, ... ]</i>,
    "<a href="#upgradestrategy" title="UpgradeStrategy">UpgradeStrategy</a>" : <i>[ <a href="upgradestrategydefinition.md">UpgradeStrategyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addonjobtimeout" title="AddonJobTimeout">AddonJobTimeout</a>: <i>Double</i>
<a href="#addons" title="Addons">Addons</a>: <i>String</i>
<a href="#addonsinclude" title="AddonsInclude">AddonsInclude</a>: <i>
      - String</i>
<a href="#ignoredockerversion" title="IgnoreDockerVersion">IgnoreDockerVersion</a>: <i>Boolean</i>
<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
<a href="#prefixpath" title="PrefixPath">PrefixPath</a>: <i>String</i>
<a href="#sshagentauth" title="SshAgentAuth">SshAgentAuth</a>: <i>Boolean</i>
<a href="#sshcertpath" title="SshCertPath">SshCertPath</a>: <i>String</i>
<a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>: <i>String</i>
<a href="#winprefixpath" title="WinPrefixPath">WinPrefixPath</a>: <i>String</i>
<a href="#authentication" title="Authentication">Authentication</a>: <i>
      - <a href="authenticationdefinition.md">AuthenticationDefinition</a></i>
<a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorizationdefinition.md">AuthorizationDefinition</a></i>
<a href="#bastionhost" title="BastionHost">BastionHost</a>: <i>
      - <a href="bastionhostdefinition.md">BastionHostDefinition</a></i>
<a href="#cloudprovider" title="CloudProvider">CloudProvider</a>: <i>
      - <a href="cloudproviderdefinition.md">CloudProviderDefinition</a></i>
<a href="#dns" title="Dns">Dns</a>: <i>
      - <a href="dnsdefinition.md">DnsDefinition</a></i>
<a href="#ingress" title="Ingress">Ingress</a>: <i>
      - <a href="ingressdefinition.md">IngressDefinition</a></i>
<a href="#monitoring" title="Monitoring">Monitoring</a>: <i>
      - <a href="monitoringdefinition.md">MonitoringDefinition</a></i>
<a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
<a href="#nodes" title="Nodes">Nodes</a>: <i>
      - <a href="nodesdefinition.md">NodesDefinition</a></i>
<a href="#privateregistries" title="PrivateRegistries">PrivateRegistries</a>: <i>
      - <a href="privateregistriesdefinition.md">PrivateRegistriesDefinition</a></i>
<a href="#services" title="Services">Services</a>: <i>
      - <a href="servicesdefinition.md">ServicesDefinition</a></i>
<a href="#upgradestrategy" title="UpgradeStrategy">UpgradeStrategy</a>: <i>
      - <a href="upgradestrategydefinition.md">UpgradeStrategyDefinition</a></i>
</pre>

## Properties

#### AddonJobTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Addons

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddonsInclude

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreDockerVersion

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshAgentAuth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshCertPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WinPrefixPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: List of <a href="authenticationdefinition.md">AuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

_Required_: No

_Type_: List of <a href="authorizationdefinition.md">AuthorizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BastionHost

_Required_: No

_Type_: List of <a href="bastionhostdefinition.md">BastionHostDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProvider

_Required_: No

_Type_: List of <a href="cloudproviderdefinition.md">CloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of <a href="dnsdefinition.md">DnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of <a href="ingressdefinition.md">IngressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

_Required_: No

_Type_: List of <a href="monitoringdefinition.md">MonitoringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodes

_Required_: No

_Type_: List of <a href="nodesdefinition.md">NodesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateRegistries

_Required_: No

_Type_: List of <a href="privateregistriesdefinition.md">PrivateRegistriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of <a href="servicesdefinition.md">ServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeStrategy

_Required_: No

_Type_: List of <a href="upgradestrategydefinition.md">UpgradeStrategyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

