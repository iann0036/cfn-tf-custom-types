# Terraform::Google::CloudSchedulerJob HttpTarget

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#body" title="Body">Body</a>" : <i>String</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ &lt;a href=&#34;httptarget-headers.md&#34;&gt;Headers&lt;/a&gt;, ... ]</i>,
    "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
    "<a href="#oauthtoken" title="OauthToken">OauthToken</a>" : <i>[ &lt;a href=&#34;httptarget-oauthtoken.md&#34;&gt;OauthToken&lt;/a&gt;, ... ]</i>,
    "<a href="#oidctoken" title="OidcToken">OidcToken</a>" : <i>[ &lt;a href=&#34;httptarget-oidctoken.md&#34;&gt;OidcToken&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#body" title="Body">Body</a>: <i>String</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - &lt;a href=&#34;httptarget-headers.md&#34;&gt;Headers&lt;/a&gt;</i>
<a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
<a href="#oauthtoken" title="OauthToken">OauthToken</a>: <i>
      - &lt;a href=&#34;httptarget-oauthtoken.md&#34;&gt;OauthToken&lt;/a&gt;</i>
<a href="#oidctoken" title="OidcToken">OidcToken</a>: <i>
      - &lt;a href=&#34;httptarget-oidctoken.md&#34;&gt;OidcToken&lt;/a&gt;</i>
</pre>

## Properties

#### Body

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No
_Type_: List of &lt;a href=&#34;httptarget-headers.md&#34;&gt;Headers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthToken

_Required_: No
_Type_: List of &lt;a href=&#34;httptarget-oauthtoken.md&#34;&gt;OauthToken&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcToken

_Required_: No
_Type_: List of &lt;a href=&#34;httptarget-oidctoken.md&#34;&gt;OidcToken&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

