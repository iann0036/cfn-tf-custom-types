# TF::AWS::LaunchTemplate

Provides an EC2 launch template resource. Can be used to create instances or auto scaling groups.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LaunchTemplate",
    "Properties" : {
        "<a href="#defaultversion" title="DefaultVersion">DefaultVersion</a>" : <i>Double</i>,
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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#updatedefaultversion" title="UpdateDefaultVersion">UpdateDefaultVersion</a>" : <i>Boolean</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#blockdevicemappings" title="BlockDeviceMappings">BlockDeviceMappings</a>" : <i>[ <a href="blockdevicemappingsdefinition.md">BlockDeviceMappingsDefinition</a>, ... ]</i>,
        "<a href="#capacityreservationspecification" title="CapacityReservationSpecification">CapacityReservationSpecification</a>" : <i>[ <a href="capacityreservationspecificationdefinition.md">CapacityReservationSpecificationDefinition</a>, ... ]</i>,
        "<a href="#cpuoptions" title="CpuOptions">CpuOptions</a>" : <i>[ <a href="cpuoptionsdefinition.md">CpuOptionsDefinition</a>, ... ]</i>,
        "<a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>" : <i>[ <a href="creditspecificationdefinition.md">CreditSpecificationDefinition</a>, ... ]</i>,
        "<a href="#elasticgpuspecifications" title="ElasticGpuSpecifications">ElasticGpuSpecifications</a>" : <i>[ <a href="elasticgpuspecificationsdefinition.md">ElasticGpuSpecificationsDefinition</a>, ... ]</i>,
        "<a href="#elasticinferenceaccelerator" title="ElasticInferenceAccelerator">ElasticInferenceAccelerator</a>" : <i>[ <a href="elasticinferenceacceleratordefinition.md">ElasticInferenceAcceleratorDefinition</a>, ... ]</i>,
        "<a href="#enclaveoptions" title="EnclaveOptions">EnclaveOptions</a>" : <i>[ <a href="enclaveoptionsdefinition.md">EnclaveOptionsDefinition</a>, ... ]</i>,
        "<a href="#hibernationoptions" title="HibernationOptions">HibernationOptions</a>" : <i>[ <a href="hibernationoptionsdefinition.md">HibernationOptionsDefinition</a>, ... ]</i>,
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>[ <a href="iaminstanceprofiledefinition.md">IamInstanceProfileDefinition</a>, ... ]</i>,
        "<a href="#instancemarketoptions" title="InstanceMarketOptions">InstanceMarketOptions</a>" : <i>[ <a href="instancemarketoptionsdefinition.md">InstanceMarketOptionsDefinition</a>, ... ]</i>,
        "<a href="#licensespecification" title="LicenseSpecification">LicenseSpecification</a>" : <i>[ <a href="licensespecificationdefinition.md">LicenseSpecificationDefinition</a>, ... ]</i>,
        "<a href="#metadataoptions" title="MetadataOptions">MetadataOptions</a>" : <i>[ <a href="metadataoptionsdefinition.md">MetadataOptionsDefinition</a>, ... ]</i>,
        "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>[ <a href="monitoringdefinition.md">MonitoringDefinition</a>, ... ]</i>,
        "<a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>" : <i>[ <a href="networkinterfacesdefinition.md">NetworkInterfacesDefinition</a>, ... ]</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ <a href="placementdefinition.md">PlacementDefinition</a>, ... ]</i>,
        "<a href="#tagspecifications" title="TagSpecifications">TagSpecifications</a>" : <i>[ <a href="tagspecificationsdefinition.md">TagSpecificationsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LaunchTemplate
