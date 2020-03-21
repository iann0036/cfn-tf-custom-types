# Terraform::Random::Password

CloudFormation equivalent of random_password

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Random::Password",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ &lt;a href=&#34;keepers.md&#34;&gt;Keepers&lt;/a&gt;, ... ]</i>,
        "<a href="#length" title="Length">Length</a>" : <i>Double</i>,
        "<a href="#lower" title="Lower">Lower</a>" : <i>Boolean</i>,
        "<a href="#minlower" title="MinLower">MinLower</a>" : <i>Double</i>,
        "<a href="#minnumeric" title="MinNumeric">MinNumeric</a>" : <i>Double</i>,
        "<a href="#minspecial" title="MinSpecial">MinSpecial</a>" : <i>Double</i>,
        "<a href="#minupper" title="MinUpper">MinUpper</a>" : <i>Double</i>,
        "<a href="#number" title="Number">Number</a>" : <i>Boolean</i>,
        "<a href="#overridespecial" title="OverrideSpecial">OverrideSpecial</a>" : <i>String</i>,
        "<a href="#special" title="Special">Special</a>" : <i>Boolean</i>,
        "<a href="#upper" title="Upper">Upper</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Random::Password
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - &lt;a href=&#34;keepers.md&#34;&gt;Keepers&lt;/a&gt;</i>
    <a href="#length" title="Length">Length</a>: <i>Double</i>
    <a href="#lower" title="Lower">Lower</a>: <i>Boolean</i>
    <a href="#minlower" title="MinLower">MinLower</a>: <i>Double</i>
    <a href="#minnumeric" title="MinNumeric">MinNumeric</a>: <i>Double</i>
    <a href="#minspecial" title="MinSpecial">MinSpecial</a>: <i>Double</i>
    <a href="#minupper" title="MinUpper">MinUpper</a>: <i>Double</i>
    <a href="#number" title="Number">Number</a>: <i>Boolean</i>
    <a href="#overridespecial" title="OverrideSpecial">OverrideSpecial</a>: <i>String</i>
    <a href="#special" title="Special">Special</a>: <i>Boolean</i>
    <a href="#upper" title="Upper">Upper</a>: <i>Boolean</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keepers

_Required_: No

_Type_: List of &lt;a href=&#34;keepers.md&#34;&gt;Keepers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Length

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lower

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinLower

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNumeric

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSpecial

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinUpper

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Number

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideSpecial

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Special

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upper

_Required_: No

_Type_: Boolean

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

