# Terraform::AWS::LaunchTemplate BlockDeviceMappings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
    "<a href="#nodevice" title="NoDevice">NoDevice</a>" : <i>String</i>,
    "<a href="#virtualname" title="VirtualName">VirtualName</a>" : <i>String</i>,
    "<a href="#ebs" title="Ebs">Ebs</a>" : <i>[ &lt;a href=&#34;blockdevicemappings-ebs.md&#34;&gt;Ebs&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
<a href="#nodevice" title="NoDevice">NoDevice</a>: <i>String</i>
<a href="#virtualname" title="VirtualName">VirtualName</a>: <i>String</i>
<a href="#ebs" title="Ebs">Ebs</a>: <i>
      - &lt;a href=&#34;blockdevicemappings-ebs.md&#34;&gt;Ebs&lt;/a&gt;</i>
</pre>

## Properties

#### DeviceName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDevice

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ebs

_Required_: No
_Type_: List of &lt;a href=&#34;blockdevicemappings-ebs.md&#34;&gt;Ebs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

