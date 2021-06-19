# TF::Rancher2::NodeTemplate OpenstackConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activetimeout" title="ActiveTimeout">ActiveTimeout</a>" : <i>String</i>,
    "<a href="#applicationcredentialid" title="ApplicationCredentialId">ApplicationCredentialId</a>" : <i>String</i>,
    "<a href="#applicationcredentialname" title="ApplicationCredentialName">ApplicationCredentialName</a>" : <i>String</i>,
    "<a href="#applicationcredentialsecret" title="ApplicationCredentialSecret">ApplicationCredentialSecret</a>" : <i>String</i>,
    "<a href="#authurl" title="AuthUrl">AuthUrl</a>" : <i>String</i>,
    "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
    "<a href="#bootfromvolume" title="BootFromVolume">BootFromVolume</a>" : <i>Boolean</i>,
    "<a href="#cacert" title="Cacert">Cacert</a>" : <i>String</i>,
    "<a href="#configdrive" title="ConfigDrive">ConfigDrive</a>" : <i>Boolean</i>,
    "<a href="#domainid" title="DomainId">DomainId</a>" : <i>String</i>,
    "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
    "<a href="#endpointtype" title="EndpointType">EndpointType</a>" : <i>String</i>,
    "<a href="#flavorid" title="FlavorId">FlavorId</a>" : <i>String</i>,
    "<a href="#flavorname" title="FlavorName">FlavorName</a>" : <i>String</i>,
    "<a href="#floatingippool" title="FloatingIpPool">FloatingIpPool</a>" : <i>String</i>,
    "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
    "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
    "<a href="#insecure" title="Insecure">Insecure</a>" : <i>Boolean</i>,
    "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>String</i>,
    "<a href="#keypairname" title="KeypairName">KeypairName</a>" : <i>String</i>,
    "<a href="#netid" title="NetId">NetId</a>" : <i>String</i>,
    "<a href="#netname" title="NetName">NetName</a>" : <i>String</i>,
    "<a href="#novanetwork" title="NovaNetwork">NovaNetwork</a>" : <i>Boolean</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#privatekeyfile" title="PrivateKeyFile">PrivateKeyFile</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#secgroups" title="SecGroups">SecGroups</a>" : <i>String</i>,
    "<a href="#sshport" title="SshPort">SshPort</a>" : <i>String</i>,
    "<a href="#sshuser" title="SshUser">SshUser</a>" : <i>String</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
    "<a href="#tenantname" title="TenantName">TenantName</a>" : <i>String</i>,
    "<a href="#userdatafile" title="UserDataFile">UserDataFile</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#volumedevicepath" title="VolumeDevicePath">VolumeDevicePath</a>" : <i>String</i>,
    "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>,
    "<a href="#volumename" title="VolumeName">VolumeName</a>" : <i>String</i>,
    "<a href="#volumesize" title="VolumeSize">VolumeSize</a>" : <i>String</i>,
    "<a href="#volumetype" title="VolumeType">VolumeType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#activetimeout" title="ActiveTimeout">ActiveTimeout</a>: <i>String</i>
<a href="#applicationcredentialid" title="ApplicationCredentialId">ApplicationCredentialId</a>: <i>String</i>
<a href="#applicationcredentialname" title="ApplicationCredentialName">ApplicationCredentialName</a>: <i>String</i>
<a href="#applicationcredentialsecret" title="ApplicationCredentialSecret">ApplicationCredentialSecret</a>: <i>String</i>
<a href="#authurl" title="AuthUrl">AuthUrl</a>: <i>String</i>
<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
<a href="#bootfromvolume" title="BootFromVolume">BootFromVolume</a>: <i>Boolean</i>
<a href="#cacert" title="Cacert">Cacert</a>: <i>String</i>
<a href="#configdrive" title="ConfigDrive">ConfigDrive</a>: <i>Boolean</i>
<a href="#domainid" title="DomainId">DomainId</a>: <i>String</i>
<a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
<a href="#endpointtype" title="EndpointType">EndpointType</a>: <i>String</i>
<a href="#flavorid" title="FlavorId">FlavorId</a>: <i>String</i>
<a href="#flavorname" title="FlavorName">FlavorName</a>: <i>String</i>
<a href="#floatingippool" title="FloatingIpPool">FloatingIpPool</a>: <i>String</i>
<a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
<a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
<a href="#insecure" title="Insecure">Insecure</a>: <i>Boolean</i>
<a href="#ipversion" title="IpVersion">IpVersion</a>: <i>String</i>
<a href="#keypairname" title="KeypairName">KeypairName</a>: <i>String</i>
<a href="#netid" title="NetId">NetId</a>: <i>String</i>
<a href="#netname" title="NetName">NetName</a>: <i>String</i>
<a href="#novanetwork" title="NovaNetwork">NovaNetwork</a>: <i>Boolean</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#privatekeyfile" title="PrivateKeyFile">PrivateKeyFile</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#secgroups" title="SecGroups">SecGroups</a>: <i>String</i>
<a href="#sshport" title="SshPort">SshPort</a>: <i>String</i>
<a href="#sshuser" title="SshUser">SshUser</a>: <i>String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
<a href="#tenantname" title="TenantName">TenantName</a>: <i>String</i>
<a href="#userdatafile" title="UserDataFile">UserDataFile</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#volumedevicepath" title="VolumeDevicePath">VolumeDevicePath</a>: <i>String</i>
<a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
<a href="#volumename" title="VolumeName">VolumeName</a>: <i>String</i>
<a href="#volumesize" title="VolumeSize">VolumeSize</a>: <i>String</i>
<a href="#volumetype" title="VolumeType">VolumeType</a>: <i>String</i>
</pre>

## Properties

#### ActiveTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationCredentialId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationCredentialName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationCredentialSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootFromVolume

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cacert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigDrive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIpPool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Insecure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeypairName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NovaNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecGroups

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDataFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeDevicePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

