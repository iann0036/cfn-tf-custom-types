# TF::Kubernetes::CronJob SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activedeadlineseconds" title="ActiveDeadlineSeconds">ActiveDeadlineSeconds</a>" : <i>Double</i>,
    "<a href="#automountserviceaccounttoken" title="AutomountServiceAccountToken">AutomountServiceAccountToken</a>" : <i>Boolean</i>,
    "<a href="#dnspolicy" title="DnsPolicy">DnsPolicy</a>" : <i>String</i>,
    "<a href="#enableservicelinks" title="EnableServiceLinks">EnableServiceLinks</a>" : <i>Boolean</i>,
    "<a href="#hostipc" title="HostIpc">HostIpc</a>" : <i>Boolean</i>,
    "<a href="#hostnetwork" title="HostNetwork">HostNetwork</a>" : <i>Boolean</i>,
    "<a href="#hostpid" title="HostPid">HostPid</a>" : <i>Boolean</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#nodename" title="NodeName">NodeName</a>" : <i>String</i>,
    "<a href="#nodeselector" title="NodeSelector">NodeSelector</a>" : <i>[ <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>, ... ]</i>,
    "<a href="#priorityclassname" title="PriorityClassName">PriorityClassName</a>" : <i>String</i>,
    "<a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>" : <i>String</i>,
    "<a href="#serviceaccountname" title="ServiceAccountName">ServiceAccountName</a>" : <i>String</i>,
    "<a href="#shareprocessnamespace" title="ShareProcessNamespace">ShareProcessNamespace</a>" : <i>Boolean</i>,
    "<a href="#subdomain" title="Subdomain">Subdomain</a>" : <i>String</i>,
    "<a href="#terminationgraceperiodseconds" title="TerminationGracePeriodSeconds">TerminationGracePeriodSeconds</a>" : <i>Double</i>,
    "<a href="#affinity" title="Affinity">Affinity</a>" : <i>[ <a href="affinitydefinition.md">AffinityDefinition</a>, ... ]</i>,
    "<a href="#container" title="Container">Container</a>" : <i>[ <a href="containerdefinition.md">ContainerDefinition</a>, ... ]</i>,
    "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ <a href="dnsconfigdefinition.md">DnsConfigDefinition</a>, ... ]</i>,
    "<a href="#hostaliases" title="HostAliases">HostAliases</a>" : <i>[ <a href="hostaliasesdefinition.md">HostAliasesDefinition</a>, ... ]</i>,
    "<a href="#imagepullsecrets" title="ImagePullSecrets">ImagePullSecrets</a>" : <i>[ <a href="imagepullsecretsdefinition.md">ImagePullSecretsDefinition</a>, ... ]</i>,
    "<a href="#initcontainer" title="InitContainer">InitContainer</a>" : <i>[ <a href="initcontainerdefinition.md">InitContainerDefinition</a>, ... ]</i>,
    "<a href="#readinessgate" title="ReadinessGate">ReadinessGate</a>" : <i>[ <a href="readinessgatedefinition.md">ReadinessGateDefinition</a>, ... ]</i>,
    "<a href="#securitycontext" title="SecurityContext">SecurityContext</a>" : <i>[ <a href="securitycontextdefinition.md">SecurityContextDefinition</a>, ... ]</i>,
    "<a href="#toleration" title="Toleration">Toleration</a>" : <i>[ <a href="tolerationdefinition.md">TolerationDefinition</a>, ... ]</i>,
    "<a href="#topologyspreadconstraint" title="TopologySpreadConstraint">TopologySpreadConstraint</a>" : <i>[ <a href="topologyspreadconstraintdefinition.md">TopologySpreadConstraintDefinition</a>, ... ]</i>,
    "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volumedefinition.md">VolumeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#activedeadlineseconds" title="ActiveDeadlineSeconds">ActiveDeadlineSeconds</a>: <i>Double</i>
