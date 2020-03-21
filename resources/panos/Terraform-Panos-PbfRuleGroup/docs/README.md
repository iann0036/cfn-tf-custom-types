# Terraform::Panos::PbfRuleGroup

CloudFormation equivalent of panos_pbf_rule_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PbfRuleGroup",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>" : <i>String</i>,
        "<a href="#positionreference" title="PositionReference">PositionReference</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;, ... ]</i>,
        "<a href="#forwarding" title="Forwarding">Forwarding</a>" : <i>[ &lt;a href=&#34;forwarding.md&#34;&gt;Forwarding&lt;/a&gt;, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;, ... ]</i>,
        "<a href="#monitor" title="Monitor">Monitor</a>" : <i>[ &lt;a href=&#34;monitor.md&#34;&gt;Monitor&lt;/a&gt;, ... ]</i>,
        "<a href="#symmetricreturn" title="SymmetricReturn">SymmetricReturn</a>" : <i>[ &lt;a href=&#34;symmetricreturn.md&#34;&gt;SymmetricReturn&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PbfRuleGroup
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>: <i>String</i>
    <a href="#positionreference" title="PositionReference">PositionReference</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;</i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;</i>
    <a href="#forwarding" title="Forwarding">Forwarding</a>: <i>
      - &lt;a href=&#34;forwarding.md&#34;&gt;Forwarding&lt;/a&gt;</i>
    <a href="#source" title="Source">Source</a>: <i>
      - &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;</i>
    <a href="#monitor" title="Monitor">Monitor</a>: <i>
      - &lt;a href=&#34;monitor.md&#34;&gt;Monitor&lt;/a&gt;</i>
    <a href="#symmetricreturn" title="SymmetricReturn">SymmetricReturn</a>: <i>
      - &lt;a href=&#34;symmetricreturn.md&#34;&gt;SymmetricReturn&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PositionKeyword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PositionReference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forwarding

_Required_: No

_Type_: List of &lt;a href=&#34;forwarding.md&#34;&gt;Forwarding&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No

_Type_: List of &lt;a href=&#34;monitor.md&#34;&gt;Monitor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SymmetricReturn

_Required_: No

_Type_: List of &lt;a href=&#34;symmetricreturn.md&#34;&gt;SymmetricReturn&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

