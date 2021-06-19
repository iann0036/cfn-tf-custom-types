# TF::ACI::Rest

CloudFormation equivalent of aci_rest

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::Rest",
    "Properties" : {
        "<a href="#classname" title="ClassName">ClassName</a>" : <i>String</i>,
        "<a href="#content" title="Content">Content</a>" : <i>[ <a href="contentdefinition.md">ContentDefinition</a>, ... ]</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#payload" title="Payload">Payload</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::Rest
Properties:
    <a href="#classname" title="ClassName">ClassName</a>: <i>String</i>
    <a href="#content" title="Content">Content</a>: <i>
      - <a href="contentdefinition.md">ContentDefinition</a></i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#payload" title="Payload">Payload</a>: <i>String</i>
</pre>

## Properties

#### ClassName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

_Required_: No

_Type_: List of <a href="contentdefinition.md">ContentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Payload

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

#### Dn

Returns the <code>Dn</code> value.

#### Id

Returns the <code>Id</code> value.

