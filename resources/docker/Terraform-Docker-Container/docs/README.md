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
        "<a href="#logopts" title="LogOpts">LogOpts</a>" : <i>[ &lt;a href=&#34;logopts.md&#34;&gt;LogOpts&lt;/a&gt;, ... ]</i>,
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
        "<a href="#sysctls" title="Sysctls">Sysctls</a>" : <i>[ &lt;a href=&#34;sysctls.md&#34;&gt;Sysctls&lt;/a&gt;, ... ]</i>,
        "<a href="#tmpfs" title="Tmpfs">Tmpfs</a>" : <i>[ &lt;a href=&#34;tmpfs.md&#34;&gt;Tmpfs&lt;/a&gt;, ... ]</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#usernsmode" title="UsernsMode">UsernsMode</a>" : <i>String</i>,
        "<a href="#workingdir" title="WorkingDir">WorkingDir</a>" : <i>String</i>,
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ &lt;a href=&#34;capabilities.md&#34;&gt;Capabilities&lt;/a&gt;, ... ]</i>,
        "<a href="#devices" title="Devices">Devices</a>" : <i>[ &lt;a href=&#34;devices.md&#34;&gt;Devices&lt;/a&gt;, ... ]</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ &lt;a href=&#34;healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;, ... ]</i>,
        "<a href="#host" title="Host">Host</a>" : <i>[ &lt;a href=&#34;host.md&#34;&gt;Host&lt;/a&gt;, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#mounts" title="Mounts">Mounts</a>" : <i>[ &lt;a href=&#34;mounts.md&#34;&gt;Mounts&lt;/a&gt;, ... ]</i>,
        "<a href="#networksadvanced" title="NetworksAdvanced">NetworksAdvanced</a>" : <i>[ &lt;a href=&#34;networksadvanced.md&#34;&gt;NetworksAdvanced&lt;/a&gt;, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;, ... ]</i>,
        "<a href="#ulimit" title="Ulimit">Ulimit</a>" : <i>[ &lt;a href=&#34;ulimit.md&#34;&gt;Ulimit&lt;/a&gt;, ... ]</i>,
        "<a href="#upload" title="Upload">Upload</a>" : <i>[ &lt;a href=&#34;upload.md&#34;&gt;Upload&lt;/a&gt;, ... ]</i>,
        "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ &lt;a href=&#34;volumes.md&#34;&gt;Volumes&lt;/a&gt;, ... ]</i>,
        "<a href="#bindoptions" title="BindOptions">BindOptions</a>" : <i>[ &lt;a href=&#34;bindoptions.md&#34;&gt;BindOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>" : <i>[ &lt;a href=&#34;tmpfsoptions.md&#34;&gt;TmpfsOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>" : <i>[ &lt;a href=&#34;volumeoptions.md&#34;&gt;VolumeOptions&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;logopts.md&#34;&gt;LogOpts&lt;/a&gt;</i>
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
      - &lt;a href=&#34;sysctls.md&#34;&gt;Sysctls&lt;/a&gt;</i>
    <a href="#tmpfs" title="Tmpfs">Tmpfs</a>: <i>
      - &lt;a href=&#34;tmpfs.md&#34;&gt;Tmpfs&lt;/a&gt;</i>
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#usernsmode" title="UsernsMode">UsernsMode</a>: <i>String</i>
    <a href="#workingdir" title="WorkingDir">WorkingDir</a>: <i>String</i>
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - &lt;a href=&#34;capabilities.md&#34;&gt;Capabilities&lt;/a&gt;</i>
    <a href="#devices" title="Devices">Devices</a>: <i>
      - &lt;a href=&#34;devices.md&#34;&gt;Devices&lt;/a&gt;</i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - &lt;a href=&#34;healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;</i>
    <a href="#host" title="Host">Host</a>: <i>
      - &lt;a href=&#34;host.md&#34;&gt;Host&lt;/a&gt;</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#mounts" title="Mounts">Mounts</a>: <i>
      - &lt;a href=&#34;mounts.md&#34;&gt;Mounts&lt;/a&gt;</i>
    <a href="#networksadvanced" title="NetworksAdvanced">NetworksAdvanced</a>: <i>
      - &lt;a href=&#34;networksadvanced.md&#34;&gt;NetworksAdvanced&lt;/a&gt;</i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;</i>
    <a href="#ulimit" title="Ulimit">Ulimit</a>: <i>
      - &lt;a href=&#34;ulimit.md&#34;&gt;Ulimit&lt;/a&gt;</i>
    <a href="#upload" title="Upload">Upload</a>: <i>
      - &lt;a href=&#34;upload.md&#34;&gt;Upload&lt;/a&gt;</i>
    <a href="#volumes" title="Volumes">Volumes</a>: <i>
      - &lt;a href=&#34;volumes.md&#34;&gt;Volumes&lt;/a&gt;</i>
    <a href="#bindoptions" title="BindOptions">BindOptions</a>: <i>
      - &lt;a href=&#34;bindoptions.md&#34;&gt;BindOptions&lt;/a&gt;</i>
    <a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>: <i>
      - &lt;a href=&#34;tmpfsoptions.md&#34;&gt;TmpfsOptions&lt;/a&gt;</i>
    <a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>: <i>
      - &lt;a href=&#34;volumeoptions.md&#34;&gt;VolumeOptions&lt;/a&gt;</i>
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

