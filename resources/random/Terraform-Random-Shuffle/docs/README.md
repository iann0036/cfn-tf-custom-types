# Terraform::Random::Shuffle

The resource `random_shuffle` generates a random permutation of a list
of strings given as an argument.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Random::Shuffle",
    "Properties" : {
        "<a href="#input" title="Input">Input</a>" : <i>[ String, ... ]</i>,
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ <a href="keepers.md">Keepers</a>, ... ]</i>,
        "<a href="#resultcount" title="ResultCount">ResultCount</a>" : <i>Double</i>,
        "<a href="#seed" title="Seed">Seed</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Random::Shuffle
Properties:
    <a href="#input" title="Input">Input</a>: <i>
      - String</i>
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - <a href="keepers.md">Keepers</a></i>
    <a href="#resultcount" title="ResultCount">ResultCount</a>: <i>Double</i>
    <a href="#seed" title="Seed">Seed</a>: <i>String</i>
</pre>

## Properties

#### Input

The list of strings to shuffle.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keepers

Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
[the main provider documentation](../index.html) for more information.

_Required_: No

_Type_: List of <a href="keepers.md">Keepers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResultCount

The number of results to return. Defaults to
the number of items in the `input` list. If fewer items are requested,
some elements will be excluded from the result. If more items are requested,
items will be repeated in the result but not more frequently than the number
of items in the input list.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Seed

Arbitrary string with which to seed the random number
generator, in order to produce less-volatile permutations of the list.
**Important:** Even with an identical seed, it is not guaranteed that the
same permutation will be produced across different versions of Terraform.
This argument causes the result to be *less volatile*, but not fixed for
all time.

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

Returns the <code>Result</code> value.

