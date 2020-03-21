# Terraform::Docker::Service

CloudFormation equivalent of docker_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Docker::Service",
    "Properties" : {
        "<a href="#auth" title="Auth">Auth</a>" : <i>[ &lt;a href=&#34;auth.md&#34;&gt;Auth&lt;/a&gt;, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#convergeconfig" title="ConvergeConfig">ConvergeConfig</a>" : <i>[ &lt;a href=&#34;convergeconfig.md&#34;&gt;ConvergeConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#endpointspec" title="EndpointSpec">EndpointSpec</a>" : <i>[ &lt;a href=&#34;endpointspec.md&#34;&gt;EndpointSpec&lt;/a&gt;, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>[ &lt;a href=&#34;mode.md&#34;&gt;Mode&lt;/a&gt;, ... ]</i>,
        "<a href="#rollbackconfig" title="RollbackConfig">RollbackConfig</a>" : <i>[ &lt;a href=&#34;rollbackconfig.md&#34;&gt;RollbackConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#taskspec" title="TaskSpec">TaskSpec</a>" : <i>[ &lt;a href=&#34;taskspec.md&#34;&gt;TaskSpec&lt;/a&gt;, ... ]</i>,
        "<a href="#updateconfig" title="UpdateConfig">UpdateConfig</a>" : <i>[ &lt;a href=&#34;updateconfig.md&#34;&gt;UpdateConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;, ... ]</i>,
        "<a href="#replicated" title="Replicated">Replicated</a>" : <i>[ &lt;a href=&#34;replicated.md&#34;&gt;Replicated&lt;/a&gt;, ... ]</i>,
        "<a href="#containerspec" title="ContainerSpec">ContainerSpec</a>" : <i>[ &lt;a href=&#34;containerspec.md&#34;&gt;ContainerSpec&lt;/a&gt;, ... ]</i>,
        "<a href="#logdriver" title="LogDriver">LogDriver</a>" : <i>[ &lt;a href=&#34;logdriver.md&#34;&gt;LogDriver&lt;/a&gt;, ... ]</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ &lt;a href=&#34;placement.md&#34;&gt;Placement&lt;/a&gt;, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;, ... ]</i>,
        "<a href="#configs" title="Configs">Configs</a>" : <i>[ &lt;a href=&#34;configs.md&#34;&gt;Configs&lt;/a&gt;, ... ]</i>,
        "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ &lt;a href=&#34;dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ &lt;a href=&#34;healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;, ... ]</i>,
        "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ &lt;a href=&#34;hosts.md&#34;&gt;Hosts&lt;/a&gt;, ... ]</i>,
        "<a href="#mounts" title="Mounts">Mounts</a>" : <i>[ &lt;a href=&#34;mounts.md&#34;&gt;Mounts&lt;/a&gt;, ... ]</i>,
        "<a href="#privileges" title="Privileges">Privileges</a>" : <i>[ &lt;a href=&#34;privileges.md&#34;&gt;Privileges&lt;/a&gt;, ... ]</i>,
        "<a href="#secrets" title="Secrets">Secrets</a>" : <i>[ &lt;a href=&#34;secrets.md&#34;&gt;Secrets&lt;/a&gt;, ... ]</i>,
        "<a href="#platforms" title="Platforms">Platforms</a>" : <i>[ &lt;a href=&#34;platforms.md&#34;&gt;Platforms&lt;/a&gt;, ... ]</i>,
        "<a href="#limits" title="Limits">Limits</a>" : <i>[ &lt;a href=&#34;limits.md&#34;&gt;Limits&lt;/a&gt;, ... ]</i>,
        "<a href="#reservation" title="Reservation">Reservation</a>" : <i>[ &lt;a href=&#34;reservation.md&#34;&gt;Reservation&lt;/a&gt;, ... ]</i>,
        "<a href="#bindoptions" title="BindOptions">BindOptions</a>" : <i>[ &lt;a href=&#34;bindoptions.md&#34;&gt;BindOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>" : <i>[ &lt;a href=&#34;tmpfsoptions.md&#34;&gt;TmpfsOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>" : <i>[ &lt;a href=&#34;volumeoptions.md&#34;&gt;VolumeOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#credentialspec" title="CredentialSpec">CredentialSpec</a>" : <i>[ &lt;a href=&#34;credentialspec.md&#34;&gt;CredentialSpec&lt;/a&gt;, ... ]</i>,
        "<a href="#selinuxcontext" title="SeLinuxContext">SeLinuxContext</a>" : <i>[ &lt;a href=&#34;selinuxcontext.md&#34;&gt;SeLinuxContext&lt;/a&gt;, ... ]</i>,
        "<a href="#genericresources" title="GenericResources">GenericResources</a>" : <i>[ &lt;a href=&#34;genericresources.md&#34;&gt;GenericResources&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Docker::Service
Properties:
    <a href="#auth" title="Auth">Auth</a>: <i>
      - &lt;a href=&#34;auth.md&#34;&gt;Auth&lt;/a&gt;</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#convergeconfig" title="ConvergeConfig">ConvergeConfig</a>: <i>
      - &lt;a href=&#34;convergeconfig.md&#34;&gt;ConvergeConfig&lt;/a&gt;</i>
    <a href="#endpointspec" title="EndpointSpec">EndpointSpec</a>: <i>
      - &lt;a href=&#34;endpointspec.md&#34;&gt;EndpointSpec&lt;/a&gt;</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#mode" title="Mode">Mode</a>: <i>
      - &lt;a href=&#34;mode.md&#34;&gt;Mode&lt;/a&gt;</i>
    <a href="#rollbackconfig" title="RollbackConfig">RollbackConfig</a>: <i>
      - &lt;a href=&#34;rollbackconfig.md&#34;&gt;RollbackConfig&lt;/a&gt;</i>
    <a href="#taskspec" title="TaskSpec">TaskSpec</a>: <i>
      - &lt;a href=&#34;taskspec.md&#34;&gt;TaskSpec&lt;/a&gt;</i>
    <a href="#updateconfig" title="UpdateConfig">UpdateConfig</a>: <i>
      - &lt;a href=&#34;updateconfig.md&#34;&gt;UpdateConfig&lt;/a&gt;</i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;</i>
    <a href="#replicated" title="Replicated">Replicated</a>: <i>
      - &lt;a href=&#34;replicated.md&#34;&gt;Replicated&lt;/a&gt;</i>
    <a href="#containerspec" title="ContainerSpec">ContainerSpec</a>: <i>
      - &lt;a href=&#34;containerspec.md&#34;&gt;ContainerSpec&lt;/a&gt;</i>
    <a href="#logdriver" title="LogDriver">LogDriver</a>: <i>
      - &lt;a href=&#34;logdriver.md&#34;&gt;LogDriver&lt;/a&gt;</i>
    <a href="#placement" title="Placement">Placement</a>: <i>
      - &lt;a href=&#34;placement.md&#34;&gt;Placement&lt;/a&gt;</i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;</i>
    <a href="#configs" title="Configs">Configs</a>: <i>
      - &lt;a href=&#34;configs.md&#34;&gt;Configs&lt;/a&gt;</i>
    <a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - &lt;a href=&#34;dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;</i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - &lt;a href=&#34;healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;</i>
    <a href="#hosts" title="Hosts">Hosts</a>: <i>
      - &lt;a href=&#34;hosts.md&#34;&gt;Hosts&lt;/a&gt;</i>
    <a href="#mounts" title="Mounts">Mounts</a>: <i>
      - &lt;a href=&#34;mounts.md&#34;&gt;Mounts&lt;/a&gt;</i>
    <a href="#privileges" title="Privileges">Privileges</a>: <i>
      - &lt;a href=&#34;privileges.md&#34;&gt;Privileges&lt;/a&gt;</i>
    <a href="#secrets" title="Secrets">Secrets</a>: <i>
      - &lt;a href=&#34;secrets.md&#34;&gt;Secrets&lt;/a&gt;</i>
    <a href="#platforms" title="Platforms">Platforms</a>: <i>
      - &lt;a href=&#34;platforms.md&#34;&gt;Platforms&lt;/a&gt;</i>
    <a href="#limits" title="Limits">Limits</a>: <i>
      - &lt;a href=&#34;limits.md&#34;&gt;Limits&lt;/a&gt;</i>
    <a href="#reservation" title="Reservation">Reservation</a>: <i>
      - &lt;a href=&#34;reservation.md&#34;&gt;Reservation&lt;/a&gt;</i>
    <a href="#bindoptions" title="BindOptions">BindOptions</a>: <i>
      - &lt;a href=&#34;bindoptions.md&#34;&gt;BindOptions&lt;/a&gt;</i>
    <a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>: <i>
      - &lt;a href=&#34;tmpfsoptions.md&#34;&gt;TmpfsOptions&lt;/a&gt;</i>
    <a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>: <i>
      - &lt;a href=&#34;volumeoptions.md&#34;&gt;VolumeOptions&lt;/a&gt;</i>
    <a href="#credentialspec" title="CredentialSpec">CredentialSpec</a>: <i>
      - &lt;a href=&#34;credentialspec.md&#34;&gt;CredentialSpec&lt;/a&gt;</i>
    <a href="#selinuxcontext" title="SeLinuxContext">SeLinuxContext</a>: <i>
      - &lt;a href=&#34;selinuxcontext.md&#34;&gt;SeLinuxContext&lt;/a&gt;</i>
    <a href="#genericresources" title="GenericResources">GenericResources</a>: <i>
      - &lt;a href=&#34;genericresources.md&#34;&gt;GenericResources&lt;/a&gt;</i>
</pre>

## Properties

#### Auth

_Required_: No

_Type_: List of &lt;a href=&#34;auth.md&#34;&gt;Auth&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConvergeConfig

_Required_: No

_Type_: List of &lt;a href=&#34;convergeconfig.md&#34;&gt;ConvergeConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointSpec

_Required_: No

_Type_: List of &lt;a href=&#34;endpointspec.md&#34;&gt;EndpointSpec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: List of &lt;a href=&#34;mode.md&#34;&gt;Mode&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollbackConfig

_Required_: No

_Type_: List of &lt;a href=&#34;rollbackconfig.md&#34;&gt;RollbackConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskSpec

_Required_: No

_Type_: List of &lt;a href=&#34;taskspec.md&#34;&gt;TaskSpec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateConfig

_Required_: No

_Type_: List of &lt;a href=&#34;updateconfig.md&#34;&gt;UpdateConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replicated

_Required_: No

_Type_: List of &lt;a href=&#34;replicated.md&#34;&gt;Replicated&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerSpec

_Required_: No

_Type_: List of &lt;a href=&#34;containerspec.md&#34;&gt;ContainerSpec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDriver

_Required_: No

_Type_: List of &lt;a href=&#34;logdriver.md&#34;&gt;LogDriver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of &lt;a href=&#34;placement.md&#34;&gt;Placement&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configs

_Required_: No

_Type_: List of &lt;a href=&#34;configs.md&#34;&gt;Configs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No

_Type_: List of &lt;a href=&#34;dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of &lt;a href=&#34;healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts

_Required_: No

_Type_: List of &lt;a href=&#34;hosts.md&#34;&gt;Hosts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mounts

_Required_: No

_Type_: List of &lt;a href=&#34;mounts.md&#34;&gt;Mounts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileges

_Required_: No

_Type_: List of &lt;a href=&#34;privileges.md&#34;&gt;Privileges&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secrets

_Required_: No

_Type_: List of &lt;a href=&#34;secrets.md&#34;&gt;Secrets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platforms

_Required_: No

_Type_: List of &lt;a href=&#34;platforms.md&#34;&gt;Platforms&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limits

_Required_: No

_Type_: List of &lt;a href=&#34;limits.md&#34;&gt;Limits&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reservation

_Required_: No

_Type_: List of &lt;a href=&#34;reservation.md&#34;&gt;Reservation&lt;/a&gt;

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

#### CredentialSpec

_Required_: No

_Type_: List of &lt;a href=&#34;credentialspec.md&#34;&gt;CredentialSpec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinuxContext

_Required_: No

_Type_: List of &lt;a href=&#34;selinuxcontext.md&#34;&gt;SeLinuxContext&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenericResources

_Required_: No

_Type_: List of &lt;a href=&#34;genericresources.md&#34;&gt;GenericResources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

