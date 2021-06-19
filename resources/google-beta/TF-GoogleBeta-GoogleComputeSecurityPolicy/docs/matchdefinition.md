# TF::GoogleBeta::GoogleComputeSecurityPolicy MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#versionedexpr" title="VersionedExpr">VersionedExpr</a>" : <i>String</i>,
    "<a href="#config" title="Config">Config</a>" : <i>[ <a href="configdefinition.md">ConfigDefinition</a>, ... ]</i>,
    "<a href="#expr" title="Expr">Expr</a>" : <i>[ <a href="exprdefinition.md">ExprDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#versionedexpr" title="VersionedExpr">VersionedExpr</a>: <i>String</i>
<a href="#config" title="Config">Config</a>: <i>
      - <a href="configdefinition.md">ConfigDefinition</a></i>
<a href="#expr" title="Expr">Expr</a>: <i>
      - <a href="exprdefinition.md">ExprDefinition</a></i>
</pre>

## Properties

#### VersionedExpr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: No

_Type_: List of <a href="configdefinition.md">ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expr

_Required_: No

_Type_: List of <a href="exprdefinition.md">ExprDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

