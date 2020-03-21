# Terraform::Docker::Service TaskSpec ContainerSpec Mounts

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#bindoptions" title="BindOptions">BindOptions</a>" : <i>[ &lt;a href=&#34;taskspec-containerspec-mounts-bindoptions.md&#34;&gt;BindOptions&lt;/a&gt;, ... ]</i>,
    "<a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>" : <i>[ &lt;a href=&#34;taskspec-containerspec-mounts-tmpfsoptions.md&#34;&gt;TmpfsOptions&lt;/a&gt;, ... ]</i>,
    "<a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>" : <i>[ &lt;a href=&#34;taskspec-containerspec-mounts-volumeoptions.md&#34;&gt;VolumeOptions&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#bindoptions" title="BindOptions">BindOptions</a>: <i>
      - &lt;a href=&#34;taskspec-containerspec-mounts-bindoptions.md&#34;&gt;BindOptions&lt;/a&gt;</i>
<a href="#tmpfsoptions" title="TmpfsOptions">TmpfsOptions</a>: <i>
      - &lt;a href=&#34;taskspec-containerspec-mounts-tmpfsoptions.md&#34;&gt;TmpfsOptions&lt;/a&gt;</i>
<a href="#volumeoptions" title="VolumeOptions">VolumeOptions</a>: <i>
      - &lt;a href=&#34;taskspec-containerspec-mounts-volumeoptions.md&#34;&gt;VolumeOptions&lt;/a&gt;</i>
</pre>

## Properties

#### ReadOnly

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindOptions

_Required_: No
_Type_: List of &lt;a href=&#34;taskspec-containerspec-mounts-bindoptions.md&#34;&gt;BindOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TmpfsOptions

_Required_: No
_Type_: List of &lt;a href=&#34;taskspec-containerspec-mounts-tmpfsoptions.md&#34;&gt;TmpfsOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeOptions

_Required_: No
_Type_: List of &lt;a href=&#34;taskspec-containerspec-mounts-volumeoptions.md&#34;&gt;VolumeOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

