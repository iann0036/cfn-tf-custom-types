# Terraform::AWS::AppmeshRoute Match

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exact" title="Exact">Exact</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#regex" title="Regex">Regex</a>" : <i>String</i>,
    "<a href="#suffix" title="Suffix">Suffix</a>" : <i>String</i>,
    "<a href="#range" title="Range">Range</a>" : <i>[ <a href="match-range.md">Range</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exact" title="Exact">Exact</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#regex" title="Regex">Regex</a>: <i>String</i>
<a href="#suffix" title="Suffix">Suffix</a>: <i>String</i>
<a href="#range" title="Range">Range</a>: <i>
      - <a href="match-range.md">Range</a></i>
</pre>

## Properties

#### Exact

The header value sent by the client must match the specified value exactly.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

The header value sent by the client must begin with the specified characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regex

The header value sent by the client must include the specified characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suffix

The header value sent by the client must end with the specified characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

_Required_: No

_Type_: List of <a href="match-range.md">Range</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

