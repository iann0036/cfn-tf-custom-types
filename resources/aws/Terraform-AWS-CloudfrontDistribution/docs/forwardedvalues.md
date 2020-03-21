# Terraform::AWS::CloudfrontDistribution ForwardedValues

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ String, ... ]</i>,
    "<a href="#querystring" title="QueryString">QueryString</a>" : <i>Boolean</i>,
    "<a href="#querystringcachekeys" title="QueryStringCacheKeys">QueryStringCacheKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#cookies" title="Cookies">Cookies</a>" : <i>[ &lt;a href=&#34;forwardedvalues-cookies.md&#34;&gt;Cookies&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#headers" title="Headers">Headers</a>: <i>
      - String</i>
<a href="#querystring" title="QueryString">QueryString</a>: <i>Boolean</i>
<a href="#querystringcachekeys" title="QueryStringCacheKeys">QueryStringCacheKeys</a>: <i>
      - String</i>
<a href="#cookies" title="Cookies">Cookies</a>: <i>
      - &lt;a href=&#34;forwardedvalues-cookies.md&#34;&gt;Cookies&lt;/a&gt;</i>
</pre>

## Properties

#### Headers

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryStringCacheKeys

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cookies

_Required_: No
_Type_: List of &lt;a href=&#34;forwardedvalues-cookies.md&#34;&gt;Cookies&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

