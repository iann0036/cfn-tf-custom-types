# TF::Okta::TemplateSms

Creates an Okta SMS Template.

This resource allows you to create and configure an Okta SMS Template.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::TemplateSms",
    "Properties" : {
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#translations" title="Translations">Translations</a>" : <i>[ <a href="translationsdefinition.md">TranslationsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::TemplateSms
Properties:
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#translations" title="Translations">Translations</a>: <i>
      - <a href="translationsdefinition.md">TranslationsDefinition</a></i>
</pre>

## Properties

#### Template

The SMS message.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

SMS template type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Translations

_Required_: No

_Type_: List of <a href="translationsdefinition.md">TranslationsDefinition</a>

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

