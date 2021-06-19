# TF::Databricks::Job NewClusterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoterminationminutes" title="AutoterminationMinutes">AutoterminationMinutes</a>" : <i>Double</i>,
    "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
    "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
    "<a href="#customtags" title="CustomTags">CustomTags</a>" : <i>[ <a href="customtagsdefinition.md">CustomTagsDefinition</a>, ... ]</i>,
    "<a href="#drivernodetypeid" title="DriverNodeTypeId">DriverNodeTypeId</a>" : <i>String</i>,
    "<a href="#enableelasticdisk" title="EnableElasticDisk">EnableElasticDisk</a>" : <i>Boolean</i>,
    "<a href="#enablelocaldiskencryption" title="EnableLocalDiskEncryption">EnableLocalDiskEncryption</a>" : <i>Boolean</i>,
    "<a href="#idempotencytoken" title="IdempotencyToken">IdempotencyToken</a>" : <i>String</i>,
    "<a href="#instancepoolid" title="InstancePoolId">InstancePoolId</a>" : <i>String</i>,
    "<a href="#nodetypeid" title="NodeTypeId">NodeTypeId</a>" : <i>String</i>,
    "<a href="#numworkers" title="NumWorkers">NumWorkers</a>" : <i>Double</i>,
    "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>String</i>,
    "<a href="#singleusername" title="SingleUserName">SingleUserName</a>" : <i>String</i>,
    "<a href="#sparkconf" title="SparkConf">SparkConf</a>" : <i>[ <a href="sparkconfdefinition.md">SparkConfDefinition</a>, ... ]</i>,
    "<a href="#sparkenvvars" title="SparkEnvVars">SparkEnvVars</a>" : <i>[ <a href="sparkenvvarsdefinition.md">SparkEnvVarsDefinition</a>, ... ]</i>,
    "<a href="#sparkversion" title="SparkVersion">SparkVersion</a>" : <i>String</i>,
    "<a href="#sshpublickeys" title="SshPublicKeys">SshPublicKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#autoscale" title="Autoscale">Autoscale</a>" : <i>[ <a href="autoscaledefinition.md">AutoscaleDefinition</a>, ... ]</i>,
    "<a href="#awsattributes" title="AwsAttributes">AwsAttributes</a>" : <i>[ <a href="awsattributesdefinition.md">AwsAttributesDefinition</a>, ... ]</i>,
    "<a href="#azureattributes" title="AzureAttributes">AzureAttributes</a>" : <i>[ <a href="azureattributesdefinition.md">AzureAttributesDefinition</a>, ... ]</i>,
    "<a href="#clusterlogconf" title="ClusterLogConf">ClusterLogConf</a>" : <i>[ <a href="clusterlogconfdefinition.md">ClusterLogConfDefinition</a>, ... ]</i>,
    "<a href="#dockerimage" title="DockerImage">DockerImage</a>" : <i>[ <a href="dockerimagedefinition.md">DockerImageDefinition</a>, ... ]</i>,
    "<a href="#gcpattributes" title="GcpAttributes">GcpAttributes</a>" : <i>[ <a href="gcpattributesdefinition.md">GcpAttributesDefinition</a>, ... ]</i>,
    "<a href="#initscripts" title="InitScripts">InitScripts</a>" : <i>[ <a href="initscriptsdefinition.md">InitScriptsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoterminationminutes" title="AutoterminationMinutes">AutoterminationMinutes</a>: <i>Double</i>
<a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
<a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
<a href="#customtags" title="CustomTags">CustomTags</a>: <i>
      - <a href="customtagsdefinition.md">CustomTagsDefinition</a></i>
<a href="#drivernodetypeid" title="DriverNodeTypeId">DriverNodeTypeId</a>: <i>String</i>
<a href="#enableelasticdisk" title="EnableElasticDisk">EnableElasticDisk</a>: <i>Boolean</i>
<a href="#enablelocaldiskencryption" title="EnableLocalDiskEncryption">EnableLocalDiskEncryption</a>: <i>Boolean</i>
<a href="#idempotencytoken" title="IdempotencyToken">IdempotencyToken</a>: <i>String</i>
<a href="#instancepoolid" title="InstancePoolId">InstancePoolId</a>: <i>String</i>
<a href="#nodetypeid" title="NodeTypeId">NodeTypeId</a>: <i>String</i>
<a href="#numworkers" title="NumWorkers">NumWorkers</a>: <i>Double</i>
<a href="#policyid" title="PolicyId">PolicyId</a>: <i>String</i>
<a href="#singleusername" title="SingleUserName">SingleUserName</a>: <i>String</i>
<a href="#sparkconf" title="SparkConf">SparkConf</a>: <i>
      - <a href="sparkconfdefinition.md">SparkConfDefinition</a></i>
<a href="#sparkenvvars" title="SparkEnvVars">SparkEnvVars</a>: <i>
      - <a href="sparkenvvarsdefinition.md">SparkEnvVarsDefinition</a></i>
<a href="#sparkversion" title="SparkVersion">SparkVersion</a>: <i>String</i>
<a href="#sshpublickeys" title="SshPublicKeys">SshPublicKeys</a>: <i>
      - String</i>
<a href="#autoscale" title="Autoscale">Autoscale</a>: <i>
      - <a href="autoscaledefinition.md">AutoscaleDefinition</a></i>
<a href="#awsattributes" title="AwsAttributes">AwsAttributes</a>: <i>
      - <a href="awsattributesdefinition.md">AwsAttributesDefinition</a></i>
<a href="#azureattributes" title="AzureAttributes">AzureAttributes</a>: <i>
      - <a href="azureattributesdefinition.md">AzureAttributesDefinition</a></i>
<a href="#clusterlogconf" title="ClusterLogConf">ClusterLogConf</a>: <i>
      - <a href="clusterlogconfdefinition.md">ClusterLogConfDefinition</a></i>
<a href="#dockerimage" title="DockerImage">DockerImage</a>: <i>
      - <a href="dockerimagedefinition.md">DockerImageDefinition</a></i>
<a href="#gcpattributes" title="GcpAttributes">GcpAttributes</a>: <i>
      - <a href="gcpattributesdefinition.md">GcpAttributesDefinition</a></i>
<a href="#initscripts" title="InitScripts">InitScripts</a>: <i>
      - <a href="initscriptsdefinition.md">InitScriptsDefinition</a></i>
</pre>

## Properties

#### AutoterminationMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTags

_Required_: No

_Type_: List of <a href="customtagsdefinition.md">CustomTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DriverNodeTypeId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableElasticDisk

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLocalDiskEncryption

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdempotencyToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancePoolId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeTypeId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumWorkers

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleUserName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkConf

_Required_: No

_Type_: List of <a href="sparkconfdefinition.md">SparkConfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkEnvVars

_Required_: No

_Type_: List of <a href="sparkenvvarsdefinition.md">SparkEnvVarsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscale

_Required_: No

_Type_: List of <a href="autoscaledefinition.md">AutoscaleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsAttributes

_Required_: No

_Type_: List of <a href="awsattributesdefinition.md">AwsAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureAttributes

_Required_: No

_Type_: List of <a href="azureattributesdefinition.md">AzureAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterLogConf

_Required_: No

_Type_: List of <a href="clusterlogconfdefinition.md">ClusterLogConfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerImage

_Required_: No

_Type_: List of <a href="dockerimagedefinition.md">DockerImageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpAttributes

_Required_: No

_Type_: List of <a href="gcpattributesdefinition.md">GcpAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitScripts

_Required_: No

_Type_: List of <a href="initscriptsdefinition.md">InitScriptsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

