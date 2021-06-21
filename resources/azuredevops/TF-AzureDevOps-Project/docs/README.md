# TF::AzureDevOps::Project

Manages a project within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::Project",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#features" title="Features">Features</a>" : <i>[ <a href="featuresdefinition.md">FeaturesDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#versioncontrol" title="VersionControl">VersionControl</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#workitemtemplate" title="WorkItemTemplate">WorkItemTemplate</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::Project
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#features" title="Features">Features</a>: <i>
      - <a href="featuresdefinition.md">FeaturesDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#versioncontrol" title="VersionControl">VersionControl</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#workitemtemplate" title="WorkItemTemplate">WorkItemTemplate</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

The Description of the Project.
- `visibility` - (Optional) Specifies the visibility of the Project. Valid values: `private` or `public`. Defaults to `private`.
- `version_control` - (Optional) Specifies the version control system. Valid values: `Git` or `Tfvc`. Defaults to `Git`.
- `work_item_template` - (Optional) Specifies the work item template. Valid values: `Agile`, `Basic`, `CMMI` or `Scrum`. Defaults to `Agile`.
- `features` - (Optional) Defines the status (`enabled`, `disabled`) of the project features.
Valid features are `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Features

Defines the status (`enabled`, `disabled`) of the project features.
Valid features are `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`.

_Required_: No

_Type_: List of <a href="featuresdefinition.md">FeaturesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Project Name.
- `description` - (Optional) The Description of the Project.
- `visibility` - (Optional) Specifies the visibility of the Project. Valid values: `private` or `public`. Defaults to `private`.
- `version_control` - (Optional) Specifies the version control system. Valid values: `Git` or `Tfvc`. Defaults to `Git`.
- `work_item_template` - (Optional) Specifies the work item template. Valid values: `Agile`, `Basic`, `CMMI` or `Scrum`. Defaults to `Agile`.
- `features` - (Optional) Defines the status (`enabled`, `disabled`) of the project features.
Valid features are `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionControl

Specifies the version control system. Valid values: `Git` or `Tfvc`. Defaults to `Git`.
- `work_item_template` - (Optional) Specifies the work item template. Valid values: `Agile`, `Basic`, `CMMI` or `Scrum`. Defaults to `Agile`.
- `features` - (Optional) Defines the status (`enabled`, `disabled`) of the project features.
Valid features are `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

Specifies the visibility of the Project. Valid values: `private` or `public`. Defaults to `private`.
- `version_control` - (Optional) Specifies the version control system. Valid values: `Git` or `Tfvc`. Defaults to `Git`.
- `work_item_template` - (Optional) Specifies the work item template. Valid values: `Agile`, `Basic`, `CMMI` or `Scrum`. Defaults to `Agile`.
- `features` - (Optional) Defines the status (`enabled`, `disabled`) of the project features.
Valid features are `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkItemTemplate

Specifies the work item template. Valid values: `Agile`, `Basic`, `CMMI` or `Scrum`. Defaults to `Agile`.
- `features` - (Optional) Defines the status (`enabled`, `disabled`) of the project features.
Valid features are `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### ProcessTemplateId

Returns the <code>ProcessTemplateId</code> value.
