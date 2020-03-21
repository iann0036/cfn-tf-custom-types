# Terraform::Circonus::RuleSetGroup

CloudFormation equivalent of circonus_rule_set_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Circonus::RuleSetGroup",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;, ... ]</i>,
        "<a href="#formula" title="Formula">Formula</a>" : <i>[ &lt;a href=&#34;formula.md&#34;&gt;Formula&lt;/a&gt;, ... ]</i>,
        "<a href="#notify" title="Notify">Notify</a>" : <i>[ &lt;a href=&#34;notify.md&#34;&gt;Notify&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Circonus::RuleSetGroup
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;</i>
    <a href="#formula" title="Formula">Formula</a>: <i>
      - &lt;a href=&#34;formula.md&#34;&gt;Formula&lt;/a&gt;</i>
    <a href="#notify" title="Notify">Notify</a>: <i>
      - &lt;a href=&#34;notify.md&#34;&gt;Notify&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Formula

_Required_: No

_Type_: List of &lt;a href=&#34;formula.md&#34;&gt;Formula&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notify

_Required_: No

_Type_: List of &lt;a href=&#34;notify.md&#34;&gt;Notify&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

