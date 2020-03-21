# Terraform::Docker::Service TaskSpec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>" : <i>Double</i>,
    "<a href="#networks" title="Networks">Networks</a>" : <i>[ String, ... ]</i>,
    "<a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>" : <i>[ &lt;a href=&#34;taskspec-restartpolicy.md&#34;&gt;RestartPolicy&lt;/a&gt;, ... ]</i>,
    "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
    "<a href="#containerspec" title="ContainerSpec">ContainerSpec</a>" : <i>[ &lt;a href=&#34;taskspec-containerspec.md&#34;&gt;ContainerSpec&lt;/a&gt;, ... ]</i>,
    "<a href="#logdriver" title="LogDriver">LogDriver</a>" : <i>[ &lt;a href=&#34;taskspec-logdriver.md&#34;&gt;LogDriver&lt;/a&gt;, ... ]</i>,
    "<a href="#placement" title="Placement">Placement</a>" : <i>[ &lt;a href=&#34;taskspec-placement.md&#34;&gt;Placement&lt;/a&gt;, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ &lt;a href=&#34;taskspec-resources.md&#34;&gt;Resources&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>: <i>Double</i>
<a href="#networks" title="Networks">Networks</a>: <i>
      - String</i>
<a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>: <i>
      - &lt;a href=&#34;taskspec-restartpolicy.md&#34;&gt;RestartPolicy&lt;/a&gt;</i>
<a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
<a href="#containerspec" title="ContainerSpec">ContainerSpec</a>: <i>
      - &lt;a href=&#34;taskspec-containerspec.md&#34;&gt;ContainerSpec&lt;/a&gt;</i>
<a href="#logdriver" title="LogDriver">LogDriver</a>: <i>
      - &lt;a href=&#34;taskspec-logdriver.md&#34;&gt;LogDriver&lt;/a&gt;</i>
<a href="#placement" title="Placement">Placement</a>: <i>
      - &lt;a href=&#34;taskspec-placement.md&#34;&gt;Placement&lt;/a&gt;</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - &lt;a href=&#34;taskspec-resources.md&#34;&gt;Resources&lt;/a&gt;</i>
</pre>

## Properties

#### ForceUpdate

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartPolicy

_Required_: No
_Type_: List of &lt;a href=&#34;taskspec-restartpolicy.md&#34;&gt;RestartPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerSpec

_Required_: No
_Type_: List of &lt;a href=&#34;taskspec-containerspec.md&#34;&gt;ContainerSpec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDriver

_Required_: No
_Type_: List of &lt;a href=&#34;taskspec-logdriver.md&#34;&gt;LogDriver&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No
_Type_: List of &lt;a href=&#34;taskspec-placement.md&#34;&gt;Placement&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No
_Type_: List of &lt;a href=&#34;taskspec-resources.md&#34;&gt;Resources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

