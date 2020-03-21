# Terraform::OVH::MeInstallationTemplate

CloudFormation equivalent of ovh_me_installation_template

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OVH::MeInstallationTemplate",
    "Properties" : {
        "<a href="#basetemplatename" title="BaseTemplateName">BaseTemplateName</a>" : <i>String</i>,
        "<a href="#defaultlanguage" title="DefaultLanguage">DefaultLanguage</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#removedefaultpartitionschemes" title="RemoveDefaultPartitionSchemes">RemoveDefaultPartitionSchemes</a>" : <i>Boolean</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#customization" title="Customization">Customization</a>" : <i>[ &lt;a href=&#34;customization.md&#34;&gt;Customization&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OVH::MeInstallationTemplate
Properties:
    <a href="#basetemplatename" title="BaseTemplateName">BaseTemplateName</a>: <i>String</i>
    <a href="#defaultlanguage" title="DefaultLanguage">DefaultLanguage</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#removedefaultpartitionschemes" title="RemoveDefaultPartitionSchemes">RemoveDefaultPartitionSchemes</a>: <i>Boolean</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#customization" title="Customization">Customization</a>: <i>
      - &lt;a href=&#34;customization.md&#34;&gt;Customization&lt;/a&gt;</i>
</pre>

## Properties

#### BaseTemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLanguage

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveDefaultPartitionSchemes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Customization

_Required_: No

_Type_: List of &lt;a href=&#34;customization.md&#34;&gt;Customization&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvailableLanguages

Returns the &lt;code&gt;AvailableLanguages&lt;/code&gt; value.

#### Beta

Returns the &lt;code&gt;Beta&lt;/code&gt; value.

#### BitFormat

Returns the &lt;code&gt;BitFormat&lt;/code&gt; value.

#### Category

Returns the &lt;code&gt;Category&lt;/code&gt; value.

#### Deprecated

Returns the &lt;code&gt;Deprecated&lt;/code&gt; value.

#### Description

Returns the &lt;code&gt;Description&lt;/code&gt; value.

#### Distribution

Returns the &lt;code&gt;Distribution&lt;/code&gt; value.

#### Family

Returns the &lt;code&gt;Family&lt;/code&gt; value.

#### Filesystems

Returns the &lt;code&gt;Filesystems&lt;/code&gt; value.

#### HardRaidConfiguration

Returns the &lt;code&gt;HardRaidConfiguration&lt;/code&gt; value.

#### LastModification

Returns the &lt;code&gt;LastModification&lt;/code&gt; value.

#### SupportsDistributionKernel

Returns the &lt;code&gt;SupportsDistributionKernel&lt;/code&gt; value.

#### SupportsGptLabel

Returns the &lt;code&gt;SupportsGptLabel&lt;/code&gt; value.

#### SupportsRtm

Returns the &lt;code&gt;SupportsRtm&lt;/code&gt; value.

#### SupportsSqlServer

Returns the &lt;code&gt;SupportsSqlServer&lt;/code&gt; value.

#### SupportsUefi

Returns the &lt;code&gt;SupportsUefi&lt;/code&gt; value.

