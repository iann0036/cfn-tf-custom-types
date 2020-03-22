# Terraform::Docker::Service

This resource manages the lifecycle of a Docker service. By default, the creation, update and delete of services are detached.

With the [Converge Config](#convergeconfig) the behavior of the `docker cli` is imitated to guarantee that
for example, all tasks of a service are running or successfully updated or to inform `terraform` that a service could not
be updated and was successfully rolled back.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Docker::Service",
    "Properties" : {
        "<a href="#auth" title="Auth">Auth</a>" : <i>[ <a href="auth.md">Auth</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#convergeconfig" title="ConvergeConfig">ConvergeConfig</a>" : <i>[ <a href="convergeconfig.md">ConvergeConfig</a>, ... ]</i>,
        "<a href="#endpointspec" title="EndpointSpec">EndpointSpec</a>" : <i>[ <a href="endpointspec.md">EndpointSpec</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>[ <a href="mode.md">Mode</a>, ... ]</i>,
        "<a href="#rollbackconfig" title="RollbackConfig">RollbackConfig</a>" : <i>[ <a href="rollbackconfig.md">RollbackConfig</a>, ... ]</i>,
        "<a href="#taskspec" title="TaskSpec">TaskSpec</a>" : <i>[ <a href="taskspec.md">TaskSpec</a>, ... ]</i>,
        "<a href="#updateconfig" title="UpdateConfig">UpdateConfig</a>" : <i>[ <a href="updateconfig.md">UpdateConfig</a>, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="ports.md">Ports</a>, ... ]</i>,
        "<a href="#replicated" title="Replicated">Replicated</a>" : <i>[ <a href="replicated.md">Replicated</a>, ... ]</i>,
        "<a href="#containerspec" title="ContainerSpec">ContainerSpec</a>" : <i>[ <a href="containerspec.md">ContainerSpec</a>, ... ]</i>,
        "<a href="#logdriver" title="LogDriver">LogDriver</a>" : <i>[ <a href="logdriver.md">LogDriver</a>, ... ]</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ <a href="placement.md">Placement</a>, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resources.md">Resources</a>, ... ]</i>,
        "<a href="#configs" title="Configs">Configs</a>" : <i>[ <a href="configs.md">Configs</a>, ... ]</i>,
        "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ <a href="dnsconfig.md">DnsConfig</a>, ... ]</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ <a href="healthcheck.md">Healthcheck</a>, ... ]</i>,
        "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ <a href="hosts.md">Hosts</a>, ... ]</i>,
        "<a href="#mounts" title="Mounts">Mounts</a>" : <i>[ <a href="mounts.md">Mounts</a>, ... ]</i>,
        "<a href="#privileges" title="Privileges">Privileges</a>" : <i>[ <a href="privileges.md">Privileges</a>, ... ]</i>,
        "<a href="#secrets" title="Secrets">Secrets</a>" : <i>[ <a href="secrets.md">Secrets</a>, ... ]</i>,
        "<a href="#platforms" title="Platforms">Platforms</a>" : <i>[ <a href="platforms.md">Platforms</a>, ... ]</i>,
        "<a href="#limits" title="Limits">Limits</a>" : <i>[ <a href="limits.md">Limits</a>, ... ]</i>,
        "<a href="#reservation" title="Reservation">Reservation</a>" : <i>[ <a href="reservation.md">Reservation</a>, ... ]</i>,
        "<a href="#bindoptions" title="BindOptions">BindOptions</a>" : <i>[ <a href="bindoptions.md">BindOptions</a>, ... ]</i>,
        "<a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>" : <i>[ <a href="tmpfsoptions.md">TmpfsOptions</a>, ... ]</i>,
        "<a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>" : <i>[ <a href="volumeoptions.md">VolumeOptions</a>, ... ]</i>,
        "<a href="#credentialspec" title="CredentialSpec">CredentialSpec</a>" : <i>[ <a href="credentialspec.md">CredentialSpec</a>, ... ]</i>,
        "<a href="#selinuxcontext" title="SeLinuxContext">SeLinuxContext</a>" : <i>[ <a href="selinuxcontext.md">SeLinuxContext</a>, ... ]</i>,
        "<a href="#genericresources" title="GenericResources">GenericResources</a>" : <i>[ <a href="genericresources.md">GenericResources</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Docker::Service
Properties:
    <a href="#auth" title="Auth">Auth</a>: <i>
      - <a href="auth.md">Auth</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#convergeconfig" title="ConvergeConfig">ConvergeConfig</a>: <i>
      - <a href="convergeconfig.md">ConvergeConfig</a></i>
    <a href="#endpointspec" title="EndpointSpec">EndpointSpec</a>: <i>
      - <a href="endpointspec.md">EndpointSpec</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#mode" title="Mode">Mode</a>: <i>
      - <a href="mode.md">Mode</a></i>
    <a href="#rollbackconfig" title="RollbackConfig">RollbackConfig</a>: <i>
      - <a href="rollbackconfig.md">RollbackConfig</a></i>
    <a href="#taskspec" title="TaskSpec">TaskSpec</a>: <i>
      - <a href="taskspec.md">TaskSpec</a></i>
    <a href="#updateconfig" title="UpdateConfig">UpdateConfig</a>: <i>
      - <a href="updateconfig.md">UpdateConfig</a></i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="ports.md">Ports</a></i>
    <a href="#replicated" title="Replicated">Replicated</a>: <i>
      - <a href="replicated.md">Replicated</a></i>
    <a href="#containerspec" title="ContainerSpec">ContainerSpec</a>: <i>
      - <a href="containerspec.md">ContainerSpec</a></i>
    <a href="#logdriver" title="LogDriver">LogDriver</a>: <i>
      - <a href="logdriver.md">LogDriver</a></i>
    <a href="#placement" title="Placement">Placement</a>: <i>
      - <a href="placement.md">Placement</a></i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resources.md">Resources</a></i>
    <a href="#configs" title="Configs">Configs</a>: <i>
      - <a href="configs.md">Configs</a></i>
    <a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - <a href="dnsconfig.md">DnsConfig</a></i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - <a href="healthcheck.md">Healthcheck</a></i>
    <a href="#hosts" title="Hosts">Hosts</a>: <i>
      - <a href="hosts.md">Hosts</a></i>
    <a href="#mounts" title="Mounts">Mounts</a>: <i>
      - <a href="mounts.md">Mounts</a></i>
    <a href="#privileges" title="Privileges">Privileges</a>: <i>
      - <a href="privileges.md">Privileges</a></i>
    <a href="#secrets" title="Secrets">Secrets</a>: <i>
      - <a href="secrets.md">Secrets</a></i>
    <a href="#platforms" title="Platforms">Platforms</a>: <i>
      - <a href="platforms.md">Platforms</a></i>
    <a href="#limits" title="Limits">Limits</a>: <i>
      - <a href="limits.md">Limits</a></i>
    <a href="#reservation" title="Reservation">Reservation</a>: <i>
      - <a href="reservation.md">Reservation</a></i>
    <a href="#bindoptions" title="BindOptions">BindOptions</a>: <i>
      - <a href="bindoptions.md">BindOptions</a></i>
    <a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>: <i>
      - <a href="tmpfsoptions.md">TmpfsOptions</a></i>
    <a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>: <i>
      - <a href="volumeoptions.md">VolumeOptions</a></i>
    <a href="#credentialspec" title="CredentialSpec">CredentialSpec</a>: <i>
      - <a href="credentialspec.md">CredentialSpec</a></i>
    <a href="#selinuxcontext" title="SeLinuxContext">SeLinuxContext</a>: <i>
      - <a href="selinuxcontext.md">SeLinuxContext</a></i>
    <a href="#genericresources" title="GenericResources">GenericResources</a>: <i>
      - <a href="genericresources.md">GenericResources</a></i>
</pre>

## Properties

#### Auth

See [Auth](#auth-1) below for details.

_Required_: No

_Type_: List of <a href="auth.md">Auth</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Docker service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConvergeConfig

_Required_: No

_Type_: List of <a href="convergeconfig.md">ConvergeConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointSpec

_Required_: No

_Type_: List of <a href="endpointspec.md">EndpointSpec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: List of <a href="mode.md">Mode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollbackConfig

_Required_: No

_Type_: List of <a href="rollbackconfig.md">RollbackConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskSpec

_Required_: No

_Type_: List of <a href="taskspec.md">TaskSpec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateConfig

_Required_: No

_Type_: List of <a href="updateconfig.md">UpdateConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="ports.md">Ports</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replicated

_Required_: No

_Type_: List of <a href="replicated.md">Replicated</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerSpec

_Required_: No

_Type_: List of <a href="containerspec.md">ContainerSpec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDriver

_Required_: No

_Type_: List of <a href="logdriver.md">LogDriver</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of <a href="placement.md">Placement</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resources.md">Resources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configs

_Required_: No

_Type_: List of <a href="configs.md">Configs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No

_Type_: List of <a href="dnsconfig.md">DnsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of <a href="healthcheck.md">Healthcheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts

_Required_: No

_Type_: List of <a href="hosts.md">Hosts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mounts

_Required_: No

_Type_: List of <a href="mounts.md">Mounts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileges

_Required_: No

_Type_: List of <a href="privileges.md">Privileges</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secrets

_Required_: No

_Type_: List of <a href="secrets.md">Secrets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platforms

_Required_: No

_Type_: List of <a href="platforms.md">Platforms</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limits

_Required_: No

_Type_: List of <a href="limits.md">Limits</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reservation

_Required_: No

_Type_: List of <a href="reservation.md">Reservation</a>

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

#### CredentialSpec

_Required_: No

_Type_: List of <a href="credentialspec.md">CredentialSpec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinuxContext

_Required_: No

_Type_: List of <a href="selinuxcontext.md">SeLinuxContext</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenericResources

_Required_: No

_Type_: List of <a href="genericresources.md">GenericResources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

