# TF::Panos::CustomDataPatternObject RegexDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filetypes" title="FileTypes">FileTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#regex" title="Regex">Regex</a>" : <i>[ <a href="regexdefinition.md">RegexDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#filetypes" title="FileTypes">FileTypes</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#regex" title="Regex">Regex</a>: <i>
      - <a href="regexdefinition.md">RegexDefinition</a></i>
</pre>

## Properties

#### FileTypes

List of file types.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regex

_Required_: Yes

_Type_: List of <a href="regexdefinition.md">RegexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

