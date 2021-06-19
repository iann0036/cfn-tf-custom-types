# TF::GoogleBeta::GoogleDataLossPreventionStoredInfoType

CloudFormation equivalent of google_data_loss_prevention_stored_info_type

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleDataLossPreventionStoredInfoType",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#dictionary" title="Dictionary">Dictionary</a>" : <i>[ <a href="dictionarydefinition.md">DictionaryDefinition</a>, ... ]</i>,
        "<a href="#largecustomdictionary" title="LargeCustomDictionary">LargeCustomDictionary</a>" : <i>[ <a href="largecustomdictionarydefinition.md">LargeCustomDictionaryDefinition</a>, ... ]</i>,
        "<a href="#regex" title="Regex">Regex</a>" : <i>[ <a href="regexdefinition.md">RegexDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleDataLossPreventionStoredInfoType
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#dictionary" title="Dictionary">Dictionary</a>: <i>
      - <a href="dictionarydefinition.md">DictionaryDefinition</a></i>
    <a href="#largecustomdictionary" title="LargeCustomDictionary">LargeCustomDictionary</a>: <i>
      - <a href="largecustomdictionarydefinition.md">LargeCustomDictionaryDefinition</a></i>
    <a href="#regex" title="Regex">Regex</a>: <i>
      - <a href="regexdefinition.md">RegexDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dictionary

_Required_: No

_Type_: List of <a href="dictionarydefinition.md">DictionaryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LargeCustomDictionary

_Required_: No

_Type_: List of <a href="largecustomdictionarydefinition.md">LargeCustomDictionaryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regex

_Required_: No

_Type_: List of <a href="regexdefinition.md">RegexDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

