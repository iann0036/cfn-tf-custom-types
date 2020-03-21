# Terraform::Kubernetes::Pod Container

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#args" title="Args">Args</a>" : <i>[ String, ... ]</i>,
    "<a href="#command" title="Command">Command</a>" : <i>[ String, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#imagepullpolicy" title="ImagePullPolicy">ImagePullPolicy</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#stdin" title="Stdin">Stdin</a>" : <i>Boolean</i>,
    "<a href="#stdinonce" title="StdinOnce">StdinOnce</a>" : <i>Boolean</i>,
    "<a href="#terminationmessagepath" title="TerminationMessagePath">TerminationMessagePath</a>" : <i>String</i>,
    "<a href="#tty" title="Tty">Tty</a>" : <i>Boolean</i>,
    "<a href="#workingdir" title="WorkingDir">WorkingDir</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ &lt;a href=&#34;container-env.md&#34;&gt;Env&lt;/a&gt;, ... ]</i>,
    "<a href="#envfrom" title="EnvFrom">EnvFrom</a>" : <i>[ &lt;a href=&#34;container-envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;, ... ]</i>,
    "<a href="#lifecycle" title="Lifecycle">Lifecycle</a>" : <i>[ &lt;a href=&#34;container-lifecycle.md&#34;&gt;Lifecycle&lt;/a&gt;, ... ]</i>,
    "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ &lt;a href=&#34;container-livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>[ &lt;a href=&#34;container-port.md&#34;&gt;Port&lt;/a&gt;, ... ]</i>,
    "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ &lt;a href=&#34;container-readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ &lt;a href=&#34;container-resources.md&#34;&gt;Resources&lt;/a&gt;, ... ]</i>,
    "<a href="#securitycontext" title="SecurityContext">SecurityContext</a>" : <i>[ &lt;a href=&#34;container-securitycontext.md&#34;&gt;SecurityContext&lt;/a&gt;, ... ]</i>,
    "<a href="#startupprobe" title="StartupProbe">StartupProbe</a>" : <i>[ &lt;a href=&#34;container-startupprobe.md&#34;&gt;StartupProbe&lt;/a&gt;, ... ]</i>,
    "<a href="#volumemount" title="VolumeMount">VolumeMount</a>" : <i>[ &lt;a href=&#34;container-volumemount.md&#34;&gt;VolumeMount&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#args" title="Args">Args</a>: <i>
      - String</i>
<a href="#command" title="Command">Command</a>: <i>
      - String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#imagepullpolicy" title="ImagePullPolicy">ImagePullPolicy</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#stdin" title="Stdin">Stdin</a>: <i>Boolean</i>
<a href="#stdinonce" title="StdinOnce">StdinOnce</a>: <i>Boolean</i>
<a href="#terminationmessagepath" title="TerminationMessagePath">TerminationMessagePath</a>: <i>String</i>
<a href="#tty" title="Tty">Tty</a>: <i>Boolean</i>
<a href="#workingdir" title="WorkingDir">WorkingDir</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>
      - &lt;a href=&#34;container-env.md&#34;&gt;Env&lt;/a&gt;</i>
<a href="#envfrom" title="EnvFrom">EnvFrom</a>: <i>
      - &lt;a href=&#34;container-envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;</i>
<a href="#lifecycle" title="Lifecycle">Lifecycle</a>: <i>
      - &lt;a href=&#34;container-lifecycle.md&#34;&gt;Lifecycle&lt;/a&gt;</i>
<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - &lt;a href=&#34;container-livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;</i>
<a href="#port" title="Port">Port</a>: <i>
      - &lt;a href=&#34;container-port.md&#34;&gt;Port&lt;/a&gt;</i>
<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - &lt;a href=&#34;container-readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - &lt;a href=&#34;container-resources.md&#34;&gt;Resources&lt;/a&gt;</i>
<a href="#securitycontext" title="SecurityContext">SecurityContext</a>: <i>
      - &lt;a href=&#34;container-securitycontext.md&#34;&gt;SecurityContext&lt;/a&gt;</i>
<a href="#startupprobe" title="StartupProbe">StartupProbe</a>: <i>
      - &lt;a href=&#34;container-startupprobe.md&#34;&gt;StartupProbe&lt;/a&gt;</i>
<a href="#volumemount" title="VolumeMount">VolumeMount</a>: <i>
      - &lt;a href=&#34;container-volumemount.md&#34;&gt;VolumeMount&lt;/a&gt;</i>
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

#### Image

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullPolicy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stdin

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StdinOnce

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationMessagePath

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tty

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDir

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No
_Type_: List of &lt;a href=&#34;container-env.md&#34;&gt;Env&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvFrom

_Required_: No
_Type_: List of &lt;a href=&#34;container-envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifecycle

_Required_: No
_Type_: List of &lt;a href=&#34;container-lifecycle.md&#34;&gt;Lifecycle&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No
_Type_: List of &lt;a href=&#34;container-livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No
_Type_: List of &lt;a href=&#34;container-port.md&#34;&gt;Port&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No
_Type_: List of &lt;a href=&#34;container-readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No
_Type_: List of &lt;a href=&#34;container-resources.md&#34;&gt;Resources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityContext

_Required_: No
_Type_: List of &lt;a href=&#34;container-securitycontext.md&#34;&gt;SecurityContext&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartupProbe

_Required_: No
_Type_: List of &lt;a href=&#34;container-startupprobe.md&#34;&gt;StartupProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMount

_Required_: No
_Type_: List of &lt;a href=&#34;container-volumemount.md&#34;&gt;VolumeMount&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

