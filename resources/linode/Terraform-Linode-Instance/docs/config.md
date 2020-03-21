# Terraform::Linode::Instance Config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
    "<a href="#kernel" title="Kernel">Kernel</a>" : <i>String</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>" : <i>Double</i>,
    "<a href="#rootdevice" title="RootDevice">RootDevice</a>" : <i>String</i>,
    "<a href="#runlevel" title="RunLevel">RunLevel</a>" : <i>String</i>,
    "<a href="#virtmode" title="VirtMode">VirtMode</a>" : <i>String</i>,
    "<a href="#devices" title="Devices">Devices</a>" : <i>[ &lt;a href=&#34;config-devices.md&#34;&gt;Devices&lt;/a&gt;, ... ]</i>,
    "<a href="#helpers" title="Helpers">Helpers</a>" : <i>[ &lt;a href=&#34;config-helpers.md&#34;&gt;Helpers&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comments" title="Comments">Comments</a>: <i>String</i>
<a href="#kernel" title="Kernel">Kernel</a>: <i>String</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>: <i>Double</i>
<a href="#rootdevice" title="RootDevice">RootDevice</a>: <i>String</i>
<a href="#runlevel" title="RunLevel">RunLevel</a>: <i>String</i>
<a href="#virtmode" title="VirtMode">VirtMode</a>: <i>String</i>
<a href="#devices" title="Devices">Devices</a>: <i>
      - &lt;a href=&#34;config-devices.md&#34;&gt;Devices&lt;/a&gt;</i>
<a href="#helpers" title="Helpers">Helpers</a>: <i>
      - &lt;a href=&#34;config-helpers.md&#34;&gt;Helpers&lt;/a&gt;</i>
</pre>

## Properties

#### Comments

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kernel

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryLimit

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootDevice

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunLevel

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtMode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: No
_Type_: List of &lt;a href=&#34;config-devices.md&#34;&gt;Devices&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Helpers

_Required_: No
_Type_: List of &lt;a href=&#34;config-helpers.md&#34;&gt;Helpers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

