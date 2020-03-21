# Terraform::AzureRM::ContainerGroup Container

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commands" title="Commands">Commands</a>" : <i>[ String, ... ]</i>,
    "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
    "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ &lt;a href=&#34;container-environmentvariables.md&#34;&gt;EnvironmentVariables&lt;/a&gt;, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#secureenvironmentvariables" title="SecureEnvironmentVariables">SecureEnvironmentVariables</a>" : <i>[ &lt;a href=&#34;container-secureenvironmentvariables.md&#34;&gt;SecureEnvironmentVariables&lt;/a&gt;, ... ]</i>,
    "<a href="#gpu" title="Gpu">Gpu</a>" : <i>[ &lt;a href=&#34;container-gpu.md&#34;&gt;Gpu&lt;/a&gt;, ... ]</i>,
    "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ &lt;a href=&#34;container-livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;, ... ]</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ &lt;a href=&#34;container-ports.md&#34;&gt;Ports&lt;/a&gt;, ... ]</i>,
    "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ &lt;a href=&#34;container-readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;, ... ]</i>,
    "<a href="#volume" title="Volume">Volume</a>" : <i>[ &lt;a href=&#34;container-volume.md&#34;&gt;Volume&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commands" title="Commands">Commands</a>: <i>
      - String</i>
<a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - &lt;a href=&#34;container-environmentvariables.md&#34;&gt;EnvironmentVariables&lt;/a&gt;</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#memory" title="Memory">Memory</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#secureenvironmentvariables" title="SecureEnvironmentVariables">SecureEnvironmentVariables</a>: <i>
      - &lt;a href=&#34;container-secureenvironmentvariables.md&#34;&gt;SecureEnvironmentVariables&lt;/a&gt;</i>
<a href="#gpu" title="Gpu">Gpu</a>: <i>
      - &lt;a href=&#34;container-gpu.md&#34;&gt;Gpu&lt;/a&gt;</i>
<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - &lt;a href=&#34;container-livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;</i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - &lt;a href=&#34;container-ports.md&#34;&gt;Ports&lt;/a&gt;</i>
<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - &lt;a href=&#34;container-readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;</i>
<a href="#volume" title="Volume">Volume</a>: <i>
      - &lt;a href=&#34;container-volume.md&#34;&gt;Volume&lt;/a&gt;</i>
</pre>

## Properties

#### Commands

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

_Required_: No
_Type_: List of &lt;a href=&#34;container-environmentvariables.md&#34;&gt;EnvironmentVariables&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureEnvironmentVariables

_Required_: No
_Type_: List of &lt;a href=&#34;container-secureenvironmentvariables.md&#34;&gt;SecureEnvironmentVariables&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gpu

_Required_: No
_Type_: List of &lt;a href=&#34;container-gpu.md&#34;&gt;Gpu&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No
_Type_: List of &lt;a href=&#34;container-livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No
_Type_: List of &lt;a href=&#34;container-ports.md&#34;&gt;Ports&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No
_Type_: List of &lt;a href=&#34;container-readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No
_Type_: List of &lt;a href=&#34;container-volume.md&#34;&gt;Volume&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

