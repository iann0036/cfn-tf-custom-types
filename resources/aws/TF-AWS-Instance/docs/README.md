# TF::AWS::Instance

Provides an EC2 instance resource. This allows instances to be created, updated, and deleted. Instances also support [provisioning](https://www.terraform.io/docs/provisioners/index.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Instance",
    "Properties" : {
        "<a href="#ami" title="Ami">Ami</a>" : <i>String</i>,
        "<a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>" : <i>Boolean</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>" : <i>Double</i>,
        "<a href="#cputhreadspercore" title="CpuThreadsPerCore">CpuThreadsPerCore</a>" : <i>Double</i>,
        "<a href="#disableapitermination" title="DisableApiTermination">DisableApiTermination</a>" : <i>Boolean</i>,
        "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#getpassworddata" title="GetPasswordData">GetPasswordData</a>" : <i>Boolean</i>,
        "<a href="#hibernation" title="Hibernation">Hibernation</a>" : <i>Boolean</i>,
        "<a href="#hostid" title="HostId">HostId</a>" : <i>String</i>,
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>String</i>,
        "<a href="#instanceinitiatedshutdownbehavior" title="InstanceInitiatedShutdownBehavior">InstanceInitiatedShutdownBehavior</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#ipv6addresscount" title="Ipv6AddressCount">Ipv6AddressCount</a>" : <i>Double</i>,
        "<a href="#ipv6addresses" title="Ipv6Addresses">Ipv6Addresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>Boolean</i>,
        "<a href="#placementgroup" title="PlacementGroup">PlacementGroup</a>" : <i>String</i>,
        "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>String</i>,
        "<a href="#secondaryprivateips" title="SecondaryPrivateIps">SecondaryPrivateIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcedestcheck" title="SourceDestCheck">SourceDestCheck</a>" : <i>Boolean</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#tenancy" title="Tenancy">Tenancy</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#userdatabase64" title="UserDataBase64">UserDataBase64</a>" : <i>String</i>,
        "<a href="#volumetags" title="VolumeTags">VolumeTags</a>" : <i>[ <a href="volumetagsdefinition.md">VolumeTagsDefinition</a>, ... ]</i>,
        "<a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#capacityreservationspecification" title="CapacityReservationSpecification">CapacityReservationSpecification</a>" : <i>[ <a href="capacityreservationspecificationdefinition.md">CapacityReservationSpecificationDefinition</a>, ... ]</i>,
        "<a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>" : <i>[ <a href="creditspecificationdefinition.md">CreditSpecificationDefinition</a>, ... ]</i>,
        "<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>" : <i>[ <a href="ebsblockdevicedefinition.md">EbsBlockDeviceDefinition</a>, ... ]</i>,
        "<a href="#enclaveoptions" title="EnclaveOptions">EnclaveOptions</a>" : <i>[ <a href="enclaveoptionsdefinition.md">EnclaveOptionsDefinition</a>, ... ]</i>,
        "<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>" : <i>[ <a href="ephemeralblockdevicedefinition.md">EphemeralBlockDeviceDefinition</a>, ... ]</i>,
        "<a href="#metadataoptions" title="MetadataOptions">MetadataOptions</a>" : <i>[ <a href="metadataoptionsdefinition.md">MetadataOptionsDefinition</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>, ... ]</i>,
        "<a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>" : <i>[ <a href="rootblockdevicedefinition.md">RootBlockDeviceDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Instance
Properties:
    <a href="#ami" title="Ami">Ami</a>: <i>String</i>
    <a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>: <i>Boolean</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>: <i>Double</i>
    <a href="#cputhreadspercore" title="CpuThreadsPerCore">CpuThreadsPerCore</a>: <i>Double</i>
    <a href="#disableapitermination" title="DisableApiTermination">DisableApiTermination</a>: <i>Boolean</i>
    <a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>Boolean</i>
    <a href="#getpassworddata" title="GetPasswordData">GetPasswordData</a>: <i>Boolean</i>
    <a href="#hibernation" title="Hibernation">Hibernation</a>: <i>Boolean</i>
    <a href="#hostid" title="HostId">HostId</a>: <i>String</i>
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>String</i>
    <a href="#instanceinitiatedshutdownbehavior" title="InstanceInitiatedShutdownBehavior">InstanceInitiatedShutdownBehavior</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#ipv6addresscount" title="Ipv6AddressCount">Ipv6AddressCount</a>: <i>Double</i>
    <a href="#ipv6addresses" title="Ipv6Addresses">Ipv6Addresses</a>: <i>
      - String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#monitoring" title="Monitoring">Monitoring</a>: <i>Boolean</i>
    <a href="#placementgroup" title="PlacementGroup">PlacementGroup</a>: <i>String</i>
    <a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>String</i>
    <a href="#secondaryprivateips" title="SecondaryPrivateIps">SecondaryPrivateIps</a>: <i>
      - String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#sourcedestcheck" title="SourceDestCheck">SourceDestCheck</a>: <i>Boolean</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#tenancy" title="Tenancy">Tenancy</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#userdatabase64" title="UserDataBase64">UserDataBase64</a>: <i>String</i>
    <a href="#volumetags" title="VolumeTags">VolumeTags</a>: <i>
      - <a href="volumetagsdefinition.md">VolumeTagsDefinition</a></i>
    <a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#capacityreservationspecification" title="CapacityReservationSpecification">CapacityReservationSpecification</a>: <i>
      - <a href="capacityreservationspecificationdefinition.md">CapacityReservationSpecificationDefinition</a></i>
    <a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>: <i>
      - <a href="creditspecificationdefinition.md">CreditSpecificationDefinition</a></i>
    <a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>: <i>
      - <a href="ebsblockdevicedefinition.md">EbsBlockDeviceDefinition</a></i>
    <a href="#enclaveoptions" title="EnclaveOptions">EnclaveOptions</a>: <i>
      - <a href="enclaveoptionsdefinition.md">EnclaveOptionsDefinition</a></i>
    <a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>: <i>
      - <a href="ephemeralblockdevicedefinition.md">EphemeralBlockDeviceDefinition</a></i>
    <a href="#metadataoptions" title="MetadataOptions">MetadataOptions</a>: <i>
      - <a href="metadataoptionsdefinition.md">MetadataOptionsDefinition</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a></i>
    <a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>: <i>
      - <a href="rootblockdevicedefinition.md">RootBlockDeviceDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Ami

AMI to use for the instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatePublicIpAddress

Whether to associate a public IP address with an instance in a VPC.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

AZ to start the instance in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCoreCount

Sets the number of CPU cores for an instance. This option is only supported on creation of instance type that support CPU Options [CPU Cores and Threads Per CPU Core Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values) - specifying this option for unsupported instance types will return an error from the EC2 API.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuThreadsPerCore

If set to to 1, hyperthreading is disabled on the launched instance. Defaults to 2 if not set. See [Optimizing CPU Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for more information.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableApiTermination

If true, enables [EC2 Instance Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

If true, the launched EC2 instance will be EBS-optimized. Note that if this is not set on an instance type that is optimized by default then this will show as disabled but if the instance type is optimized by default then there is no need to set this and there is no effect to disabling it. See the [EBS Optimized section](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) of the AWS User Guide for more information.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GetPasswordData

If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hibernation

If true, the launched EC2 instance will support hibernation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostId

ID of a dedicated host that the instance will be assigned to. Use when an instance is to be launched on a specific dedicated host.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

IAM Instance Profile to launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the [EC2 documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions), notably `iam:PassRole`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceInitiatedShutdownBehavior

Shutdown behavior for the instance. Amazon defaults this to `stop` for EBS-backed instances and `terminate` for instance-store instances. Cannot be set on instance-store instances. See [Shutdown Behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior) for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

Type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6AddressCount

A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Addresses

Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

Key name of the Key Pair to use for the instance; which can be managed using [the `aws_key_pair` resource](key_pair.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementGroup

Placement Group to start the instance in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

Private IP address to associate with the instance in a VPC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryPrivateIps

A list of secondary private IPv4 addresses to assign to the instance's primary network interface (eth0) in a VPC. Can only be assigned to the primary network interface (eth0) attached at instance creation, not a pre-existing network interface i.e. referenced in a `network_interface` block. Refer to the [Elastic network interfaces documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI) to see the maximum number of private IP addresses allowed per instance type.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

A list of security group names (EC2-Classic) or IDs (default VPC) to associate with.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDestCheck

Controls if traffic is routed to the instance when the destination address does not match the instance. Used for NAT or VPNs. Defaults true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

VPC Subnet ID to launch in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. Note that these tags apply to the instance and not block storage devices. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenancy

Tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

User data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDataBase64

Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeTags

A map of tags to assign, at instance-creation time, to root and EBS volumes.

_Required_: No

_Type_: List of <a href="volumetagsdefinition.md">VolumeTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSecurityGroupIds

A list of security group IDs to associate with.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityReservationSpecification

_Required_: No

_Type_: List of <a href="capacityreservationspecificationdefinition.md">CapacityReservationSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreditSpecification

_Required_: No

_Type_: List of <a href="creditspecificationdefinition.md">CreditSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsBlockDevice

_Required_: No

_Type_: List of <a href="ebsblockdevicedefinition.md">EbsBlockDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnclaveOptions

_Required_: No

_Type_: List of <a href="enclaveoptionsdefinition.md">EnclaveOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralBlockDevice

_Required_: No

_Type_: List of <a href="ephemeralblockdevicedefinition.md">EphemeralBlockDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataOptions

_Required_: No

_Type_: List of <a href="metadataoptionsdefinition.md">MetadataOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootBlockDevice

_Required_: No

_Type_: List of <a href="rootblockdevicedefinition.md">RootBlockDeviceDefinition</a>

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceState

Returns the <code>InstanceState</code> value.

#### OutpostArn

Returns the <code>OutpostArn</code> value.

#### PasswordData

Returns the <code>PasswordData</code> value.

#### PrimaryNetworkInterfaceId

Returns the <code>PrimaryNetworkInterfaceId</code> value.

#### PrivateDns

Returns the <code>PrivateDns</code> value.

#### PublicDns

Returns the <code>PublicDns</code> value.

#### PublicIp

Returns the <code>PublicIp</code> value.

