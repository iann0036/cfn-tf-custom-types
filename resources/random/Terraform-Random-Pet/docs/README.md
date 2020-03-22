# Terraform::Random::Pet

The resource `random_pet` generates random pet names that are intended to be
used as unique identifiers for other resources.

This resource can be used in conjunction with resources that have
the `create_before_destroy` lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Random::Pet",
    "Properties" : {
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ <a href="keepers.md">Keepers</a>, ... ]</i>,
        "<a href="#length" title="Length">Length</a>" : <i>Double</i>,
        "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
        "<a href="#separator" title="Separator">Separator</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Random::Pet
Properties:
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - <a href="keepers.md">Keepers</a></i>
    <a href="#length" title="Length">Length</a>: <i>Double</i>
    <a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
    <a href="#separator" title="Separator">Separator</a>: <i>String</i>
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

The length (in words) of the pet name.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

A string to prefix the name with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Separator

The character to separate words in the pet name.

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

