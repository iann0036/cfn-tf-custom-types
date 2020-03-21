# Terraform::VSphere::VirtualMachine Clone

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#linkedclone" title="LinkedClone">LinkedClone</a>" : <i>Boolean</i>,
    "<a href="#templateuuid" title="TemplateUuid">TemplateUuid</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#customize" title="Customize">Customize</a>" : <i>[ &lt;a href=&#34;clone-customize.md&#34;&gt;Customize&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#linkedclone" title="LinkedClone">LinkedClone</a>: <i>Boolean</i>
<a href="#templateuuid" title="TemplateUuid">TemplateUuid</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#customize" title="Customize">Customize</a>: <i>
      - &lt;a href=&#34;clone-customize.md&#34;&gt;Customize&lt;/a&gt;</i>
</pre>

## Properties

#### LinkedClone

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUuid

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Customize

_Required_: No
_Type_: List of &lt;a href=&#34;clone-customize.md&#34;&gt;Customize&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

