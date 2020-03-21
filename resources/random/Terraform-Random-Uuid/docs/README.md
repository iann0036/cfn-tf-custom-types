# Terraform::Random::Uuid

The resource `random_uuid` generates random uuid string that is intended to be
used as unique identifiers for other resources.

This resource uses the `hashicorp/go-uuid` to generate a UUID-formatted string
for use with services needed a unique string identifier.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Random::Uuid",
    "Properties" : {
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ <a href="keepers.md">Keepers</a>, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Random::Uuid
Properties:
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - <a href="keepers.md">Keepers</a></i>
</pre>

## Properties

#### Keepers

Arbitrary map of values that, when changed, will
trigger a new uuid to be generated. See
[the main provider documentation](../index.html) for more information.

_Required_: No

_Type_: List of <a href="keepers.md">Keepers</a>

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

