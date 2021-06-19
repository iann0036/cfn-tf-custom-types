# TF::OCI::LoggingUnifiedAgentConfiguration SourcesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#channels" title="Channels">Channels</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#paths" title="Paths">Paths</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
    "<a href="#parser" title="Parser">Parser</a>" : <i>[ <a href="parserdefinition.md">ParserDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#channels" title="Channels">Channels</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#paths" title="Paths">Paths</a>: <i>
      - String</i>
<a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
<a href="#parser" title="Parser">Parser</a>: <i>
      - <a href="parserdefinition.md">ParserDefinition</a></i>
</pre>

## Properties

#### Channels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Paths

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parser

_Required_: No

_Type_: List of <a href="parserdefinition.md">ParserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

