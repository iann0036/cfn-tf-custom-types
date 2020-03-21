# Terraform::Google::ComputeUrlMap PathRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#paths" title="Paths">Paths</a>" : <i>[ String, ... ]</i>,
    "<a href="#service" title="Service">Service</a>" : <i>String</i>,
    "<a href="#routeaction" title="RouteAction">RouteAction</a>" : <i>[ &lt;a href=&#34;pathrule-routeaction.md&#34;&gt;RouteAction&lt;/a&gt;, ... ]</i>,
    "<a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>" : <i>[ &lt;a href=&#34;pathrule-urlredirect.md&#34;&gt;UrlRedirect&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#paths" title="Paths">Paths</a>: <i>
      - String</i>
<a href="#service" title="Service">Service</a>: <i>String</i>
<a href="#routeaction" title="RouteAction">RouteAction</a>: <i>
      - &lt;a href=&#34;pathrule-routeaction.md&#34;&gt;RouteAction&lt;/a&gt;</i>
<a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>: <i>
      - &lt;a href=&#34;pathrule-urlredirect.md&#34;&gt;UrlRedirect&lt;/a&gt;</i>
</pre>

## Properties

#### Paths

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAction

_Required_: No
_Type_: List of &lt;a href=&#34;pathrule-routeaction.md&#34;&gt;RouteAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRedirect

_Required_: No
_Type_: List of &lt;a href=&#34;pathrule-urlredirect.md&#34;&gt;UrlRedirect&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

