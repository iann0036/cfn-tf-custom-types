# Terraform::Datadog::Dashboard TemplateVariablePreset

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>" : <i>[ <a href="templatevariablepreset-templatevariable.md">TemplateVariable</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>: <i>
      - <a href="templatevariablepreset-templatevariable.md">TemplateVariable</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVariable

_Required_: No

_Type_: List of <a href="templatevariablepreset-templatevariable.md">TemplateVariable</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

