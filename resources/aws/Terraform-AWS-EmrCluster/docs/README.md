# Terraform::AWS::EmrCluster

Provides an Elastic MapReduce Cluster, a web service that makes it easy to
process large amounts of data efficiently. See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/elastic-mapreduce/)
for more information.

To configure [Instance Groups](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups) for [task nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-task), see the [`aws_emr_instance_group` resource](/docs/providers/aws/r/emr_instance_group.html).

-> Support for [Instance Fleets](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-fleets) will be made available in an upcoming release.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EmrCluster",
    "Properties" : {
        "<a href="#additionalinfo" title="AdditionalInfo">AdditionalInfo</a>" : <i>String</i>,
        "<a href="#applications" title="Applications">Applications</a>" : <i>[ String, ... ]</i>,
        "<a href="#autoscalingrole" title="AutoscalingRole">AutoscalingRole</a>" : <i>String</i>,
        "<a href="#configurations" title="Configurations">Configurations</a>" : <i>String</i>,
        "<a href="#configurationsjson" title="ConfigurationsJson">ConfigurationsJson</a>" : <i>String</i>,
        "<a href="#coreinstancecount" title="CoreInstanceCount">CoreInstanceCount</a>" : <i>Double</i>,
        "<a href="#coreinstancetype" title="CoreInstanceType">CoreInstanceType</a>" : <i>String</i>,
        "<a href="#customamiid" title="CustomAmiId">CustomAmiId</a>" : <i>String</i>,
        "<a href="#ebsrootvolumesize" title="EbsRootVolumeSize">EbsRootVolumeSize</a>" : <i>Double</i>,
        "<a href="#keepjobflowalivewhennosteps" title="KeepJobFlowAliveWhenNoSteps">KeepJobFlowAliveWhenNoSteps</a>" : <i>Boolean</i>,
        "<a href="#loguri" title="LogUri">LogUri</a>" : <i>String</i>,
        "<a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#releaselabel" title="ReleaseLabel">ReleaseLabel</a>" : <i>String</i>,
        "<a href="#scaledownbehavior" title="ScaleDownBehavior">ScaleDownBehavior</a>" : <i>String</i>,
        "<a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>" : <i>String</i>,
        "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
        "<a href="#step" title="Step">Step</a>" : <i>[ <a href="step.md">Step</a>, ... ]</i>,
        "<a href="#stepconcurrencylevel" title="StepConcurrencyLevel">StepConcurrencyLevel</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#terminationprotection" title="TerminationProtection">TerminationProtection</a>" : <i>Boolean</i>,
        "<a href="#visibletoallusers" title="VisibleToAllUsers">VisibleToAllUsers</a>" : <i>Boolean</i>,
        "<a href="#bootstrapaction" title="BootstrapAction">BootstrapAction</a>" : <i>[ <a href="bootstrapaction.md">BootstrapAction</a>, ... ]</i>,
        "<a href="#coreinstancegroup" title="CoreInstanceGroup">CoreInstanceGroup</a>" : <i>[ <a href="coreinstancegroup.md">CoreInstanceGroup</a>, ... ]</i>,
        "<a href="#ec2attributes" title="Ec2Attributes">Ec2Attributes</a>" : <i>[ <a href="ec2attributes.md">Ec2Attributes</a>, ... ]</i>,
        "<a href="#instancegroup" title="InstanceGroup">InstanceGroup</a>" : <i>[ <a href="instancegroup.md">InstanceGroup</a>, ... ]</i>,
        "<a href="#kerberosattributes" title="KerberosAttributes">KerberosAttributes</a>" : <i>[ <a href="kerberosattributes.md">KerberosAttributes</a>, ... ]</i>,
        "<a href="#masterinstancegroup" title="MasterInstanceGroup">MasterInstanceGroup</a>" : <i>[ <a href="masterinstancegroup.md">MasterInstanceGroup</a>, ... ]</i>,
        "<a href="#ebsconfig" title="EbsConfig">EbsConfig</a>" : <i>[ <a href="ebsconfig.md">EbsConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EmrCluster
Properties:
    <a href="#additionalinfo" title="AdditionalInfo">AdditionalInfo</a>: <i>String</i>
    <a href="#applications" title="Applications">Applications</a>: <i>
      - String</i>
    <a href="#autoscalingrole" title="AutoscalingRole">AutoscalingRole</a>: <i>String</i>
    <a href="#configurations" title="Configurations">Configurations</a>: <i>String</i>
    <a href="#configurationsjson" title="ConfigurationsJson">ConfigurationsJson</a>: <i>String</i>
    <a href="#coreinstancecount" title="CoreInstanceCount">CoreInstanceCount</a>: <i>Double</i>
    <a href="#coreinstancetype" title="CoreInstanceType">CoreInstanceType</a>: <i>String</i>
    <a href="#customamiid" title="CustomAmiId">CustomAmiId</a>: <i>String</i>
    <a href="#ebsrootvolumesize" title="EbsRootVolumeSize">EbsRootVolumeSize</a>: <i>Double</i>
    <a href="#keepjobflowalivewhennosteps" title="KeepJobFlowAliveWhenNoSteps">KeepJobFlowAliveWhenNoSteps</a>: <i>Boolean</i>
    <a href="#loguri" title="LogUri">LogUri</a>: <i>String</i>
    <a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#releaselabel" title="ReleaseLabel">ReleaseLabel</a>: <i>String</i>
    <a href="#scaledownbehavior" title="ScaleDownBehavior">ScaleDownBehavior</a>: <i>String</i>
    <a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>: <i>String</i>
    <a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
    <a href="#step" title="Step">Step</a>: <i>
      - <a href="step.md">Step</a></i>
    <a href="#stepconcurrencylevel" title="StepConcurrencyLevel">StepConcurrencyLevel</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#terminationprotection" title="TerminationProtection">TerminationProtection</a>: <i>Boolean</i>
    <a href="#visibletoallusers" title="VisibleToAllUsers">VisibleToAllUsers</a>: <i>Boolean</i>
    <a href="#bootstrapaction" title="BootstrapAction">BootstrapAction</a>: <i>
      - <a href="bootstrapaction.md">BootstrapAction</a></i>
    <a href="#coreinstancegroup" title="CoreInstanceGroup">CoreInstanceGroup</a>: <i>
      - <a href="coreinstancegroup.md">CoreInstanceGroup</a></i>
    <a href="#ec2attributes" title="Ec2Attributes">Ec2Attributes</a>: <i>
      - <a href="ec2attributes.md">Ec2Attributes</a></i>
    <a href="#instancegroup" title="InstanceGroup">InstanceGroup</a>: <i>
      - <a href="instancegroup.md">InstanceGroup</a></i>
    <a href="#kerberosattributes" title="KerberosAttributes">KerberosAttributes</a>: <i>
      - <a href="kerberosattributes.md">KerberosAttributes</a></i>
    <a href="#masterinstancegroup" title="MasterInstanceGroup">MasterInstanceGroup</a>: <i>
      - <a href="masterinstancegroup.md">MasterInstanceGroup</a></i>
    <a href="#ebsconfig" title="EbsConfig">EbsConfig</a>: <i>
      - <a href="ebsconfig.md">EbsConfig</a></i>
</pre>

## Properties

#### AdditionalInfo

A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Applications

A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, `Spark`, and `JupyterHub` (as of EMR 5.14.0). Case insensitive.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingRole

An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configurations

List of configurations supplied for the EMR cluster you are creating.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationsJson

A JSON string for supplying list of configurations for the EMR cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreInstanceCount

Use the `core_instance_group` configuration block `instance_count` argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`core_instance_count`-1) as core nodes. Cannot be specified if `core_instance_group` or `instance_group` configuration blocks are set. Default `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreInstanceType

Use the `core_instance_group` configuration block `instance_type` argument instead. The EC2 instance type of the slave nodes. Cannot be specified if `core_instance_group` or `instance_group` configuration blocks are set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAmiId

A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsRootVolumeSize

Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepJobFlowAliveWhenNoSteps

Switch on/off run cluster with no steps or when all steps are complete (default is on).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogUri

S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceType

Use the `master_instance_group` configuration block `instance_type` argument instead. The EC2 instance type of the master node. Cannot be specified if `master_instance_group` or `instance_group` configuration blocks are set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the job flow.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseLabel

The release label for the Amazon EMR release.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownBehavior

The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfiguration

The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `release_label` 4.8.0 or greater.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

IAM role that will be assumed by the Amazon EMR service to access AWS resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Step

List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](/docs/configuration/resources.html) with `ignore_changes` if other steps are being managed outside of Terraform. This argument is processed in [attribute-as-blocks mode](/docs/configuration/attr-as-blocks.html).

_Required_: No

_Type_: List of <a href="step.md">Step</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepConcurrencyLevel

The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with `release_label` 5.28.0 or greater. (default is 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

list of tags to apply to the EMR Cluster.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationProtection

Switch on/off termination protection (default is `false`, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisibleToAllUsers

Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootstrapAction

_Required_: No

_Type_: List of <a href="bootstrapaction.md">BootstrapAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreInstanceGroup

_Required_: No

_Type_: List of <a href="coreinstancegroup.md">CoreInstanceGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2Attributes

_Required_: No

_Type_: List of <a href="ec2attributes.md">Ec2Attributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceGroup

_Required_: No

_Type_: List of <a href="instancegroup.md">InstanceGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KerberosAttributes

_Required_: No

_Type_: List of <a href="kerberosattributes.md">KerberosAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceGroup

_Required_: No

_Type_: List of <a href="masterinstancegroup.md">MasterInstanceGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsConfig

_Required_: No

_Type_: List of <a href="ebsconfig.md">EbsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### ClusterState

Returns the <code>ClusterState</code> value.

#### Id

Returns the <code>Id</code> value.

#### MasterPublicDns

Returns the <code>MasterPublicDns</code> value.

