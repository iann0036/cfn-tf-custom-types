# Terraform::Google::CloudRunService Spec Containers

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#args" title="Args">Args</a>" : <i>[ String, ... ]</i>,
    "<a href="#command" title="Command">Command</a>" : <i>[ String, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#workingdir" title="WorkingDir">WorkingDir</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ &lt;a href=&#34;spec-containers-env.md&#34;&gt;Env&lt;/a&gt;, ... ]</i>,
    "<a href="#envfrom" title="EnvFrom">EnvFrom</a>" : <i>[ &lt;a href=&#34;spec-containers-envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ &lt;a href=&#34;spec-containers-resources.md&#34;&gt;Resources&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#args" title="Args">Args</a>: <i>
      - String</i>
<a href="#command" title="Command">Command</a>: <i>
      - String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#workingdir" title="WorkingDir">WorkingDir</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>
      - &lt;a href=&#34;spec-containers-env.md&#34;&gt;Env&lt;/a&gt;</i>
<a href="#envfrom" title="EnvFrom">EnvFrom</a>: <i>
      - &lt;a href=&#34;spec-containers-envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - &lt;a href=&#34;spec-containers-resources.md&#34;&gt;Resources&lt;/a&gt;</i>
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

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDir

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No
_Type_: List of &lt;a href=&#34;spec-containers-env.md&#34;&gt;Env&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvFrom

_Required_: No
_Type_: List of &lt;a href=&#34;spec-containers-envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No
_Type_: List of &lt;a href=&#34;spec-containers-resources.md&#34;&gt;Resources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

