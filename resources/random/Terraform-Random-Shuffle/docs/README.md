# Terraform::Random::Shuffle

CloudFormation equivalent of random_shuffle

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Random::Shuffle",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#input" title="Input">Input</a>" : <i>[ String, ... ]</i>,
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ &lt;a href=&#34;keepers.md&#34;&gt;Keepers&lt;/a&gt;, ... ]</i>,
        "<a href="#result" title="Result">Result</a>" : <i>[ String, ... ]</i>,
        "<a href="#resultcount" title="ResultCount">ResultCount</a>" : <i>Double</i>,
        "<a href="#seed" title="Seed">Seed</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Random::Shuffle
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#input" title="Input">Input</a>: <i>
      - String</i>
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - &lt;a href=&#34;keepers.md&#34;&gt;Keepers&lt;/a&gt;</i>
    <a href="#result" title="Result">Result</a>: <i>
      - String</i>
    <a href="#resultcount" title="ResultCount">ResultCount</a>: <i>Double</i>
    <a href="#seed" title="Seed">Seed</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Input

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keepers

_Required_: No

_Type_: List of &lt;a href=&#34;keepers.md&#34;&gt;Keepers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Result

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResultCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Seed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Result

Returns the &lt;code&gt;Result&lt;/code&gt; value.

