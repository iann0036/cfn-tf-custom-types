# Terraform::AWS::SpotInstanceRequest

CloudFormation equivalent of aws_spot_instance_request

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SpotInstanceRequest",
    "Properties" : {
        "<a href="#ami" title="Ami">Ami</a>" : <i>String</i>,
        "<a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>" : <i>Boolean</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#blockdurationminutes" title="BlockDurationMinutes">BlockDurationMinutes</a>" : <i>Double</i>,
        "<a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>" : <i>Double</i>,
        "<a href="#cputhreadspercore" title="CpuThreadsPerCore">CpuThreadsPerCore</a>" : <i>Double</i>,
        "<a href="#disableapitermination" title="DisableApiTermination">DisableApiTermination</a>" : <i>Boolean</i>,
        "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#getpassworddata" title="GetPasswordData">GetPasswordData</a>" : <i>Boolean</i>,
        "<a href="#hibernation" title="Hibernation">Hibernation</a>" : <i>Boolean</i>,
        "<a href="#hostid" title="HostId">HostId</a>" : <i>String</i>,
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>String</i>,
        "<a href="#instanceinitiatedshutdownbehavior" title="InstanceInitiatedShutdownBehavior">InstanceInitiatedShutdownBehavior</a>" : <i>String</i>,
        "<a href="#instanceinterruptionbehaviour" title="InstanceInterruptionBehaviour">InstanceInterruptionBehaviour</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#ipv6addresscount" title="Ipv6AddressCount">Ipv6AddressCount</a>" : <i>Double</i>,
        "<a href="#ipv6addresses" title="Ipv6Addresses">Ipv6Addresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#launchgroup" title="LaunchGroup">LaunchGroup</a>" : <i>String</i>,
        "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>Boolean</i>,
        "<a href="#placementgroup" title="PlacementGroup">PlacementGroup</a>" : <i>String</i>,
        "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcedestcheck" title="SourceDestCheck">SourceDestCheck</a>" : <i>Boolean</i>,
        "<a href="#spotprice" title="SpotPrice">SpotPrice</a>" : <i>String</i>,
        "<a href="#spottype" title="SpotType">SpotType</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#tenancy" title="Tenancy">Tenancy</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#userdatabase64" title="UserDataBase64">UserDataBase64</a>" : <i>String</i>,
        "<a href="#validfrom" title="ValidFrom">ValidFrom</a>" : <i>String</i>,
        "<a href="#validuntil" title="ValidUntil">ValidUntil</a>" : <i>String</i>,
        "<a href="#volumetags" title="VolumeTags">VolumeTags</a>" : <i>[ <a href="volumetags.md">VolumeTags</a>, ... ]</i>,
        "<a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#waitforfulfillment" title="WaitForFulfillment">WaitForFulfillment</a>" : <i>Boolean</i>,
        "<a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>" : <i>[ <a href="creditspecification.md">CreditSpecification</a>, ... ]</i>,
        "<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>" : <i>[ <a href="ebsblockdevice.md">EbsBlockDevice</a>, ... ]</i>,
        "<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>" : <i>[ <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterface.md">NetworkInterface</a>, ... ]</i>,
        "<a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>" : <i>[ <a href="rootblockdevice.md">RootBlockDevice</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SpotInstanceRequest
Properties:
    <a href="#ami" title="Ami">Ami</a>: <i>String</i>
    <a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>: <i>Boolean</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#blockdurationminutes" title="BlockDurationMinutes">BlockDurationMinutes</a>: <i>Double</i>
    <a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>: <i>Double</i>
    <a href="#cputhreadspercore" title="CpuThreadsPerCore">CpuThreadsPerCore</a>: <i>Double</i>
    <a href="#disableapitermination" title="DisableApiTermination">DisableApiTermination</a>: <i>Boolean</i>
    <a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>Boolean</i>
    <a href="#getpassworddata" title="GetPasswordData">GetPasswordData</a>: <i>Boolean</i>
    <a href="#hibernation" title="Hibernation">Hibernation</a>: <i>Boolean</i>
    <a href="#hostid" title="HostId">HostId</a>: <i>String</i>
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>String</i>
    <a href="#instanceinitiatedshutdownbehavior" title="InstanceInitiatedShutdownBehavior">InstanceInitiatedShutdownBehavior</a>: <i>String</i>
    <a href="#instanceinterruptionbehaviour" title="InstanceInterruptionBehaviour">InstanceInterruptionBehaviour</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#ipv6addresscount" title="Ipv6AddressCount">Ipv6AddressCount</a>: <i>Double</i>
    <a href="#ipv6addresses" title="Ipv6Addresses">Ipv6Addresses</a>: <i>
      - String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#launchgroup" title="LaunchGroup">LaunchGroup</a>: <i>String</i>
    <a href="#monitoring" title="Monitoring">Monitoring</a>: <i>Boolean</i>
    <a href="#placementgroup" title="PlacementGroup">PlacementGroup</a>: <i>String</i>
    <a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#sourcedestcheck" title="SourceDestCheck">SourceDestCheck</a>: <i>Boolean</i>
    <a href="#spotprice" title="SpotPrice">SpotPrice</a>: <i>String</i>
    <a href="#spottype" title="SpotType">SpotType</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#tenancy" title="Tenancy">Tenancy</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#userdatabase64" title="UserDataBase64">UserDataBase64</a>: <i>String</i>
    <a href="#validfrom" title="ValidFrom">ValidFrom</a>: <i>String</i>
    <a href="#validuntil" title="ValidUntil">ValidUntil</a>: <i>String</i>
    <a href="#volumetags" title="VolumeTags">VolumeTags</a>: <i>
      - <a href="volumetags.md">VolumeTags</a></i>
    <a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#waitforfulfillment" title="WaitForFulfillment">WaitForFulfillment</a>: <i>Boolean</i>
    <a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>: <i>
      - <a href="creditspecification.md">CreditSpecification</a></i>
    <a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>: <i>
      - <a href="ebsblockdevice.md">EbsBlockDevice</a></i>
    <a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>: <i>
      - <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterface.md">NetworkInterface</a></i>
    <a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>: <i>
      - <a href="rootblockdevice.md">RootBlockDevice</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Ami

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatePublicIpAddress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDurationMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCoreCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuThreadsPerCore

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableApiTermination

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GetPasswordData

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hibernation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceInitiatedShutdownBehavior

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceInterruptionBehaviour

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6AddressCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Addresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDestCheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPrice

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenancy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDataBase64

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidFrom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidUntil

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeTags

_Required_: No

_Type_: List of <a href="volumetags.md">VolumeTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForFulfillment

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreditSpecification

_Required_: No

_Type_: List of <a href="creditspecification.md">CreditSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsBlockDevice

_Required_: No

_Type_: List of <a href="ebsblockdevice.md">EbsBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralBlockDevice

_Required_: No

_Type_: List of <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterface.md">NetworkInterface</a>

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

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

#### NetworkInterfaceId

Returns the <code>NetworkInterfaceId</code> value.

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

#### SpotBidStatus

Returns the <code>SpotBidStatus</code> value.

#### SpotInstanceId

Returns the <code>SpotInstanceId</code> value.

#### SpotRequestState

Returns the <code>SpotRequestState</code> value.

