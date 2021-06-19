# TF::Rancher2::NodeTemplate VsphereConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#boot2dockerurl" title="Boot2dockerUrl">Boot2dockerUrl</a>" : <i>String</i>,
    "<a href="#cfgparam" title="Cfgparam">Cfgparam</a>" : <i>[ String, ... ]</i>,
    "<a href="#clonefrom" title="CloneFrom">CloneFrom</a>" : <i>String</i>,
    "<a href="#cloudconfig" title="CloudConfig">CloudConfig</a>" : <i>String</i>,
    "<a href="#cloudinit" title="Cloudinit">Cloudinit</a>" : <i>String</i>,
    "<a href="#contentlibrary" title="ContentLibrary">ContentLibrary</a>" : <i>String</i>,
    "<a href="#cpucount" title="CpuCount">CpuCount</a>" : <i>String</i>,
    "<a href="#creationtype" title="CreationType">CreationType</a>" : <i>String</i>,
    "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ String, ... ]</i>,
    "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
    "<a href="#datastore" title="Datastore">Datastore</a>" : <i>String</i>,
    "<a href="#datastorecluster" title="DatastoreCluster">DatastoreCluster</a>" : <i>String</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>String</i>,
    "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
    "<a href="#hostsystem" title="Hostsystem">Hostsystem</a>" : <i>String</i>,
    "<a href="#memorysize" title="MemorySize">MemorySize</a>" : <i>String</i>,
    "<a href="#network" title="Network">Network</a>" : <i>[ String, ... ]</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#pool" title="Pool">Pool</a>" : <i>String</i>,
    "<a href="#sshpassword" title="SshPassword">SshPassword</a>" : <i>String</i>,
    "<a href="#sshport" title="SshPort">SshPort</a>" : <i>String</i>,
    "<a href="#sshuser" title="SshUser">SshUser</a>" : <i>String</i>,
    "<a href="#sshusergroup" title="SshUserGroup">SshUserGroup</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#vappipallocationpolicy" title="VappIpAllocationPolicy">VappIpAllocationPolicy</a>" : <i>String</i>,
    "<a href="#vappipprotocol" title="VappIpProtocol">VappIpProtocol</a>" : <i>String</i>,
    "<a href="#vappproperty" title="VappProperty">VappProperty</a>" : <i>[ String, ... ]</i>,
    "<a href="#vapptransport" title="VappTransport">VappTransport</a>" : <i>String</i>,
    "<a href="#vcenter" title="Vcenter">Vcenter</a>" : <i>String</i>,
    "<a href="#vcenterport" title="VcenterPort">VcenterPort</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#boot2dockerurl" title="Boot2dockerUrl">Boot2dockerUrl</a>: <i>String</i>
<a href="#cfgparam" title="Cfgparam">Cfgparam</a>: <i>
      - String</i>
<a href="#clonefrom" title="CloneFrom">CloneFrom</a>: <i>String</i>
<a href="#cloudconfig" title="CloudConfig">CloudConfig</a>: <i>String</i>
<a href="#cloudinit" title="Cloudinit">Cloudinit</a>: <i>String</i>
<a href="#contentlibrary" title="ContentLibrary">ContentLibrary</a>: <i>String</i>
<a href="#cpucount" title="CpuCount">CpuCount</a>: <i>String</i>
<a href="#creationtype" title="CreationType">CreationType</a>: <i>String</i>
<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - String</i>
<a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
<a href="#datastore" title="Datastore">Datastore</a>: <i>String</i>
<a href="#datastorecluster" title="DatastoreCluster">DatastoreCluster</a>: <i>String</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>String</i>
<a href="#folder" title="Folder">Folder</a>: <i>String</i>
<a href="#hostsystem" title="Hostsystem">Hostsystem</a>: <i>String</i>
<a href="#memorysize" title="MemorySize">MemorySize</a>: <i>String</i>
<a href="#network" title="Network">Network</a>: <i>
      - String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#pool" title="Pool">Pool</a>: <i>String</i>
<a href="#sshpassword" title="SshPassword">SshPassword</a>: <i>String</i>
<a href="#sshport" title="SshPort">SshPort</a>: <i>String</i>
<a href="#sshuser" title="SshUser">SshUser</a>: <i>String</i>
<a href="#sshusergroup" title="SshUserGroup">SshUserGroup</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#vappipallocationpolicy" title="VappIpAllocationPolicy">VappIpAllocationPolicy</a>: <i>String</i>
<a href="#vappipprotocol" title="VappIpProtocol">VappIpProtocol</a>: <i>String</i>
<a href="#vappproperty" title="VappProperty">VappProperty</a>: <i>
      - String</i>
<a href="#vapptransport" title="VappTransport">VappTransport</a>: <i>String</i>
<a href="#vcenter" title="Vcenter">Vcenter</a>: <i>String</i>
<a href="#vcenterport" title="VcenterPort">VcenterPort</a>: <i>String</i>
</pre>

## Properties

#### Boot2dockerUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cfgparam

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloneFrom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cloudinit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentLibrary

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datastore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatastoreCluster

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostsystem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemorySize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPassword

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

#### SshUserGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappIpAllocationPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappIpProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappProperty

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappTransport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcenter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

