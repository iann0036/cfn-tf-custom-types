# TF::Okta::TemplateEmail

Creates an Okta Email Template.

This resource allows you to create and configure an Okta Email Template.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::TemplateEmail",
    "Properties" : {
        "<a href="#defaultlanguage" title="DefaultLanguage">DefaultLanguage</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#translations" title="Translations">Translations</a>" : <i>[ <a href="translationsdefinition.md">TranslationsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::TemplateEmail
Properties:
    <a href="#defaultlanguage" title="DefaultLanguage">DefaultLanguage</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#translations" title="Translations">Translations</a>: <i>
      - <a href="translationsdefinition.md">TranslationsDefinition</a></i>
</pre>

## Properties

#### DefaultLanguage

The default language, by default is set to `"en"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Email template type.

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