<a href="#automountserviceaccounttoken" title="AutomountServiceAccountToken">AutomountServiceAccountToken</a>: <i>Boolean</i>
<a href="#dnspolicy" title="DnsPolicy">DnsPolicy</a>: <i>String</i>
<a href="#enableservicelinks" title="EnableServiceLinks">EnableServiceLinks</a>: <i>Boolean</i>
<a href="#hostipc" title="HostIpc">HostIpc</a>: <i>Boolean</i>
<a href="#hostnetwork" title="HostNetwork">HostNetwork</a>: <i>Boolean</i>
<a href="#hostpid" title="HostPid">HostPid</a>: <i>Boolean</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#nodename" title="NodeName">NodeName</a>: <i>String</i>
<a href="#nodeselector" title="NodeSelector">NodeSelector</a>: <i>
      - <a href="nodeselectordefinition.md">NodeSelectorDefinition</a></i>
<a href="#priorityclassname" title="PriorityClassName">PriorityClassName</a>: <i>String</i>
<a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>: <i>String</i>
<a href="#serviceaccountname" title="ServiceAccountName">ServiceAccountName</a>: <i>String</i>
<a href="#shareprocessnamespace" title="ShareProcessNamespace">ShareProcessNamespace</a>: <i>Boolean</i>
<a href="#subdomain" title="Subdomain">Subdomain</a>: <i>String</i>
<a href="#terminationgraceperiodseconds" title="TerminationGracePeriodSeconds">TerminationGracePeriodSeconds</a>: <i>Double</i>
<a href="#affinity" title="Affinity">Affinity</a>: <i>
      - <a href="affinitydefinition.md">AffinityDefinition</a></i>
<a href="#container" title="Container">Container</a>: <i>
      - <a href="containerdefinition.md">ContainerDefinition</a></i>
<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - <a href="dnsconfigdefinition.md">DnsConfigDefinition</a></i>
<a href="#hostaliases" title="HostAliases">HostAliases</a>: <i>
      - <a href="hostaliasesdefinition.md">HostAliasesDefinition</a></i>
<a href="#imagepullsecrets" title="ImagePullSecrets">ImagePullSecrets</a>: <i>
      - <a href="imagepullsecretsdefinition.md">ImagePullSecretsDefinition</a></i>
<a href="#initcontainer" title="InitContainer">InitContainer</a>: <i>
      - <a href="initcontainerdefinition.md">InitContainerDefinition</a></i>
<a href="#readinessgate" title="ReadinessGate">ReadinessGate</a>: <i>
      - <a href="readinessgatedefinition.md">ReadinessGateDefinition</a></i>
<a href="#securitycontext" title="SecurityContext">SecurityContext</a>: <i>
      - <a href="securitycontextdefinition.md">SecurityContextDefinition</a></i>
<a href="#toleration" title="Toleration">Toleration</a>: <i>
      - <a href="tolerationdefinition.md">TolerationDefinition</a></i>
<a href="#topologyspreadconstraint" title="TopologySpreadConstraint">TopologySpreadConstraint</a>: <i>
      - <a href="topologyspreadconstraintdefinition.md">TopologySpreadConstraintDefinition</a></i>
<a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volumedefinition.md">VolumeDefinition</a></i>
</pre>

## Properties

#### ActiveDeadlineSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomountServiceAccountToken

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableServiceLinks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostIpc

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPid

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeSelector

_Required_: No

_Type_: List of <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityClassName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareProcessNamespace

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subdomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationGracePeriodSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Affinity

_Required_: No

_Type_: List of <a href="affinitydefinition.md">AffinityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of <a href="containerdefinition.md">ContainerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No

_Type_: List of <a href="dnsconfigdefinition.md">DnsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostAliases

_Required_: No

_Type_: List of <a href="hostaliasesdefinition.md">HostAliasesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullSecrets

_Required_: No

_Type_: List of <a href="imagepullsecretsdefinition.md">ImagePullSecretsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitContainer

_Required_: No

_Type_: List of <a href="initcontainerdefinition.md">InitContainerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessGate

_Required_: No

_Type_: List of <a href="readinessgatedefinition.md">ReadinessGateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityContext

_Required_: No

_Type_: List of <a href="securitycontextdefinition.md">SecurityContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Toleration

_Required_: No

_Type_: List of <a href="tolerationdefinition.md">TolerationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologySpreadConstraint

_Required_: No

_Type_: List of <a href="topologyspreadconstraintdefinition.md">TopologySpreadConstraintDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of <a href="volumedefinition.md">VolumeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

