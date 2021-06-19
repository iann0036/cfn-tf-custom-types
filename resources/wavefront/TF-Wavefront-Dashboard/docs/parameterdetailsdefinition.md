# TF::Wavefront::Dashboard ParameterDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>" : <i>String</i>,
    "<a href="#dynamicfieldtype" title="DynamicFieldType">DynamicFieldType</a>" : <i>String</i>,
    "<a href="#hidefromview" title="HideFromView">HideFromView</a>" : <i>Boolean</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#parametertype" title="ParameterType">ParameterType</a>" : <i>String</i>,
    "<a href="#queryvalue" title="QueryValue">QueryValue</a>" : <i>String</i>,
    "<a href="#tagkey" title="TagKey">TagKey</a>" : <i>String</i>,
    "<a href="#valuestoreadablestrings" title="ValuesToReadableStrings">ValuesToReadableStrings</a>" : <i>[ <a href="valuestoreadablestringsdefinition.md">ValuesToReadableStringsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>: <i>String</i>
<a href="#dynamicfieldtype" title="DynamicFieldType">DynamicFieldType</a>: <i>String</i>
<a href="#hidefromview" title="HideFromView">HideFromView</a>: <i>Boolean</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#parametertype" title="ParameterType">ParameterType</a>: <i>String</i>
<a href="#queryvalue" title="QueryValue">QueryValue</a>: <i>String</i>
<a href="#tagkey" title="TagKey">TagKey</a>: <i>String</i>
<a href="#valuestoreadablestrings" title="ValuesToReadableStrings">ValuesToReadableStrings</a>: <i>
      - <a href="valuestoreadablestringsdefinition.md">ValuesToReadableStringsDefinition</a></i>
</pre>

## Properties

#### DefaultValue

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicFieldType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideFromView

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValuesToReadableStrings

_Required_: Yes

_Type_: List of <a href="valuestoreadablestringsdefinition.md">ValuesToReadableStringsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

