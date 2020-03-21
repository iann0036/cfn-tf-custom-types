# Terraform::Spotinst::MrscalerAws

CloudFormation equivalent of spotinst_mrscaler_aws

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::MrscalerAws",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#additionalinfo" title="AdditionalInfo">AdditionalInfo</a>" : <i>String</i>,
        "<a href="#additionalprimarysecuritygroups" title="AdditionalPrimarySecurityGroups">AdditionalPrimarySecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#additionalreplicasecuritygroups" title="AdditionalReplicaSecurityGroups">AdditionalReplicaSecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#coredesiredcapacity" title="CoreDesiredCapacity">CoreDesiredCapacity</a>" : <i>Double</i>,
        "<a href="#coreebsoptimized" title="CoreEbsOptimized">CoreEbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#coreinstancetypes" title="CoreInstanceTypes">CoreInstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#corelifecycle" title="CoreLifecycle">CoreLifecycle</a>" : <i>String</i>,
        "<a href="#coremaxsize" title="CoreMaxSize">CoreMaxSize</a>" : <i>Double</i>,
        "<a href="#coreminsize" title="CoreMinSize">CoreMinSize</a>" : <i>Double</i>,
        "<a href="#customamiid" title="CustomAmiId">CustomAmiId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ebsrootvolumesize" title="EbsRootVolumeSize">EbsRootVolumeSize</a>" : <i>Double</i>,
        "<a href="#ec2keyname" title="Ec2KeyName">Ec2KeyName</a>" : <i>String</i>,
        "<a href="#exposeclusterid" title="ExposeClusterId">ExposeClusterId</a>" : <i>Boolean</i>,
        "<a href="#jobflowrole" title="JobFlowRole">JobFlowRole</a>" : <i>String</i>,
        "<a href="#keepjobflowalive" title="KeepJobFlowAlive">KeepJobFlowAlive</a>" : <i>Boolean</i>,
        "<a href="#loguri" title="LogUri">LogUri</a>" : <i>String</i>,
        "<a href="#managedprimarysecuritygroup" title="ManagedPrimarySecurityGroup">ManagedPrimarySecurityGroup</a>" : <i>String</i>,
        "<a href="#managedreplicasecuritygroup" title="ManagedReplicaSecurityGroup">ManagedReplicaSecurityGroup</a>" : <i>String</i>,
        "<a href="#masterebsoptimized" title="MasterEbsOptimized">MasterEbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#masterinstancetypes" title="MasterInstanceTypes">MasterInstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#masterlifecycle" title="MasterLifecycle">MasterLifecycle</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outputclusterid" title="OutputClusterId">OutputClusterId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#releaselabel" title="ReleaseLabel">ReleaseLabel</a>" : <i>String</i>,
        "<a href="#repoupgradeonboot" title="RepoUpgradeOnBoot">RepoUpgradeOnBoot</a>" : <i>String</i>,
        "<a href="#retries" title="Retries">Retries</a>" : <i>Double</i>,
        "<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>" : <i>String</i>,
        "<a href="#serviceaccesssecuritygroup" title="ServiceAccessSecurityGroup">ServiceAccessSecurityGroup</a>" : <i>String</i>,
        "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
        "<a href="#strategy" title="Strategy">Strategy</a>" : <i>String</i>,
        "<a href="#taskdesiredcapacity" title="TaskDesiredCapacity">TaskDesiredCapacity</a>" : <i>Double</i>,
        "<a href="#taskebsoptimized" title="TaskEbsOptimized">TaskEbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#taskinstancetypes" title="TaskInstanceTypes">TaskInstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#tasklifecycle" title="TaskLifecycle">TaskLifecycle</a>" : <i>String</i>,
        "<a href="#taskmaxsize" title="TaskMaxSize">TaskMaxSize</a>" : <i>Double</i>,
        "<a href="#taskminsize" title="TaskMinSize">TaskMinSize</a>" : <i>Double</i>,
        "<a href="#terminationprotected" title="TerminationProtected">TerminationProtected</a>" : <i>Boolean</i>,
        "<a href="#visibletoallusers" title="VisibleToAllUsers">VisibleToAllUsers</a>" : <i>Boolean</i>,
        "<a href="#applications" title="Applications">Applications</a>" : <i>[ &lt;a href=&#34;applications.md&#34;&gt;Applications&lt;/a&gt;, ... ]</i>,
        "<a href="#bootstrapactionsfile" title="BootstrapActionsFile">BootstrapActionsFile</a>" : <i>[ &lt;a href=&#34;bootstrapactionsfile.md&#34;&gt;BootstrapActionsFile&lt;/a&gt;, ... ]</i>,
        "<a href="#configurationsfile" title="ConfigurationsFile">ConfigurationsFile</a>" : <i>[ &lt;a href=&#34;configurationsfile.md&#34;&gt;ConfigurationsFile&lt;/a&gt;, ... ]</i>,
        "<a href="#coreebsblockdevice" title="CoreEbsBlockDevice">CoreEbsBlockDevice</a>" : <i>[ &lt;a href=&#34;coreebsblockdevice.md&#34;&gt;CoreEbsBlockDevice&lt;/a&gt;, ... ]</i>,
        "<a href="#corescalingdownpolicy" title="CoreScalingDownPolicy">CoreScalingDownPolicy</a>" : <i>[ &lt;a href=&#34;corescalingdownpolicy.md&#34;&gt;CoreScalingDownPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#corescalinguppolicy" title="CoreScalingUpPolicy">CoreScalingUpPolicy</a>" : <i>[ &lt;a href=&#34;corescalinguppolicy.md&#34;&gt;CoreScalingUpPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#instanceweights" title="InstanceWeights">InstanceWeights</a>" : <i>[ &lt;a href=&#34;instanceweights.md&#34;&gt;InstanceWeights&lt;/a&gt;, ... ]</i>,
        "<a href="#masterebsblockdevice" title="MasterEbsBlockDevice">MasterEbsBlockDevice</a>" : <i>[ &lt;a href=&#34;masterebsblockdevice.md&#34;&gt;MasterEbsBlockDevice&lt;/a&gt;, ... ]</i>,
        "<a href="#provisioningtimeout" title="ProvisioningTimeout">ProvisioningTimeout</a>" : <i>[ &lt;a href=&#34;provisioningtimeout.md&#34;&gt;ProvisioningTimeout&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;, ... ]</i>,
        "<a href="#stepsfile" title="StepsFile">StepsFile</a>" : <i>[ &lt;a href=&#34;stepsfile.md&#34;&gt;StepsFile&lt;/a&gt;, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#taskebsblockdevice" title="TaskEbsBlockDevice">TaskEbsBlockDevice</a>" : <i>[ &lt;a href=&#34;taskebsblockdevice.md&#34;&gt;TaskEbsBlockDevice&lt;/a&gt;, ... ]</i>,
        "<a href="#taskscalingdownpolicy" title="TaskScalingDownPolicy">TaskScalingDownPolicy</a>" : <i>[ &lt;a href=&#34;taskscalingdownpolicy.md&#34;&gt;TaskScalingDownPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#taskscalinguppolicy" title="TaskScalingUpPolicy">TaskScalingUpPolicy</a>" : <i>[ &lt;a href=&#34;taskscalinguppolicy.md&#34;&gt;TaskScalingUpPolicy&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::MrscalerAws
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#additionalinfo" title="AdditionalInfo">AdditionalInfo</a>: <i>String</i>
    <a href="#additionalprimarysecuritygroups" title="AdditionalPrimarySecurityGroups">AdditionalPrimarySecurityGroups</a>: <i>
      - String</i>
    <a href="#additionalreplicasecuritygroups" title="AdditionalReplicaSecurityGroups">AdditionalReplicaSecurityGroups</a>: <i>
      - String</i>
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#coredesiredcapacity" title="CoreDesiredCapacity">CoreDesiredCapacity</a>: <i>Double</i>
    <a href="#coreebsoptimized" title="CoreEbsOptimized">CoreEbsOptimized</a>: <i>Boolean</i>
    <a href="#coreinstancetypes" title="CoreInstanceTypes">CoreInstanceTypes</a>: <i>
      - String</i>
    <a href="#corelifecycle" title="CoreLifecycle">CoreLifecycle</a>: <i>String</i>
    <a href="#coremaxsize" title="CoreMaxSize">CoreMaxSize</a>: <i>Double</i>
    <a href="#coreminsize" title="CoreMinSize">CoreMinSize</a>: <i>Double</i>
    <a href="#customamiid" title="CustomAmiId">CustomAmiId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ebsrootvolumesize" title="EbsRootVolumeSize">EbsRootVolumeSize</a>: <i>Double</i>
    <a href="#ec2keyname" title="Ec2KeyName">Ec2KeyName</a>: <i>String</i>
    <a href="#exposeclusterid" title="ExposeClusterId">ExposeClusterId</a>: <i>Boolean</i>
    <a href="#jobflowrole" title="JobFlowRole">JobFlowRole</a>: <i>String</i>
    <a href="#keepjobflowalive" title="KeepJobFlowAlive">KeepJobFlowAlive</a>: <i>Boolean</i>
    <a href="#loguri" title="LogUri">LogUri</a>: <i>String</i>
    <a href="#managedprimarysecuritygroup" title="ManagedPrimarySecurityGroup">ManagedPrimarySecurityGroup</a>: <i>String</i>
    <a href="#managedreplicasecuritygroup" title="ManagedReplicaSecurityGroup">ManagedReplicaSecurityGroup</a>: <i>String</i>
    <a href="#masterebsoptimized" title="MasterEbsOptimized">MasterEbsOptimized</a>: <i>Boolean</i>
    <a href="#masterinstancetypes" title="MasterInstanceTypes">MasterInstanceTypes</a>: <i>
      - String</i>
    <a href="#masterlifecycle" title="MasterLifecycle">MasterLifecycle</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outputclusterid" title="OutputClusterId">OutputClusterId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#releaselabel" title="ReleaseLabel">ReleaseLabel</a>: <i>String</i>
    <a href="#repoupgradeonboot" title="RepoUpgradeOnBoot">RepoUpgradeOnBoot</a>: <i>String</i>
    <a href="#retries" title="Retries">Retries</a>: <i>Double</i>
    <a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>: <i>String</i>
    <a href="#serviceaccesssecuritygroup" title="ServiceAccessSecurityGroup">ServiceAccessSecurityGroup</a>: <i>String</i>
    <a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
    <a href="#strategy" title="Strategy">Strategy</a>: <i>String</i>
    <a href="#taskdesiredcapacity" title="TaskDesiredCapacity">TaskDesiredCapacity</a>: <i>Double</i>
    <a href="#taskebsoptimized" title="TaskEbsOptimized">TaskEbsOptimized</a>: <i>Boolean</i>
    <a href="#taskinstancetypes" title="TaskInstanceTypes">TaskInstanceTypes</a>: <i>
      - String</i>
    <a href="#tasklifecycle" title="TaskLifecycle">TaskLifecycle</a>: <i>String</i>
    <a href="#taskmaxsize" title="TaskMaxSize">TaskMaxSize</a>: <i>Double</i>
    <a href="#taskminsize" title="TaskMinSize">TaskMinSize</a>: <i>Double</i>
    <a href="#terminationprotected" title="TerminationProtected">TerminationProtected</a>: <i>Boolean</i>
    <a href="#visibletoallusers" title="VisibleToAllUsers">VisibleToAllUsers</a>: <i>Boolean</i>
    <a href="#applications" title="Applications">Applications</a>: <i>
      - &lt;a href=&#34;applications.md&#34;&gt;Applications&lt;/a&gt;</i>
    <a href="#bootstrapactionsfile" title="BootstrapActionsFile">BootstrapActionsFile</a>: <i>
      - &lt;a href=&#34;bootstrapactionsfile.md&#34;&gt;BootstrapActionsFile&lt;/a&gt;</i>
    <a href="#configurationsfile" title="ConfigurationsFile">ConfigurationsFile</a>: <i>
      - &lt;a href=&#34;configurationsfile.md&#34;&gt;ConfigurationsFile&lt;/a&gt;</i>
    <a href="#coreebsblockdevice" title="CoreEbsBlockDevice">CoreEbsBlockDevice</a>: <i>
      - &lt;a href=&#34;coreebsblockdevice.md&#34;&gt;CoreEbsBlockDevice&lt;/a&gt;</i>
    <a href="#corescalingdownpolicy" title="CoreScalingDownPolicy">CoreScalingDownPolicy</a>: <i>
      - &lt;a href=&#34;corescalingdownpolicy.md&#34;&gt;CoreScalingDownPolicy&lt;/a&gt;</i>
    <a href="#corescalinguppolicy" title="CoreScalingUpPolicy">CoreScalingUpPolicy</a>: <i>
      - &lt;a href=&#34;corescalinguppolicy.md&#34;&gt;CoreScalingUpPolicy&lt;/a&gt;</i>
    <a href="#instanceweights" title="InstanceWeights">InstanceWeights</a>: <i>
      - &lt;a href=&#34;instanceweights.md&#34;&gt;InstanceWeights&lt;/a&gt;</i>
    <a href="#masterebsblockdevice" title="MasterEbsBlockDevice">MasterEbsBlockDevice</a>: <i>
      - &lt;a href=&#34;masterebsblockdevice.md&#34;&gt;MasterEbsBlockDevice&lt;/a&gt;</i>
    <a href="#provisioningtimeout" title="ProvisioningTimeout">ProvisioningTimeout</a>: <i>
      - &lt;a href=&#34;provisioningtimeout.md&#34;&gt;ProvisioningTimeout&lt;/a&gt;</i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;</i>
    <a href="#stepsfile" title="StepsFile">StepsFile</a>: <i>
      - &lt;a href=&#34;stepsfile.md&#34;&gt;StepsFile&lt;/a&gt;</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#taskebsblockdevice" title="TaskEbsBlockDevice">TaskEbsBlockDevice</a>: <i>
      - &lt;a href=&#34;taskebsblockdevice.md&#34;&gt;TaskEbsBlockDevice&lt;/a&gt;</i>
    <a href="#taskscalingdownpolicy" title="TaskScalingDownPolicy">TaskScalingDownPolicy</a>: <i>
      - &lt;a href=&#34;taskscalingdownpolicy.md&#34;&gt;TaskScalingDownPolicy&lt;/a&gt;</i>
    <a href="#taskscalinguppolicy" title="TaskScalingUpPolicy">TaskScalingUpPolicy</a>: <i>
      - &lt;a href=&#34;taskscalinguppolicy.md&#34;&gt;TaskScalingUpPolicy&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalInfo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalPrimarySecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalReplicaSecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreDesiredCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreEbsOptimized

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreInstanceTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreLifecycle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreMaxSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreMinSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAmiId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsRootVolumeSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposeClusterId

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobFlowRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepJobFlowAlive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedPrimarySecurityGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedReplicaSecurityGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterEbsOptimized

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterLifecycle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoUpgradeOnBoot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccessSecurityGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskDesiredCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskEbsOptimized

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskInstanceTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskLifecycle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskMaxSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskMinSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationProtected

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisibleToAllUsers

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Applications

