# Terraform::Random::Id

CloudFormation equivalent of random_id

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

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keepers

_Required_: No

_Type_: List of <a href="keepers.md">Keepers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

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

