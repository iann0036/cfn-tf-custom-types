# TF::AWS::LexSlotType

Provides an Amazon Lex Slot Type resource. For more information see
[Amazon Lex: How It Works](https://docs.aws.amazon.com/lex/latest/dg/how-it-works.html)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LexSlotType",
    "Properties" : {
        "<a href="#createversion" title="CreateVersion">CreateVersion</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#valueselectionstrategy" title="ValueSelectionStrategy">ValueSelectionStrategy</a>" : <i>String</i>,
        "<a href="#enumerationvalue" title="EnumerationValue">EnumerationValue</a>" : <i>[ <a href="enumerationvaluedefinition.md">EnumerationValueDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LexSlotType
Properties:
    <a href="#createversion" title="CreateVersion">CreateVersion</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#valueselectionstrategy" title="ValueSelectionStrategy">ValueSelectionStrategy</a>: <i>String</i>
    <a href="#enumerationvalue" title="EnumerationValue">EnumerationValue</a>: <i>
      - <a href="enumerationvaluedefinition.md">EnumerationValueDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CreateVersion

Determines if a new slot type version is created when the initial resource is created and on each
update. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the slot type. Must be less than or equal to 200 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the slot type. The name is not case sensitive. Must be less than or equal to 100 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSelectionStrategy

Determines the slot resolution strategy that Amazon Lex
uses to return slot type values. `ORIGINAL_VALUE` returns the value entered by the user if the user
value is similar to the slot value. `TOP_RESOLUTION` returns the first value in the resolution list
if there is a resolution list for the slot, otherwise null is returned. Defaults to `ORIGINAL_VALUE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnumerationValue

_Required_: No

_Type_: List of <a href="enumerationvaluedefinition.md">EnumerationValueDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Checksum

Returns the <code>Checksum</code> value.

#### CreatedDate

Returns the <code>CreatedDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdatedDate

Returns the <code>LastUpdatedDate</code> value.

#### Version

Returns the <code>Version</code> value.