_Type_: List of &lt;a href=&#34;logopts.md&#34;&gt;LogOpts&lt;/a&gt;

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

_Type_: List of &lt;a href=&#34;sysctls.md&#34;&gt;Sysctls&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tmpfs

_Required_: No

_Type_: List of &lt;a href=&#34;tmpfs.md&#34;&gt;Tmpfs&lt;/a&gt;

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

_Type_: List of &lt;a href=&#34;capabilities.md&#34;&gt;Capabilities&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: No

_Type_: List of &lt;a href=&#34;devices.md&#34;&gt;Devices&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of &lt;a href=&#34;healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: List of &lt;a href=&#34;host.md&#34;&gt;Host&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mounts

_Required_: No

_Type_: List of &lt;a href=&#34;mounts.md&#34;&gt;Mounts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworksAdvanced

_Required_: No

_Type_: List of &lt;a href=&#34;networksadvanced.md&#34;&gt;NetworksAdvanced&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ulimit

_Required_: No

_Type_: List of &lt;a href=&#34;ulimit.md&#34;&gt;Ulimit&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upload

_Required_: No

_Type_: List of &lt;a href=&#34;upload.md&#34;&gt;Upload&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of &lt;a href=&#34;volumes.md&#34;&gt;Volumes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindOptions

_Required_: No

_Type_: List of &lt;a href=&#34;bindoptions.md&#34;&gt;BindOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TmpfsOptions

_Required_: No

_Type_: List of &lt;a href=&#34;tmpfsoptions.md&#34;&gt;TmpfsOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeOptions

_Required_: No

_Type_: List of &lt;a href=&#34;volumeoptions.md&#34;&gt;VolumeOptions&lt;/a&gt;

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

Returns the &lt;code&gt;Bridge&lt;/code&gt; value.

#### ContainerLogs

Returns the &lt;code&gt;ContainerLogs&lt;/code&gt; value.

#### ExitCode

Returns the &lt;code&gt;ExitCode&lt;/code&gt; value.

#### Gateway

Returns the &lt;code&gt;Gateway&lt;/code&gt; value.

#### IpAddress

Returns the &lt;code&gt;IpAddress&lt;/code&gt; value.

#### IpPrefixLength

Returns the &lt;code&gt;IpPrefixLength&lt;/code&gt; value.

#### NetworkData

Returns the &lt;code&gt;NetworkData&lt;/code&gt; value.

