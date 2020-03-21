# Terraform::OCI::CoreInstanceConfiguration InstanceDetails BlockVolumes

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>,
    "<a href="#attachdetails" title="AttachDetails">AttachDetails</a>" : <i>[ &lt;a href=&#34;instancedetails-blockvolumes-attachdetails.md&#34;&gt;AttachDetails&lt;/a&gt;, ... ]</i>,
    "<a href="#createdetails" title="CreateDetails">CreateDetails</a>" : <i>[ &lt;a href=&#34;instancedetails-blockvolumes-createdetails.md&#34;&gt;CreateDetails&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
<a href="#attachdetails" title="AttachDetails">AttachDetails</a>: <i>
      - &lt;a href=&#34;instancedetails-blockvolumes-attachdetails.md&#34;&gt;AttachDetails&lt;/a&gt;</i>
<a href="#createdetails" title="CreateDetails">CreateDetails</a>: <i>
      - &lt;a href=&#34;instancedetails-blockvolumes-createdetails.md&#34;&gt;CreateDetails&lt;/a&gt;</i>
</pre>

## Properties

#### VolumeId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachDetails

_Required_: No
_Type_: List of &lt;a href=&#34;instancedetails-blockvolumes-attachdetails.md&#34;&gt;AttachDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDetails

_Required_: No
_Type_: List of &lt;a href=&#34;instancedetails-blockvolumes-createdetails.md&#34;&gt;CreateDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

