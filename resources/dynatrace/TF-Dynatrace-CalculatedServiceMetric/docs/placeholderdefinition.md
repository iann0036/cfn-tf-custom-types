# TF::Dynatrace::CalculatedServiceMetric PlaceholderDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aggregation" title="Aggregation">Aggregation</a>" : <i>String</i>,
    "<a href="#attribute" title="Attribute">Attribute</a>" : <i>String</i>,
    "<a href="#delimiterorregex" title="DelimiterOrRegex">DelimiterOrRegex</a>" : <i>String</i>,
    "<a href="#enddelimiter" title="EndDelimiter">EndDelimiter</a>" : <i>String</i>,
    "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#normalization" title="Normalization">Normalization</a>" : <i>String</i>,
    "<a href="#requestattribute" title="RequestAttribute">RequestAttribute</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#usefromchildcalls" title="UseFromChildCalls">UseFromChildCalls</a>" : <i>Boolean</i>,
    "<a href="#source" title="Source">Source</a>" : <i>[ <a href="sourcedefinition.md">SourceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aggregation" title="Aggregation">Aggregation</a>: <i>String</i>
<a href="#attribute" title="Attribute">Attribute</a>: <i>String</i>
<a href="#delimiterorregex" title="DelimiterOrRegex">DelimiterOrRegex</a>: <i>String</i>
<a href="#enddelimiter" title="EndDelimiter">EndDelimiter</a>: <i>String</i>
<a href="#kind" title="Kind">Kind</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#normalization" title="Normalization">Normalization</a>: <i>String</i>
<a href="#requestattribute" title="RequestAttribute">RequestAttribute</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#usefromchildcalls" title="UseFromChildCalls">UseFromChildCalls</a>: <i>Boolean</i>
<a href="#source" title="Source">Source</a>: <i>
      - <a href="sourcedefinition.md">SourceDefinition</a></i>
</pre>

## Properties

#### Aggregation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attribute

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelimiterOrRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndDelimiter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kind

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Normalization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseFromChildCalls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="sourcedefinition.md">SourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