_Required_: No

_Type_: List of &lt;a href=&#34;applications.md&#34;&gt;Applications&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootstrapActionsFile

_Required_: No

_Type_: List of &lt;a href=&#34;bootstrapactionsfile.md&#34;&gt;BootstrapActionsFile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationsFile

_Required_: No

_Type_: List of &lt;a href=&#34;configurationsfile.md&#34;&gt;ConfigurationsFile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreEbsBlockDevice

_Required_: No

_Type_: List of &lt;a href=&#34;coreebsblockdevice.md&#34;&gt;CoreEbsBlockDevice&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreScalingDownPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;corescalingdownpolicy.md&#34;&gt;CoreScalingDownPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreScalingUpPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;corescalinguppolicy.md&#34;&gt;CoreScalingUpPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceWeights

_Required_: No

_Type_: List of &lt;a href=&#34;instanceweights.md&#34;&gt;InstanceWeights&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterEbsBlockDevice

_Required_: No

_Type_: List of &lt;a href=&#34;masterebsblockdevice.md&#34;&gt;MasterEbsBlockDevice&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisioningTimeout

_Required_: No

_Type_: List of &lt;a href=&#34;provisioningtimeout.md&#34;&gt;ProvisioningTimeout&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTask

_Required_: No

_Type_: List of &lt;a href=&#34;scheduledtask.md&#34;&gt;ScheduledTask&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepsFile

_Required_: No

_Type_: List of &lt;a href=&#34;stepsfile.md&#34;&gt;StepsFile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskEbsBlockDevice

_Required_: No

_Type_: List of &lt;a href=&#34;taskebsblockdevice.md&#34;&gt;TaskEbsBlockDevice&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskScalingDownPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;taskscalingdownpolicy.md&#34;&gt;TaskScalingDownPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskScalingUpPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;taskscalinguppolicy.md&#34;&gt;TaskScalingUpPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### OutputClusterId

Returns the &lt;code&gt;OutputClusterId&lt;/code&gt; value.

