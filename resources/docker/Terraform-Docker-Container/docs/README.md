# Terraform::Docker::Container

Manages the lifecycle of a Docker container.

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

If true attach to the container after its creation and waits the end of his execution.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

The command to use to start the
container. For example, to run `/usr/bin/myprogram -f baz.conf` set the
command to be `["/usr/bin/myprogram", "-f", "baz.conf"]`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuSet

A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. `0-1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShares

CPU shares (relative weight) for the container.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestroyGraceSeconds

If defined will attempt to stop the container before destroying. Container will be destroyed after `n` seconds or on successful stop.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

Set of DNS servers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsOpts

Set of DNS options used by the DNS provider(s), see `resolv.conf` documentation for valid list of options.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSearch

Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domainname

Domain name of the container.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entrypoint

The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run `/usr/bin/myprogram`
when starting a container, set the entrypoint to be
`["/usr/bin/myprogram"]`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

Environment variables to set.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupAdd

Add additional groups to run as.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

Hostname of the container.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

The ID of the image to back this container.
The easiest way to get this value is to use the `docker_image` resource
as is shown in the example above.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpcMode

IPC sharing mode for the container. Possible values are: `none`, `private`, `shareable`, `container:<name|id>` or `host`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Links

Set of links for link based
connectivity between containers that are running on the same host.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDriver

The logging driver to use for the container.
Defaults to "json-file".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogOpts

Key/value pairs to use as options for
the logging driver.

_Required_: No

_Type_: List of <a href="logopts.md">LogOpts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logs

Save the container logs (`attach` must be enabled).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetryCount

The maximum amount of times to an attempt
a restart when `restart` is set to "on-failure".

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

The memory limit for the container in MBs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemorySwap

The total memory limit (memory + swap) for the
container in MBs. This setting may compute to `-1` after `terraform apply` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustRun

If true, then the Docker container will be
kept running. If false, then as long as the container exists, Terraform
assumes it is successful.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Docker container.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkAlias

Network aliases of the container for user-defined networks only. *Deprecated:* use `networks_advanced` instead.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkMode

Network mode of the container.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

Id of the networks in which the
container is. *Deprecated:* use `networks_advanced` instead.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidMode

The PID (Process) Namespace mode for the container. Either `container:<name|id>` or `host`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileged

Run container in privileged mode.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishAllPorts

Publish all ports of the container.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

If true, the container will be started as readonly.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restart

The restart policy for the container. Must be
one of "no", "on-failure", "always", "unless-stopped".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rm

If true, then the container will be automatically removed after his execution. Terraform
won't check this container after creation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShmSize

Size of `/dev/shm` in MBs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

If true, then the Docker container will be
started after creation. If false, then the container is only created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sysctls

A map of kernel parameters (sysctls) to set in the container.

_Required_: No

_Type_: List of <a href="sysctls.md">Sysctls</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tmpfs

A map of container directories which should be replaced by `tmpfs mounts`, and their corresponding mount options.

_Required_: No

_Type_: List of <a href="tmpfs.md">Tmpfs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

User used for run the first process. Format is
`user` or `user:group` which user and group can be passed literraly or
by name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernsMode

Sets the usernamespace mode for the container when usernamespace remapping option is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDir

The working directory for commands to run in.

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

