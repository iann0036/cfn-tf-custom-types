# Terraform::Random::String

The resource `random_string` generates a random permutation of alphanumeric
characters and optionally special characters.

This resource *does* use a cryptographic random number generator.

Historically this resource's intended usage has been ambiguous as the original example
used it in a password. For backwards compatibility it will
continue to exist. For unique ids please use [random_id](id.html), for sensitive
random values please use [random_password](password.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Random::String",
    "Properties" : {
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ <a href="keepers.md">Keepers</a>, ... ]</i>,
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
Type: Terraform::Random::String
Properties:
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - <a href="keepers.md">Keepers</a></i>
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

#### Keepers

Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
[the main provider documentation](../index.html) for more information.

_Required_: No

_Type_: List of <a href="keepers.md">Keepers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Length

The length of the string desired.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lower

(default true) Include lowercase alphabet characters
in random string.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinLower

(default 0) Minimum number of lowercase alphabet
characters in random string.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNumeric

(default 0) Minimum number of numeric characters
in random string.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSpecial

(default 0) Minimum number of special characters
in random string.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinUpper

(default 0) Minimum number of uppercase alphabet
characters in random string.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Number

(default true) Include numeric characters in random
string.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideSpecial

Supply your own list of special characters to
use for string generation.  This overrides the default character list in the special
argument.  The special argument must still be set to true for any overwritten
characters to be used in generation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Special

(default true) Include special characters in random
string. These are `!@#$%&*()-_=+[]{}<>:?`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upper

(default true) Include uppercase alphabet characters
in random string.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Result

Returns the <code>Result</code> value.

