# TF::Panos::UrlFilteringSecurityProfile HttpHeaderInsertionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ <a href="httpheaderdefinition.md">HttpHeaderDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - <a href="httpheaderdefinition.md">HttpHeaderDefinition</a></i>
</pre>

## Properties

#### Domains

Header domains.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Header type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No

_Type_: List of <a href="httpheaderdefinition.md">HttpHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