Properties:
    <a href="#defaultversion" title="DefaultVersion">DefaultVersion</a>: <i>Double</i>
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
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#updatedefaultversion" title="UpdateDefaultVersion">UpdateDefaultVersion</a>: <i>Boolean</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#blockdevicemappings" title="BlockDeviceMappings">BlockDeviceMappings</a>: <i>
      - <a href="blockdevicemappingsdefinition.md">BlockDeviceMappingsDefinition</a></i>
    <a href="#capacityreservationspecification" title="CapacityReservationSpecification">CapacityReservationSpecification</a>: <i>
      - <a href="capacityreservationspecificationdefinition.md">CapacityReservationSpecificationDefinition</a></i>
    <a href="#cpuoptions" title="CpuOptions">CpuOptions</a>: <i>
      - <a href="cpuoptionsdefinition.md">CpuOptionsDefinition</a></i>
    <a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>: <i>
      - <a href="creditspecificationdefinition.md">CreditSpecificationDefinition</a></i>
    <a href="#elasticgpuspecifications" title="ElasticGpuSpecifications">ElasticGpuSpecifications</a>: <i>
      - <a href="elasticgpuspecificationsdefinition.md">ElasticGpuSpecificationsDefinition</a></i>
    <a href="#elasticinferenceaccelerator" title="ElasticInferenceAccelerator">ElasticInferenceAccelerator</a>: <i>
      - <a href="elasticinferenceacceleratordefinition.md">ElasticInferenceAcceleratorDefinition</a></i>
    <a href="#enclaveoptions" title="EnclaveOptions">EnclaveOptions</a>: <i>
      - <a href="enclaveoptionsdefinition.md">EnclaveOptionsDefinition</a></i>
    <a href="#hibernationoptions" title="HibernationOptions">HibernationOptions</a>: <i>
      - <a href="hibernationoptionsdefinition.md">HibernationOptionsDefinition</a></i>
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>
      - <a href="iaminstanceprofiledefinition.md">IamInstanceProfileDefinition</a></i>
    <a href="#instancemarketoptions" title="InstanceMarketOptions">InstanceMarketOptions</a>: <i>
      - <a href="instancemarketoptionsdefinition.md">InstanceMarketOptionsDefinition</a></i>
    <a href="#licensespecification" title="LicenseSpecification">LicenseSpecification</a>: <i>
      - <a href="licensespecificationdefinition.md">LicenseSpecificationDefinition</a></i>
    <a href="#metadataoptions" title="MetadataOptions">MetadataOptions</a>: <i>
      - <a href="metadataoptionsdefinition.md">MetadataOptionsDefinition</a></i>
    <a href="#monitoring" title="Monitoring">Monitoring</a>: <i>
      - <a href="monitoringdefinition.md">MonitoringDefinition</a></i>
    <a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>: <i>
      - <a href="networkinterfacesdefinition.md">NetworkInterfacesDefinition</a></i>
    <a href="#placement" title="Placement">Placement</a>: <i>
      - <a href="placementdefinition.md">PlacementDefinition</a></i>
    <a href="#tagspecifications" title="TagSpecifications">TagSpecifications</a>: <i>
      - <a href="tagspecificationsdefinition.md">TagSpecificationsDefinition</a></i>
</pre>

## Properties

#### DefaultVersion

Default Version of the launch template.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

A map of tags to assign to the launch template. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateDefaultVersion

Whether to update Default Version each update. Conflicts with `default_version`.

_Required_: No

_Type_: Boolean

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

_Type_: List of <a href="blockdevicemappingsdefinition.md">BlockDeviceMappingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityReservationSpecification

_Required_: No

_Type_: List of <a href="capacityreservationspecificationdefinition.md">CapacityReservationSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuOptions

_Required_: No

_Type_: List of <a href="cpuoptionsdefinition.md">CpuOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreditSpecification

_Required_: No

_Type_: List of <a href="creditspecificationdefinition.md">CreditSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticGpuSpecifications

_Required_: No

_Type_: List of <a href="elasticgpuspecificationsdefinition.md">ElasticGpuSpecificationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticInferenceAccelerator

_Required_: No

_Type_: List of <a href="elasticinferenceacceleratordefinition.md">ElasticInferenceAcceleratorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnclaveOptions

_Required_: No

_Type_: List of <a href="enclaveoptionsdefinition.md">EnclaveOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HibernationOptions

_Required_: No

_Type_: List of <a href="hibernationoptionsdefinition.md">HibernationOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

_Required_: No

_Type_: List of <a href="iaminstanceprofiledefinition.md">IamInstanceProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceMarketOptions

_Required_: No

_Type_: List of <a href="instancemarketoptionsdefinition.md">InstanceMarketOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseSpecification

_Required_: No

_Type_: List of <a href="licensespecificationdefinition.md">LicenseSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataOptions

_Required_: No

_Type_: List of <a href="metadataoptionsdefinition.md">MetadataOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

_Required_: No

_Type_: List of <a href="monitoringdefinition.md">MonitoringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaces

_Required_: No

_Type_: List of <a href="networkinterfacesdefinition.md">NetworkInterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of <a href="placementdefinition.md">PlacementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagSpecifications

_Required_: No

_Type_: List of <a href="tagspecificationsdefinition.md">TagSpecificationsDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### LatestVersion

Returns the <code>LatestVersion</code> value.

