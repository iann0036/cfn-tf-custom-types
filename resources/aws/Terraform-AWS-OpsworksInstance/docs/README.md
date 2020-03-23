# Terraform::AWS::OpsworksInstance

Provides an OpsWorks instance resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::OpsworksInstance",
    "Properties" : {
        "<a href="#agentversion" title="AgentVersion">AgentVersion</a>" : <i>String</i>,
        "<a href="#amiid" title="AmiId">AmiId</a>" : <i>String</i>,
        "<a href="#architecture" title="Architecture">Architecture</a>" : <i>String</i>,
        "<a href="#autoscalingtype" title="AutoScalingType">AutoScalingType</a>" : <i>String</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#createdat" title="CreatedAt">CreatedAt</a>" : <i>String</i>,
        "<a href="#deleteebs" title="DeleteEbs">DeleteEbs</a>" : <i>Boolean</i>,
        "<a href="#deleteeip" title="DeleteEip">DeleteEip</a>" : <i>Boolean</i>,
        "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#ecsclusterarn" title="EcsClusterArn">EcsClusterArn</a>" : <i>String</i>,
        "<a href="#elasticip" title="ElasticIp">ElasticIp</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#infrastructureclass" title="InfrastructureClass">InfrastructureClass</a>" : <i>String</i>,
        "<a href="#installupdatesonboot" title="InstallUpdatesOnBoot">InstallUpdatesOnBoot</a>" : <i>Boolean</i>,
        "<a href="#instanceprofilearn" title="InstanceProfileArn">InstanceProfileArn</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#lastserviceerrorid" title="LastServiceErrorId">LastServiceErrorId</a>" : <i>String</i>,
        "<a href="#layerids" title="LayerIds">LayerIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#os" title="Os">Os</a>" : <i>String</i>,
        "<a href="#platform" title="Platform">Platform</a>" : <i>String</i>,
        "<a href="#privatedns" title="PrivateDns">PrivateDns</a>" : <i>String</i>,
        "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>String</i>,
        "<a href="#publicdns" title="PublicDns">PublicDns</a>" : <i>String</i>,
        "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>String</i>,
        "<a href="#registeredby" title="RegisteredBy">RegisteredBy</a>" : <i>String</i>,
        "<a href="#reportedagentversion" title="ReportedAgentVersion">ReportedAgentVersion</a>" : <i>String</i>,
        "<a href="#reportedosfamily" title="ReportedOsFamily">ReportedOsFamily</a>" : <i>String</i>,
        "<a href="#reportedosname" title="ReportedOsName">ReportedOsName</a>" : <i>String</i>,
        "<a href="#reportedosversion" title="ReportedOsVersion">ReportedOsVersion</a>" : <i>String</i>,
        "<a href="#rootdevicetype" title="RootDeviceType">RootDeviceType</a>" : <i>String</i>,
        "<a href="#rootdevicevolumeid" title="RootDeviceVolumeId">RootDeviceVolumeId</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#sshhostdsakeyfingerprint" title="SshHostDsaKeyFingerprint">SshHostDsaKeyFingerprint</a>" : <i>String</i>,
        "<a href="#sshhostrsakeyfingerprint" title="SshHostRsaKeyFingerprint">SshHostRsaKeyFingerprint</a>" : <i>String</i>,
        "<a href="#sshkeyname" title="SshKeyName">SshKeyName</a>" : <i>String</i>,
        "<a href="#stackid" title="StackId">StackId</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tenancy" title="Tenancy">Tenancy</a>" : <i>String</i>,
        "<a href="#virtualizationtype" title="VirtualizationType">VirtualizationType</a>" : <i>String</i>,
        "<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>" : <i>[ <a href="ebsblockdevice.md">EbsBlockDevice</a>, ... ]</i>,
        "<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>" : <i>[ <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>, ... ]</i>,
        "<a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>" : <i>[ <a href="rootblockdevice.md">RootBlockDevice</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::OpsworksInstance
Properties:
    <a href="#agentversion" title="AgentVersion">AgentVersion</a>: <i>String</i>
    <a href="#amiid" title="AmiId">AmiId</a>: <i>String</i>
    <a href="#architecture" title="Architecture">Architecture</a>: <i>String</i>
    <a href="#autoscalingtype" title="AutoScalingType">AutoScalingType</a>: <i>String</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#createdat" title="CreatedAt">CreatedAt</a>: <i>String</i>
    <a href="#deleteebs" title="DeleteEbs">DeleteEbs</a>: <i>Boolean</i>
    <a href="#deleteeip" title="DeleteEip">DeleteEip</a>: <i>Boolean</i>
    <a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>Boolean</i>
    <a href="#ecsclusterarn" title="EcsClusterArn">EcsClusterArn</a>: <i>String</i>
    <a href="#elasticip" title="ElasticIp">ElasticIp</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#infrastructureclass" title="InfrastructureClass">InfrastructureClass</a>: <i>String</i>
    <a href="#installupdatesonboot" title="InstallUpdatesOnBoot">InstallUpdatesOnBoot</a>: <i>Boolean</i>
    <a href="#instanceprofilearn" title="InstanceProfileArn">InstanceProfileArn</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#lastserviceerrorid" title="LastServiceErrorId">LastServiceErrorId</a>: <i>String</i>
    <a href="#layerids" title="LayerIds">LayerIds</a>: <i>
      - String</i>
    <a href="#os" title="Os">Os</a>: <i>String</i>
    <a href="#platform" title="Platform">Platform</a>: <i>String</i>
    <a href="#privatedns" title="PrivateDns">PrivateDns</a>: <i>String</i>
    <a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>String</i>
    <a href="#publicdns" title="PublicDns">PublicDns</a>: <i>String</i>
    <a href="#publicip" title="PublicIp">PublicIp</a>: <i>String</i>
    <a href="#registeredby" title="RegisteredBy">RegisteredBy</a>: <i>String</i>
    <a href="#reportedagentversion" title="ReportedAgentVersion">ReportedAgentVersion</a>: <i>String</i>
    <a href="#reportedosfamily" title="ReportedOsFamily">ReportedOsFamily</a>: <i>String</i>
    <a href="#reportedosname" title="ReportedOsName">ReportedOsName</a>: <i>String</i>
    <a href="#reportedosversion" title="ReportedOsVersion">ReportedOsVersion</a>: <i>String</i>
    <a href="#rootdevicetype" title="RootDeviceType">RootDeviceType</a>: <i>String</i>
    <a href="#rootdevicevolumeid" title="RootDeviceVolumeId">RootDeviceVolumeId</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#sshhostdsakeyfingerprint" title="SshHostDsaKeyFingerprint">SshHostDsaKeyFingerprint</a>: <i>String</i>
    <a href="#sshhostrsakeyfingerprint" title="SshHostRsaKeyFingerprint">SshHostRsaKeyFingerprint</a>: <i>String</i>
    <a href="#sshkeyname" title="SshKeyName">SshKeyName</a>: <i>String</i>
    <a href="#stackid" title="StackId">StackId</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tenancy" title="Tenancy">Tenancy</a>: <i>String</i>
    <a href="#virtualizationtype" title="VirtualizationType">VirtualizationType</a>: <i>String</i>
    <a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>: <i>
      - <a href="ebsblockdevice.md">EbsBlockDevice</a></i>
    <a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>: <i>
      - <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a></i>
    <a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>: <i>
      - <a href="rootblockdevice.md">RootBlockDevice</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AgentVersion

The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AmiId

The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Architecture

Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingType

Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

Name of the availability zone where instances will be created
by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedAt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteEbs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteEip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

If true, the launched EC2 instance will be EBS-optimized.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsClusterArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The instance's host name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfrastructureClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallUpdatesOnBoot

Controls where to install OS and package updates when the instance boots.  Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceProfileArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The type of instance to start.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastServiceErrorId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LayerIds

The ids of the layers the instance will belong to.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Os

Name of operating system that will be installed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platform

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateDns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicDns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisteredBy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportedAgentVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportedOsFamily

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportedOsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportedOsVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootDeviceType

Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootDeviceVolumeId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshHostDsaKeyFingerprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshHostRsaKeyFingerprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyName

Name of the SSH keypair that instances will have by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackId

The id of the stack the instance will belong to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

The desired state of the instance.  Can be either `"running"` or `"stopped"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Subnet ID to attach to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenancy

Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualizationType

Keyword to choose what virtualization mode created instances
will use. Can be either `"paravirtual"` or `"hvm"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsBlockDevice

_Required_: No

_Type_: List of <a href="ebsblockdevice.md">EbsBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralBlockDevice

_Required_: No

_Type_: List of <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootBlockDevice

_Required_: No

_Type_: List of <a href="rootblockdevice.md">RootBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Ec2InstanceId

Returns the <code>Ec2InstanceId</code> value.

#### Id

Returns the <code>Id</code> value.

