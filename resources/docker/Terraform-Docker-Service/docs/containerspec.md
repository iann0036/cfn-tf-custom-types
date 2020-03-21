# Terraform::Docker::Service ContainerSpec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#args" title="Args">Args</a>" : <i>[ String, ... ]</i>,
    "<a href="#command" title="Command">Command</a>" : <i>[ String, ... ]</i>,
    "<a href="#dir" title="Dir">Dir</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ &lt;a href=&#34;containerspec-env.md&#34;&gt;Env&lt;/a&gt;, ... ]</i>,
    "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#isolation" title="Isolation">Isolation</a>" : <i>String</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#stopgraceperiod" title="StopGracePeriod">StopGracePeriod</a>" : <i>String</i>,
    "<a href="#stopsignal" title="StopSignal">StopSignal</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>,
    "<a href="#configs" title="Configs">Configs</a>" : <i>[ &lt;a href=&#34;containerspec-configs.md&#34;&gt;Configs&lt;/a&gt;, ... ]</i>,
    "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ &lt;a href=&#34;containerspec-dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ &lt;a href=&#34;containerspec-healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;, ... ]</i>,
    "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ &lt;a href=&#34;containerspec-hosts.md&#34;&gt;Hosts&lt;/a&gt;, ... ]</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;containerspec-labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
    "<a href="#mounts" title="Mounts">Mounts</a>" : <i>[ &lt;a href=&#34;containerspec-mounts.md&#34;&gt;Mounts&lt;/a&gt;, ... ]</i>,
    "<a href="#privileges" title="Privileges">Privileges</a>" : <i>[ &lt;a href=&#34;containerspec-privileges.md&#34;&gt;Privileges&lt;/a&gt;, ... ]</i>,
    "<a href="#secrets" title="Secrets">Secrets</a>" : <i>[ &lt;a href=&#34;containerspec-secrets.md&#34;&gt;Secrets&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#args" title="Args">Args</a>: <i>
      - String</i>
<a href="#command" title="Command">Command</a>: <i>
      - String</i>
<a href="#dir" title="Dir">Dir</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>
      - &lt;a href=&#34;containerspec-env.md&#34;&gt;Env&lt;/a&gt;</i>
<a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#isolation" title="Isolation">Isolation</a>: <i>String</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#stopgraceperiod" title="StopGracePeriod">StopGracePeriod</a>: <i>String</i>
<a href="#stopsignal" title="StopSignal">StopSignal</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
<a href="#configs" title="Configs">Configs</a>: <i>
      - &lt;a href=&#34;containerspec-configs.md&#34;&gt;Configs&lt;/a&gt;</i>
<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - &lt;a href=&#34;containerspec-dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;</i>
<a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - &lt;a href=&#34;containerspec-healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;</i>
<a href="#hosts" title="Hosts">Hosts</a>: <i>
      - &lt;a href=&#34;containerspec-hosts.md&#34;&gt;Hosts&lt;/a&gt;</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;containerspec-labels.md&#34;&gt;Labels&lt;/a&gt;</i>
<a href="#mounts" title="Mounts">Mounts</a>: <i>
      - &lt;a href=&#34;containerspec-mounts.md&#34;&gt;Mounts&lt;/a&gt;</i>
<a href="#privileges" title="Privileges">Privileges</a>: <i>
      - &lt;a href=&#34;containerspec-privileges.md&#34;&gt;Privileges&lt;/a&gt;</i>
<a href="#secrets" title="Secrets">Secrets</a>: <i>
      - &lt;a href=&#34;containerspec-secrets.md&#34;&gt;Secrets&lt;/a&gt;</i>
</pre>

## Properties

#### Args

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dir

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No
_Type_: List of &lt;a href=&#34;containerspec-env.md&#34;&gt;Env&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Isolation

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopGracePeriod

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopSignal

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configs

_Required_: No
_Type_: List of &lt;a href=&#34;containerspec-configs.md&#34;&gt;Configs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No
_Type_: List of &lt;a href=&#34;containerspec-dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No
_Type_: List of &lt;a href=&#34;containerspec-healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts

_Required_: No
_Type_: List of &lt;a href=&#34;containerspec-hosts.md&#34;&gt;Hosts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No
_Type_: List of &lt;a href=&#34;containerspec-labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mounts

_Required_: No
_Type_: List of &lt;a href=&#34;containerspec-mounts.md&#34;&gt;Mounts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileges

_Required_: No
_Type_: List of &lt;a href=&#34;containerspec-privileges.md&#34;&gt;Privileges&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secrets

_Required_: No
_Type_: List of &lt;a href=&#34;containerspec-secrets.md&#34;&gt;Secrets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

