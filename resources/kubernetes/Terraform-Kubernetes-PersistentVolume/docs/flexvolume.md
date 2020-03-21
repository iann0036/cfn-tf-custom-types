# Terraform::Kubernetes::PersistentVolume FlexVolume

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
    "<a href="#fstype" title="FsType">FsType</a>" : <i>String</i>,
    "<a href="#options" title="Options">Options</a>" : <i>[ &lt;a href=&#34;flexvolume-options.md&#34;&gt;Options&lt;/a&gt;, ... ]</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ &lt;a href=&#34;flexvolume-secretref.md&#34;&gt;SecretRef&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#driver" title="Driver">Driver</a>: <i>String</i>
<a href="#fstype" title="FsType">FsType</a>: <i>String</i>
<a href="#options" title="Options">Options</a>: <i>
      - &lt;a href=&#34;flexvolume-options.md&#34;&gt;Options&lt;/a&gt;</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - &lt;a href=&#34;flexvolume-secretref.md&#34;&gt;SecretRef&lt;/a&gt;</i>
</pre>

## Properties

#### Driver

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No
_Type_: List of &lt;a href=&#34;flexvolume-options.md&#34;&gt;Options&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No
_Type_: List of &lt;a href=&#34;flexvolume-secretref.md&#34;&gt;SecretRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

