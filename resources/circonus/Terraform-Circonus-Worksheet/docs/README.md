# Terraform::Circonus::Worksheet

The ``circonus_worksheet`` resource creates and manages a
[Circonus Worksheet](https://login.circonus.com/resources/api/calls/worksheet).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Circonus::Worksheet",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#favourite" title="Favourite">Favourite</a>" : <i>Boolean</i>,
        "<a href="#graphs" title="Graphs">Graphs</a>" : <i>[ String, ... ]</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#smartqueries" title="SmartQueries">SmartQueries</a>" : <i>[ <a href="smartqueries.md">SmartQueries</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Circonus::Worksheet
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#favourite" title="Favourite">Favourite</a>: <i>Boolean</i>
    <a href="#graphs" title="Graphs">Graphs</a>: <i>
      - String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#smartqueries" title="SmartQueries">SmartQueries</a>: <i>
      - <a href="smartqueries.md">SmartQueries</a></i>
</pre>

## Properties

#### Description

Description of what the worksheet is for.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Favourite

Mark (star) this worksheet as a favorite. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Graphs

A list of graphs that compose this worksheet.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

A place to store notes about this worksheet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags assigned to this worksheet.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

The title of the worksheet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmartQueries

_Required_: No

_Type_: List of <a href="smartqueries.md">SmartQueries</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

