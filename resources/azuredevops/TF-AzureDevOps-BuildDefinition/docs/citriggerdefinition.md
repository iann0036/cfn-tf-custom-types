# TF::AzureDevOps::BuildDefinition CiTriggerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#useyaml" title="UseYaml">UseYaml</a>" : <i>Boolean</i>,
    "<a href="#override" title="Override">Override</a>" : <i>[ <a href="overridedefinition.md">OverrideDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#useyaml" title="UseYaml">UseYaml</a>: <i>Boolean</i>
<a href="#override" title="Override">Override</a>: <i>
      - <a href="overridedefinition.md">OverrideDefinition</a></i>
</pre>

## Properties

#### UseYaml

Use the azure-pipeline file for the build configuration. Defaults to `false`.
- `override` - (Optional) Override the azure-pipeline file and use a this configuration for all builds.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

_Required_: No

_Type_: List of <a href="overridedefinition.md">OverrideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

