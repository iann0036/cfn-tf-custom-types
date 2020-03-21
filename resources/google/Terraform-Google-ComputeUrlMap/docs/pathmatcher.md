# Terraform::Google::ComputeUrlMap PathMatcher

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultservice" title="DefaultService">DefaultService</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#headeraction" title="HeaderAction">HeaderAction</a>" : <i>[ &lt;a href=&#34;pathmatcher-headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;, ... ]</i>,
    "<a href="#pathrule" title="PathRule">PathRule</a>" : <i>[ &lt;a href=&#34;pathmatcher-pathrule.md&#34;&gt;PathRule&lt;/a&gt;, ... ]</i>,
    "<a href="#routerules" title="RouteRules">RouteRules</a>" : <i>[ &lt;a href=&#34;pathmatcher-routerules.md&#34;&gt;RouteRules&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultservice" title="DefaultService">DefaultService</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#headeraction" title="HeaderAction">HeaderAction</a>: <i>
      - &lt;a href=&#34;pathmatcher-headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;</i>
<a href="#pathrule" title="PathRule">PathRule</a>: <i>
      - &lt;a href=&#34;pathmatcher-pathrule.md&#34;&gt;PathRule&lt;/a&gt;</i>
<a href="#routerules" title="RouteRules">RouteRules</a>: <i>
      - &lt;a href=&#34;pathmatcher-routerules.md&#34;&gt;RouteRules&lt;/a&gt;</i>
</pre>

## Properties

#### DefaultService

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderAction

_Required_: No
_Type_: List of &lt;a href=&#34;pathmatcher-headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRule

_Required_: No
_Type_: List of &lt;a href=&#34;pathmatcher-pathrule.md&#34;&gt;PathRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteRules

_Required_: No
_Type_: List of &lt;a href=&#34;pathmatcher-routerules.md&#34;&gt;RouteRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

