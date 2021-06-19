# TF::NS1::Record

Provides a NS1 Record resource. This can be used to create, modify, and delete records.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NS1::Record",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#link" title="Link">Link</a>" : <i>String</i>,
        "<a href="#meta" title="Meta">Meta</a>" : <i>[ <a href="metadefinition.md">MetaDefinition</a>, ... ]</i>,
        "<a href="#shortanswers" title="ShortAnswers">ShortAnswers</a>" : <i>[ String, ... ]</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#useclientsubnet" title="UseClientSubnet">UseClientSubnet</a>" : <i>Boolean</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#answers" title="Answers">Answers</a>" : <i>[ <a href="answersdefinition.md">AnswersDefinition</a>, ... ]</i>,
        "<a href="#filters" title="Filters">Filters</a>" : <i>[ <a href="filtersdefinition.md">FiltersDefinition</a>, ... ]</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ <a href="regionsdefinition.md">RegionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NS1::Record
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#link" title="Link">Link</a>: <i>String</i>
    <a href="#meta" title="Meta">Meta</a>: <i>
      - <a href="metadefinition.md">MetaDefinition</a></i>
    <a href="#shortanswers" title="ShortAnswers">ShortAnswers</a>: <i>
      - String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#useclientsubnet" title="UseClientSubnet">UseClientSubnet</a>: <i>Boolean</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#answers" title="Answers">Answers</a>: <i>
      - <a href="answersdefinition.md">AnswersDefinition</a></i>
    <a href="#filters" title="Filters">Filters</a>: <i>
      - <a href="filtersdefinition.md">FiltersDefinition</a></i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - <a href="regionsdefinition.md">RegionsDefinition</a></i>
</pre>

## Properties

#### Domain

The records' domain. Cannot have leading or trailing
dots - see the example above and `FQDN formatting` below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Link

The target record to link to. This means this record is a
'linked' record, and it inherits all properties from its target.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Meta

_Required_: No

_Type_: List of <a href="metadefinition.md">MetaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortAnswers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The records' time to live (in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The records' RR type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseClientSubnet

Whether to use EDNS client subnet data when
available(in filter chain).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The zone the record belongs to. Cannot have leading or
trailing dots (".") - see the example above and `FQDN formatting` below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Answers

_Required_: No

_Type_: List of <a href="answersdefinition.md">AnswersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filters

_Required_: No

_Type_: List of <a href="filtersdefinition.md">FiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

_Required_: No

_Type_: List of <a href="regionsdefinition.md">RegionsDefinition</a>

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

