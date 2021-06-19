# TF::Intersight::WorkflowWorkflowDefinition

Workflow definition is a collection of tasks that are sequenced in a certain way using control tasks. The tasks in the workflow definition is represented as a directed acyclic graph where each node in the graph is a task and the edges in the graph are transitions from one task to another.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::WorkflowWorkflowDefinition",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#catalog" title="Catalog">Catalog</a>" : <i>[ <a href="catalogdefinition.md">CatalogDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#clonedfrom" title="ClonedFrom">ClonedFrom</a>" : <i>[ <a href="clonedfromdefinition.md">ClonedFromDefinition</a>, ... ]</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#defaultversion" title="DefaultVersion">DefaultVersion</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#inputdefinition" title="InputDefinition">InputDefinition</a>" : <i>[ <a href="inputdefinitiondefinition5.md">InputDefinitionDefinition5</a>, ... ]</i>,
        "<a href="#inputparameterset" title="InputParameterSet">InputParameterSet</a>" : <i>[ <a href="inputparametersetdefinition.md">InputParameterSetDefinition</a>, ... ]</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#licenseentitlement" title="LicenseEntitlement">LicenseEntitlement</a>" : <i>String</i>,
        "<a href="#maxtaskcount" title="MaxTaskCount">MaxTaskCount</a>" : <i>Double</i>,
        "<a href="#maxworkertaskcount" title="MaxWorkerTaskCount">MaxWorkerTaskCount</a>" : <i>Double</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nrversion" title="NrVersion">NrVersion</a>" : <i>Double</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#outputdefinition" title="OutputDefinition">OutputDefinition</a>" : <i>[ <a href="outputdefinitiondefinition5.md">OutputDefinitionDefinition5</a>, ... ]</i>,
        "<a href="#outputparameters" title="OutputParameters">OutputParameters</a>" : <i>[ <a href="outputparametersdefinition.md">OutputParametersDefinition</a>, ... ]</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="propertiesdefinition.md">PropertiesDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tasks" title="Tasks">Tasks</a>" : <i>[ <a href="tasksdefinition.md">TasksDefinition</a>, ... ]</i>,
        "<a href="#uiinputfilters" title="UiInputFilters">UiInputFilters</a>" : <i>[ <a href="uiinputfiltersdefinition.md">UiInputFiltersDefinition</a>, ... ]</i>,
        "<a href="#uirenderingdata" title="UiRenderingData">UiRenderingData</a>" : <i>[ <a href="uirenderingdatadefinition.md">UiRenderingDataDefinition</a>, ... ]</i>,
        "<a href="#validationinformation" title="ValidationInformation">ValidationInformation</a>" : <i>[ <a href="validationinformationdefinition2.md">ValidationInformationDefinition2</a>, ... ]</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#workflowmetadata" title="WorkflowMetadata">WorkflowMetadata</a>" : <i>[ <a href="workflowmetadatadefinition.md">WorkflowMetadataDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::WorkflowWorkflowDefinition
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#catalog" title="Catalog">Catalog</a>: <i>
      - <a href="catalogdefinition.md">CatalogDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#clonedfrom" title="ClonedFrom">ClonedFrom</a>: <i>
      - <a href="clonedfromdefinition.md">ClonedFromDefinition</a></i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#defaultversion" title="DefaultVersion">DefaultVersion</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#inputdefinition" title="InputDefinition">InputDefinition</a>: <i>
      - <a href="inputdefinitiondefinition5.md">InputDefinitionDefinition5</a></i>
    <a href="#inputparameterset" title="InputParameterSet">InputParameterSet</a>: <i>
      - <a href="inputparametersetdefinition.md">InputParameterSetDefinition</a></i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#licenseentitlement" title="LicenseEntitlement">LicenseEntitlement</a>: <i>String</i>
    <a href="#maxtaskcount" title="MaxTaskCount">MaxTaskCount</a>: <i>Double</i>
    <a href="#maxworkertaskcount" title="MaxWorkerTaskCount">MaxWorkerTaskCount</a>: <i>Double</i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nrversion" title="NrVersion">NrVersion</a>: <i>Double</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#outputdefinition" title="OutputDefinition">OutputDefinition</a>: <i>
      - <a href="outputdefinitiondefinition5.md">OutputDefinitionDefinition5</a></i>
    <a href="#outputparameters" title="OutputParameters">OutputParameters</a>: <i>
      - <a href="outputparametersdefinition.md">OutputParametersDefinition</a></i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="propertiesdefinition.md">PropertiesDefinition</a></i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tasks" title="Tasks">Tasks</a>: <i>
      - <a href="tasksdefinition.md">TasksDefinition</a></i>
    <a href="#uiinputfilters" title="UiInputFilters">UiInputFilters</a>: <i>
      - <a href="uiinputfiltersdefinition.md">UiInputFiltersDefinition</a></i>
    <a href="#uirenderingdata" title="UiRenderingData">UiRenderingData</a>: <i>
      - <a href="uirenderingdatadefinition.md">UiRenderingDataDefinition</a></i>
    <a href="#validationinformation" title="ValidationInformation">ValidationInformation</a>: <i>
      - <a href="validationinformationdefinition2.md">ValidationInformationDefinition2</a></i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
    <a href="#workflowmetadata" title="WorkflowMetadata">WorkflowMetadata</a>: <i>
      - <a href="workflowmetadatadefinition.md">WorkflowMetadataDefinition</a></i>
</pre>

## Properties

#### AccountMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ancestors

_Required_: No

_Type_: List of <a href="ancestorsdefinition.md">AncestorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Catalog

_Required_: No

_Type_: List of <a href="catalogdefinition.md">CatalogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClonedFrom

_Required_: No

_Type_: List of <a href="clonedfromdefinition.md">ClonedFromDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultVersion

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGroupMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputDefinition

_Required_: No

_Type_: List of <a href="inputdefinitiondefinition5.md">InputDefinitionDefinition5</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputParameterSet

_Required_: No

_Type_: List of <a href="inputparametersetdefinition.md">InputParameterSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseEntitlement

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTaskCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxWorkerTaskCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Moid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NrVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputDefinition

_Required_: No

_Type_: List of <a href="outputdefinitiondefinition5.md">OutputDefinitionDefinition5</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputParameters

_Required_: No

_Type_: List of <a href="outputparametersdefinition.md">OutputParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

_Required_: No

_Type_: List of <a href="parentdefinition.md">ParentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionResources

_Required_: No

_Type_: List of <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of <a href="propertiesdefinition.md">PropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tasks

_Required_: No

_Type_: List of <a href="tasksdefinition.md">TasksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UiInputFilters

_Required_: No

_Type_: List of <a href="uiinputfiltersdefinition.md">UiInputFiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UiRenderingData

_Required_: No

_Type_: List of <a href="uirenderingdatadefinition.md">UiRenderingDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidationInformation

_Required_: No

_Type_: List of <a href="validationinformationdefinition2.md">ValidationInformationDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkflowMetadata

_Required_: No

_Type_: List of <a href="workflowmetadatadefinition.md">WorkflowMetadataDefinition</a>

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

