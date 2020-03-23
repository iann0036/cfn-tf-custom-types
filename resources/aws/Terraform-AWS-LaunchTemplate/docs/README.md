# Terraform::AWS::LaunchTemplate

Provides an EC2 launch template resource. Can be used to create instances or auto scaling groups.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LaunchTemplate",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disableapitermination" title="DisableApiTermination">DisableApiTermination</a>" : <i>Boolean</i>,
        "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#instanceinitiatedshutdownbehavior" title="InstanceInitiatedShutdownBehavior">InstanceInitiatedShutdownBehavior</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#kernelid" title="KernelId">KernelId</a>" : <i>String</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#ramdiskid" title="RamDiskId">RamDiskId</a>" : <i>String</i>,
        "<a href="#securitygroupnames" title="SecurityGroupNames">SecurityGroupNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#blockdevicemappings" title="BlockDeviceMappings">BlockDeviceMappings</a>" : <i>[ <a href="blockdevicemappings.md">BlockDeviceMappings</a>, ... ]</i>,
        "<a href="#capacityreservationspecification" title="CapacityReservationSpecification">CapacityReservationSpecification</a>" : <i>[ <a href="capacityreservationspecification.md">CapacityReservationSpecification</a>, ... ]</i>,
        "<a href="#cpuoptions" title="CpuOptions">CpuOptions</a>" : <i>[ <a href="cpuoptions.md">CpuOptions</a>, ... ]</i>,
        "<a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>" : <i>[ <a href="creditspecification.md">CreditSpecification</a>, ... ]</i>,
        "<a href="#elasticgpuspecifications" title="ElasticGpuSpecifications">ElasticGpuSpecifications</a>" : <i>[ <a href="elasticgpuspecifications.md">ElasticGpuSpecifications</a>, ... ]</i>,
        "<a href="#elasticinferenceaccelerator" title="ElasticInferenceAccelerator">ElasticInferenceAccelerator</a>" : <i>[ <a href="elasticinferenceaccelerator.md">ElasticInferenceAccelerator</a>, ... ]</i>,
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>[ <a href="iaminstanceprofile.md">IamInstanceProfile</a>, ... ]</i>,
        "<a href="#instancemarketoptions" title="InstanceMarketOptions">InstanceMarketOptions</a>" : <i>[ <a href="instancemarketoptions.md">InstanceMarketOptions</a>, ... ]</i>,
        "<a href="#licensespecification" title="LicenseSpecification">LicenseSpecification</a>" : <i>[ <a href="licensespecification.md">LicenseSpecification</a>, ... ]</i>,
        "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>[ <a href="monitoring.md">Monitoring</a>, ... ]</i>,
        "<a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>" : <i>[ <a href="networkinterfaces.md">NetworkInterfaces</a>, ... ]</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ <a href="placement.md">Placement</a>, ... ]</i>,
        "<a href="#tagspecifications" title="TagSpecifications">TagSpecifications</a>" : <i>[ <a href="tagspecifications.md">TagSpecifications</a>, ... ]</i>,
        "<a href="#ebs" title="Ebs">Ebs</a>" : <i>[ <a href="ebs.md">Ebs</a>, ... ]</i>,
        "<a href="#capacityreservationtarget" title="CapacityReservationTarget">CapacityReservationTarget</a>" : <i>[ <a href="capacityreservationtarget.md">CapacityReservationTarget</a>, ... ]</i>,
        "<a href="#spotoptions" title="SpotOptions">SpotOptions</a>" : <i>[ <a href="spotoptions.md">SpotOptions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LaunchTemplate
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disableapitermination" title="DisableApiTermination">DisableApiTermination</a>: <i>Boolean</i>
    <a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#instanceinitiatedshutdownbehavior" title="InstanceInitiatedShutdownBehavior">InstanceInitiatedShutdownBehavior</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#kernelid" title="KernelId">KernelId</a>: <i>String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#ramdiskid" title="RamDiskId">RamDiskId</a>: <i>String</i>
    <a href="#securitygroupnames" title="SecurityGroupNames">SecurityGroupNames</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#blockdevicemappings" title="BlockDeviceMappings">BlockDeviceMappings</a>: <i>
      - <a href="blockdevicemappings.md">BlockDeviceMappings</a></i>
    <a href="#capacityreservationspecification" title="CapacityReservationSpecification">CapacityReservationSpecification</a>: <i>
      - <a href="capacityreservationspecification.md">CapacityReservationSpecification</a></i>
    <a href="#cpuoptions" title="CpuOptions">CpuOptions</a>: <i>
      - <a href="cpuoptions.md">CpuOptions</a></i>
    <a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>: <i>
      - <a href="creditspecification.md">CreditSpecification</a></i>
    <a href="#elasticgpuspecifications" title="ElasticGpuSpecifications">ElasticGpuSpecifications</a>: <i>
      - <a href="elasticgpuspecifications.md">ElasticGpuSpecifications</a></i>
    <a href="#elasticinferenceaccelerator" title="ElasticInferenceAccelerator">ElasticInferenceAccelerator</a>: <i>
      - <a href="elasticinferenceaccelerator.md">ElasticInferenceAccelerator</a></i>
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>
      - <a href="iaminstanceprofile.md">IamInstanceProfile</a></i>
    <a href="#instancemarketoptions" title="InstanceMarketOptions">InstanceMarketOptions</a>: <i>
      - <a href="instancemarketoptions.md">InstanceMarketOptions</a></i>
    <a href="#licensespecification" title="LicenseSpecification">LicenseSpecification</a>: <i>
      - <a href="licensespecification.md">LicenseSpecification</a></i>
    <a href="#monitoring" title="Monitoring">Monitoring</a>: <i>
      - <a href="monitoring.md">Monitoring</a></i>
    <a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>: <i>
      - <a href="networkinterfaces.md">NetworkInterfaces</a></i>
    <a href="#placement" title="Placement">Placement</a>: <i>
      - <a href="placement.md">Placement</a></i>
    <a href="#tagspecifications" title="TagSpecifications">TagSpecifications</a>: <i>
      - <a href="tagspecifications.md">TagSpecifications</a></i>
    <a href="#ebs" title="Ebs">Ebs</a>: <i>
      - <a href="ebs.md">Ebs</a></i>
    <a href="#capacityreservationtarget" title="CapacityReservationTarget">CapacityReservationTarget</a>: <i>
      - <a href="capacityreservationtarget.md">CapacityReservationTarget</a></i>
    <a href="#spotoptions" title="SpotOptions">SpotOptions</a>: <i>
      - <a href="spotoptions.md">SpotOptions</a></i>
