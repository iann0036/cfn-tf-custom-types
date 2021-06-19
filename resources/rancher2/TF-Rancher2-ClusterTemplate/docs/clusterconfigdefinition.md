# TF::Rancher2::ClusterTemplate ClusterConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultclusterroleforprojectmembers" title="DefaultClusterRoleForProjectMembers">DefaultClusterRoleForProjectMembers</a>" : <i>String</i>,
    "<a href="#defaultpodsecuritypolicytemplateid" title="DefaultPodSecurityPolicyTemplateId">DefaultPodSecurityPolicyTemplateId</a>" : <i>String</i>,
    "<a href="#desiredagentimage" title="DesiredAgentImage">DesiredAgentImage</a>" : <i>String</i>,
    "<a href="#desiredauthimage" title="DesiredAuthImage">DesiredAuthImage</a>" : <i>String</i>,
    "<a href="#dockerrootdir" title="DockerRootDir">DockerRootDir</a>" : <i>String</i>,
    "<a href="#enableclusteralerting" title="EnableClusterAlerting">EnableClusterAlerting</a>" : <i>Boolean</i>,
    "<a href="#enableclustermonitoring" title="EnableClusterMonitoring">EnableClusterMonitoring</a>" : <i>Boolean</i>,
    "<a href="#enablenetworkpolicy" title="EnableNetworkPolicy">EnableNetworkPolicy</a>" : <i>Boolean</i>,
    "<a href="#windowspreferedcluster" title="WindowsPreferedCluster">WindowsPreferedCluster</a>" : <i>Boolean</i>,
    "<a href="#clusterauthendpoint" title="ClusterAuthEndpoint">ClusterAuthEndpoint</a>" : <i>[ <a href="clusterauthendpointdefinition.md">ClusterAuthEndpointDefinition</a>, ... ]</i>,
    "<a href="#rkeconfig" title="RkeConfig">RkeConfig</a>" : <i>[ <a href="rkeconfigdefinition.md">RkeConfigDefinition</a>, ... ]</i>,
    "<a href="#scheduledclusterscan" title="ScheduledClusterScan">ScheduledClusterScan</a>" : <i>[ <a href="scheduledclusterscandefinition.md">ScheduledClusterScanDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultclusterroleforprojectmembers" title="DefaultClusterRoleForProjectMembers">DefaultClusterRoleForProjectMembers</a>: <i>String</i>
<a href="#defaultpodsecuritypolicytemplateid" title="DefaultPodSecurityPolicyTemplateId">DefaultPodSecurityPolicyTemplateId</a>: <i>String</i>
<a href="#desiredagentimage" title="DesiredAgentImage">DesiredAgentImage</a>: <i>String</i>
<a href="#desiredauthimage" title="DesiredAuthImage">DesiredAuthImage</a>: <i>String</i>
<a href="#dockerrootdir" title="DockerRootDir">DockerRootDir</a>: <i>String</i>
<a href="#enableclusteralerting" title="EnableClusterAlerting">EnableClusterAlerting</a>: <i>Boolean</i>
<a href="#enableclustermonitoring" title="EnableClusterMonitoring">EnableClusterMonitoring</a>: <i>Boolean</i>
<a href="#enablenetworkpolicy" title="EnableNetworkPolicy">EnableNetworkPolicy</a>: <i>Boolean</i>
<a href="#windowspreferedcluster" title="WindowsPreferedCluster">WindowsPreferedCluster</a>: <i>Boolean</i>
<a href="#clusterauthendpoint" title="ClusterAuthEndpoint">ClusterAuthEndpoint</a>: <i>
      - <a href="clusterauthendpointdefinition.md">ClusterAuthEndpointDefinition</a></i>
<a href="#rkeconfig" title="RkeConfig">RkeConfig</a>: <i>
      - <a href="rkeconfigdefinition.md">RkeConfigDefinition</a></i>
<a href="#scheduledclusterscan" title="ScheduledClusterScan">ScheduledClusterScan</a>: <i>
      - <a href="scheduledclusterscandefinition.md">ScheduledClusterScanDefinition</a></i>
</pre>

## Properties

#### DefaultClusterRoleForProjectMembers

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPodSecurityPolicyTemplateId

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

#### WindowsPreferedCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAuthEndpoint

_Required_: No

_Type_: List of <a href="clusterauthendpointdefinition.md">ClusterAuthEndpointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RkeConfig

_Required_: No

_Type_: List of <a href="rkeconfigdefinition.md">RkeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledClusterScan

_Required_: No

_Type_: List of <a href="scheduledclusterscandefinition.md">ScheduledClusterScanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

