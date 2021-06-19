# TF::SumoLogic::Collector

Provides a [Sumologic (Hosted) Collector][1].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SumoLogic::Collector",
    "Properties" : {
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#fields" title="Fields">Fields</a>" : <i>[ <a href="fieldsdefinition.md">FieldsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SumoLogic::Collector
Properties:
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#fields" title="Fields">Fields</a>: <i>
      - <a href="fieldsdefinition.md">FieldsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
</pre>

## Properties

#### Category

The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
* `timezone` - (Optional) The time zone to use for this collector. The value follows the [tzdata][2] naming convention.
* `fields` - (Optional) Map containing [key/value pairs][3].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the collector.
* `category` - (Optional) The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
* `timezone` - (Optional) The time zone to use for this collector. The value follows the [tzdata][2] naming convention.
* `fields` - (Optional) Map containing [key/value pairs][3].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fields

Map containing [key/value pairs][3].

_Required_: No

_Type_: List of <a href="fieldsdefinition.md">FieldsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the collector. This is required, and has to be unique. Changing this will force recreation the collector.
* `description` - (Optional) The description of the collector.
* `category` - (Optional) The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
* `timezone` - (Optional) The time zone to use for this collector. The value follows the [tzdata][2] naming convention.
* `fields` - (Optional) Map containing [key/value pairs][3].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

The time zone to use for this collector. The value follows the [tzdata][2] naming convention.
* `fields` - (Optional) Map containing [key/value pairs][3].

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

#### Id

Returns the <code>Id</code> value.

