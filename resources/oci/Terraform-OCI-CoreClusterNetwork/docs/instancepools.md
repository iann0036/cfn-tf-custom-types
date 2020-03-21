# Terraform::OCI::CoreClusterNetwork InstancePools

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ &lt;a href=&#34;instancepools-definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;, ... ]</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ &lt;a href=&#34;instancepools-freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;, ... ]</i>,
    "<a href="#instanceconfigurationid" title="InstanceConfigurationId">InstanceConfigurationId</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - &lt;a href=&#34;instancepools-definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - &lt;a href=&#34;instancepools-freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;</i>
<a href="#instanceconfigurationid" title="InstanceConfigurationId">InstanceConfigurationId</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
</pre>

## Properties

#### DefinedTags

_Required_: No
_Type_: List of &lt;a href=&#34;instancepools-definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No
_Type_: List of &lt;a href=&#34;instancepools-freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceConfigurationId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

