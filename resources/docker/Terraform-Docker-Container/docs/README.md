# Terraform::Docker::Container

CloudFormation equivalent of docker_container

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Docker::Container",
    "Properties" : {
        "<a href="#attach" title="Attach">Attach</a>" : <i>Boolean</i>,
        "<a href="#command" title="Command">Command</a>" : <i>[ String, ... ]</i>,
        "<a href="#cpuset" title="CpuSet">CpuSet</a>" : <i>String</i>,
        "<a href="#cpushares" title="CpuShares">CpuShares</a>" : <i>Double</i>,
        "<a href="#destroygraceseconds" title="DestroyGraceSeconds">DestroyGraceSeconds</a>" : <i>Double</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ String, ... ]</i>,
        "<a href="#dnsopts" title="DnsOpts">DnsOpts</a>" : <i>[ String, ... ]</i>,
        "<a href="#dnssearch" title="DnsSearch">DnsSearch</a>" : <i>[ String, ... ]</i>,
        "<a href="#domainname" title="Domainname">Domainname</a>" : <i>String</i>,
        "<a href="#entrypoint" title="Entrypoint">Entrypoint</a>" : <i>[ String, ... ]</i>,
        "<a href="#env" title="Env">Env</a>" : <i>[ String, ... ]</i>,
        "<a href="#groupadd" title="GroupAdd">GroupAdd</a>" : <i>[ String, ... ]</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#ipcmode" title="IpcMode">IpcMode</a>" : <i>String</i>,
        "<a href="#links" title="Links">Links</a>" : <i>[ String, ... ]</i>,
        "<a href="#logdriver" title="LogDriver">LogDriver</a>" : <i>String</i>,
        "<a href="#logopts" title="LogOpts">LogOpts</a>" : <i>[ <a href="logopts.md">LogOpts</a>, ... ]</i>,
        "<a href="#logs" title="Logs">Logs</a>" : <i>Boolean</i>,
        "<a href="#maxretrycount" title="MaxRetryCount">MaxRetryCount</a>" : <i>Double</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#memoryswap" title="MemorySwap">MemorySwap</a>" : <i>Double</i>,
        "<a href="#mustrun" title="MustRun">MustRun</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkalias" title="NetworkAlias">NetworkAlias</a>" : <i>[ String, ... ]</i>,
        "<a href="#networkmode" title="NetworkMode">NetworkMode</a>" : <i>String</i>,
        "<a href="#networks" title="Networks">Networks</a>" : <i>[ String, ... ]</i>,
        "<a href="#pidmode" title="PidMode">PidMode</a>" : <i>String</i>,
        "<a href="#privileged" title="Privileged">Privileged</a>" : <i>Boolean</i>,
        "<a href="#publishallports" title="PublishAllPorts">PublishAllPorts</a>" : <i>Boolean</i>,
        "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
        "<a href="#restart" title="Restart">Restart</a>" : <i>String</i>,
        "<a href="#rm" title="Rm">Rm</a>" : <i>Boolean</i>,
        "<a href="#shmsize" title="ShmSize">ShmSize</a>" : <i>Double</i>,
        "<a href="#start" title="Start">Start</a>" : <i>Boolean</i>,
        "<a href="#sysctls" title="Sysctls">Sysctls</a>" : <i>[ <a href="sysctls.md">Sysctls</a>, ... ]</i>,
        "<a href="#tmpfs" title="Tmpfs">Tmpfs</a>" : <i>[ <a href="tmpfs.md">Tmpfs</a>, ... ]</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#usernsmode" title="UsernsMode">UsernsMode</a>" : <i>String</i>,
        "<a href="#workingdir" title="WorkingDir">WorkingDir</a>" : <i>String</i>,
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ <a href="capabilities.md">Capabilities</a>, ... ]</i>,
        "<a href="#devices" title="Devices">Devices</a>" : <i>[ <a href="devices.md">Devices</a>, ... ]</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ <a href="healthcheck.md">Healthcheck</a>, ... ]</i>,
        "<a href="#host" title="Host">Host</a>" : <i>[ <a href="host.md">Host</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#mounts" title="Mounts">Mounts</a>" : <i>[ <a href="mounts.md">Mounts</a>, ... ]</i>,
        "<a href="#networksadvanced" title="NetworksAdvanced">NetworksAdvanced</a>" : <i>[ <a href="networksadvanced.md">NetworksAdvanced</a>, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="ports.md">Ports</a>, ... ]</i>,
        "<a href="#ulimit" title="Ulimit">Ulimit</a>" : <i>[ <a href="ulimit.md">Ulimit</a>, ... ]</i>,
        "<a href="#upload" title="Upload">Upload</a>" : <i>[ <a href="upload.md">Upload</a>, ... ]</i>,
        "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ <a href="volumes.md">Volumes</a>, ... ]</i>,
        "<a href="#bindoptions" title="BindOptions">BindOptions</a>" : <i>[ <a href="bindoptions.md">BindOptions</a>, ... ]</i>,
        "<a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>" : <i>[ <a href="tmpfsoptions.md">TmpfsOptions</a>, ... ]</i>,
        "<a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>" : <i>[ <a href="volumeoptions.md">VolumeOptions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Docker::Container
Properties:
    <a href="#attach" title="Attach">Attach</a>: <i>Boolean</i>
    <a href="#command" title="Command">Command</a>: <i>
      - String</i>
    <a href="#cpuset" title="CpuSet">CpuSet</a>: <i>String</i>
    <a href="#cpushares" title="CpuShares">CpuShares</a>: <i>Double</i>
    <a href="#destroygraceseconds" title="DestroyGraceSeconds">DestroyGraceSeconds</a>: <i>Double</i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - String</i>
    <a href="#dnsopts" title="DnsOpts">DnsOpts</a>: <i>
      - String</i>
    <a href="#dnssearch" title="DnsSearch">DnsSearch</a>: <i>
      - String</i>
    <a href="#domainname" title="Domainname">Domainname</a>: <i>String</i>
    <a href="#entrypoint" title="Entrypoint">Entrypoint</a>: <i>
      - String</i>
    <a href="#env" title="Env">Env</a>: <i>
      - String</i>
    <a href="#groupadd" title="GroupAdd">GroupAdd</a>: <i>
      - String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#ipcmode" title="IpcMode">IpcMode</a>: <i>String</i>
    <a href="#links" title="Links">Links</a>: <i>
      - String</i>
    <a href="#logdriver" title="LogDriver">LogDriver</a>: <i>String</i>
    <a href="#logopts" title="LogOpts">LogOpts</a>: <i>
      - <a href="logopts.md">LogOpts</a></i>
    <a href="#logs" title="Logs">Logs</a>: <i>Boolean</i>
    <a href="#maxretrycount" title="MaxRetryCount">MaxRetryCount</a>: <i>Double</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#memoryswap" title="MemorySwap">MemorySwap</a>: <i>Double</i>
    <a href="#mustrun" title="MustRun">MustRun</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkalias" title="NetworkAlias">NetworkAlias</a>: <i>
      - String</i>
    <a href="#networkmode" title="NetworkMode">NetworkMode</a>: <i>String</i>
    <a href="#networks" title="Networks">Networks</a>: <i>
      - String</i>
    <a href="#pidmode" title="PidMode">PidMode</a>: <i>String</i>
    <a href="#privileged" title="Privileged">Privileged</a>: <i>Boolean</i>
    <a href="#publishallports" title="PublishAllPorts">PublishAllPorts</a>: <i>Boolean</i>
    <a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
    <a href="#restart" title="Restart">Restart</a>: <i>String</i>
    <a href="#rm" title="Rm">Rm</a>: <i>Boolean</i>
    <a href="#shmsize" title="ShmSize">ShmSize</a>: <i>Double</i>
    <a href="#start" title="Start">Start</a>: <i>Boolean</i>
    <a href="#sysctls" title="Sysctls">Sysctls</a>: <i>
      - <a href="sysctls.md">Sysctls</a></i>
    <a href="#tmpfs" title="Tmpfs">Tmpfs</a>: <i>
      - <a href="tmpfs.md">Tmpfs</a></i>
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#usernsmode" title="UsernsMode">UsernsMode</a>: <i>String</i>
    <a href="#workingdir" title="WorkingDir">WorkingDir</a>: <i>String</i>
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - <a href="capabilities.md">Capabilities</a></i>
    <a href="#devices" title="Devices">Devices</a>: <i>
      - <a href="devices.md">Devices</a></i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - <a href="healthcheck.md">Healthcheck</a></i>
    <a href="#host" title="Host">Host</a>: <i>
      - <a href="host.md">Host</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#mounts" title="Mounts">Mounts</a>: <i>
      - <a href="mounts.md">Mounts</a></i>
    <a href="#networksadvanced" title="NetworksAdvanced">NetworksAdvanced</a>: <i>
      - <a href="networksadvanced.md">NetworksAdvanced</a></i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="ports.md">Ports</a></i>
    <a href="#ulimit" title="Ulimit">Ulimit</a>: <i>
      - <a href="ulimit.md">Ulimit</a></i>
    <a href="#upload" title="Upload">Upload</a>: <i>
      - <a href="upload.md">Upload</a></i>
    <a href="#volumes" title="Volumes">Volumes</a>: <i>
      - <a href="volumes.md">Volumes</a></i>
    <a href="#bindoptions" title="BindOptions">BindOptions</a>: <i>
      - <a href="bindoptions.md">BindOptions</a></i>
    <a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>: <i>
      - <a href="tmpfsoptions.md">TmpfsOptions</a></i>
    <a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>: <i>
      - <a href="volumeoptions.md">VolumeOptions</a></i>
</pre>

## Properties

#### Attach

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuSet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShares

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestroyGraceSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsOpts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSearch

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domainname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entrypoint

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupAdd

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpcMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Links

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDriver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogOpts

_Required_: No

_Type_: List of <a href="logopts.md">LogOpts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetryCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemorySwap

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustRun

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkAlias

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileged

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishAllPorts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restart

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rm

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShmSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sysctls

_Required_: No

_Type_: List of <a href="sysctls.md">Sysctls</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tmpfs

_Required_: No

_Type_: List of <a href="tmpfs.md">Tmpfs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernsMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capabilities

_Required_: No

_Type_: List of <a href="capabilities.md">Capabilities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: No

_Type_: List of <a href="devices.md">Devices</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of <a href="healthcheck.md">Healthcheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: List of <a href="host.md">Host</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mounts

_Required_: No

_Type_: List of <a href="mounts.md">Mounts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworksAdvanced

_Required_: No

_Type_: List of <a href="networksadvanced.md">NetworksAdvanced</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="ports.md">Ports</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ulimit

_Required_: No

_Type_: List of <a href="ulimit.md">Ulimit</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upload

_Required_: No

_Type_: List of <a href="upload.md">Upload</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of <a href="volumes.md">Volumes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindOptions

_Required_: No

_Type_: List of <a href="bindoptions.md">BindOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TmpfsOptions

_Required_: No

_Type_: List of <a href="tmpfsoptions.md">TmpfsOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeOptions

_Required_: No

_Type_: List of <a href="volumeoptions.md">VolumeOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Bridge

Returns the <code>Bridge</code> value.

#### ContainerLogs

Returns the <code>ContainerLogs</code> value.

#### ExitCode

Returns the <code>ExitCode</code> value.

#### Gateway

Returns the <code>Gateway</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### IpPrefixLength

Returns the <code>IpPrefixLength</code> value.

#### NetworkData

Returns the <code>NetworkData</code> value.

