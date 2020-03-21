# Terraform::Random::Id

The resource `random_id` generates random numbers that are intended to be
used as unique identifiers for other resources.

This resource *does* use a cryptographic random number generator in order
to minimize the chance of collisions, making the results of this resource
when a 16-byte identifier is requested of equivalent uniqueness to a
type-4 UUID.

This resource can be used in conjunction with resources that have
the `create_before_destroy` lifecycle flag set to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Random::Id",
    "Properties" : {
        "<a href="#bytelength" title="ByteLength">ByteLength</a>" : <i>Double</i>,
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ <a href="keepers.md">Keepers</a>, ... ]</i>,
        "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Random::Id
Properties:
    <a href="#bytelength" title="ByteLength">ByteLength</a>: <i>Double</i>
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - <a href="keepers.md">Keepers</a></i>
    <a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
</pre>

## Properties

#### ByteLength

The number of random bytes to produce. The
minimum value is 1, which produces eight bits of randomness.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keepers

Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
[the main provider documentation](../index.html) for more information.

_Required_: No

_Type_: List of <a href="keepers.md">Keepers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

Arbitrary string to prefix the output value with. This
string is supplied as-is, meaning it is not guaranteed to be URL-safe or
base64 encoded.

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

#### B64

Returns the <code>B64</code> value.

#### B64Std

Returns the <code>B64Std</code> value.

#### B64Url

Returns the <code>B64Url</code> value.

#### Dec

Returns the <code>Dec</code> value.

#### Hex

Returns the <code>Hex</code> value.

