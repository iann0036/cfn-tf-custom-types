# TF::RKE::Cluster

Provides RKE cluster resource. This can be used to create RKE clusters and retrieve their information.

RKE clusters can be defined in the provider:
- Using cluster_yaml: The full RKE cluster is defined in an RKE cluster.yml file.
- Using the TF provider arguments to define the entire cluster.
- Using a combination of both the cluster_yaml and TF provider arguments. The TF arguments will override the cluster_yaml options if collisions occur.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::RKE::Cluster",
    "Properties" : {
        "<a href="#addonjobtimeout" title="AddonJobTimeout">AddonJobTimeout</a>" : <i>Double</i>,
        "<a href="#addons" title="Addons">Addons</a>" : <i>String</i>,
        "<a href="#addonsinclude" title="AddonsInclude">AddonsInclude</a>" : <i>[ String, ... ]</i>,
        "<a href="#certdir" title="CertDir">CertDir</a>" : <i>String</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#clusteryaml" title="ClusterYaml">ClusterYaml</a>" : <i>String</i>,
        "<a href="#customcerts" title="CustomCerts">CustomCerts</a>" : <i>Boolean</i>,
        "<a href="#delayoncreation" title="DelayOnCreation">DelayOnCreation</a>" : <i>Double</i>,
        "<a href="#dind" title="Dind">Dind</a>" : <i>Boolean</i>,
        "<a href="#dinddnsserver" title="DindDnsServer">DindDnsServer</a>" : <i>String</i>,
        "<a href="#dindstoragedriver" title="DindStorageDriver">DindStorageDriver</a>" : <i>String</i>,
        "<a href="#disableportcheck" title="DisablePortCheck">DisablePortCheck</a>" : <i>Boolean</i>,
        "<a href="#ignoredockerversion" title="IgnoreDockerVersion">IgnoreDockerVersion</a>" : <i>Boolean</i>,
        "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
        "<a href="#nodesconf" title="NodesConf">NodesConf</a>" : <i>[ String, ... ]</i>,
        "<a href="#prefixpath" title="PrefixPath">PrefixPath</a>" : <i>String</i>,
        "<a href="#sshagentauth" title="SshAgentAuth">SshAgentAuth</a>" : <i>Boolean</i>,
        "<a href="#sshcertpath" title="SshCertPath">SshCertPath</a>" : <i>String</i>,
        "<a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>" : <i>String</i>,
        "<a href="#updateonly" title="UpdateOnly">UpdateOnly</a>" : <i>Boolean</i>,
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
        "<a href="#restore" title="Restore">Restore</a>" : <i>[ <a href="restoredefinition.md">RestoreDefinition</a>, ... ]</i>,
        "<a href="#rotatecertificates" title="RotateCertificates">RotateCertificates</a>" : <i>[ <a href="rotatecertificatesdefinition.md">RotateCertificatesDefinition</a>, ... ]</i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ <a href="servicesdefinition.md">ServicesDefinition</a>, ... ]</i>,
        "<a href="#servicesetcd" title="ServicesEtcd">ServicesEtcd</a>" : <i>[ <a href="servicesetcddefinition.md">ServicesEtcdDefinition</a>, ... ]</i>,
        "<a href="#serviceskubeapi" title="ServicesKubeApi">ServicesKubeApi</a>" : <i>[ <a href="serviceskubeapidefinition.md">ServicesKubeApiDefinition</a>, ... ]</i>,
        "<a href="#serviceskubecontroller" title="ServicesKubeController">ServicesKubeController</a>" : <i>[ <a href="serviceskubecontrollerdefinition.md">ServicesKubeControllerDefinition</a>, ... ]</i>,
        "<a href="#serviceskubelet" title="ServicesKubelet">ServicesKubelet</a>" : <i>[ <a href="serviceskubeletdefinition.md">ServicesKubeletDefinition</a>, ... ]</i>,
        "<a href="#serviceskubeproxy" title="ServicesKubeproxy">ServicesKubeproxy</a>" : <i>[ <a href="serviceskubeproxydefinition.md">ServicesKubeproxyDefinition</a>, ... ]</i>,
        "<a href="#servicesscheduler" title="ServicesScheduler">ServicesScheduler</a>" : <i>[ <a href="servicesschedulerdefinition.md">ServicesSchedulerDefinition</a>, ... ]</i>,
        "<a href="#systemimages" title="SystemImages">SystemImages</a>" : <i>[ <a href="systemimagesdefinition.md">SystemImagesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#upgradestrategy" title="UpgradeStrategy">UpgradeStrategy</a>" : <i>[ <a href="upgradestrategydefinition.md">UpgradeStrategyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::RKE::Cluster
Properties:
    <a href="#addonjobtimeout" title="AddonJobTimeout">AddonJobTimeout</a>: <i>Double</i>
    <a href="#addons" title="Addons">Addons</a>: <i>String</i>
    <a href="#addonsinclude" title="AddonsInclude">AddonsInclude</a>: <i>
      - String</i>
    <a href="#certdir" title="CertDir">CertDir</a>: <i>String</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#clusteryaml" title="ClusterYaml">ClusterYaml</a>: <i>String</i>
    <a href="#customcerts" title="CustomCerts">CustomCerts</a>: <i>Boolean</i>
    <a href="#delayoncreation" title="DelayOnCreation">DelayOnCreation</a>: <i>Double</i>
    <a href="#dind" title="Dind">Dind</a>: <i>Boolean</i>
    <a href="#dinddnsserver" title="DindDnsServer">DindDnsServer</a>: <i>String</i>
    <a href="#dindstoragedriver" title="DindStorageDriver">DindStorageDriver</a>: <i>String</i>
    <a href="#disableportcheck" title="DisablePortCheck">DisablePortCheck</a>: <i>Boolean</i>
    <a href="#ignoredockerversion" title="IgnoreDockerVersion">IgnoreDockerVersion</a>: <i>Boolean</i>
    <a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
    <a href="#nodesconf" title="NodesConf">NodesConf</a>: <i>
      - String</i>
    <a href="#prefixpath" title="PrefixPath">PrefixPath</a>: <i>String</i>
    <a href="#sshagentauth" title="SshAgentAuth">SshAgentAuth</a>: <i>Boolean</i>
    <a href="#sshcertpath" title="SshCertPath">SshCertPath</a>: <i>String</i>
    <a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>: <i>String</i>
    <a href="#updateonly" title="UpdateOnly">UpdateOnly</a>: <i>Boolean</i>
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
    <a href="#restore" title="Restore">Restore</a>: <i>
      - <a href="restoredefinition.md">RestoreDefinition</a></i>
    <a href="#rotatecertificates" title="RotateCertificates">RotateCertificates</a>: <i>
      - <a href="rotatecertificatesdefinition.md">RotateCertificatesDefinition</a></i>
    <a href="#services" title="Services">Services</a>: <i>
      - <a href="servicesdefinition.md">ServicesDefinition</a></i>
    <a href="#servicesetcd" title="ServicesEtcd">ServicesEtcd</a>: <i>
      - <a href="servicesetcddefinition.md">ServicesEtcdDefinition</a></i>
    <a href="#serviceskubeapi" title="ServicesKubeApi">ServicesKubeApi</a>: <i>
      - <a href="serviceskubeapidefinition.md">ServicesKubeApiDefinition</a></i>
    <a href="#serviceskubecontroller" title="ServicesKubeController">ServicesKubeController</a>: <i>
      - <a href="serviceskubecontrollerdefinition.md">ServicesKubeControllerDefinition</a></i>
    <a href="#serviceskubelet" title="ServicesKubelet">ServicesKubelet</a>: <i>
      - <a href="serviceskubeletdefinition.md">ServicesKubeletDefinition</a></i>
    <a href="#serviceskubeproxy" title="ServicesKubeproxy">ServicesKubeproxy</a>: <i>
      - <a href="serviceskubeproxydefinition.md">ServicesKubeproxyDefinition</a></i>
    <a href="#servicesscheduler" title="ServicesScheduler">ServicesScheduler</a>: <i>
      - <a href="servicesschedulerdefinition.md">ServicesSchedulerDefinition</a></i>
    <a href="#systemimages" title="SystemImages">SystemImages</a>: <i>
      - <a href="systemimagesdefinition.md">SystemImagesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#upgradestrategy" title="UpgradeStrategy">UpgradeStrategy</a>: <i>
      - <a href="upgradestrategydefinition.md">UpgradeStrategyDefinition</a></i>
</pre>

## Properties

#### AddonJobTimeout

RKE k8s cluster addon deployment timeout in seconds for status check (int).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Addons

RKE k8s cluster user addons YAML manifest to be deployed (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddonsInclude

RKE k8s cluster user addons YAML manifest urls or paths to be deployed (list).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertDir

Specify a certificate dir path (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

RKE k8s cluster name used in the kube config (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterYaml

RKE k8s cluster config yaml encoded. Provider arguments take precedence over this one (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCerts

Use custom certificates from a cert dir (string).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayOnCreation

RKE k8s cluster delay on creation (int).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dind

Deploy RKE cluster on a dind environment. Default: `false` (bool).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DindDnsServer

DinD RKE cluster dns (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DindStorageDriver

DinD RKE cluster storage driver (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisablePortCheck

Enable/Disable RKE k8s cluster port checking. Default `false` (bool).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreDockerVersion

Enable/Disable RKE k8s cluster strict docker version checking. Default `false` (bool).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

K8s version to deploy. If kubernetes image is specified, image version takes precedence. Default: `rke default` (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodesConf

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixPath

RKE k8s directory path (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshAgentAuth

SSH Agent Auth enable (bool).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshCertPath

SSH Certificate Path (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyPath

SSH Private Key Path (string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateOnly

Skip idempotent deployment of control and etcd plane. Default `false` (bool).

_Required_: No

_Type_: Boolean

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

#### Restore

_Required_: No

_Type_: List of <a href="restoredefinition.md">RestoreDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotateCertificates

_Required_: No

_Type_: List of <a href="rotatecertificatesdefinition.md">RotateCertificatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of <a href="servicesdefinition.md">ServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesEtcd

_Required_: No

_Type_: List of <a href="servicesetcddefinition.md">ServicesEtcdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesKubeApi

_Required_: No

_Type_: List of <a href="serviceskubeapidefinition.md">ServicesKubeApiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesKubeController

_Required_: No

_Type_: List of <a href="serviceskubecontrollerdefinition.md">ServicesKubeControllerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesKubelet

_Required_: No

_Type_: List of <a href="serviceskubeletdefinition.md">ServicesKubeletDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesKubeproxy

_Required_: No

_Type_: List of <a href="serviceskubeproxydefinition.md">ServicesKubeproxyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesScheduler

_Required_: No

_Type_: List of <a href="servicesschedulerdefinition.md">ServicesSchedulerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemImages

_Required_: No

_Type_: List of <a href="systemimagesdefinition.md">SystemImagesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeStrategy

_Required_: No

_Type_: List of <a href="upgradestrategydefinition.md">UpgradeStrategyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiServerUrl

Returns the <code>ApiServerUrl</code> value.

#### CaCrt

Returns the <code>CaCrt</code> value.

#### Certificates

Returns the <code>Certificates</code> value.

#### ClientCert

Returns the <code>ClientCert</code> value.

#### ClientKey

Returns the <code>ClientKey</code> value.

#### ClusterCidr

Returns the <code>ClusterCidr</code> value.

#### ClusterDnsServer

Returns the <code>ClusterDnsServer</code> value.

#### ClusterDomain

Returns the <code>ClusterDomain</code> value.

#### ControlPlaneHosts

Returns the <code>ControlPlaneHosts</code> value.

#### EtcdHosts

Returns the <code>EtcdHosts</code> value.

#### Id

Returns the <code>Id</code> value.

#### InactiveHosts

Returns the <code>InactiveHosts</code> value.

#### InternalKubeConfigYaml

Returns the <code>InternalKubeConfigYaml</code> value.

#### KubeAdminUser

Returns the <code>KubeAdminUser</code> value.

#### KubeConfigYaml

Returns the <code>KubeConfigYaml</code> value.

#### RkeClusterYaml

Returns the <code>RkeClusterYaml</code> value.

#### RkeState

Returns the <code>RkeState</code> value.

#### RunningSystemImages

Returns the <code>RunningSystemImages</code> value.

#### WorkerHosts

Returns the <code>WorkerHosts</code> value.

