# Terraform::Google::ComputeUrlMap PathMatcher RouteRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#service" title="Service">Service</a>" : <i>String</i>,
    "<a href="#headeraction" title="HeaderAction">HeaderAction</a>" : <i>[ &lt;a href=&#34;pathmatcher-routerules-headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;, ... ]</i>,
    "<a href="#matchrules" title="MatchRules">MatchRules</a>" : <i>[ &lt;a href=&#34;pathmatcher-routerules-matchrules.md&#34;&gt;MatchRules&lt;/a&gt;, ... ]</i>,
    "<a href="#routeaction" title="RouteAction">RouteAction</a>" : <i>[ &lt;a href=&#34;pathmatcher-routerules-routeaction.md&#34;&gt;RouteAction&lt;/a&gt;, ... ]</i>,
    "<a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>" : <i>[ &lt;a href=&#34;pathmatcher-routerules-urlredirect.md&#34;&gt;UrlRedirect&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#service" title="Service">Service</a>: <i>String</i>
<a href="#headeraction" title="HeaderAction">HeaderAction</a>: <i>
      - &lt;a href=&#34;pathmatcher-routerules-headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;</i>
<a href="#matchrules" title="MatchRules">MatchRules</a>: <i>
      - &lt;a href=&#34;pathmatcher-routerules-matchrules.md&#34;&gt;MatchRules&lt;/a&gt;</i>
<a href="#routeaction" title="RouteAction">RouteAction</a>: <i>
      - &lt;a href=&#34;pathmatcher-routerules-routeaction.md&#34;&gt;RouteAction&lt;/a&gt;</i>
<a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>: <i>
      - &lt;a href=&#34;pathmatcher-routerules-urlredirect.md&#34;&gt;UrlRedirect&lt;/a&gt;</i>
</pre>

## Properties

#### Priority

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderAction

_Required_: No
_Type_: List of &lt;a href=&#34;pathmatcher-routerules-headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchRules

_Required_: No
_Type_: List of &lt;a href=&#34;pathmatcher-routerules-matchrules.md&#34;&gt;MatchRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAction

_Required_: No
_Type_: List of &lt;a href=&#34;pathmatcher-routerules-routeaction.md&#34;&gt;RouteAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRedirect

_Required_: No
_Type_: List of &lt;a href=&#34;pathmatcher-routerules-urlredirect.md&#34;&gt;UrlRedirect&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

