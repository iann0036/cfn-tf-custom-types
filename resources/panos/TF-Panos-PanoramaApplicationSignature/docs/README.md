# TF::Panos::PanoramaApplicationSignature

This resource allows you to add/update/delete Panorama application signatures.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaApplicationSignature",
    "Properties" : {
        "<a href="#applicationobject" title="ApplicationObject">ApplicationObject</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#orderedmatch" title="OrderedMatch">OrderedMatch</a>" : <i>Boolean</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#andcondition" title="AndCondition">AndCondition</a>" : <i>[ <a href="andconditiondefinition.md">AndConditionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::PanoramaApplicationSignature
Properties:
    <a href="#applicationobject" title="ApplicationObject">ApplicationObject</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#orderedmatch" title="OrderedMatch">OrderedMatch</a>: <i>Boolean</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#andcondition" title="AndCondition">AndCondition</a>: <i>
      - <a href="andconditiondefinition.md">AndConditionDefinition</a></i>
</pre>

## Properties

#### ApplicationObject

The applciation object for this signature.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group (default: `shared`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The signature's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedMatch

Set to `false` to disable ordered matching
(default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

The signature's scope.  Valid values are
`transaction` (default) or `session`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AndCondition

_Required_: No

_Type_: List of <a href="andconditiondefinition.md">AndConditionDefinition</a>

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
