# TF::Spotinst::MrscalerAws

CloudFormation equivalent of spotinst_mrscaler_aws

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Spotinst::MrscalerAws",
    "Properties" : {
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
        "<a href="#coreunit" title="CoreUnit">CoreUnit</a>" : <i>String</i>,
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
        "<a href="#taskunit" title="TaskUnit">TaskUnit</a>" : <i>String</i>,
        "<a href="#terminationprotected" title="TerminationProtected">TerminationProtected</a>" : <i>Boolean</i>,
        "<a href="#visibletoallusers" title="VisibleToAllUsers">VisibleToAllUsers</a>" : <i>Boolean</i>,
        "<a href="#applications" title="Applications">Applications</a>" : <i>[ <a href="applicationsdefinition.md">ApplicationsDefinition</a>, ... ]</i>,
        "<a href="#bootstrapactionsfile" title="BootstrapActionsFile">BootstrapActionsFile</a>" : <i>[ <a href="bootstrapactionsfiledefinition.md">BootstrapActionsFileDefinition</a>, ... ]</i>,
        "<a href="#configurationsfile" title="ConfigurationsFile">ConfigurationsFile</a>" : <i>[ <a href="configurationsfiledefinition.md">ConfigurationsFileDefinition</a>, ... ]</i>,
        "<a href="#coreebsblockdevice" title="CoreEbsBlockDevice">CoreEbsBlockDevice</a>" : <i>[ <a href="coreebsblockdevicedefinition.md">CoreEbsBlockDeviceDefinition</a>, ... ]</i>,
        "<a href="#corescalingdownpolicy" title="CoreScalingDownPolicy">CoreScalingDownPolicy</a>" : <i>[ <a href="corescalingdownpolicydefinition.md">CoreScalingDownPolicyDefinition</a>, ... ]</i>,
        "<a href="#corescalinguppolicy" title="CoreScalingUpPolicy">CoreScalingUpPolicy</a>" : <i>[ <a href="corescalinguppolicydefinition.md">CoreScalingUpPolicyDefinition</a>, ... ]</i>,
        "<a href="#instanceweights" title="InstanceWeights">InstanceWeights</a>" : <i>[ <a href="instanceweightsdefinition.md">InstanceWeightsDefinition</a>, ... ]</i>,
        "<a href="#masterebsblockdevice" title="MasterEbsBlockDevice">MasterEbsBlockDevice</a>" : <i>[ <a href="masterebsblockdevicedefinition.md">MasterEbsBlockDeviceDefinition</a>, ... ]</i>,
        "<a href="#provisioningtimeout" title="ProvisioningTimeout">ProvisioningTimeout</a>" : <i>[ <a href="provisioningtimeoutdefinition.md">ProvisioningTimeoutDefinition</a>, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ <a href="scheduledtaskdefinition.md">ScheduledTaskDefinition</a>, ... ]</i>,
        "<a href="#stepsfile" title="StepsFile">StepsFile</a>" : <i>[ <a href="stepsfiledefinition.md">StepsFileDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#taskebsblockdevice" title="TaskEbsBlockDevice">TaskEbsBlockDevice</a>" : <i>[ <a href="taskebsblockdevicedefinition.md">TaskEbsBlockDeviceDefinition</a>, ... ]</i>,
        "<a href="#taskscalingdownpolicy" title="TaskScalingDownPolicy">TaskScalingDownPolicy</a>" : <i>[ <a href="taskscalingdownpolicydefinition.md">TaskScalingDownPolicyDefinition</a>, ... ]</i>,
        "<a href="#taskscalinguppolicy" title="TaskScalingUpPolicy">TaskScalingUpPolicy</a>" : <i>[ <a href="taskscalinguppolicydefinition.md">TaskScalingUpPolicyDefinition</a>, ... ]</i>,
        "<a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>" : <i>[ <a href="terminationpoliciesdefinition.md">TerminationPoliciesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Spotinst::MrscalerAws
Properties:
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
    <a href="#coreunit" title="CoreUnit">CoreUnit</a>: <i>String</i>
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
    <a href="#taskunit" title="TaskUnit">TaskUnit</a>: <i>String</i>
    <a href="#terminationprotected" title="TerminationProtected">TerminationProtected</a>: <i>Boolean</i>
    <a href="#visibletoallusers" title="VisibleToAllUsers">VisibleToAllUsers</a>: <i>Boolean</i>
    <a href="#applications" title="Applications">Applications</a>: <i>
      - <a href="applicationsdefinition.md">ApplicationsDefinition</a></i>
    <a href="#bootstrapactionsfile" title="BootstrapActionsFile">BootstrapActionsFile</a>: <i>
      - <a href="bootstrapactionsfiledefinition.md">BootstrapActionsFileDefinition</a></i>
    <a href="#configurationsfile" title="ConfigurationsFile">ConfigurationsFile</a>: <i>
      - <a href="configurationsfiledefinition.md">ConfigurationsFileDefinition</a></i>
    <a href="#coreebsblockdevice" title="CoreEbsBlockDevice">CoreEbsBlockDevice</a>: <i>
      - <a href="coreebsblockdevicedefinition.md">CoreEbsBlockDeviceDefinition</a></i>
    <a href="#corescalingdownpolicy" title="CoreScalingDownPolicy">CoreScalingDownPolicy</a>: <i>
      - <a href="corescalingdownpolicydefinition.md">CoreScalingDownPolicyDefinition</a></i>
    <a href="#corescalinguppolicy" title="CoreScalingUpPolicy">CoreScalingUpPolicy</a>: <i>
      - <a href="corescalinguppolicydefinition.md">CoreScalingUpPolicyDefinition</a></i>
    <a href="#instanceweights" title="InstanceWeights">InstanceWeights</a>: <i>
      - <a href="instanceweightsdefinition.md">InstanceWeightsDefinition</a></i>
    <a href="#masterebsblockdevice" title="MasterEbsBlockDevice">MasterEbsBlockDevice</a>: <i>
      - <a href="masterebsblockdevicedefinition.md">MasterEbsBlockDeviceDefinition</a></i>
    <a href="#provisioningtimeout" title="ProvisioningTimeout">ProvisioningTimeout</a>: <i>
      - <a href="provisioningtimeoutdefinition.md">ProvisioningTimeoutDefinition</a></i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - <a href="scheduledtaskdefinition.md">ScheduledTaskDefinition</a></i>
    <a href="#stepsfile" title="StepsFile">StepsFile</a>: <i>
      - <a href="stepsfiledefinition.md">StepsFileDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#taskebsblockdevice" title="TaskEbsBlockDevice">TaskEbsBlockDevice</a>: <i>
      - <a href="taskebsblockdevicedefinition.md">TaskEbsBlockDeviceDefinition</a></i>
    <a href="#taskscalingdownpolicy" title="TaskScalingDownPolicy">TaskScalingDownPolicy</a>: <i>
      - <a href="taskscalingdownpolicydefinition.md">TaskScalingDownPolicyDefinition</a></i>
    <a href="#taskscalinguppolicy" title="TaskScalingUpPolicy">TaskScalingUpPolicy</a>: <i>
      - <a href="taskscalinguppolicydefinition.md">TaskScalingUpPolicyDefinition</a></i>
    <a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>: <i>
      - <a href="terminationpoliciesdefinition.md">TerminationPoliciesDefinition</a></i>
</pre>

## Properties

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

#### CoreUnit

_Required_: No

_Type_: String

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

#### TaskUnit

_Required_: No

_Type_: String

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

_Type_: List of <a href="applicationsdefinition.md">ApplicationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootstrapActionsFile

_Required_: No

_Type_: List of <a href="bootstrapactionsfiledefinition.md">BootstrapActionsFileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationsFile

_Required_: No

_Type_: List of <a href="configurationsfiledefinition.md">ConfigurationsFileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreEbsBlockDevice

_Required_: No

_Type_: List of <a href="coreebsblockdevicedefinition.md">CoreEbsBlockDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreScalingDownPolicy

_Required_: No

_Type_: List of <a href="corescalingdownpolicydefinition.md">CoreScalingDownPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreScalingUpPolicy

_Required_: No

_Type_: List of <a href="corescalinguppolicydefinition.md">CoreScalingUpPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceWeights

_Required_: No

_Type_: List of <a href="instanceweightsdefinition.md">InstanceWeightsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterEbsBlockDevice

_Required_: No

_Type_: List of <a href="masterebsblockdevicedefinition.md">MasterEbsBlockDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisioningTimeout

_Required_: No

_Type_: List of <a href="provisioningtimeoutdefinition.md">ProvisioningTimeoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTask

_Required_: No

_Type_: List of <a href="scheduledtaskdefinition.md">ScheduledTaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepsFile

_Required_: No

_Type_: List of <a href="stepsfiledefinition.md">StepsFileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskEbsBlockDevice

_Required_: No

_Type_: List of <a href="taskebsblockdevicedefinition.md">TaskEbsBlockDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskScalingDownPolicy

_Required_: No

_Type_: List of <a href="taskscalingdownpolicydefinition.md">TaskScalingDownPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskScalingUpPolicy

_Required_: No

_Type_: List of <a href="taskscalinguppolicydefinition.md">TaskScalingUpPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationPolicies

_Required_: No

_Type_: List of <a href="terminationpoliciesdefinition.md">TerminationPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### OutputClusterId

Returns the <code>OutputClusterId</code> value.

