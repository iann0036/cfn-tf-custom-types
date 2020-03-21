# Terraform::Google::PubsubSubscription PushConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attributes" title="Attributes">Attributes</a>" : <i>[ &lt;a href=&#34;pushconfig-attributes.md&#34;&gt;Attributes&lt;/a&gt;, ... ]</i>,
    "<a href="#pushendpoint" title="PushEndpoint">PushEndpoint</a>" : <i>String</i>,
    "<a href="#oidctoken" title="OidcToken">OidcToken</a>" : <i>[ &lt;a href=&#34;pushconfig-oidctoken.md&#34;&gt;OidcToken&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#attributes" title="Attributes">Attributes</a>: <i>
      - &lt;a href=&#34;pushconfig-attributes.md&#34;&gt;Attributes&lt;/a&gt;</i>
<a href="#pushendpoint" title="PushEndpoint">PushEndpoint</a>: <i>String</i>
<a href="#oidctoken" title="OidcToken">OidcToken</a>: <i>
      - &lt;a href=&#34;pushconfig-oidctoken.md&#34;&gt;OidcToken&lt;/a&gt;</i>
</pre>

## Properties

#### Attributes

_Required_: No
_Type_: List of &lt;a href=&#34;pushconfig-attributes.md&#34;&gt;Attributes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushEndpoint

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcToken

_Required_: No
_Type_: List of &lt;a href=&#34;pushconfig-oidctoken.md&#34;&gt;OidcToken&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

