# Terraform::Template::CloudinitConfig

CloudFormation equivalent of template_cloudinit_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Template::CloudinitConfig",
    "Properties" : {
        "<a href="#base64encode" title="Base64Encode">Base64Encode</a>" : <i>Boolean</i>,
        "<a href="#gzip" title="Gzip">Gzip</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#part" title="Part">Part</a>" : <i>[ &lt;a href=&#34;part.md&#34;&gt;Part&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Template::CloudinitConfig
Properties:
    <a href="#base64encode" title="Base64Encode">Base64Encode</a>: <i>Boolean</i>
    <a href="#gzip" title="Gzip">Gzip</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#part" title="Part">Part</a>: <i>
      - &lt;a href=&#34;part.md&#34;&gt;Part&lt;/a&gt;</i>
</pre>

## Properties

#### Base64Encode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gzip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Part

_Required_: No

_Type_: List of &lt;a href=&#34;part.md&#34;&gt;Part&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Rendered

Returns the &lt;code&gt;Rendered&lt;/code&gt; value.

