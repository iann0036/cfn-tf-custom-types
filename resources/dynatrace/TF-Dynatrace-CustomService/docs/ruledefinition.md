# TF::Dynatrace::CustomService RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ String, ... ]</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#class" title="Class">Class</a>" : <i>[ <a href="classdefinition.md">ClassDefinition</a>, ... ]</i>,
    "<a href="#file" title="File">File</a>" : <i>[ <a href="filedefinition.md">FileDefinition</a>, ... ]</i>,
    "<a href="#method" title="Method">Method</a>" : <i>[ <a href="methoddefinition.md">MethodDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#annotations" title="Annotations">Annotations</a>: <i>
      - String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#class" title="Class">Class</a>: <i>
      - <a href="classdefinition.md">ClassDefinition</a></i>
<a href="#file" title="File">File</a>: <i>
      - <a href="filedefinition.md">FileDefinition</a></i>
<a href="#method" title="Method">Method</a>: <i>
      - <a href="methoddefinition.md">MethodDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Class

_Required_: No

_Type_: List of <a href="classdefinition.md">ClassDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### File

_Required_: No

_Type_: List of <a href="filedefinition.md">FileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: List of <a href="methoddefinition.md">MethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

