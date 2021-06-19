# TF::Rancher2::NodeTemplate Amazonec2ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
    "<a href="#ami" title="Ami">Ami</a>" : <i>String</i>,
    "<a href="#blockdurationminutes" title="BlockDurationMinutes">BlockDurationMinutes</a>" : <i>String</i>,
    "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
    "<a href="#encryptebsvolume" title="EncryptEbsVolume">EncryptEbsVolume</a>" : <i>Boolean</i>,
    "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
    "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>String</i>,
    "<a href="#insecuretransport" title="InsecureTransport">InsecureTransport</a>" : <i>Boolean</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#keypairname" title="KeypairName">KeypairName</a>" : <i>String</i>,
    "<a href="#kmskey" title="KmsKey">KmsKey</a>" : <i>String</i>,
    "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>Boolean</i>,
    "<a href="#openport" title="OpenPort">OpenPort</a>" : <i>[ String, ... ]</i>,
    "<a href="#privateaddressonly" title="PrivateAddressOnly">PrivateAddressOnly</a>" : <i>Boolean</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#requestspotinstance" title="RequestSpotInstance">RequestSpotInstance</a>" : <i>Boolean</i>,
    "<a href="#retries" title="Retries">Retries</a>" : <i>String</i>,
    "<a href="#rootsize" title="RootSize">RootSize</a>" : <i>String</i>,
    "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>,
    "<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>" : <i>[ String, ... ]</i>,
    "<a href="#securitygroupreadonly" title="SecurityGroupReadonly">SecurityGroupReadonly</a>" : <i>Boolean</i>,
    "<a href="#sessiontoken" title="SessionToken">SessionToken</a>" : <i>String</i>,
    "<a href="#spotprice" title="SpotPrice">SpotPrice</a>" : <i>String</i>,
    "<a href="#sshkeypath" title="SshKeypath">SshKeypath</a>" : <i>String</i>,
    "<a href="#sshuser" title="SshUser">SshUser</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>String</i>,
    "<a href="#useebsoptimizedinstance" title="UseEbsOptimizedInstance">UseEbsOptimizedInstance</a>" : <i>Boolean</i>,
    "<a href="#useprivateaddress" title="UsePrivateAddress">UsePrivateAddress</a>" : <i>Boolean</i>,
    "<a href="#userdata" title="Userdata">Userdata</a>" : <i>String</i>,
    "<a href="#volumetype" title="VolumeType">VolumeType</a>" : <i>String</i>,
    "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
<a href="#ami" title="Ami">Ami</a>: <i>String</i>
<a href="#blockdurationminutes" title="BlockDurationMinutes">BlockDurationMinutes</a>: <i>String</i>
<a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
<a href="#encryptebsvolume" title="EncryptEbsVolume">EncryptEbsVolume</a>: <i>Boolean</i>
<a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>String</i>
<a href="#insecuretransport" title="InsecureTransport">InsecureTransport</a>: <i>Boolean</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#keypairname" title="KeypairName">KeypairName</a>: <i>String</i>
<a href="#kmskey" title="KmsKey">KmsKey</a>: <i>String</i>
<a href="#monitoring" title="Monitoring">Monitoring</a>: <i>Boolean</i>
<a href="#openport" title="OpenPort">OpenPort</a>: <i>
      - String</i>
<a href="#privateaddressonly" title="PrivateAddressOnly">PrivateAddressOnly</a>: <i>Boolean</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#requestspotinstance" title="RequestSpotInstance">RequestSpotInstance</a>: <i>Boolean</i>
<a href="#retries" title="Retries">Retries</a>: <i>String</i>
<a href="#rootsize" title="RootSize">RootSize</a>: <i>String</i>
<a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>: <i>
      - String</i>
<a href="#securitygroupreadonly" title="SecurityGroupReadonly">SecurityGroupReadonly</a>: <i>Boolean</i>
<a href="#sessiontoken" title="SessionToken">SessionToken</a>: <i>String</i>
<a href="#spotprice" title="SpotPrice">SpotPrice</a>: <i>String</i>
<a href="#sshkeypath" title="SshKeypath">SshKeypath</a>: <i>String</i>
<a href="#sshuser" title="SshUser">SshUser</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>String</i>
<a href="#useebsoptimizedinstance" title="UseEbsOptimizedInstance">UseEbsOptimizedInstance</a>: <i>Boolean</i>
<a href="#useprivateaddress" title="UsePrivateAddress">UsePrivateAddress</a>: <i>Boolean</i>
<a href="#userdata" title="Userdata">Userdata</a>: <i>String</i>
<a href="#volumetype" title="VolumeType">VolumeType</a>: <i>String</i>
<a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
<a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### AccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ami

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDurationMinutes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptEbsVolume

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsecureTransport

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeypairName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenPort

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateAddressOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSpotInstance

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retries

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroup

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupReadonly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPrice

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeypath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseEbsOptimizedInstance

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePrivateAddress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Userdata

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

