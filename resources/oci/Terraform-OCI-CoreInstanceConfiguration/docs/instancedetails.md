# Terraform::OCI::CoreInstanceConfiguration InstanceDetails

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#blockvolumes" title="BlockVolumes">BlockVolumes</a>" : <i>[ &lt;a href=&#34;instancedetails-blockvolumes.md&#34;&gt;BlockVolumes&lt;/a&gt;, ... ]</i>,
    "<a href="#launchdetails" title="LaunchDetails">LaunchDetails</a>" : <i>[ &lt;a href=&#34;instancedetails-launchdetails.md&#34;&gt;LaunchDetails&lt;/a&gt;, ... ]</i>,
    "<a href="#secondaryvnics" title="SecondaryVnics">SecondaryVnics</a>" : <i>[ &lt;a href=&#34;instancedetails-secondaryvnics.md&#34;&gt;SecondaryVnics&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#blockvolumes" title="BlockVolumes">BlockVolumes</a>: <i>
      - &lt;a href=&#34;instancedetails-blockvolumes.md&#34;&gt;BlockVolumes&lt;/a&gt;</i>
<a href="#launchdetails" title="LaunchDetails">LaunchDetails</a>: <i>
      - &lt;a href=&#34;instancedetails-launchdetails.md&#34;&gt;LaunchDetails&lt;/a&gt;</i>
<a href="#secondaryvnics" title="SecondaryVnics">SecondaryVnics</a>: <i>
      - &lt;a href=&#34;instancedetails-secondaryvnics.md&#34;&gt;SecondaryVnics&lt;/a&gt;</i>
</pre>

## Properties

#### InstanceType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockVolumes

_Required_: No
_Type_: List of &lt;a href=&#34;instancedetails-blockvolumes.md&#34;&gt;BlockVolumes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchDetails

_Required_: No
_Type_: List of &lt;a href=&#34;instancedetails-launchdetails.md&#34;&gt;LaunchDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryVnics

_Required_: No
_Type_: List of &lt;a href=&#34;instancedetails-secondaryvnics.md&#34;&gt;SecondaryVnics&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

