# TF::Rancher2::Cluster

CloudFormation equivalent of rancher2_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::Cluster",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#clustertemplateid" title="ClusterTemplateId">ClusterTemplateId</a>" : <i>String</i>,
        "<a href="#clustertemplaterevisionid" title="ClusterTemplateRevisionId">ClusterTemplateRevisionId</a>" : <i>String</i>,
        "<a href="#defaultpodsecuritypolicytemplateid" title="DefaultPodSecurityPolicyTemplateId">DefaultPodSecurityPolicyTemplateId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredagentimage" title="DesiredAgentImage">DesiredAgentImage</a>" : <i>String</i>,
        "<a href="#desiredauthimage" title="DesiredAuthImage">DesiredAuthImage</a>" : <i>String</i>,
        "<a href="#dockerrootdir" title="DockerRootDir">DockerRootDir</a>" : <i>String</i>,
        "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
        "<a href="#enableclusteralerting" title="EnableClusterAlerting">EnableClusterAlerting</a>" : <i>Boolean</i>,
        "<a href="#enableclustermonitoring" title="EnableClusterMonitoring">EnableClusterMonitoring</a>" : <i>Boolean</i>,
        "<a href="#enablenetworkpolicy" title="EnableNetworkPolicy">EnableNetworkPolicy</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#windowspreferedcluster" title="WindowsPreferedCluster">WindowsPreferedCluster</a>" : <i>Boolean</i>,
        "<a href="#agentenvvars" title="AgentEnvVars">AgentEnvVars</a>" : <i>[ <a href="agentenvvarsdefinition.md">AgentEnvVarsDefinition</a>, ... ]</i>,
        "<a href="#aksconfig" title="AksConfig">AksConfig</a>" : <i>[ <a href="aksconfigdefinition.md">AksConfigDefinition</a>, ... ]</i>,
        "<a href="#clusterauthendpoint" title="ClusterAuthEndpoint">ClusterAuthEndpoint</a>" : <i>[ <a href="clusterauthendpointdefinition.md">ClusterAuthEndpointDefinition</a>, ... ]</i>,
        "<a href="#clustermonitoringinput" title="ClusterMonitoringInput">ClusterMonitoringInput</a>" : <i>[ <a href="clustermonitoringinputdefinition.md">ClusterMonitoringInputDefinition</a>, ... ]</i>,
        "<a href="#clustertemplateanswers" title="ClusterTemplateAnswers">ClusterTemplateAnswers</a>" : <i>[ <a href="clustertemplateanswersdefinition.md">ClusterTemplateAnswersDefinition</a>, ... ]</i>,
        "<a href="#clustertemplatequestions" title="ClusterTemplateQuestions">ClusterTemplateQuestions</a>" : <i>[ <a href="clustertemplatequestionsdefinition.md">ClusterTemplateQuestionsDefinition</a>, ... ]</i>,
        "<a href="#eksconfig" title="EksConfig">EksConfig</a>" : <i>[ <a href="eksconfigdefinition.md">EksConfigDefinition</a>, ... ]</i>,
        "<a href="#eksconfigv2" title="EksConfigV2">EksConfigV2</a>" : <i>[ <a href="eksconfigv2definition.md">EksConfigV2Definition</a>, ... ]</i>,
        "<a href="#gkeconfig" title="GkeConfig">GkeConfig</a>" : <i>[ <a href="gkeconfigdefinition.md">GkeConfigDefinition</a>, ... ]</i>,
        "<a href="#gkeconfigv2" title="GkeConfigV2">GkeConfigV2</a>" : <i>[ <a href="gkeconfigv2definition.md">GkeConfigV2Definition</a>, ... ]</i>,
        "<a href="#k3sconfig" title="K3sConfig">K3sConfig</a>" : <i>[ <a href="k3sconfigdefinition.md">K3sConfigDefinition</a>, ... ]</i>,
        "<a href="#okeconfig" title="OkeConfig">OkeConfig</a>" : <i>[ <a href="okeconfigdefinition.md">OkeConfigDefinition</a>, ... ]</i>,
        "<a href="#rke2config" title="Rke2Config">Rke2Config</a>" : <i>[ <a href="rke2configdefinition.md">Rke2ConfigDefinition</a>, ... ]</i>,
        "<a href="#rkeconfig" title="RkeConfig">RkeConfig</a>" : <i>[ <a href="rkeconfigdefinition.md">RkeConfigDefinition</a>, ... ]</i>,
        "<a href="#scheduledclusterscan" title="ScheduledClusterScan">ScheduledClusterScan</a>" : <i>[ <a href="scheduledclusterscandefinition.md">ScheduledClusterScanDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::Cluster
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#clustertemplateid" title="ClusterTemplateId">ClusterTemplateId</a>: <i>String</i>
    <a href="#clustertemplaterevisionid" title="ClusterTemplateRevisionId">ClusterTemplateRevisionId</a>: <i>String</i>
    <a href="#defaultpodsecuritypolicytemplateid" title="DefaultPodSecurityPolicyTemplateId">DefaultPodSecurityPolicyTemplateId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredagentimage" title="DesiredAgentImage">DesiredAgentImage</a>: <i>String</i>
    <a href="#desiredauthimage" title="DesiredAuthImage">DesiredAuthImage</a>: <i>String</i>
    <a href="#dockerrootdir" title="DockerRootDir">DockerRootDir</a>: <i>String</i>
    <a href="#driver" title="Driver">Driver</a>: <i>String</i>
    <a href="#enableclusteralerting" title="EnableClusterAlerting">EnableClusterAlerting</a>: <i>Boolean</i>
    <a href="#enableclustermonitoring" title="EnableClusterMonitoring">EnableClusterMonitoring</a>: <i>Boolean</i>
    <a href="#enablenetworkpolicy" title="EnableNetworkPolicy">EnableNetworkPolicy</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#windowspreferedcluster" title="WindowsPreferedCluster">WindowsPreferedCluster</a>: <i>Boolean</i>
    <a href="#agentenvvars" title="AgentEnvVars">AgentEnvVars</a>: <i>
      - <a href="agentenvvarsdefinition.md">AgentEnvVarsDefinition</a></i>
    <a href="#aksconfig" title="AksConfig">AksConfig</a>: <i>
      - <a href="aksconfigdefinition.md">AksConfigDefinition</a></i>
    <a href="#clusterauthendpoint" title="ClusterAuthEndpoint">ClusterAuthEndpoint</a>: <i>
      - <a href="clusterauthendpointdefinition.md">ClusterAuthEndpointDefinition</a></i>
    <a href="#clustermonitoringinput" title="ClusterMonitoringInput">ClusterMonitoringInput</a>: <i>
      - <a href="clustermonitoringinputdefinition.md">ClusterMonitoringInputDefinition</a></i>
    <a href="#clustertemplateanswers" title="ClusterTemplateAnswers">ClusterTemplateAnswers</a>: <i>
      - <a href="clustertemplateanswersdefinition.md">ClusterTemplateAnswersDefinition</a></i>
    <a href="#clustertemplatequestions" title="ClusterTemplateQuestions">ClusterTemplateQuestions</a>: <i>
      - <a href="clustertemplatequestionsdefinition.md">ClusterTemplateQuestionsDefinition</a></i>
    <a href="#eksconfig" title="EksConfig">EksConfig</a>: <i>
      - <a href="eksconfigdefinition.md">EksConfigDefinition</a></i>
    <a href="#eksconfigv2" title="EksConfigV2">EksConfigV2</a>: <i>
      - <a href="eksconfigv2definition.md">EksConfigV2Definition</a></i>
    <a href="#gkeconfig" title="GkeConfig">GkeConfig</a>: <i>
      - <a href="gkeconfigdefinition.md">GkeConfigDefinition</a></i>
    <a href="#gkeconfigv2" title="GkeConfigV2">GkeConfigV2</a>: <i>
      - <a href="gkeconfigv2definition.md">GkeConfigV2Definition</a></i>
    <a href="#k3sconfig" title="K3sConfig">K3sConfig</a>: <i>
      - <a href="k3sconfigdefinition.md">K3sConfigDefinition</a></i>
    <a href="#okeconfig" title="OkeConfig">OkeConfig</a>: <i>
      - <a href="okeconfigdefinition.md">OkeConfigDefinition</a></i>
    <a href="#rke2config" title="Rke2Config">Rke2Config</a>: <i>
      - <a href="rke2configdefinition.md">Rke2ConfigDefinition</a></i>
    <a href="#rkeconfig" title="RkeConfig">RkeConfig</a>: <i>
      - <a href="rkeconfigdefinition.md">RkeConfigDefinition</a></i>
    <a href="#scheduledclusterscan" title="ScheduledClusterScan">ScheduledClusterScan</a>: <i>
      - <a href="scheduledclusterscandefinition.md">ScheduledClusterScanDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterTemplateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterTemplateRevisionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPodSecurityPolicyTemplateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredAgentImage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredAuthImage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerRootDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Driver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableClusterAlerting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableClusterMonitoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNetworkPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsPreferedCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentEnvVars

