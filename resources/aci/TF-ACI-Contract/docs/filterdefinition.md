# TF::ACI::Contract FilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#filtername" title="FilterName">FilterName</a>" : <i>String</i>,
    "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
    "<a href="#filterentry" title="FilterEntry">FilterEntry</a>" : <i>[ <a href="filterentrydefinition.md">FilterEntryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#filtername" title="FilterName">FilterName</a>: <i>String</i>
<a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
<a href="#filterentry" title="FilterEntry">FilterEntry</a>: <i>
      - <a href="filterentrydefinition.md">FilterEntryDefinition</a></i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterEntry

_Required_: No

_Type_: List of <a href="filterentrydefinition.md">FilterEntryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