</pre>

## Properties

#### Description

Description of the launch template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableApiTermination

If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

If `true`, the launched EC2 instance will be EBS-optimized.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

The AMI from which to launch the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceInitiatedShutdownBehavior

Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The type of the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelId

The kernel ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

The key name to use for the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the launch template. If you leave this blank, Terraform will auto-generate a unique name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

Creates a unique name beginning with the specified prefix. Conflicts with `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RamDiskId

The ID of the RAM disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupNames

A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the launch template.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

The Base64-encoded user data to provide when launching the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSecurityGroupIds

A list of security group IDs to associate with.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDeviceMappings

_Required_: No

_Type_: List of <a href="blockdevicemappings.md">BlockDeviceMappings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityReservationSpecification

_Required_: No

_Type_: List of <a href="capacityreservationspecification.md">CapacityReservationSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuOptions

_Required_: No

_Type_: List of <a href="cpuoptions.md">CpuOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreditSpecification

_Required_: No

_Type_: List of <a href="creditspecification.md">CreditSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticGpuSpecifications

_Required_: No

_Type_: List of <a href="elasticgpuspecifications.md">ElasticGpuSpecifications</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticInferenceAccelerator

_Required_: No

_Type_: List of <a href="elasticinferenceaccelerator.md">ElasticInferenceAccelerator</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

_Required_: No

_Type_: List of <a href="iaminstanceprofile.md">IamInstanceProfile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceMarketOptions

_Required_: No

_Type_: List of <a href="instancemarketoptions.md">InstanceMarketOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseSpecification

_Required_: No

_Type_: List of <a href="licensespecification.md">LicenseSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

_Required_: No

_Type_: List of <a href="monitoring.md">Monitoring</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaces

_Required_: No

_Type_: List of <a href="networkinterfaces.md">NetworkInterfaces</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of <a href="placement.md">Placement</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagSpecifications

_Required_: No

_Type_: List of <a href="tagspecifications.md">TagSpecifications</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ebs

_Required_: No

_Type_: List of <a href="ebs.md">Ebs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityReservationTarget

_Required_: No

_Type_: List of <a href="capacityreservationtarget.md">CapacityReservationTarget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotOptions

_Required_: No

_Type_: List of <a href="spotoptions.md">SpotOptions</a>

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

#### DefaultVersion

Returns the <code>DefaultVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### LatestVersion

Returns the <code>LatestVersion</code> value.

