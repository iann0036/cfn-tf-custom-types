# TF::Google::DataLossPreventionJobTrigger InspectJobDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inspecttemplatename" title="InspectTemplateName">InspectTemplateName</a>" : <i>String</i>,
    "<a href="#actions" title="Actions">Actions</a>" : <i>[ <a href="actionsdefinition.md">ActionsDefinition</a>, ... ]</i>,
    "<a href="#storageconfig" title="StorageConfig">StorageConfig</a>" : <i>[ <a href="storageconfigdefinition.md">StorageConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#inspecttemplatename" title="InspectTemplateName">InspectTemplateName</a>: <i>String</i>
<a href="#actions" title="Actions">Actions</a>: <i>
      - <a href="actionsdefinition.md">ActionsDefinition</a></i>
<a href="#storageconfig" title="StorageConfig">StorageConfig</a>: <i>
      - <a href="storageconfigdefinition.md">StorageConfigDefinition</a></i>
</pre>

## Properties

#### InspectTemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Actions

_Required_: No

_Type_: List of <a href="actionsdefinition.md">ActionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageConfig

_Required_: No

_Type_: List of <a href="storageconfigdefinition.md">StorageConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

