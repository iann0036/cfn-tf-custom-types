# Terraform::Google::ComputeSecurityPolicy Match

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#versionedexpr" title="VersionedExpr">VersionedExpr</a>" : <i>String</i>,
    "<a href="#config" title="Config">Config</a>" : <i>[ &lt;a href=&#34;match-config.md&#34;&gt;Config&lt;/a&gt;, ... ]</i>,
    "<a href="#expr" title="Expr">Expr</a>" : <i>[ &lt;a href=&#34;match-expr.md&#34;&gt;Expr&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#versionedexpr" title="VersionedExpr">VersionedExpr</a>: <i>String</i>
<a href="#config" title="Config">Config</a>: <i>
      - &lt;a href=&#34;match-config.md&#34;&gt;Config&lt;/a&gt;</i>
<a href="#expr" title="Expr">Expr</a>: <i>
      - &lt;a href=&#34;match-expr.md&#34;&gt;Expr&lt;/a&gt;</i>
</pre>

## Properties

#### VersionedExpr

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: No
_Type_: List of &lt;a href=&#34;match-config.md&#34;&gt;Config&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expr

_Required_: No
_Type_: List of &lt;a href=&#34;match-expr.md&#34;&gt;Expr&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

