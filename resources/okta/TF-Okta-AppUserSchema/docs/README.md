# TF::Okta::AppUserSchema

Creates an Application User Schema property.

This resource allows you to create and configure a custom user schema property and associate it with an application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::AppUserSchema",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#arrayenum" title="ArrayEnum">ArrayEnum</a>" : <i>[ String, ... ]</i>,
        "<a href="#arraytype" title="ArrayType">ArrayType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enum" title="Enum">Enum</a>" : <i>[ String, ... ]</i>,
        "<a href="#externalname" title="ExternalName">ExternalName</a>" : <i>String</i>,
        "<a href="#externalnamespace" title="ExternalNamespace">ExternalNamespace</a>" : <i>String</i>,
        "<a href="#index" title="Index">Index</a>" : <i>String</i>,
        "<a href="#master" title="Master">Master</a>" : <i>String</i>,
        "<a href="#maxlength" title="MaxLength">MaxLength</a>" : <i>Double</i>,
        "<a href="#minlength" title="MinLength">MinLength</a>" : <i>Double</i>,
        "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>String</i>,
        "<a href="#required" title="Required">Required</a>" : <i>Boolean</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#union" title="Union">Union</a>" : <i>Boolean</i>,
        "<a href="#unique" title="Unique">Unique</a>" : <i>String</i>,
        "<a href="#usertype" title="UserType">UserType</a>" : <i>String</i>,
        "<a href="#arrayoneof" title="ArrayOneOf">ArrayOneOf</a>" : <i>[ <a href="arrayoneofdefinition.md">ArrayOneOfDefinition</a>, ... ]</i>,
        "<a href="#oneof" title="OneOf">OneOf</a>" : <i>[ <a href="oneofdefinition.md">OneOfDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::AppUserSchema
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#arrayenum" title="ArrayEnum">ArrayEnum</a>: <i>
      - String</i>
    <a href="#arraytype" title="ArrayType">ArrayType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enum" title="Enum">Enum</a>: <i>
      - String</i>
    <a href="#externalname" title="ExternalName">ExternalName</a>: <i>String</i>
    <a href="#externalnamespace" title="ExternalNamespace">ExternalNamespace</a>: <i>String</i>
    <a href="#index" title="Index">Index</a>: <i>String</i>
    <a href="#master" title="Master">Master</a>: <i>String</i>
    <a href="#maxlength" title="MaxLength">MaxLength</a>: <i>Double</i>
    <a href="#minlength" title="MinLength">MinLength</a>: <i>Double</i>
    <a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>String</i>
    <a href="#required" title="Required">Required</a>: <i>Boolean</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#union" title="Union">Union</a>: <i>Boolean</i>
    <a href="#unique" title="Unique">Unique</a>: <i>String</i>
    <a href="#usertype" title="UserType">UserType</a>: <i>String</i>
    <a href="#arrayoneof" title="ArrayOneOf">ArrayOneOf</a>: <i>
      - <a href="arrayoneofdefinition.md">ArrayOneOfDefinition</a></i>
    <a href="#oneof" title="OneOf">OneOf</a>: <i>
      - <a href="oneofdefinition.md">OneOfDefinition</a></i>
</pre>

## Properties

#### AppId

The Application's ID the user custom schema property should be assigned to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArrayEnum

Array of values that an array property's items can be set to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArrayType

The type of the array elements if `type` is set to `"array"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the user schema property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enum

Array of values a primitive property can be set to. See `array_enum` for arrays.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalName

External name of the user schema property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNamespace

External namespace of the user schema property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

The property name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Master

Master priority for the user schema property. It can be set to `"PROFILE_MASTER"` or `"OKTA"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLength

The maximum length of the user property value. Only applies to type `"string"`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinLength

The minimum length of the user property value. Only applies to type `"string"`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

Access control permissions for the property. It can be set to `"READ_WRITE"`, `"READ_ONLY"`, `"HIDE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Required

Whether the property is required for this application's users.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

determines whether an app user attribute can be set at the Individual or Group Level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

display name for the enum value.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the schema property. It can be `"string"`, `"boolean"`, `"number"`, `"integer"`, `"array"`, or `"object"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Union

Used to assign attribute group priority. Can not be set to 'true' if `scope` is set to Individual level.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unique

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArrayOneOf

_Required_: No

_Type_: List of <a href="arrayoneofdefinition.md">ArrayOneOfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OneOf

_Required_: No

_Type_: List of <a href="oneofdefinition.md">OneOfDefinition</a>

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

