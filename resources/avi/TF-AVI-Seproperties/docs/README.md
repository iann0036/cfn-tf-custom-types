# TF::AVI::Seproperties

The SeProperties resource allows the creation and management of Avi SeProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Seproperties",
    "Properties" : {
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#seagentproperties" title="SeAgentProperties">SeAgentProperties</a>" : <i>[ <a href="seagentpropertiesdefinition.md">SeAgentPropertiesDefinition</a>, ... ]</i>,
        "<a href="#sebootupproperties" title="SeBootupProperties">SeBootupProperties</a>" : <i>[ <a href="sebootuppropertiesdefinition.md">SeBootupPropertiesDefinition</a>, ... ]</i>,
        "<a href="#seruntimeproperties" title="SeRuntimeProperties">SeRuntimeProperties</a>" : <i>[ <a href="seruntimepropertiesdefinition.md">SeRuntimePropertiesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Seproperties
Properties:
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#seagentproperties" title="SeAgentProperties">SeAgentProperties</a>: <i>
      - <a href="seagentpropertiesdefinition.md">SeAgentPropertiesDefinition</a></i>
    <a href="#sebootupproperties" title="SeBootupProperties">SeBootupProperties</a>: <i>
      - <a href="sebootuppropertiesdefinition.md">SeBootupPropertiesDefinition</a></i>
    <a href="#seruntimeproperties" title="SeRuntimeProperties">SeRuntimeProperties</a>: <i>
      - <a href="seruntimepropertiesdefinition.md">SeRuntimePropertiesDefinition</a></i>
</pre>

## Properties

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeAgentProperties

_Required_: No

_Type_: List of <a href="seagentpropertiesdefinition.md">SeAgentPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeBootupProperties

_Required_: No

_Type_: List of <a href="sebootuppropertiesdefinition.md">SeBootupPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeRuntimeProperties

_Required_: No

_Type_: List of <a href="seruntimepropertiesdefinition.md">SeRuntimePropertiesDefinition</a>

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

