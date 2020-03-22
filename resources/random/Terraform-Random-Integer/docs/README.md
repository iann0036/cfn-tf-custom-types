# Terraform::Random::Integer

The resource `random_integer` generates random values from a given range, described by the `min` and `max` attributes of a given resource.

This resource can be used in conjunction with resources that have
the `create_before_destroy` lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Random::Integer",
    "Properties" : {
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ <a href="keepers.md">Keepers</a>, ... ]</i>,
        "<a href="#max" title="Max">Max</a>" : <i>Double</i>,
        "<a href="#min" title="Min">Min</a>" : <i>Double</i>,
        "<a href="#seed" title="Seed">Seed</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Random::Integer
Properties:
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - <a href="keepers.md">Keepers</a></i>
    <a href="#max" title="Max">Max</a>: <i>Double</i>
    <a href="#min" title="Min">Min</a>: <i>Double</i>
    <a href="#seed" title="Seed">Seed</a>: <i>String</i>
</pre>

## Properties

#### Keepers

Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
[the main provider documentation](../index.html) for more information.

_Required_: No

_Type_: List of <a href="keepers.md">Keepers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Max

The maximum inclusive value of the range.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Min

The minimum inclusive value of the range.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Seed

A custom seed to always produce the same value.

_Required_: No

_Type_: String

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

