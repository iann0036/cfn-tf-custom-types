# Terraform::Google::ComposerEnvironment Config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
    "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ &lt;a href=&#34;config-nodeconfig.md&#34;&gt;NodeConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#privateenvironmentconfig" title="PrivateEnvironmentConfig">PrivateEnvironmentConfig</a>" : <i>[ &lt;a href=&#34;config-privateenvironmentconfig.md&#34;&gt;PrivateEnvironmentConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>" : <i>[ &lt;a href=&#34;config-softwareconfig.md&#34;&gt;SoftwareConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - &lt;a href=&#34;config-nodeconfig.md&#34;&gt;NodeConfig&lt;/a&gt;</i>
<a href="#privateenvironmentconfig" title="PrivateEnvironmentConfig">PrivateEnvironmentConfig</a>: <i>
      - &lt;a href=&#34;config-privateenvironmentconfig.md&#34;&gt;PrivateEnvironmentConfig&lt;/a&gt;</i>
<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - &lt;a href=&#34;config-softwareconfig.md&#34;&gt;SoftwareConfig&lt;/a&gt;</i>
</pre>

## Properties

#### NodeCount

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No
_Type_: List of &lt;a href=&#34;config-nodeconfig.md&#34;&gt;NodeConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEnvironmentConfig

_Required_: No
_Type_: List of &lt;a href=&#34;config-privateenvironmentconfig.md&#34;&gt;PrivateEnvironmentConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareConfig

_Required_: No
_Type_: List of &lt;a href=&#34;config-softwareconfig.md&#34;&gt;SoftwareConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