_Required_: No

_Type_: List of <a href="agentenvvarsdefinition.md">AgentEnvVarsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AksConfig

_Required_: No

_Type_: List of <a href="aksconfigdefinition.md">AksConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAuthEndpoint

_Required_: No

_Type_: List of <a href="clusterauthendpointdefinition.md">ClusterAuthEndpointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMonitoringInput

_Required_: No

_Type_: List of <a href="clustermonitoringinputdefinition.md">ClusterMonitoringInputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterTemplateAnswers

_Required_: No

_Type_: List of <a href="clustertemplateanswersdefinition.md">ClusterTemplateAnswersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterTemplateQuestions

_Required_: No

_Type_: List of <a href="clustertemplatequestionsdefinition.md">ClusterTemplateQuestionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EksConfig

_Required_: No

_Type_: List of <a href="eksconfigdefinition.md">EksConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EksConfigV2

_Required_: No

_Type_: List of <a href="eksconfigv2definition.md">EksConfigV2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GkeConfig

_Required_: No

_Type_: List of <a href="gkeconfigdefinition.md">GkeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GkeConfigV2

_Required_: No

_Type_: List of <a href="gkeconfigv2definition.md">GkeConfigV2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### K3sConfig

_Required_: No

_Type_: List of <a href="k3sconfigdefinition.md">K3sConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OkeConfig

_Required_: No

_Type_: List of <a href="okeconfigdefinition.md">OkeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rke2Config

_Required_: No

_Type_: List of <a href="rke2configdefinition.md">Rke2ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RkeConfig

_Required_: No

_Type_: List of <a href="rkeconfigdefinition.md">RkeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledClusterScan

_Required_: No

_Type_: List of <a href="scheduledclusterscandefinition.md">ScheduledClusterScanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CaCert

Returns the <code>CaCert</code> value.

#### ClusterRegistrationToken

Returns the <code>ClusterRegistrationToken</code> value.

#### DefaultProjectId

Returns the <code>DefaultProjectId</code> value.

#### EnableClusterIstio

Returns the <code>EnableClusterIstio</code> value.

#### Id

Returns the <code>Id</code> value.

#### IstioEnabled

Returns the <code>IstioEnabled</code> value.

#### KubeConfig

Returns the <code>KubeConfig</code> value.

#### SystemProjectId

Returns the <code>SystemProjectId</code> value.

