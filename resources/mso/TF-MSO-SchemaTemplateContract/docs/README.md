# TF::MSO::SchemaTemplateContract

CloudFormation equivalent of mso_schema_template_contract

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MSO::SchemaTemplateContract",
    "Properties" : {
        "<a href="#contractname" title="ContractName">ContractName</a>" : <i>String</i>,
        "<a href="#directives" title="Directives">Directives</a>" : <i>[ String, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#filterrelationships" title="FilterRelationships">FilterRelationships</a>" : <i>[ <a href="filterrelationshipsdefinition.md">FilterRelationshipsDefinition</a>, ... ]</i>,
        "<a href="#filtertype" title="FilterType">FilterType</a>" : <i>String</i>,
        "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MSO::SchemaTemplateContract
Properties:
    <a href="#contractname" title="ContractName">ContractName</a>: <i>String</i>
    <a href="#directives" title="Directives">Directives</a>: <i>
      - String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#filterrelationships" title="FilterRelationships">FilterRelationships</a>: <i>
      - <a href="filterrelationshipsdefinition.md">FilterRelationshipsDefinition</a></i>
    <a href="#filtertype" title="FilterType">FilterType</a>: <i>String</i>
    <a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
</pre>

## Properties

#### ContractName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Directives

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterRelationships

_Required_: Yes

_Type_: List of <a href="filterrelationshipsdefinition.md">FilterRelationshipsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: Yes

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

